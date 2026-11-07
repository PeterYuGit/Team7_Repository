# 8 Prototype Evidence: Architecture Spike

| Field | Entry |
|---|---|
| Spike ID and title | S-01 Reading the packing-station scale |
| Risk or decision it addresses | R1, ADR-02, QR-01 (FR-01, FR-02, A2) |
| Question (answerable yes or no) | Can BookPack read a stable weight from a serial/USB postal scale within ±0.05 lb (FR-01), within QR-01's 3 s budget, and detect a missing scale fast enough to switch to manual entry (FR-02)? |
| Set-up | Python 3 standard library. The bookstore's scale is not available yet (Q3), so a simulated serial postal scale runs on a pseudo-terminal: about 10 readings/s, unstable readings while settling, ±0.02 lb noise, 5% garbled lines, and "unplugged" cases. The reader waits for two agreeing stable readings and falls back to manual entry after 1.0 s of silence or 3.0 s without a stable reading. Folder: /spikes/S-01-scale-read/ |
| How it was measured | 105 normal trials (15 each at 0.50, 1.00, 2.00, 3.00, 5.00, 5.10 and 12.00 lb, on the Table 3.1 and FR-08 boundaries) and 20 disconnect trials. Each trial logged the weight returned, the error and the elapsed time to results.csv. |
| Result (numbers) | 105/105 reads within ±0.05 lb (max error 0.020 lb). Time to stable weight: median 0.73 s, p95 1.05 s, max 1.25 s. 30 of 812 garbled lines ignored with no wrong reading. 20/20 disconnects fell back to manual entry, detected in at most 1.22 s. A 5.00 lb book read as over 5.0 lb in 5 of 15 trials. |
| What it changed or confirmed | Confirmed ADR-02 (direct scale read with manual fallback): reading uses about 35% of QR-01's 3 s at p95. Changed FR-08's acceptance criterion (CH-xx) because scale noise makes the exact 5.0 lb boundary unreliable. Q3/A2 is still open: the real scale has not been tested. |
| Where to see it | /spikes/S-01-scale-read/ (README.md, results.csv, results.md), commit ce38eaf |
