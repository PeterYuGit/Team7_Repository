## 5.1 Domain Model

| Class | What it represents (one line) | Key attributes | Associations (with multiplicity) |
|---|---|---|---|
| **Book** | Physical book being shipped | title | Book `1` — `1` ShippingRecord |
| **Measurement** | Recorded book measurements | weight, length, width, thickness, weightSource | Measurement `0..1` — `1` ShippingRecord |
| **ShippingRecord** | Existing record tracking a book's shipment | orderNumber, valuableFlag, shippingStatus, inspectionStatus | ShippingRecord `1` — `1` Book; `1` — `0..1` Measurement; `1` — `0..1` PackagingDecision; `1` — `0..1` Inspection |
| **PackagingDecision** | Classification and packaging selection | sizeClass, recommendedType, chosenType, overrideReason | PackagingDecision `0..1` — `1` ShippingRecord; PackagingDecision `0..*` — `1` ShippingRules |
| **ShippingRules** | Business rules determining packaging classification and inspection requirements | smallWeightLimit, smallThicknessLimit, mediumWeightLimit, inspectionWeightLimit, maximumWeight | ShippingRules `1` — `0..*` PackagingDecision |
| **Inspection** | Inspection result for a flagged book | result, inspector, inspectionTime | Inspection `0..1` — `1` ShippingRecord |
