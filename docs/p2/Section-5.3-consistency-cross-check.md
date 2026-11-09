## 5.3 Consistency cross-check

Six checks were run across the domain model (5.1), the expanded use cases (4.2), the scenario tables and the sequence diagrams (5.2.1 UC-02, 5.2.2 UC-03).

| Check | Result (pass, or what failed) | Fixed in |
|---|---|---|
| K1. Every item in an actor column (4.2) is an attribute in the domain model (5.1) | **Pass.** Order number, valuable flag, status and inspection status are on ShippingRecord; title on Book; weight, length, width and thickness on Measurement; size class, recommended type, chosen type and reason on PackagingDecision; result, inspector and time on Inspection. | n/a |
| K2. Every object on a sequence diagram is a domain class or a declared interaction object | **Pass.** Figures 5.2.1 and 5.2.2 use only ShippingRecord, PackagingDecision and Inspection (domain classes) and PackingController and InspectionController (declared interaction objects). | n/a |
| K3. Every message on a sequence diagram corresponds to exactly one scenario-table row | **Failed for UC-02.** Fig. 5.2.1 has 9 messages but the 5.2.1(b) table had 7 rows. Messages 2 and 8 had no rows, and later numbers were shifted. UC-03 passes (9 rows, 9 messages). | 5.2.1(b) rebuilt with 9 rows |
| K4. Every non-trivial step in 5.2 (a) has at least one scenario-table row | **Failed for UC-02.** Step (4) was listed as non-trivial, but no row validates anything (the empty-reason check is alternate flow A1). 4.1 also disagreed with 5.2.1(a). UC-03 passes. | 5.2.1(a) revised to match 4.1. |
| K5. Every analyzed use case traces to at least one functional requirement | **Pass.** UC-01 traces to FR-01 to FR-10 and FR-16, UC-02 to FR-10 to FR-12, and UC-03 to FR-10, FR-13 and FR-14 (consuming FR-08). | n/a |
| K6. The last messages of each diagram make the use-case postcondition true | Pass. UC-02 messages 7–9 save the chosen type and reason, then confirm. UC-03 messages 7–9 record Pass, mark the book ready to ship, and show the updated list. The Fail scenario is handled separately in alternate flow A2.  | n/a |

Result: two checks failed for UC-02 (K3, K4). Both were fixed and re-run, and all six checks now pass for both analyzed use cases.
