# UC-01 Process Book for Shipment

P2 Section 4 (Use-Case Analysis): Afeef Zarraf

## 4.1 Use case selected for analysis

| Use case | Name | Why it was selected | Non-trivial steps |
|---|---|---|---|
| UC-01 | Process Book for Shipment | It's the core of the product (FR-01 to FR-10 and FR-16) and most quality requirements (QR-01,QR-02, QR-04); the only use case that works with two external systems(the scale and the shipping record system), each with a failure the employee can see. | (2), (4), (6), (8). (10) |

## 4.2 Expanded use case

| Field | Content |
|---|---|
| Primary actor | Packing Employee |
| Supporting actors and external systems | Scale(external device); existing shipping record system(external system) |
| TUCBW (this use case begins when) | The packing employee starts processing the book for shipment by giving its order number |
| TUCEW (this use case ends when) | The packing employee sees confirmation that the book's weight, packaging type and inspection status were saved to its record. |
| Preconditions | The book has to have been picked for an order and is at the packing station. |
| Postconditions | The shipping holds the book’s weight, length, width, thickness, packaging type and inspection status. A book over 5.0 lbs is awaiting inspection and can’t be marked ready to ship until Pass is recorded for it (UC-03). |
| Traces to requirements | FR-01 to FR-10, FR-16; QR-01, QR-02, QR-04;, CON-01, CON-02 |

| Actor input / action | System response |
|---|---|
| | (0) The system shows that it’s ready to process a book and asks for order number |
| (1) The packing employee gives the book order number | (2) The system finds the book’s shipping record, shows the order number and title, and asks the employee to place book on scale. |
| (3) The packing employee places book on scale. | (4) The system reads the weight and shows it, and asks for the book length, width and thickness. |
| (5) The packing employee enters the length, width, and thickness in INCHES. | (6) The system classifies the book using the weight and thickness thresholds that are set in Table 3.1 and shows its size category with weight and thickness. |
| (7) The packing employee asks for packaging type recommendation. . | (8) The system shows the recommended packaging type according to the Table 3.1 and displays if the book requires additional inspection under FR-08. |
| (9) The packing employee accepts the recommendation. | (10) The system saves the weight, dimensions, packing type and inspection status to the shipping record and confirms that the book was processes. |

| Alternate flow | At step | Condition | What happens | Ends or rejoins at |
|---|---|---|---|---|
| A1 | (2) | No shipping record matches the order number | The system says no record found and saves nothing | Rejoins (1) |
| A2 | (3) | No scale reading is available | The packing employee enters the weight by hand (FR-02) | Rejoins (4) with the entered weight |
| A3 | (4) | The weight is 0lbs or less, or over 70lbs | The system shows error and saves nothing (FR-09, CON-01) | Rejoins (3) |
| A4 | (8) | The book's weight meets the FR-08 inspection criteria, accounting for the applicable manual-entry or scale-reading tolerance | The system shows the recommendation and that the book requires additional inspection (FR-08). At step (10), the inspection status is saved as awaiting inspection. | Rejoins (9) |
| A5 | (8) | The shipping record marks the book as valuable | The system recommends a reinforced without regards to size class and says why; the weight and dimensions are still recorded (FR-16) | Rejoins (9) |
| A6 | (9) | The packing employee rejects the recommendation | The employee chooses another packing type with a reason | Continues in UC-02 Override Packing Recommendation |
| A7 | (10) | The shipping record cannot be saved | The system says the record was not saved and keeps the entries on screen. | Rejoins (9) |

## 4.3 Self-review log (UC-01)

| Use case | Check from the Lesson 13 review checklist | Defect found | How it was fixed |
|---|---|---|---|
| UC-01 | Step(0) present | P1 had no step (0) | Added (0): the system shows it’s ready and asks for the order number |
| UC-01 | Precondition or alternate flow | P1 precondition “an existing shipping record” can be false during normal work(wrong order number) | Moved to A1 |
| UC-01 | One turn per row | P1 steps 6, 7 and 8 were three system steps in a row with no actor to turn between them | Split into (6) classification, (7) employee asks for recommendation, (8) recommendation and inspection check |
| UC-01 | No technology | P1 step 3 said the weight “displays on the user interface” | Reworded: the system reads the weight from the scale and shows it. |
| UC-01 | Acknowledgement at the end | P1 step 10 updated the record but gave the employee no confirmation | (10) now ends with a confirmation that book was processed |
| UC-01 | Traces to requirements | P1 step 6 used “dimension thresholds”, not table 3.1 (CH-03), and UC-01 had no path for valuable books (CH-05) | Step(6) uses the weight and thickness thresholds in Table 3.1; added A5 tracing to FR-16 |
| UC-01 | Real alternate flows | P1 had no flow for a record that can’t be saved | Added A7 |
