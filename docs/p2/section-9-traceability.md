# 9 Traceability

## 9.1 Extended traceability matrix
 
| Requirement | Use case\ | Analysis classes\ | Component(s) | QAS / ADR | Evidence |
|---|---|---|---|---|---|
| FR-01 | UC-01 s3 | ScaleReader, PackingController | Scale Reader | QAS-02, ADR-02 | S-01 (105/105 reads) |
| FR-02 | UC-01 3a | PackingController, Measurement | Station UI, Packing Workflow | QAS-02, ADR-02 | S-01 (20/20 fallbacks) |
| FR-03, CON-02 | UC-01 s5 | Measurement | Station UI, Packing Workflow, Record Gateway | none | Entry and unit tests |
| FR-04 to FR-07, QR-02 | UC-01 s6–7 | ShippingRules, PackagingDecision | Classification Rules | QAS-03/04, ADR-01/03 | 200-book test set |
| FR-08 | UC-01 8a; UC-03 | ShippingRules, Inspection | Classification Rules, Packing Workflow | QAS-03, ADR-02/03 | 5.0/5.1 lb test; S-01 |
| CON-01, FR-09 | UC-01 s4, 4a | ShippingRules, ScaleReader | Classification Rules, Scale Reader | QAS-03, ADR-02, ADR-03 | 0/-1/71 lb tests |
| FR-10 | UC-01 s10; UC-03 (6) | PackagingDecision, ShippingRecord | Packing/Inspection Workflow, Record Gateway | ADR-01 | Record field test |
| FR-11, FR-12 | UC-02 | PackagingDecision, PackingController | Packing Workflow, Station UI | none | Override tests |
| FR-13, FR-14 | UC-03 (1)–(2), (5)–(6) | InspectionController, Inspection | Inspection Workflow, Record Gateway | none | Pass and list tests |
| FR-15 | UC-04 (not analyzed) | none | Record Gateway, Station UI | ADR-01 | Record view test |
| FR-16 | UC-01 s7 (to add) | ShippingRecord, PackagingDecision | Record Gateway, Packing Workflow | ADR-01, ADR-03 | Valuable-book test |
| QR-01 | UC-01 s5–7 | PackingController, ShippingRules | Packing Workflow, Classification Rules | QAS-01, ADR-01, ADR-02 | S-01 (p95 1.05 s); trial |
| QR-03 | UC-01 s3 | ScaleReader | Scale Reader | QAS-02, ADR-01, ADR-02 | S-01 (1.22 s); uptime log |
| QR-04 | UC-01 | PackingController | Station UI | none | Usability test |
| CON-03 | UC-01 s3 | ScaleReader | All six (6.4) | ADR-01, ADR-02 | S-01 (simulated scale) |
 
Evidence is S-01 (measured, simulated scale) or a test planned for P3. None withdrawn.
 
## 9.2 Gap analysis
 
| Gap | Items | What we did about it |
|---|---|---|
| Requirements with no component | None | Every FR, QR and CON reaches a component in 6.3. |
| Components with no requirement, QAS or ADR | None | Every 6.3 component answers to a use case, QAS or ADR. |
| Use cases not analyzed (and why acceptable) | UC-04 | It only realizes FR-15 (SHOULD), a read-only view through Record Gateway. |
| Other gaps | FR-15 has no analysis classes; QR-04 has no QAS; FR-16 is not yet in UC-01; QR-01 trial, QR-03 uptime log, QR-04 test and S-01 on the real scale (Q3) not yet run | FR-15 and QR-04 are deferred as SHOULD. The unrun checks move to P3 (10.2). |
