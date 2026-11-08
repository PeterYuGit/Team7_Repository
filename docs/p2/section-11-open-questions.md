# P2 Section 11 Open Questions (updated; was P1 section 5)

Owner: Ahmet Keles

| ID | Question | Raised by | Owner and due date | Status or answer | Assumption meanwhile |
|---|---|---|---|---|---|
   | Q1 | What weight and thickness limits decide the packaging type, and is 5.0 lb the right flag limit? | P1 requirements | Peter, Nov 18 | Partly answered 11/05 by the owner by email (docs/p2/Stakeholder_Interview.md, PR #13): Table 3.1 thresholds approved; 5.0 lb flag limit not yet confirmed | Table 3.1 as approved; 5.0 lb flag limit as written; thresholds in rules.json (ADR-03) |
| Q2 | Is the inspector a different person from the packer, and always available? | P1 (A3) | Ahmet, Nov 18 | Open | A separate inspector during business hours |
| Q3 | Does the existing scale connect to the PC, and what does it send? | P1 (A2, CON-03) | Nicholas, Nov 18 | Partly answered: S-01 works on a simulated scale; real scale untested | Serial line format as in S-01, manual fallback (ADR-02) |
| Q4 | What happens to a book that fails inspection? | P1 (UC-03) | Ahmet, Nov 18 | Open | Returned for repackaging through UC-01 (UC-03 A2) |
| Q5 (new) | How does BookPack reach the existing shipping record system (API, database, export) and with what account? | Section 6.4 deployment | Ahmet, Nov 25 | Open | HTTPS over the store LAN, behind Record Gateway |
| Q6 (new) | Does the inspector use a packing-station PC or a separate computer? | Section 6.4 deployment | Ahmet, Nov 18 | Open | Station PC in the inspector role |
| Q7 (new) | Does the bookstore accept that a book read at exactly 5.0 lb on the scale may be flagged (CH-01)? | Spike S-01 / R7 | Peter, Nov 18 | Open | Extra inspection is acceptable |
