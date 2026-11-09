# UC-02 Override Packaging Recommendation (Section 4)
 
Owner: Nicholas Suther
 
## 4.1 row
 
| Use case | Name | Why it was selected | Non-trivial steps |
|---|---|---|---|
| UC-02 | Override Packaging Recommendation | The only path where the employee disagrees with the system; carries FR-11 and FR-12, the only rule that rejects an entry for being empty; interacts with the valuable-book exception (FR-16) | (4), (6) |
 
## 4.2 Expanded use case
 
**UC-02 Override Packaging Recommendation**
 
| Field | Entry |
|---|---|
| Primary actor | Packing Employee |
| Supporting actors and external systems | Existing shipping record system (external system) |
| TUCBW (this use case begins when) | The packing employee rejects the packaging BookPack recommended for the book being processed (UC-01 alternate flow 9a) |
| TUCEW (this use case ends when) | The packing employee sees confirmation that the chosen packaging and the reason were saved to the book's shipping record |
| Preconditions | The employee is processing a book in UC-01 and BookPack has shown a recommended packaging type for it. |
| Postconditions | The shipping record holds the packaging type the employee chose, in place of the recommendation, together with the written reason. The book's inspection status is unchanged. |
| Traces to requirements | FR-11, FR-12, FR-10; FR-05 to FR-07 and FR-16 (the recommendation being overridden) |
 
| Actor input / action | System response |
|---|---|
| | (0) The system shows the recommended packaging type with the book's size class, weight and thickness, and offers the choice to use a different packaging type. |
| (1) The packing employee asks to use a different packaging type. | (2) The system shows the other packaging types and asks for a reason. |
| (3) The packing employee chooses a packaging type and writes the reason. | (4) The system shows the chosen packaging type and the reason and asks the employee to confirm. |
| (5) The packing employee confirms. | (6) The system saves the chosen packaging type and the reason to the shipping record in place of the recommendation and confirms that the override was saved. |
 
| Alternate flow | At step | Condition | What happens | Ends or rejoins at |
|---|---|---|---|---|
| A1 | (4) | The reason is empty | The system says a reason is required and saves nothing (FR-12) | Rejoins (3) |
| A2 | (3) | The employee chooses the packaging type that was already recommended | The system says this matches the recommendation and no override is needed | Ends; UC-01 continues at step 10 with the recommendation |
| A3 | (5) | The employee cancels | The system keeps the original recommendation and saves nothing | Ends; UC-01 continues at step 9 |
| A4 | (6) | The override cannot be saved to the shipping record | The system says the override was not saved and keeps the chosen type and reason on screen | Rejoins (5) |
 
## 4.3 Self-review log rows
 
| Use case | Check from the Lesson 13 review checklist | Defect found | How it was fixed |
|---|---|---|---|
| UC-02 | Step (0) present | UC-02 had no expansion in P1, so no step (0) existed | Added (0): the recommendation is shown with class, weight and thickness so the employee can judge it |
| UC-02 | Precondition or alternate flow | "The employee gives a reason" can be false during normal work | Kept out of the preconditions; handled as A1 (FR-12) |
| UC-02 | Real alternate flows | FR-11 does not say what happens if the employee picks the type that was already recommended | Added A2 (no override recorded) |
| UC-02 | Acknowledgment at end | None; (6) ends with a confirmation the employee can see | No defect |
| UC-02 | No technology | None; no screens, widgets or storage named | No defect |
| UC-02 | Traces to requirements | Whether an employee may override the reinforced box a valuable book receives (FR-16) is not specified | Not invented; raised as open question Q8 |
## 5.2.1 Object interaction model

(a) Non-trivial steps. Steps (2), (4), and (6) are non-trivial because they require the system to retrieve alternate packaging options, validate input, and persist override data to the shipping record. Steps (0) and (1) are initial displays and actor inputs; steps (3) and (5) are direct employee inputs/confirmations handled in-memory by the UI.

(b) Scenario table

| Step | Subject (who acts) | Subject action | Other data / objects | Object acted upon |
|---|---|---|---|---|
| 1 | Packaging Employee | asks to use a different packaging type | — | Packing Controller |
| 2 | PackingController | shows the other packaging types and asks for a reason | Packaging Decision | Packing Employee |
| 3 | Packaging Employee | chooses a packaging type and write the reason | chosen type, reason | Packing Controller |
| 4 | PackingController | shows the chosen packaging type and the reason and asks to confirm | chosen type, reason | Packing Employee |
| 5 | Packaging Employee | confirms  | confirmation | Packing Controller |
| 6 | PackingController | saves the chosen packaging type and reason to the shipping record | chosen type, reason | ShippingRecord |
| 7 | PackingController | confirms that the override was saved | confirmation | Packing Employee |

(c) Analysis sequence diagram

<img width="710" height="270" alt="seq-uc02" src="https://github.com/user-attachments/assets/6c7f0e27-ee3d-4e32-99a7-61d4c044333a" />


Figure 5.2.1  Analysis sequence diagram for UC-02; message numbers match the scenario table PackingController is an interaction object that controls UC-02.
 
## Section 11 row (new open question)
 
| ID | Question | Raised by | Owner and due date | Status or answer | Assumption meanwhile |
|---|---|---|---|---|---|
| Q8 (new) | May a packing employee override the reinforced box that a valuable book receives (FR-16)? | UC-02 analysis | Peter, Nov 18 | Open | The override is allowed but requires a reason, like any other override |
 
## Note for the domain model (5.1) and K1
 
Items named in the UC-02 actor column: packaging type and reason. The domain model needs these as attributes (for example on the packaging decision: recommended type, chosen type, override reason).
 
