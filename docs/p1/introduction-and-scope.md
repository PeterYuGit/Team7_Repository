# BookPack — Introduction and Scope

## 1.1 Purpose of this document and of the system

The purpose of this document is to present the initial proposal and requirements for BookPack, an automated book packaging and shipping management system. It is intended for the project development team, instructors, and stakeholders to understand the system's goals, scope, functional and nonfunctional requirements, and expected capabilities. This document will serve as a baseline for future development and help ensure that the system meets the needs of its users.

BookPack is designed to help shipping facilities determine the appropriate packaging for books based on their weight and size. Currently, packaging decisions may rely on employees manually determining which materials and inspections are necessary, leading to inconsistent packaging, wasted materials, or potential damage during shipping. The system aims to improve this process by recommending cardboard mailers for smaller, lighter books and more protective packaging for larger, heavier books. Books weighing more than 5.0 lb will be flagged for additional inspection before shipping. BookPack will also update packaging information in shipping records to improve accuracy and efficiency.

## 1.2 Scope

| In scope — we will build this | Out of scope — we will not, and why |
|---|---|
| Record the weight of each book using a connected scale or manual input. | Manufacture or develop the physical weighing scale, since the focus is on software. |
| Classify books based on weight and dimensions. | Automatically measure book dimensions using cameras or sensors, due to additional hardware requirements. |
| Recommend appropriate packaging, such as cardboard mailers, padded mailers, or reinforced boxes. | Physically package books or operate automated packaging machinery, since this requires mechanical equipment. |
| Flag books weighing more than 5.0 lb for additional inspection before shipping. | Automatically inspect books for physical damage, since this requires advanced detection technology. |
| Update shipping records with the book's weight, packaging type, and inspection status. | Manage carrier delivery, shipment tracking, or transportation logistics, since these are handled by external shipping services. |
| Allow employees to review packaging recommendations and inspection results. | Process customer payments or calculate shipping charges, since these are outside the packaging decision process. |

These features were excluded to keep the project focused on improving packaging decisions and shipping record management rather than developing physical automation equipment or a complete shipping service. Limiting the scope allows the team to develop and evaluate the core software functionality within the available project timeline and resources.
