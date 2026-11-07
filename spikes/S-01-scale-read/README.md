# Spike S-01: Reading the packing-station scale

**Owner:** Nicholas Suther
**Addresses:** Risk R1 (scale may fail to communicate with BookPack), FR-01, FR-02, QR-01, assumption A2, Spike-01 promised in P1 Section 2.6
**Feeds:** ADR-02 (scale integration)

## Question (yes/no)

Can BookPack read a stable book weight from a serial/USB postal scale to within FR-01's tolerance (±0.05 lb), fast enough to fit inside QR-01's 3-second budget, and detect a missing scale quickly enough to switch to manual entry (FR-02)?

## Answer

**Yes, against a simulated scale.** All 105 reads were within tolerance, the p95 read time was 1.05 s, and all 20 disconnects fell back to manual entry within 1.22 s.
It also found one problem: **5 of 15 books weighing exactly 5.00 lb were read as just over 5.0 lb** and would be flagged for inspection. As a result, FR-08's acceptance test ("5.0 lb is not flagged") cannot pass reliably on a real scale (see CH row in docs/p2).

## Set-up

- Python 3 standard library only. Runs on macOS or Linux with `python3 run_spike.py`.
- **What was simulated:** We do not yet have access to the bookstore's scale (open question Q3), so `scale_sim.py` imitates a typical serial postal scale on a pseudo-terminal (a fake serial port):
  - ~10 readings per second in the form `ST,GS,+0002.00lb`
  - 3 to 8 `US` (unstable) readings while the book settles, then `ST` (stable) readings
  - ±0.02 lb noise on stable readings
  - 5% of lines deliberately garbled
  - "Unplugged" cases where the scale stops sending, either immediately or partway through settling
- `scale_reader.py` is the part BookPack would use. It ignores garbled and unstable lines and returns the average of two stable readings that agree within 0.02 lb. If the scale is silent for 1.0 s or never settles within 3.0 s, it raises `ScaleUnavailable`, which tells the UI to switch to manual entry.

## How it was measured

`run_spike.py` ran 105 normal trials (15 each at 0.50, 1.00, 2.00, 3.00, 5.00, 5.10 and 12.00 lb, chosen to sit on the Table 3.1 and FR-08 boundaries) and 20 disconnect trials. For every trial it recorded the weight returned, the error, and the elapsed time. Raw data is in `results.csv`; the summary is in `results.md`.

## Result

| Measure | Result |
|---|---|
| Within FR-01 tolerance (±0.05 lb) | 105 / 105 |
| Max / mean absolute error | 0.020 lb / 0.007 lb |
| Time to stable weight: median / p95 / max | 0.73 s / 1.05 s / 1.25 s (p95 uses 35% of QR-01's 3 s) |
| Garbled lines safely ignored | 30 of 812 |
| Disconnects that fell back to manual entry | 20 / 20 |
| Time to detect disconnect: median / max | 1.11 s / 1.22 s |
| 5.00 lb book wrongly flagged (FR-08) | 5 / 15 |
| 5.10 lb book correctly flagged | 15 / 15 |

## What it changed or confirmed

- **Confirmed ADR-02:** BookPack reads the scale directly, waits for a stable reading, and falls back to manual entry. Reading the scale uses about a third of the 3 s budget, which leaves room for classification and saving the record.
- **Changed FR-08:** Scale noise means a book at exactly 5.0 lb can read 5.01 or 5.02 lb. We record this as a change (see docs/p2/changes-since-p1.md) instead of pretending the boundary test will pass.
- **Not answered (still open):** Whether the bookstore's actual scale has a computer connection and sends this kind of format (Q3, A2). The next step is to rerun the reader against the real scale and swap in its line format.

## Files

- `scale_sim.py`: simulated scale
- `scale_reader.py`: reader BookPack would use
- `run_spike.py`: runs the trials
- `results.csv`, `results.md`: measured output from the committed run
