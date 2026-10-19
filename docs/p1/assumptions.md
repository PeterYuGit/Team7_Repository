# P1 Section 2.5 Assumptions and Dependencies

| # | Assumption or dependency | What breaks if it does not hold |
|---|---|---|
| A1 | Book measurements are accurate | System recommends wrong packaging |
| A2 | The scale at the packing station can connect to the computer so BookPack can read the weight automatically | Every weight has to be typed in by hand, which is slower and leads to more mistakes |
| A3 | Someone other than the packing employee is available to inspect heavy books during business hours | Flagged books wait with no one to check them, so they can't be shipped |
| A4 | The bookstore agrees with the weight and thickness limits we chose for each packaging type and for flagging a book | The size rules and packaging recommendations have to be rewritten and retested |
| A5 | Every book already has a shipping record before it reaches the packing station | BookPack would also have to create records, which makes the system bigger than planned |
