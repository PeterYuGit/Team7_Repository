# P1 Section 3.5 Requirements to use case traceability

| Requirement ID | Use case(s) that realise it | If blank — why, and what you will do |
|---|---|---|
| FR-01 | UC-01 (step 3) | |
| FR-02 | UC-01 (alt. flow 3a) | |
| FR-03 | UC-01 (step 5) | |
| FR-04 | UC-01 (step 6) | |
| FR-05 | UC-01 (step 7) | |
| FR-06 | UC-01 (step 7) | |
| FR-07 | UC-01 (step 7) | |
| FR-08 | UC-01 (alt. flow 8a), the flag it sets is consumed by UC-03 | |
| FR-09 | UC-01 (step 4, alt. flow 4a) | |
| FR-10 | UC-01 (step 10) | |
| FR-11 | UC-02 Override Packaging Recommendation | |
| FR-12 | UC-02 Override Packaging Recommendation | |
| FR-13 | UC-03 (steps 5 and 6, alt. flows 5b and 6b) | |
| FR-14 | UC-03 (steps 1 and 2) | |
| FR-15 | UC-04 Review Shipping Record | |

*What the matrix revealed, and what you changed because of it:*

1. Use case numbering inconsistent. The expanded Inspect Flagged Book use case was labeled UC-02, but the diagram and UC-01's alternative flows call it UC-03. We renamed it UC-03 so the document matches the diagram.
2. UC-04 Review Shipping Record had no requirement behind it. This is the "use case nothing traces to" case: either it is out of scope or a requirement was never written. It is in scope (Section 1.2 permits employees to review shipping records, recommendations, and inspection results), so we added FR-15.
3. UC-03 steps 1 and 2 had no requirement behind them. The inspector's list of books awaiting inspection was not covered by any FR, so we added FR-14.
4. UC-01 realises ten of the fifteen requirements. This is acceptable because they are steps toward one goal, so we kept it as one use case rather than splitting it into step-level ones.
5. The failed-inspection path is undefined. UC-03 alt. flow 5b blocks a failed book, but no requirement says what happens next. We recorded this as open question Q4 instead of inventing a requirement.