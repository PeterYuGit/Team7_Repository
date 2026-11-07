# ADR-02 Read the scale directly, with manual entry as the fallback

| Field | Entry |
|---|---|
| Status | Accepted |
| Date and owner | 2026-11-07, Nicholas Suther |
| Context (drivers) | FR-01 (read weight from the scale) and FR-02 (manual entry when no reading); QR-01 (recommendation within 3 s); CON-03 (existing computer and scale, no new hardware); A2 (scale can connect to the computer, unconfirmed, Q3); risk R1. UC-01 steps 2 to 4 and alternate flow 3a. |
| Options considered | (1) **Direct read:** BookPack reads the scale's data stream, waits for a stable reading, and switches to manual entry if the scale is silent. (2) **Keyboard wedge:** the scale "types" its weight into whatever field has focus, so BookPack needs no scale code. (3) **Manual entry only:** the employee reads the scale display and types the weight. |
| Decision | Option 1, direct read with manual fallback. |
| Consequences | **Favors** accuracy and usability: no typing errors, and BookPack only accepts a *stable* weight, which a keyboard wedge cannot tell apart from a still-settling one. The keyboard wedge can also type into the wrong field. **Costs:** we have to write and maintain code tied to the scale's data format; changing scale models means updating the reader. There is up to about 1 s of waiting before a disconnected scale is noticed. Scale noise of about ±0.02 lb makes books at exactly the 5.0 lb flag limit unreliable, so FR-08's acceptance criterion had to change. |
| Evidence | Spike S-01 (section 8): 105/105 reads within ±0.05 lb, p95 1.00 s, and 20/20 disconnects fell back to manual entry within 1.2 s, against a simulated scale. Not yet tested on the bookstore's actual scale (Q3). |
| Related | R1, QR-01, CON-03, A2, Q3, S-01, CH-xx (FR-08) |

## Trade-off summary row (for 7.2)

| Quality favored | Architectural move | Cost accepted | Recorded in |
|---|---|---|---|
| Accuracy and usability of weight capture | Read the scale directly and accept only stable readings, with manual fallback | Scale-specific reader code; ~1 s disconnect detection; FR-08 boundary needs a tolerance rule | ADR-02 |
