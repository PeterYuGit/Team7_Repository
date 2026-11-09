# 1. Introduction

## 1.1 Purpose of this document and of the system

This document establishes the analysis and high-level design baseline for **BookPack**, a software system that assists bookstore packing employees with book packaging and shipping decisions. It carries forward the P1 requirements and scope, records changes made in P2, and connects the required workflows to the proposed architecture, design decisions, and evidence for P3. Its intended readers are the development team, instructor, and bookstore stakeholders.

BookPack addresses inconsistent manual packaging decisions by recording each book's weight and dimensions, classifying it using the **weight and thickness thresholds** in Table 3.1, and recommending a cardboard mailer, padded mailer, or reinforced box. Length and width are still captured for the shipping record, but do not determine the classification tier under CH-03. Books marked as valuable in the existing shipping record receive a reinforced-box recommendation regardless of size class (FR-16).


The system flags heavy books for additional inspection before shipment, supports manual weight entry when a connected scale cannot provide a reading, and updates an existing shipping record with packaging and inspection information. The revised FR-08 acceptance criterion distinguishes manual entry from scale readings near 5.0 lb: a manually entered 5.0 lb must not be flagged and 5.1 lb must be flagged; a scale reading above 5.05 lb must be flagged, while readings within the scale's ±0.05 lb tolerance around 5.0 lb may be flagged (CH-01). The revised validation rule FR-09 is a MUST requirement (CH-02). These changes reflect the simulated scale evidence in spike S-01, not verification with the bookstore's actual scale. The actual scale protocol (Q3) and the **5.0 lb inspection threshold** remain open. The bookstore stakeholder approved the Table 3.1 classification thresholds (Q1).

## 1.2 Scope

| In scope — BookPack supports | Out of scope — BookPack does not |
|---|---|
| Read weight from a connected scale, with manual entry as a fallback (FR-01, FR-02). | Manufacture weighing hardware or require a new scale purchase. |
| Record weight in pounds plus manually entered length, width, and thickness in inches (FR-03, CON-02). | Measure dimensions automatically using cameras or sensors. |
| Classify Small, Medium, or Large using **bookstore-approved Table 3.1 thresholds** (FR-04, CH-03). | Use length and width as classification thresholds without an approved requirement change. |
| Recommend cardboard mailers, padded mailers, or reinforced boxes for the resulting class (FR-05–FR-07). | Physically pack books or operate packing machines. |
| Validate weight input and refuse to save book records for zero, negative, or values above 70 lb (FR-09, CON-01). | Manage transportation, shipment tracking, or carrier logistics. |
| Apply the revised heavy-book inspection rule and capture inspection outcomes (FR-08, FR-13, FR-14). | Automatically identify physical book damage. |
| Save packaging, weight, and inspection status into an **existing** shipping record and support review (FR-10, FR-15). | Build sales/payment functions or create missing shipping records (A5). |
| Retrieve valuable-book designation from an existing shipping record and recommend reinforced-box packaging regardless of size class (FR-16). | Determine monetary book value or designate books as valuable. |
| Allow documented packaging overrides when permitted (FR-11, FR-12). | Package multi-book shipments automatically or manage packing-material inventory. |

The boundary is the packing-station decision and recording workflow. It assumes an existing station computer and scale (CON-03/A2), an available inspector (A3/Q2), bookstore-approved classification thresholds (A4/Q1), a shipping record that already exists (A5), and existing shipping records may contain a valuable-book designation (FR-16). Unresolved assumptions are tracked separately rather than presented as confirmed.

## 1.3 Definitions, acronyms and abbreviations

The P1 definitions remain the baseline, with these P2 clarifications: **size class** means the Small/Medium/Large tier determined by weight and thickness only (CH-03); **flagged** means the FR-08 inspection status according to the manual-entry or scale-tolerance acceptance criterion (CH-01); **valuable-book designation** is an attribute retrieved from an existing shipping record indicating that a book requires reinforced-box packaging regardless of size classification. All other definitions in [`docs/p1/definitions.md`](../p1/definitions.md) are unchanged since the P1 baseline.

## 1.4 References

[R1] USPS shipping requirement https://www.usps.com/ship/packages.htm

[R2] Blog explaining book shipping costs https://goshippo.com/blog/how-to-ship-books-tips-and-best-practices-for-shipping-books

[R3] Student interview transcript https://docs.google.com/document/d/1TVzl55JsLxMukrQFq5bTf4vavkQTuQM04Xo0r75Nc60/edit?usp=sharing

[R4] Amazon packaging instructions https://sell.amazon.com/blog/fba-packaging-prep-labeling

[R5] Indeed shipping coordinator description https://sg.indeed.com/career-advice/finding-a-job/what-does-a-shipping-coordinator-do

*Unchanged since v0.8.*
