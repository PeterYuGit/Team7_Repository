# P1 Section 3.1 Functional Requirements

| ID | Requirement | Priority | Source | Acceptance criterion |
|---|---|---|---|---|
| FR-01 | The system shall read a book's weight from a connected scale. | MUST | Packing employee | Place a known 2.00 lb test weight on the scale; recorded weight is 2.00 lb ± 0.05. |
| FR-02 | The system shall allow manual entry of a book's weight when no scale reading is available. | MUST | Packing employee | With the scale disconnected, enter 1.5 lb; the record stores 1.5 lb. |
| FR-03 | The system shall accept manual entry of a book's length, width, and thickness in inches. | MUST | Packing employee | Enter 9 × 6 × 1; the record stores all three values. |
| FR-04 | The system shall classify each book as Small, Medium, or Large using the thresholds in Table 3.1. | MUST | Bookstore | For 9 test books at and around each threshold, the class matches Table 3.1. |
| FR-05 | The system shall recommend a cardboard mailer for a Small book. | MUST | Bookstore | A Small book shows "Cardboard mailer." |
| FR-06 | The system shall recommend a padded mailer for a Medium book. | MUST | Bookstore | A Medium book shows "Padded mailer." |
| FR-07 | The system shall recommend a reinforced box for a Large book. | MUST | Bookstore, Student | A Large book shows "Reinforced box." |
| FR-08 | The system shall flag a book for inspection when its weight exceeds 5.0 lb. | MUST | Student | 5.0 lb is not flagged; 5.1 lb is flagged. |
| FR-09 | The system shall reject a weight entry less than or equal to 0 lb or greater than 70 lb. | SHOULD | USPS [R1] | Entering 0, -1, or 71 shows an error and saves nothing. |
| FR-10 | The system shall save the weight, packaging type, and inspection status to the book's shipping record. | MUST | Bookstore | After processing, the record shows all three fields. |
| FR-11 | The system shall allow an employee to override a packaging recommendation. | SHOULD | Packing employee | The override is saved, replacing the original recommendation. |
| FR-12 | The system shall require a written reason when an employee overrides a recommendation. | SHOULD | Bookstore | An override with an empty reason is rejected. |
| FR-13 | The system shall allow an inspector to record Pass or Fail for a flagged book. | MUST | Bookstore | A flagged book cannot be marked ready to ship until Pass is recorded. |

## Table 3.1 - Classification thresholds (ASSUMED, see Open Questions)

| Class | Rule |
|---|---|
| Small | 1.0 lb or less and 1 in thick or less |
| Medium | 3.0 lb or less (and not Small) |
| Large | More than 3.0 lb |


## Notes for other sections

**For Section 5 (Open Questions):**
- Q1: What weight and size thresholds should decide each packaging type? Answerable by the bookstore or shipping manager. Needed before P2. Assumed in the meantime: the values in Table 3.1.
- Q2: Who performs the inspection for flagged books, a separate inspector or the packing employee? Answerable by the shipping facility manager. Assumed in the meantime: a separate inspector role.

**For Section 2.2 (Stakeholders):**
- Add "Packing employee" (primary user, enters weights and follows recommendations). Source for FR-01, FR-02, FR-03, FR-11.
- Add "Inspector" (reviews flagged books). Needed for FR-13.

**For Section 1.4 (References):**
- [R1] USPS maximum package weight (70 lb), used in FR-09. Add the USPS page link.

**For Section 3.4 (Use Cases):**
- UC: Process Book for Shipment (FR-01 to FR-10)
- UC: Override Packaging Recommendation (FR-11, FR-12)
- UC: Inspect Flagged Book (FR-13)
