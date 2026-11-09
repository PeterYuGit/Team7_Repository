# ADR-01 Use a layered architecture on each packing station

| Field | Value |
|---|---|
| Status | Accepted |
| Date and owner | 2026-11-08, Ahmet Keles |
| Context (drivers) | QAS-01 (3 s for 95%), QAS-02 (scale loss), QAS-04 (threshold change); CON-03 (existing PC, no new hardware); UC-01 to UC-03 are synchronous requests the actor waits for |
| Options considered | 1. Layered application on each station PC, with client-server access to the existing shipping record system |
| Options considered | 2. Microservices for scale, rules and records on a separate server |
| Options considered | 3. Pipe-and-filter pipeline from weighing to saving |
| Decision | Option 1, layered (presentation, application, rules, integration) |
| Consequences | Favors performance (in-process calls) and modifiability (rules in one layer). Costs: each of up to 20 stations must be updated when the code changes; layers add pass-through calls; one station's failure is not covered by another |
| Evidence | Spike S-01 shows the scale read uses 1.05 s at p95, leaving about 1.95 s for classification and saving in one process |
| Related | Section 6.2, QAS-01, QAS-02, QAS-04, CON-03 |

## 7.2 Trade-off row

| Quality favored | Architectural move | Cost accepted | Recorded in |
|---|---|---|---|
| Performance and simplicity | Layered app running in one process on each station | Updates on up to 20 stations; no failover between stations | ADR-01 |
