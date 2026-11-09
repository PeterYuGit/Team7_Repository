# 9 Traceability

## 9.1 Extended traceability matrix

| Requirement | Use case | Analysis classes | Component(s) | QAS / ADR | Evidence |
|---|---|---|---|---|---|
| FR-01 | UC-01 (3)–(4) | Measurement | Scale Reader, Packing Workflow | QAS-02, ADR-02 | S-01 (105/105 reads) |
| FR-02 | UC-01 A2 | Measurement | Station UI, Packing Workflow | QAS-02, ADR-02 | S-01 (20/20 fallbacks) |
| FR-03, CON-02 | UC-01 (5) | Measurement | Station UI, Packing Workflow, Record Gateway | none | Entry and unit tests |
| FR-04 to FR-07, QR-02 | UC-01 (6), (8), A5 | ShippingRules, PackagingDecision | Classification Rules | QAS-03/04, ADR-01/03 | 200-book test set |
| FR-08 | UC-01 A4; UC-03 | ShippingRules, ShippingRecord | Classification Rules, Packing Workflow | QAS-03, ADR-02/03 | 5.0/5.1 lb test; S-01 |
| CON-01, FR-09 | UC-01 (4), A3 | ShippingRules, Measurement | Classification Rules, Scale Reader | QAS-03, ADR-02/03 | 0/-1/71 lb tests |
| FR-10 | UC-01 (10); UC-02 (6); UC-03 (6) | Measurement, PackagingDecision, ShippingRecord, Inspection | Packing/Inspection Workflow, Record Gateway | ADR-01 | Record field test |
| FR-11, FR-12 | UC-02 (1)–(3), A1 | PackagingDecision, PackingController | Packing Workflow, Station UI | none | Override tests |
| FR-13, FR-14 | UC-03 (1)–(2), (5)–(6) | InspectionController, Inspection, ShippingRecord | Inspection Workflow, Record Gateway | none | Pass and list tests |
| FR-15 | UC-04 (not analyzed) | ShippingRecord | Record Gateway, Station UI | ADR-01 | Record view test |
| FR-16 | UC-01 A5 | ShippingRecord, ShippingRules, PackagingDecision | Record Gateway, Packing Workflow, Classification Rules | ADR-01/03 | Valuable-book tests |
| QR-01 | UC-01 (5)–(8) | Measurement, PackagingDecision, ShippingRules | Packing Workflow, Classification Rules | QAS-01, ADR-01/02 | S-01 (p95 1.05 s); trial |
| QR-03 | UC-01 (3)–(4), A2 | Measurement | Scale Reader | QAS-02, ADR-01/02 | S-01 (1.22 s); uptime log |
| QR-04 | UC-01 (0)–(10) | none | Station UI | none | Usability test |
| CON-03 | UC-01 (3)–(4) | Measurement | All six (6.4) | ADR-01/02 | S-01 (simulated scale) |

Evidence is S-01 (measured, simulated scale) or a test planned for P3. No requirement has been withdrawn.

## 9.2 Gap analysis

| Gap | Items | What we did about it |
|---|---|---|
| Requirements with no component | None | Every FR, QR and CON reaches a component in 6.3. |
| Components with no requirement, QAS or ADR | None | Every 6.3 component answers to a use case, QAS or ADR. |
| Use cases not analyzed (and why that is acceptable) | UC-04 | It only realizes FR-15 (SHOULD), a read-only view through Record Gateway. |
| Other gaps | QR-04 has no dedicated QAS; no FR explicitly covers the "no record found" and "cannot be saved" flows (UC-01 A1, A7; UC-02 A4; UC-03 A3); QR-01 trial, QR-03 uptime log, QR-04 usability test and real-scale validation (Q3) have not yet been completed. | QR-04 is a SHOULD requirement and will be verified through usability testing in P3. Failed writes are tracked as risk R4 and will be tested in P3. Remaining verification activities are planned for P3 (Section 10.2). |
