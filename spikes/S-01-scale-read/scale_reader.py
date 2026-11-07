"""Scale reader for spike S-01: the piece BookPack itself would use.

read_stable_weight() waits for the scale to report a stable weight (FR-01).
If the scale sends nothing for SILENCE_TIMEOUT_S, or never settles within
TOTAL_TIMEOUT_S, it raises ScaleUnavailable so the UI can switch to manual
weight entry (FR-02).
"""

import os
import re
import select
import time

LINE_RE = re.compile(r"^(ST|US),GS,([+-]\d+\.\d+)lb$")

SILENCE_TIMEOUT_S = 1.0   # no bytes at all for this long = scale disconnected
TOTAL_TIMEOUT_S = 3.0     # never got a stable weight = give up, go manual
AGREE_LB = 0.02           # two stable readings must agree within this
NEEDED_STABLE = 2         # how many agreeing stable readings we require


class ScaleUnavailable(Exception):
    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


def read_stable_weight(fd):
    """Return (weight_lb, stats). Raises ScaleUnavailable on failure."""
    stats = {"lines": 0, "rejected": 0, "unstable": 0}
    start = time.monotonic()
    buf = b""
    recent = []
    while True:
        elapsed = time.monotonic() - start
        if elapsed >= TOTAL_TIMEOUT_S:
            raise ScaleUnavailable("no stable reading")
        wait = min(SILENCE_TIMEOUT_S, TOTAL_TIMEOUT_S - elapsed)
        ready, _, _ = select.select([fd], [], [], wait)
        if not ready:
            raise ScaleUnavailable("scale silent (disconnected?)")
        try:
            chunk = os.read(fd, 256)
        except OSError:
            raise ScaleUnavailable("read error")
        if not chunk:
            raise ScaleUnavailable("scale closed")
        buf += chunk
        while b"\n" in buf:
            raw, buf = buf.split(b"\n", 1)
            line = raw.decode("ascii", "replace").strip()
            if not line:
                continue
            stats["lines"] += 1
            m = LINE_RE.match(line)
            if not m:
                stats["rejected"] += 1      # garbled line: ignore it
                continue
            if m.group(1) != "ST":
                stats["unstable"] += 1      # book still moving
                recent.clear()
                continue
            w = float(m.group(2))
            if recent and abs(w - recent[-1]) > AGREE_LB:
                recent.clear()
            recent.append(w)
            if len(recent) >= NEEDED_STABLE:
                avg = sum(recent[-NEEDED_STABLE:]) / NEEDED_STABLE
                return round(avg, 2), stats
