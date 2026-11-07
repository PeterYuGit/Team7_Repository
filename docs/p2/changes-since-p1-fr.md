# 0.2 Changes since the P1 baseline: functional requirement rows (Nicholas Suther)

These rows go into the team's 0.2 table. CH numbers will be assigned when the table is merged.

| Change ID | What changed (IDs affected) | Why (P1 feedback, new finding, spike result) | Knock-on effect | Agreed on |
|---|---|---|---|---|
| CH-xx | FR-08 acceptance criterion changed from "5.0 lb is not flagged; 5.1 lb is flagged" to: "Entered manually, 5.0 lb is not flagged and 5.1 lb is flagged. Read from the scale, any book over 5.05 lb is always flagged; a book within the scale's ±0.05 lb tolerance of 5.0 lb may be flagged." | Spike S-01: scale noise caused a 5.00 lb book to read just over 5.0 lb in 5 of 15 trials, so the old criterion cannot pass reliably. Extra inspection is the safe direction to be wrong in (student and bookstore needs in 2.2). | ADR-02 cites this; Q1 (flag limit) still open with the bookstore. | |
| CH-xx | FR-09 priority raised from SHOULD to MUST. | FR-09 enforces the same 70 lb limit as CON-01, which is non-negotiable (USPS). The two priorities contradicted each other. | None; FR-09 is already realized in UC-01 step 4 / alt 4a. | |
| CH-xx | Table 3.1 note added: classification uses weight and thickness only. FR-03 kept: length and width are still recorded for the shipping record and shown to the inspector (FR-14). UC-01 step 6 reworded from "dimension thresholds" to "the weight and thickness thresholds in Table 3.1". | Review found FR-03 collects length and width that no rule used, and UC-01 step 6 described the classification differently from Table 3.1. | UC-01 (section 4.2) and the domain model must use the same wording. | |
