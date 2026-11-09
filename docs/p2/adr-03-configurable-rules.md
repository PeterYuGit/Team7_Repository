# ADR-03 Keep classification thresholds in a configuration file

| Field | Value |
|---|---|
| Status | Accepted |
| Date and owner | 2026-11-08, Ahmet Keles |
| Context (drivers) | Table 3.1 thresholds were approved by the owner on 11/05 but may still change, and the 5.0 lb flag limit is still open (Q1, A4, R5); QAS-03, QAS-04; CH-01 added a scale tolerance |
| Options considered | 1. Hard-code the thresholds in the classification code |
| Options considered | 2. Store them in rules.json on each station, loaded and validated at start-up |
| Options considered | 3. Store them in the bookstore's shipping record database |
| Decision | Option 2, rules.json read by Classification Rules |
| Consequences | Favors modifiability: a Q1 answer changes one file with no code change. Costs: the file must be validated at start-up (a typo could misclassify every book); 20 stations need the same file; the 70 lb CON-01 limit and the FR-16 valuable-book exception stay in code so a config edit cannot weaken them |
| Evidence | None yet; boundary tests in P3 will load two different rule files and check both |
| Related | QAS-04, Q1, A4, R5, CON-01, CH-01, CH-05, FR-16 |

## 7.2 Trade-off row

| Quality favored | Architectural move | Cost accepted | Recorded in |
|---|---|---|---|
| Modifiability of rules | Thresholds in rules.json, 70 lb limit kept in code | Start-up validation needed; file must match on every station | ADR-03 |
