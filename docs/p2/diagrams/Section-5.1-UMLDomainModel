# BookPack Domain Model

## Section 5.1 — UML Domain Model

```mermaid
classDiagram
    direction TB

    class Book {
        title
    }

    class ShippingRecord {
        orderNumber
        valuableFlag
        shippingStatus
        inspectionStatus
    }

    class Measurement {
        weight
        length
        width
        thickness
        weightSource
    }

    class PackagingDecision {
        sizeClass
        recommendedType
        chosenType
        overrideReason
    }

    class Inspection {
        result
        inspector
        inspectionTime
    }

    class ShippingRules {
        smallWeightLimit
        smallThicknessLimit
        mediumWeightLimit
        inspectionWeightLimit
        maximumWeight
    }

    Book "1" -- "1" ShippingRecord : identified by
    ShippingRecord "1" -- "0..1" Measurement : stores
    ShippingRecord "1" -- "0..1" PackagingDecision : records
    ShippingRecord "1" -- "0..1" Inspection : has
    ShippingRules "1" -- "0..*" PackagingDecision : determines
```

Figure 5.1 — BookPack Conceptual Domain Model

The domain model shows the conceptual classes, attributes,
associations, and multiplicities used by BookPack.
