"""Simulated postal scale for spike S-01.

Acts like a serial/USB postal scale: it streams about 10 readings per second,
marked US (unstable) while the book is settling and ST (stable) once it stops
moving. Format of each line:  ST,GS,+0002.00lb

To be realistic it also:
  - adds small measurement noise (+/- 0.02 lb) to stable readings
  - sends a garbled line now and then (electrical noise / partial reads)
  - can "go silent" after N readings to imitate the scale being unplugged
"""

import os
import random
import threading
import time

LINE_INTERVAL_S = 0.1     # 10 readings per second
STABLE_NOISE_LB = 0.02    # noise on a stable reading
GARBLE_RATE = 0.05        # 5% of lines are corrupted


class SimulatedScale:
    def __init__(self, fd, true_weight_lb, settle_readings=None,
                 stop_after=None, seed=None):
        self.fd = fd
        self.true_weight = true_weight_lb
        self.rng = random.Random(seed)
        # how many unstable readings before the book stops moving
        self.settle = settle_readings if settle_readings is not None else self.rng.randint(3, 8)
        self.stop_after = stop_after   # None = keeps sending until stopped
        self._stopped = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def start(self):
        self._thread.start()

    def stop(self):
        self._stopped.set()
        self._thread.join(timeout=1)

    def _line(self, n):
        if n < self.settle:
            status = "US"
            swing = 0.5 * (self.settle - n) / self.settle
            value = self.true_weight + self.rng.uniform(-swing, swing)
        else:
            status = "ST"
            value = self.true_weight + self.rng.uniform(-STABLE_NOISE_LB, STABLE_NOISE_LB)
        value = max(0.0, round(value, 2))
        line = f"{status},GS,{value:+08.2f}lb"
        if self.rng.random() < GARBLE_RATE:
            cut = self.rng.randint(1, len(line) - 1)
            line = line[:cut] + "#?" + line[cut + 2:]
        return line + "\r\n"

    def _run(self):
        n = 0
        while not self._stopped.is_set():
            if self.stop_after is not None and n >= self.stop_after:
                return  # scale unplugged: no more data
            try:
                os.write(self.fd, self._line(n).encode("ascii"))
            except OSError:
                return
            n += 1
            time.sleep(LINE_INTERVAL_S)
