# 10. Project Plan

## 10.1 Roles and working agreement

P1's assignment of responsibilities carries into P2 unless team members explicitly agree otherwise. Section 0.1 of the final report must record **actual P2 commits, pull requests, and reviews**, not merely these expected responsibilities.

| Member | P2 responsibility |
|---|---|
| Peter Yu | Team coordination, stakeholder information and references, classification-threshold confirmation, and submission review. |
| Patrick Paul | Purpose and scope, project planning and risks, repository documentation, document consistency, and final P2 review. |
| Nicholas Suther | Functional requirements, classification and acceptance criteria, and scale integration investigation. |
| Jasmine Tran | Quality requirements, measurement validation, traceability, and design review. |
| Afeef Zarraf | Constraints and feasibility, use cases, shipping-record integration, and interfaces. |
| Ahmet Keles | Context diagrams, assumptions/open questions, inspection flow, and architecture. |
| Lucas Pham | Packing-employee and inspector workflows and interface review. |

**Communication and meetings:** The team initially planned to meet once per week, but routine coordination evolved into **asynchronous Discord messages** and repository/issue discussions. Members raise blockers and review one another's work asynchronously. **Synchronous meetings are arranged when needed** for unresolved design choices, deadlines, or coordination; a weekly synchronous meeting has not consistently occurred. This reflects actual practice rather than implying meetings were held each week.

The working agreement remains to seek consensus, escalate unresolved decisions to the team, and document changes affecting requirements or architecture. A majority vote can resolve an internal disagreement, but it cannot substitute for bookstore approval of stakeholder-dependent assumptions such as Q1. For P2 contributions, Patrick proposes a branch and pull request per independently reviewable section, a teammate review, and merging only once comments have been addressed. Previous P1 commits went directly to `main`; use actual PR history, not the proposed process, as evidence in Section 0.1.

## 10.2 Plan to P3

The confirmed course deadline for P3 is **December 9, 2026**. The internal milestones below are a **proposed** schedule for team review, with owners and completion conditions; they are not reported as commitments already approved by all members.

| Proposed milestone | Target date | Proposed owner(s) | Done when |
|---|---|---|---|
| Triage instructor P2 feedback and assign changes | Nov. 12 | Peter, Patrick, section owners | Each instructor comment has an owner, a decision, and a tracked action or reason for retaining current design. |
| Seek direct bookstore input and validate actual scale access | Nov. 18 | Peter (stakeholder contact), Nicholas (scale) | Q1 and Q3 have evidence-backed answers or documented escalation; actual device messages are collected and tested if available. |
| Finish P3 detailed design and interfaces | Nov. 25 | Ahmet, Lucas, Afeef; Jasmine for traceability | Detailed components, external interfaces, and major user flows trace to P2 design and relevant FR IDs. |
| Integrate priority workflows | Dec. 2 | Implementation owners to be agreed | Weight capture/manual fallback, classification, inspection status and existing-record updates work end-to-end against approved criteria. |
| Run verification and boundary tests | Dec. 5 | Jasmine, Nicholas, implementation owners | FR-08/09 edge cases, failures, relevant QR cases and persistence are tested and recorded; defects have owners. |
| Freeze and review submission candidate | Dec. 8 | Patrick, Peter, all members | Document, diagrams, code/evidence, individual contribution record and exported PDF are consistent and reviewed. |
| Submit P3 | Dec. 9 (official deadline) | Canvas submitter to be designated | Required files and milestone-specific Git tag are checked and one submission is made before the course cutoff. |

## 10.3 Updated risk register

P1's risks R1–R5 remain identifiable. Spike S-01 tested a **simulated** scale, so it reduces uncertainty but does not establish real-device compatibility. The likelihood/impact judgments and new risks R6/R7 are **proposals** for team confirmation.

| Risk and owner | Current status, likelihood / impact | Mitigation and evidence |
|---|---|---|
| **R1 — Scale cannot communicate** (Nicholas) | Partly mitigated but open; Medium / High. S-01 observed stable simulated messages and fallback; actual scale Q3 remains untested. | Test the bookstore's device and format; isolate parser behind interface; keep manual fallback under ADR-02; record failures and FR-01/02 tests. |
| **R2 — Valid measurements incorrectly rejected** (Jasmine) | Open; Medium / High. P2 changes FR-08/09 and S-01 does not verify full validation. | Test negative, zero, 70 and over-70 lb, manual 5.0/5.1 and scale tolerance edges; ensure rejected data are not saved. |
| **R3 — Inspector unavailable** (Ahmet) | Open; Medium / High. A3/Q2 not verified. | Confirm staffing with bookstore; keep flagged books pending rather than mark them shippable without inspection (FR-13/14). |
| **R4 — Shipping records not updated reliably** (Afeef) | Open; Medium / High. No completed end-to-end persistence test is documented in existing P2 evidence. | Test successful and failed writes, recovery and stored weight/packaging/inspection values; record how missing records are handled under A5 (FR-10/15). |
| **R5 — Packaging thresholds do not match bookstore need** (Peter) | Open; Medium / High. Table 3.1 is assumed; P1 instructor requested direct stakeholder elicitation (Q1/A4). | Obtain direct threshold approval or documented revisions; Nicholas/Jasmine update FR-04/08 tests using approved change control. |
| **R6 — Device protocol lock-in** (Nicholas) | New risk from ADR-02; Medium / High. Direct scale reading depends on specific message format. | Obtain real-device samples; keep transport/parser separated from classification; test disconnect/reconnect and fallback (Q3, S-01). |
| **R7 — Weight noise triggers avoidable inspections** (Jasmine/Nicholas) | New operational risk; Medium / Medium. In S-01, 5 of 15 simulated 5.00 lb readings exceeded the nominal 5.0 threshold. | Verify CH-01's tolerance and manual-vs-scale acceptance cases; log unnecessary flags and seek stakeholder approval (Q1). |

No risk is marked closed without evidence. Record status changes in the P2 revision log and link corresponding FR, QR, ADR or spike results where relevant.

## 10.4 Repository and collaboration

The public team repository is **https://github.com/PeterYuGit/Team7_Repository**. P1 sources are in `docs/p1/`; current P2 source contributions belong in `docs/p2/`, including design decisions and section files; the source for P2 diagrams should be placed in `docs/p2/diagrams/`; prototypes and test evidence belong under `spikes/` (currently `spikes/S-01-scale-read/`). Documentation should use relative links and preserve the canonical FR, QR, CON, UC, CH, ADR and risk IDs.

For remaining P2 work, the team follows a branch-based contribution process: one feature/section branch per coherent contribution, a pull request into `main`, a meaningful teammate review, and documented resolution before merging. Each person's row in Section 0.1 must link to actual contribution evidence.

**Final submission check (required, not yet complete):** Assemble sections 0–12 and the supporting diagrams into one P2 PDF, commit the final PDF and editable diagram sources, and create the `p2` Git tag pointing to the commit that contains that PDF. Verify the tag, public/instructor repository access, and correct Canvas upload.

## 10.5 AI tool-use disclosure

The final document discloses each person's actual AI-tool usage, scope, and independent checks. The following entries document known usage for the listed contributors.

| Contributor | Tool | Purpose | Human verification required |
|---|---|---|---|
| Patrick Paul | ChatGPT (OpenAI) | Helped draft P2 sections 1, 2 and 10, identify inconsistencies and prepare document/repository review. | Patrick reviews wording, checks FR/CH references, resolves assumptions, and verifies final files and review evidence before use. |
| Patrick Paul | Strata / local Qwen3.8-Flash-Next | Inspected repository content and suggested P2 duties and missing deliverables. | Patrick checks conclusions against actual repository files and records any additional use truthfully. |
| Patrick Paul | Hermes Agent (Nous Research) | Reviewed and modified P2 documentation, performed repository operations, and verified changes against P1 baselines. | Patrick verifies documentation changes and Git operations before export. |
| Nicholas Suther | Claude (Anthropic) | P2 template credits assistance with scale spike S-01, README, ADR-02 and change rows. Nicholas ran the scale spike personally and updated results using his own timings. | Nicholas verifies prototype run logs, calculations, outputs, authorship and final description. |

Each other contributor must add an accurate row if an AI tool was used, or confirm no use as the course requires. Do not substitute a teammate's guess for an actual disclosure.
