# P1 Section 1.3 Definitions, Acronyms and Abbreviations

| Term or abbreviation | Meaning as used in this project |
|---|---|
| BookPack | The software system this document specifies. It records a book's weight and dimensions, recommends packaging style, flags books for inspection and updates the book's shipping record. |
| Packing employee | The person at the packing station who weighs, measures, and packs the books. This is the primary user. |
| Inspector | The person who records pass or fail for a flagged book (FR-13). The stakeholder table also calls this role shipping coordinator. Both names are the same role. Whether it is a separate person from the packing employee is still open (Q2). |
| Book weight | The weight of the book alone, in pounds, read from the scale or entered by hand (FR-01, FR-02). |
| Dimensions | The book's length, width, and thickness in inches (FR-03). Thickness is referring to the shortest side, the one measured when the book lies flat. |
| Size class | Small, medium, large, assigned from the weight and thickness using the thresholds in Table 3.1 (FR-04). The thresholds are assumed in Q1. |
| Packaging type | The packaging BookPack recommends: cardboard mailer (small), padded mailer (medium), reinforced box (large) (FR-05 to FR-07). |
| Recommendation | The packaging type BookPack proposes for a book. The packing employee may accept it or override it. |
| Override | The packing employee replacing the recommendation with a different type with a valid written reason (FR-11, FR-12). |
| FR / QR / CON | Functional requirement / quality requirement / constraint requirement (Section 3). |
| Flagged | A book that weighs over 5 lb, so it must be checked before it can be shipped (FR-08). |
| Inspection | The inspector's check of a flagged book and its packaging, recorded as pass or fail (FR-13). |
| Scale | The existing scale at the packing station. It sits outside the system boundary and is a «system» actor in the use case diagram. |
