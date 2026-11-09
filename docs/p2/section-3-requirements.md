# 3 Specific Requirements
 
Carried forward from P1 v0.8 with CH-01, CH-02, CH-03, CH-05 and CH-06 applied. Existing requirement IDs are unchanged, FR-16 is new, and no requirement has been withdrawn.
 
## 3.1 Functional requirements
 
| ID | Requirement (one "shall" sentence) | Priority | Source | Acceptance criterion |
|---|---|---|---|---|
| FR-01 | The system shall read a book's weight from a connected scale. | MUST | Packing employee | Place a known 2.00 lb test weight on the scale; recorded weight is 2.00 lb ± 0.05. |
| FR-02 | The system shall allow manual entry of a book's weight when no scale reading is available. | MUST | Packing employee | With the scale disconnected, enter 1.5 lb; the record stores 1.5 lb. |
| FR-03 | The system shall accept manual entry of a book's length, width, and thickness in inches. | MUST | Packing employee | Enter 9 × 6 × 1; the record stores all three values. |
| FR-04 | The system shall classify each book as Small, Medium, or Large using the thresholds in Table 3.1. | MUST | Bookstore | For 9 test books at and around each threshold, the class matches Table 3.1. |
| FR-05 | The system shall recommend a cardboard mailer for a Small book, unless the book is marked as valuable (see FR-16). | MUST | Bookstore | A Small book not marked as valuable shows "Cardboard mailer." *(Changed, CH-05)* |
| FR-06 | The system shall recommend a padded mailer for a Medium book, unless the book is marked as valuable (see FR-16). | MUST | Bookstore | A Medium book not marked as valuable shows "Padded mailer." *(Changed, CH-05)* |
| FR-07 | The system shall recommend a reinforced box for a Large book. | MUST | Bookstore, Student | A Large book shows "Reinforced box." |
| FR-08 | The system shall flag a book for inspection when its weight exceeds 5.0 lb. | MUST | Student | Entered manually: 5.0 lb is not flagged and 5.1 lb is flagged. Read from the scale: any book over 5.05 lb is always flagged; a book within the scale's ±0.05 lb tolerance of 5.0 lb may be flagged. *(Changed, CH-01)* |
| FR-09 | The system shall reject a weight entry less than or equal to 0 lb or greater than 70 lb. | MUST *(was SHOULD, CH-02)* | USPS [R1] | Entering 0, -1, or 71 shows an error and saves nothing. |
| FR-10 | The system shall save the weight, dimensions, packaging type, inspection status and any override reason to the book's shipping record. | MUST | Bookstore | After processing, the record shows the weight, length, width, thickness, packaging type and inspection status, and the reason when the recommendation was overridden. *(Changed, CH-06)* |
| FR-11 | The system shall allow an employee to override a packaging recommendation. | SHOULD | Packing employee | The override is saved, replacing the original recommendation. |
| FR-12 | The system shall require a written reason when an employee overrides a recommendation. | SHOULD | Bookstore | An override with an empty reason is rejected. |
| FR-13 | The system shall allow an inspector to record Pass or Fail for a flagged book. | MUST | Bookstore | A flagged book cannot be marked ready to ship until Pass is recorded. |
| FR-14 | The system shall display all books with an inspection status of "awaiting inspection", including each book's weight, dimensions, and packaging type. | SHOULD | Inspector | With two flagged books and one unflagged book in the system, the list shows exactly the two flagged books, each with weight, dimensions, and packaging type. |
| FR-15 | The system shall allow an employee to view a book's shipping record, including its weight, packaging type, and inspection status. | SHOULD | Packing employee | After a book is processed, opening its record shows weight, packaging type, and inspection status. |
| FR-16 | The system shall retrieve the valuable flag from a book's shipping record and, when the flag is set, apply the packaging exception by recommending a reinforced box regardless of the book's weight or size. | MUST | Bookstore owner (interview, 11/05/2026) | A 0.5 lb, 0.5 in thick book (Small) and a 2.0 lb book (Medium) with the valuable flag set both show "Reinforced box," and their weight and dimensions are still recorded. The same books without the flag show "Cardboard mailer" and "Padded mailer." A shipping record with no valuable flag is treated as not valuable. *(Added, CH-05)* |
 
**Table 3.1 Packaging classification thresholds (approved by the bookstore owner, interview 11/05/2026)**
 
| Class | Rule |
|---|---|
| Small | 1.0 lb or less and 1 in thick or less |
| Medium | 3.0 lb or less (and not Small) |
| Large | More than 3.0 lb |
 
Classification uses weight and thickness only. Length and width are recorded (FR-03) for the shipping record and the inspector's list (FR-14) but do not affect the class. *(Added, CH-03)* A book whose shipping record has the valuable flag set is still measured and classified, but receives a reinforced box regardless of its class (FR-16). *(Added, CH-05)* The bookstore owner approved these thresholds on 11/05/2026 (Stakeholder_Interview.md, PR #13); the 5.0 lb flag limit is still open (Q9).
 
## 3.2 Quality requirements
 
Unchanged since v0.8.
 
| ID | Requirement (with threshold, condition and method) | Priority | Source | How it will be verified |
|---|---|---|---|---|
| QR-01 | Ninety-five percent of packaging recommendations shall be returned within 3 seconds of a book's weight and dimensions being entered, measured over one working week under normal load of up to 20 concurrent employees. | MUST | Warehouse operations / instructor | Timestamp logging of request and response, analyzed over a one-week trial |
| QR-02 | The system shall recommend the correct packaging type (mailer, padded mailer, or reinforced box) for at least 98% of books in a 200-book test set, as judged against the documented weight and dimension rules. | MUST | Shipping staff | Run the test set through the system and compare results against the expected packaging table |
| QR-03 | The system shall be available 99% of the time during business hours (8am to 6pm, Monday to Friday), measured over a 30-day period. | SHOULD | Stakeholders | Uptime monitoring log reviewed at the end of the period |
| QR-04 | A new employee shall be able to record a book's weight, view the packaging recommendation, and view the inspection flag within 5 minutes of training, with at least 90% of 10 test users succeeding on the first attempt. | SHOULD | Employees / instructors | Moderated usability test with 10 participants using a task checklist |
 
## 3.3 Constraint requirements
 
Unchanged since v0.8.
 
| ID | Constraint (one sentence) | Source | Why it cannot be negotiated |
|---|---|---|---|
| CON-01 | The system shall not save a book record if its weight exceeds 70 lb. | R1 USPS package weight | USPS sets limits and will refuse heavier packages. Neither the team nor the bookstore can work around this requirement. |
| CON-02 | The system shall store book weight in pounds and length, width, and thickness in inches. | R1 USPS shipping requirements | USPS publishes limits in pounds and inches. Using other units would conflict at checking points and lead to conversion errors. |
| CON-03 | The system shall run on the packing station's existing computer system and scale without requiring new hardware purchases. | Bookstore (2.4 C3); assumed, Q3 | We assumed the bookstore will not buy new hardware. If the answer to Q3 differs, the constraint will be reviewed through change control. |
 
## 3.4 Initial use cases
 
The use-case diagram is unchanged since v0.8 (docs/p1/use-case-diagram.png). Use cases at actor-goal level:
 
| ID | Use case | Primary actor | Goal |
|---|---|---|---|
| UC-01 | Process Book for Shipment | Packing Employee | Get a packaging recommendation and record the book's weight, packaging and inspection status |
| UC-02 | Override Packaging Recommendation | Packing Employee | Replace a recommendation with another packaging type and a written reason |
| UC-03 | Inspect Flagged Book | Inspector | Record Pass or Fail for a book flagged for inspection |
| UC-04 | Review Shipping Record | Packing Employee | View a book's weight, packaging type and inspection status |
 
The turn-by-turn expansions are in section 4.2. UC-01 step 6 now reads "the system classifies the book using the weight and thickness thresholds in Table 3.1" (CH-03).
 
## 3.5 Requirements to use-case traceability
 
Replaced by the extended matrix in section 9.1.
