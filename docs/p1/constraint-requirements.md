# P1 Section 3.3 Constraint Requirements

| ID | Constraint (one sentence) | Source | Why it cannot be negotiated |
|---|---|---|---|
| CON-01 | The system shall not save any book with a record weight greater than 70 lb. | R1 USPS package weight | USPS sets limits and will refuse heavier packages. Neither the team nor the bookstore can work around this requirement. |
| CON-02 | The system shall store weight in pounds and length, width, and thickness in inches. | R1 USPS shipping requirements | USPS has published limits in pounds and inches. Using other units would conflict at the checking point and lead to conversion errors. |
| CON-03 | The system shall run on the packing station's existing computer system and scale without requiring new hardware purchases. | Bookstore (2.4 C3); Assumed, Q3 | We assumed that the bookstore will not buy new hardware. If the answer to Q3 is a different result, the constraint will be reviewed through change control. |
