# P1 Section 3.2 Quality Requirements

| ID | Requirement | Priority | Source | How it will be verified |
|---|---|---|---|---|
| QR-01 | Ninety-five percent of packaging recommendations shall be returned within 3 seconds of a book’s weight and dimensions being entered, measured over one working week under normal load of up to 20 concurrent employees. | MUST | Warehouse operations/instructor | Timestamp logging of request and response, analyzed over a one-week trial |
| QR-02 | The system shall recommend the correct packaging type (mailer, padded mailer, or reinforced box) for at least 98% of books in a 200-book test set, as judged against the documented weight and dimension rules. | MUST | Shipping staff | Run the test set through the system and compare results against the expected packaging table |
| QR-03 | The system shall be available 99% of the time during business hours (8am to 6pm, Monday to Friday), measured over a 30-day period. | SHOULD | Stakeholders | Uptime monitoring log reviewed at the end of the period |
| QR-04 | A new employee shall be able to record a book’s weight, view the packaging recommendation, and view the inspection flag within 5 minutes of training, with at least 90% of 10 test users succeeding on the first attempt. | SHOULD | Employees/instructors | Moderated usability test with 10 participants using a task checklist |