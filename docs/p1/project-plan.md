# BookPack — P1 Section 4 Project Plan

## 4.1 Team roles and working agreement

| Team member | Confirmed role for P1 to P2 |
|---|---|
| Peter Yu | Team coordination, stakeholder information and references, packaging-threshold confirmation, and P2 submission review. |
| Patrick Paul | Purpose and scope, project planning and risks, repository documentation, document consistency, and final P2 review. |
| Nicholas Suther | Functional requirements, packaging classification and acceptance criteria, scale communication, and integration assessment. |
| Jasmine Tran | Nonfunctional requirements, measurement validation, traceability, and P2 design review. |
| Afeef Zarraf | System constraints, feasibility, use cases, shipping-record integration, and interface assessment. |
| Ahmet Keles | System context diagrams, assumptions and open questions, inspection workflow, and P2 architecture. |
| Lucas Pham | P2 user workflow and interface requirements review, including packing employee and inspector interactions. |

**Working agreement:** The team discusses work and disagreements in Discord and tracks assignments and decisions through GitHub Issues. Members seek consensus first; a majority vote is proposed if consensus cannot be reached. Stakeholder-dependent requirement changes need confirmation. All seven team members have confirmed their assigned roles for P1 to P2.

## 4.2 Plan to P2

| Date | What will be finished | Owner |
|---|---|---|
| October 22, 2026 | Review and finalize functional requirements FR-01 through FR-15, classification thresholds, and references. | Nicholas Suther, Jasmine Tran |
| October 27, 2026 | Review open questions Q1–Q4, contact stakeholders for clarification, and document any remaining assumptions. | Peter Yu, Ahmet Keles |
| November 1, 2026 | Evaluate scale connectivity, shipping record integration, and relevant system constraints. | Afeef Zarraf, Nicholas Suther, Lucas Pham |
| November 5, 2026 | Prepare P2 design documentation, including system architecture, interfaces, and updated requirements traceability. | Ahmet Keles, Jasmine Tran, Lucas Pham |
| November 8, 2026 | Review the P2 deliverable, verify documentation and repository consistency, and complete submission. | Patrick Paul, Peter Yu, all members |

## 4.3 Risks

| # | Risk | Likelihood | Impact | Mitigation — action and owner |
|---|---|---|---|---|
| R1 | The physical weighing scale may fail to communicate with BookPack. | Medium | High | Test the scale connection and verify weight transmission. Use manual weight entry if the connection fails. Owner: Nicholas Suther. |
| R2 | BookPack may incorrectly reject valid book measurements. | Medium | High | Test valid, invalid, and boundary measurements to verify input validation. Owner: Jasmine Tran. |
| R3 | Inspection personnel may be unavailable when a book requires inspection. | Medium | High | Confirm backup inspection personnel and hold flagged shipments until inspection is completed. Owner: Ahmet Keles. |
| R4 | BookPack may fail to automatically update shipping records after processing a book. | Medium | High | Test shipping record updates, verify saved information, and display an error when an update fails. Owner: Afeef Zarraf. |
| R5 | BookPack may recommend incorrect packaging due to inaccurate classification thresholds. | Medium | High | Confirm packaging thresholds with the bookstore and test recommendations against approved rules. Owner: Peter Yu |

## 4.4 Repository and tooling

https://github.com/PeterYuGit/Team7_Repository

All team members have access.

**Repository structure and version control:** BookPack uses `main` as its default and currently only branch. P1 documentation is stored under `docs/p1/`. Existing contributions to `main` are recorded in Git commits. The team has not confirmed a branch naming convention or pull-request requirement. Proposed for P2 (pending team agreement): descriptive commit messages, task-specific branches for larger changes, and pull-request reviews before merging.

**Issue tracking and communication:** The team uses Discord for discussion and GitHub Issues to assign owners, record section tasks, track progress with checklists, and link contribution evidence. Completed Issues #1, #2, and #3 are closed. Issue #4 is closed. Section 4 was committed to docs/p1/project-plan.md in commit c97934a.

**Instructor access:** The repository is public and can be viewed through the URL above without a team invitation. Direct confirmation that the instructor has opened it is still pending.

## 4.5 Declaration of AI tool use

| Tool | What it was used for | Who used it | How the output was checked |
|---|---|---|---|
| Claude (Anthropic) | Drafting functional requirements FR-01 to FR-13 and acceptance criteria; GitHub setup guidance | Nicholas Suther | Reviewed each requirement against the P1 testability rule (one “shall” sentence, pass/fail criterion); checked sources against Section 2.2; flagged assumed thresholds as open questions |
| ChatGPT (OpenAI) | Helped draft and refine Sections 1.1, 1.2, and 4.1–4.4, including repository and issue-tracking documentation, and prepare and review the GitHub documentation synchronization (references, UC-01, feasibility, C5). | Patrick Paul | Reviewed drafts against P1 instructions and BookPack requirements; corrected the FR-08 threshold, compared Google Docs with GitHub, reviewed the five-file diff, verified commits fcb7301 and c97934a, and updated team assignments after all members confirmed their roles. |
| Claude (Anthropic) | Drafting the context diagram, assumptions A2 to A5 and open questions Q1 to Q3 and guidance on committing them to GitHub | Ahmet Keles | Checked each item against the team’s functional requirements from Table 3.1, the use cases and the constraints, then edited the wording myself |
