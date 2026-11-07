# 2. Overall Description

## 2.1 Product perspective and system context

BookPack is a packing-station support system. It receives a book's weight from an external scale or an employee's manual entry, takes employee-entered length, width, and thickness, recommends packaging, requests inspection when the weight warrants it, and saves the result to an existing shipping record. The employee and inspector interact with BookPack directly; the scale and existing shipping-record store remain outside its boundary. Physical weighing, measuring, inspection, packing, delivery, payment, and tracking are not automated by BookPack.

The P1 [context diagram](../p1/context-diagram.png) describes these external actors and interfaces. Its high-level system boundary is unchanged since P1; P2 architecture diagrams and the interfaces in Sections 5–7 must preserve the same boundary. Under CH-03, only **weight and thickness** determine the packaging size class; all three dimensions are still recorded.

## 2.2 Stakeholders and sources

| Stakeholder | Role or primary need | Evidence / outstanding confirmation |
|---|---|---|
| Bookstore manager or owner | Reduce inconsistent packaging and unnecessary packing costs; confirm business thresholds. | P1 literature-based shipping/cost sources; **direct elicitation and Table 3.1 approval remain outstanding (Q1)**. |
| Packing employee | Obtain a usable packaging recommendation, enter measurements, and document any override. | P1 task analysis and published packaging guidance; validate workflow directly if an employee becomes available. |
| Inspector or shipping coordinator | Resolve flagged-book inspection before shipment proceeds. | P1 external job-role information; actual availability and separation of duties **unconfirmed (Q2/A3)**. |
| Student recipient | Receive an undamaged book. | One P1 student interview; this is not a substitute for bookstore requirements confirmation. |
| Development team and instructor | Analyze, implement, and assess a traceable design. | Course milestones, P1 instructor feedback, version-controlled evidence. |

The P1 stakeholder list is otherwise carried forward. The P1 instructor's C1 feedback called for more direct bookstore elicitation, so secondary sources must not be mistaken for completed stakeholder confirmation.

## 2.3 User characteristics

**Packing employee (primary user):** Uses the packing-station computer and scale, enters measurements, follows or overrides a recommendation with an explanation (FR-11/12), and processes books in succession. No specialized shipping-rule knowledge is assumed. **Inspector:** Records pass or fail for flagged books (FR-13). A flagged book remains pending until the required action is recorded (FR-08/14). Whether the bookstore has a separate inspector remains open (Q2). These roles are unchanged since P1; CH-01 and CH-03 affect the rules displayed in their workflows, not the identities of the actors.

## 2.4 Constraints

- **CON-01:** BookPack must not save a book whose recorded weight is greater than 70 lb.
- **CON-02:** Weight is stored in pounds, and length, width, and thickness in inches.
- **CON-03:** The system is intended to run with the packing station's existing computer and scale, without new hardware purchases. The physical scale/interface remains unverified (Q3).

These constraints are carried forward from P1. The CH-02 upgrade of FR-09 to MUST strengthens validation priority; it does not silently modify CON-01.

## 2.5 Assumptions and dependencies

| ID | Assumption | Consequence if false / P2 status |
|---|---|---|
| A1 | Book measurements entered or read are accurate. | Incorrect data leads to an incorrect recommendation; validate inputs and expose review. |
| A2 | The existing scale can communicate with the computer. | Manual weight entry becomes the only path; simulated S-01 is encouraging but **real hardware is untested (Q3)**. |
| A3 | Someone other than the packing employee can inspect flagged books. | Flagged shipments wait for a qualified person; unresolved (Q2). |
| A4 | The bookstore agrees to the Table 3.1 weight/thickness and heavy-book thresholds. | Rule changes, testing and possible design updates are required; **direct confirmation still needed (Q1)**. |
| A5 | A shipping record already exists for every book entering packing. | Additional record creation would exceed the defined scope; not independently verified. |

Assumption identifiers remain unchanged since P1. Design mitigation for A2 is documented in ADR-02 (direct reading with manual fallback), and S-01 provides simulated evidence only. Open-question status must be changed with actual stakeholder or hardware evidence.

## 2.6 Feasibility summary

**Technical:** Core classification, inspection status, and record updates are feasible with familiar application and database techniques; direct scale integration remains conditional on the actual device protocol (Q3). **Operational:** Feasibility depends on bookstore approval of thresholds and inspector availability (Q1/Q2). **Schedule:** P2 covers analysis and high-level design; P3 is due **December 9, 2026** and requires an agreed implementation/test plan. **Resource/economic:** The team assumes existing hardware and free development tools; operating-cost savings are plausible goals, **not measured results**. This assessment carries forward P1's conditional feasibility and incorporates ADR-02/S-01 without claiming the actual scale has been validated.
