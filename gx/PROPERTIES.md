# Properties of SHACL Files in this folder

## Prefixes

- dcat: <http://www.w3.org/ns/dcat#>
- dcterms: <http://purl.org/dc/terms/>
- gx: <https://w3id.org/gaia-x/development/>
- odrl: <http://www.w3.org/ns/odrl/2/>
- schema: <https://schema.org/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| http://qudt.org/schema/qudt/floatPercentageShape | gx | value |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| http://qudt.org/vocab/QuantityKindShape |  | http://qudt.org/vocab/unit | 1 | 1 | Unit of physical quantity. See https://qudt.org/schema/qudt/Unit | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| http://qudt.org/vocab/QuantityKindShape |  | http://qudt.org/vocab/value | 1 | 1 | Value of physical quantity. See https://qudt.org/schema/qudt/value | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| http://qudt.org/vocab/quantitykind/DataRateShape |  | http://qudt.org/vocab/value | 1 | 1 | Value of physical quantity. See https://qudt.org/schema/qudt/value | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| http://qudt.org/vocab/quantitykind/DataRateShape |  | http://qudt.org/vocab/unit | 1 | 1 | Unit of physical quantity. See https://qudt.org/schema/qudt/Unit | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| http://qudt.org/vocab/quantitykind/FrequencyDefinitionShape |  | http://qudt.org/vocab/unit | 1 | 1 | Unit of physical quantity. See https://qudt.org/schema/qudt/Unit | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| http://qudt.org/vocab/quantitykind/FrequencyDefinitionShape |  | http://qudt.org/vocab/value | 1 | 1 | Value of physical quantity. See https://qudt.org/schema/qudt/value | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| http://qudt.org/vocab/quantitykind/PowerShape |  | http://qudt.org/vocab/value | 1 | 1 | Value of physical quantity. See https://qudt.org/schema/qudt/value | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| http://qudt.org/vocab/quantitykind/PowerShape |  | http://qudt.org/vocab/unit | 1 | 1 | Unit of physical quantity. See https://qudt.org/schema/qudt/Unit | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| http://qudt.org/vocab/quantitykind/TimeShape |  | http://qudt.org/vocab/value | 1 | 1 | Value of physical quantity. See https://qudt.org/schema/qudt/value | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| http://qudt.org/vocab/quantitykind/TimeShape |  | http://qudt.org/vocab/unit | 1 | 1 | Unit of physical quantity. See https://qudt.org/schema/qudt/Unit | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | dcat | packageFormat |  | 1 | The package format of the distribution in which one or more data files are grouped together | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | dcat | byteSize |  | 1 | Size of the dataset distribution | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | gx | hashAlgorithm |  | 1 | Algorithm used to create the hash. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | gx | dataLicensors |  |  | A list of Licensors either as a free form string or participant self-description. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DistributionShape | gx | dataUsageAgreements |  |  | List of authorizations from the data subjects as Natural Person when the dataset contains PII, as defined by the Trust Framework | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DistributionShape | dcterms | license |  |  | A list of URIs to license documents. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | gx | expirationDateTime |  | 1 | Date time in ISO 8601 format after which data is expired and shall be deleted. | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| DistributionShape | dcterms | issued |  | 1 | Publication date in ISO 8601 format | <http://www.w3.org/2001/XMLSchema#date> | gx_shacl.ttl |
| DistributionShape | gx | location |  |  | List of dataset storage locations | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | dcterms | title | 1 | 1 | Title of the Distribution. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | dcterms | format | 1 | 1 | Format of the dataset distribution (PDF, CSV, …) | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | gx | hash |  | 1 | To uniquely identify the data contained in the dataset distribution. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | dcterms | language |  | 1 | Language | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DistributionShape | dcat | compressFormat |  | 1 | The compression format of the distribution in which the data is contained in a compressed form | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| AgreementShape | odrl | profile |  | 1 | Profile information for the policy. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| AgreementShape | odrl | inheritFrom |  | 1 | Indicates inheritance from another policy. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| AgreementShape | odrl | assigner | 1 | 1 | Party assigning a responsibility. |  | gx_shacl.ttl |
| AgreementShape | odrl | permission |  |  | Defines a permission. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| AgreementShape | odrl | assignee | 1 | 1 | Party assigned a responsibility. |  | gx_shacl.ttl |
| AgreementShape | odrl | prohibition |  |  | Defines a prohibition. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| AgreementShape | odrl | obligation |  |  | Defines an obligation. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| AgreementShape | odrl | uid |  | 1 | Unique identifier for policies. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| AssetShape | odrl | AssetCollection |  | 1 | A collection of assets. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| AssetShape | odrl | uid |  | 1 | Unique identifier for policies. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConflictTermShape | odrl | prohibit |  | 1 | Prohibition in conflict. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConflictTermShape | odrl | perm |  | 1 | Permission in conflict. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConflictTermShape | odrl | invalid |  | 1 | Invalid state. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConflictTermShape | odrl | conflict |  | 1 | Conflict strategy. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperandsShape | odrl | or |  | 1 | Or operand. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperandsShape | odrl | andSequence |  | 1 | Logical AND sequence operand. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperandsShape | odrl | xone |  | 1 | Logical XOR operand. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperandsShape | odrl | and |  | 1 | And operand. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | isA |  | 1 | Relationship of type. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | lt |  | 1 | Less than operator. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | lteq |  | 1 | Less than or equal to operator. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | hasPart |  | 1 | Has part relationship. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | neq |  | 1 | Not equal to operator. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | isNoneOf |  | 1 | Is none of a. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | gteq |  | 1 | Greater than or equal to operator. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | isPartOf |  | 1 | Is part of relationship. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | gt |  | 1 | Greater than operator. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | isAnyOf |  | 1 | Is any of a. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | isAllOf |  | 1 | Is all of a set relationship. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintOperatorsShape | odrl | eq |  | 1 | Equals operator. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintShape | odrl | operator |  | 1 | Constraint operator. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintShape | odrl | rightOperand |  | 1 | Right operand in constraint. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintShape | odrl | rightOperandReference |  | 1 | Reference to the right operand. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintShape | odrl | leftOperand |  | 1 | Left operand. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConstraintShape | odrl | refinement |  | 1 | A constraint refinement. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DutyShape | odrl | action | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DutyShape | odrl | function |  | 1 | Function description in rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DutyShape | odrl | target |  |  |  |  | gx_shacl.ttl |
| DutyShape | odrl | assigner |  | 1 | Party assigning a responsibility. |  | gx_shacl.ttl |
| DutyShape | odrl | failure |  | 1 | Failure conditions in rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DutyShape | odrl | consequence |  | 1 | Defines a consequence. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DutyShape | odrl | remedy |  | 1 | Defines a remedy for unmet duties. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DutyShape | odrl | relation |  | 1 | Describes relationships between rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DutyShape | odrl | constraint |  |  |  | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DutyShape | odrl | obligation |  |  | Defines an obligation. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DutyShape | odrl | logicalConstraint |  |  |  | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DutyShape | odrl | assignee |  | 1 | Party assigned a responsibility. |  | gx_shacl.ttl |
| DutyShape | odrl | duty |  |  | Defines a duty. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LogicalConstraintShape | odrl | operand |  | 1 | Logical operand used in constraints. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| OfferShape | odrl | uid |  | 1 | Unique identifier for policies. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| OfferShape | odrl | inheritFrom |  | 1 | Indicates inheritance from another policy. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| OfferShape | odrl | permission |  |  | Defines a permission. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| OfferShape | odrl | obligation |  |  | Defines an obligation. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| OfferShape | odrl | profile |  | 1 | Profile information for the policy. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| OfferShape | odrl | prohibition |  |  | Defines a prohibition. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| OfferShape | odrl | assigner |  | 1 | Party assigning a responsibility. |  | gx_shacl.ttl |
| PartyShape | odrl | assignee |  | 1 | Party assigned a responsibility. |  | gx_shacl.ttl |
| PartyShape | odrl | assigneeOf |  | 1 | Role of assignee in a policy. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PartyShape | odrl | uid |  | 1 | Unique identifier for policies. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PartyShape | odrl | assigner |  | 1 | Party assigning a responsibility. |  | gx_shacl.ttl |
| PartyShape | odrl | assignerOf |  | 1 | Role of assigner in a policy. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PartyShape | odrl | PartyCollection |  | 1 | A collection of parties. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PermissionShape | odrl | duty |  |  | Defines a duty. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PermissionShape | odrl | permission |  |  | Defines a permission. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PermissionShape | odrl | constraint |  |  |  | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PermissionShape | odrl | failure |  | 1 | Failure conditions in rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PermissionShape | odrl | logicalConstraint |  |  |  | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PermissionShape | odrl | assigner |  | 1 | Party assigning a responsibility. |  | gx_shacl.ttl |
| PermissionShape | odrl | function |  | 1 | Function description in rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PermissionShape | odrl | relation |  | 1 | Describes relationships between rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PermissionShape | odrl | target | 1 |  |  |  | gx_shacl.ttl |
| PermissionShape | odrl | action | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PermissionShape | odrl | assignee |  | 1 | Party assigned a responsibility. |  | gx_shacl.ttl |
| PolicyShape | odrl | inheritFrom |  | 1 | Indicates inheritance from another policy. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PolicyShape | odrl | prohibition |  |  | Defines a prohibition. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PolicyShape | odrl | profile |  | 1 | Profile information for the policy. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PolicyShape | odrl | obligation |  |  | Defines an obligation. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PolicyShape | odrl | uid |  | 1 | Unique identifier for policies. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PolicyShape | odrl | permission |  |  | Defines a permission. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ProhibitionShape | odrl | target | 1 |  |  |  | gx_shacl.ttl |
| ProhibitionShape | odrl | logicalConstraint |  |  |  | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ProhibitionShape | odrl | function |  | 1 | Function description in rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ProhibitionShape | odrl | action | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ProhibitionShape | odrl | relation |  | 1 | Describes relationships between rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ProhibitionShape | odrl | failure |  | 1 | Failure conditions in rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ProhibitionShape | odrl | assignee |  | 1 | Party assigned a responsibility. |  | gx_shacl.ttl |
| ProhibitionShape | odrl | duty |  |  | Defines a duty. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ProhibitionShape | odrl | constraint |  |  |  | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ProhibitionShape | odrl | assigner |  | 1 | Party assigning a responsibility. |  | gx_shacl.ttl |
| ProhibitionShape | odrl | prohibition |  |  | Defines a prohibition. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| RuleShape | odrl | assignee |  | 1 | Party assigned a responsibility. |  | gx_shacl.ttl |
| RuleShape | odrl | action | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| RuleShape | odrl | failure |  | 1 | Failure conditions in rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| RuleShape | odrl | duty |  |  | Defines a duty. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| RuleShape | odrl | function |  | 1 | Function description in rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| RuleShape | odrl | logicalConstraint |  |  |  | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| RuleShape | odrl | constraint |  |  |  | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| RuleShape | odrl | assigner |  | 1 | Party assigning a responsibility. |  | gx_shacl.ttl |
| RuleShape | odrl | relation |  | 1 | Describes relationships between rules. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SetShape | odrl | inheritFrom |  | 1 | Indicates inheritance from another policy. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SetShape | odrl | profile |  | 1 | Profile information for the policy. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SetShape | odrl | permission |  |  | Defines a permission. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| SetShape | odrl | uid |  | 1 | Unique identifier for policies. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SetShape | odrl | prohibition |  |  | Defines a prohibition. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| SetShape | odrl | obligation |  |  | Defines an obligation. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| AccessControlManagementShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| AccessControlManagementShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| AccessControlManagementShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| AccessControlManagementShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| AccessUsagePolicyShape | gx | policyLanguage | 1 | 1 | The language in which the policy is expressed (e.g., ODRL, XACML, Rego, JSON-based policies). |  | gx_shacl.ttl |
| AccessUsagePolicyShape | gx | policyDocument | 1 | 1 | A link to the actual policy or the content of the policy itself.
 |  | gx_shacl.ttl |
| AddressShape |  | https://www.w3.org/2006/vcard/ns#locality |  | 1 | The locality (e.g. city or town) associated with the address. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| AddressShape |  | https://www.w3.org/2006/vcard/ns#street-address |  | 1 | The street address of a postal address. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| AddressShape | gx | gps |  |  | GPS in ISO 6709:2008/Cor 1:2009 format. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| AddressShape |  | https://www.w3.org/2006/vcard/ns#postal-code |  | 1 | The local postal code of the address. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| AddressShape | gx | countryCode | 1 | 1 | Country code in ISO 3166-1 alpha2, alpha-3 or numeric format. |  | gx_shacl.ttl |
| AddressShape | gx | countryName |  | 1 | The name of the country. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| AddressShape | gx | region |  | 1 | The NUTS2 region code of the geographical location. |  | gx_shacl.ttl |
| AssetsManagementShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| AssetsManagementShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| AssetsManagementShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| AssetsManagementShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| AvailabilityShape | gx | metric | 1 | 1 | Availability expressed as time. |  | gx_shacl.ttl |
| AvailabilityShape | gx | guaranteed |  | 1 | Minimum percentage of time where a performance-level is guaranteed to be met. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| AvailabilityZoneShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| AvailabilityZoneShape | gx | address |  | 1 | The physical address associated with the availability zone | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| AvailabilityZoneShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| AvailabilityZoneShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BackupPolicyShape | gx | protectionRetention | 1 | 1 | How long captured/protected data are kept available. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BackupPolicyShape | gx | protectionMethod |  | 1 | Method used to protect data, can be be full copy, incremental,... |  | gx_shacl.ttl |
| BackupPolicyShape | gx | backupLocation | 1 |  | Where are located data backups | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BackupPolicyShape | gx | backupReplication |  |  | Backups replication policy, if any | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BackupPolicyShape | gx | protectionFrequency | 1 | 1 | Frequency at which data are captured/protected. |  | gx_shacl.ttl |
| BandWidthShape | gx | guaranteed |  | 1 | Minimum percentage of time where a performance-level is guaranteed to be met. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BandWidthShape | gx | metric | 1 | 1 | Data rate expressing bandwidth. |  | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | instantiationReq | 1 |  | Set of bare metal server flavors available for this service offering. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | tenantSeparation |  | 1 | How compute resources of different tenants are separated. Default value = hw-virtualized. |  | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | codeArtifact | 1 |  | Set of available bare metal server images for this service offering. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BareMetalServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BaseContainerImageShape | gx | containerImageLink | 1 | 1 | Link to the image's repository | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| BaseContainerImageShape | gx | containerImageTag |  |  | Tag(s) associated with a container image | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BlockStorageConfigurationShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BlockStorageConfigurationShape | gx | storageRedundancyMechanism |  |  | Underlying data protection mechanism (such as RAID levels or Erasure Codes). |  | gx_shacl.ttl |
| BlockStorageConfigurationShape | gx | storageQoS |  |  | Available QoS class for storage service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageConfigurationShape | gx | blockStorageTechnology |  |  | Underlying storage technology type to be used |  | gx_shacl.ttl |
| BlockStorageConfigurationShape | gx | storageProtection |  |  | Available data protection features. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageConfigurationShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BlockStorageConfigurationShape | gx | storageDeduplication |  |  | Deduplication features available for the storage service, such as inline or post-processing. |  | gx_shacl.ttl |
| BlockStorageConfigurationShape | gx | blockSize |  |  | Available block size to be used. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageConfigurationShape | gx | lowLevelBlockAccessProtocol |  |  | Underlying low level access protocol for the storage service to be used. These are various methods to access the storage technology. Some examples anbd references - https://www.enterprisestorageforum.com/hardware/nvme-vs-sata-comparing-storage-technologies/ |  | gx_shacl.ttl |
| BlockStorageConfigurationShape | gx | storageCompression |  |  | Available compression features. |  | gx_shacl.ttl |
| BlockStorageConfigurationShape | gx | storageEncryption | 1 |  | Available encryption features. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | versioning |  | 1 | Whether versioning is available on this storage service. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | multipleViews |  | 1 | Capability for multiple views. For example is it possible to view Objects as Files, or the other way around | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | dataViews |  | 1 | Capability to compose logical data views and present the subset of the data as a logical data entity | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | storageConsistency |  | 1 | Consistency model provided. See https://en.wikipedia.org/wiki/Consistency_model |  | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | storageConfiguration | 1 | 1 | Attributes that are configurable at service instantiation. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | minimumSize |  | 1 | Minimum Capacity (expressed as value + unit) supported by the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | maximumSize |  | 1 | Maximum Capacity (expressed as value + unit) supported by the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | lifetimeManagement |  | 1 | Lifetime (in hours) of data (since last access), before it is moved externally, archived or deleted and will not be accessible through the storage service. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| BlockStorageServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| BusinessContinuityMeasuresShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| BusinessContinuityMeasuresShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| BusinessContinuityMeasuresShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| BusinessContinuityMeasuresShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| CPUShape | gx | cpuArchitecture |  | 1 | Architecture of CPU as defined per .name string of structure static const X86CPUDefinition builtin_x86_defs[] defined in https://gitlab.com/qemu-project/qemu/-/blob/master/target/i386/cpu.c. Non-listed architectures to be designated as 'other' |  | gx_shacl.ttl |
| CPUShape | gx | baseFrequency |  | 1 | Base frequency of the CPU. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| CPUShape | gx | numberOfCores |  | 1 | Number of cores of the CPU. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| CPUShape | gx | lastLevelCacheSize |  | 1 | Last Level Cache size of the CPU. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| CPUShape | gx | vendor |  | 1 | Vendor of the device. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CPUShape | gx | boostFrequency |  | 1 | Boost frequency of the CPU. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| CPUShape | gx | generation |  | 1 | Vendor specific generation of the device. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CPUShape | gx | smtEnabled |  | 1 | Is simultaneous multithreading (SMT) or hyper threading (HT) active in this CPU? Default "False". | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| CPUShape | gx | cpuFlag |  |  | CPU flags as documented by lscpu and defined in https://github.com/torvalds/linux/blob/master/tools/arch/x86/include/asm/cpufeatures.h. Non-listed flags to be designated as 'other'. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CPUShape | gx | thermalDesignPower |  | 1 | CPU Thermal Design Power. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| CPUShape | gx | defaultOversubscriptionRatio |  | 1 | Over-subscription means assigning more capacity to virtual machines that the physical device has. Default over-subscription ratio defines the amount of default over-subscription as a value larger or equal to 1.0. 1.0 means no over-subscription. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| CPUShape | gx | numberOfThreads |  | 1 | Number of threads of the CPU. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| CPUShape | gx | supportedOversubscriptionRatio |  | 1 | Over-subscription means assigning more capacity to virtual machines that the physical device has. Supported over-subscription ratio defines the amount of supported over-subscription as a value larger or equal to 1.0. 1.0 means no over-subscription. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| ChangeAndConfigurationManagementShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| ChangeAndConfigurationManagementShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| ChangeAndConfigurationManagementShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| ChangeAndConfigurationManagementShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| CheckSumShape | gx | checkSumCalculation | 1 | 1 | Algorithm used to create checksum. |  | gx_shacl.ttl |
| CheckSumShape | gx | checkSumValue | 1 | 1 | Value of the check sum. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CodeArtifactShape | gx | signature |  | 1 | Details with respect to signature of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| CodeArtifactShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| CodeArtifactShape | gx | checkSum |  | 1 | Details on checksum of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| CodeArtifactShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CodeArtifactShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CodeArtifactShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CodeArtifactShape | gx | version |  | 1 | Version of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CodeArtifactShape | gx | patchLevel |  | 1 | Software specific patch number describing patch level of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CodeArtifactShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| CodeArtifactShape | gx | buildDate |  | 1 | Date and time the software was build, formated according to ISO 8601 (UTC - 24 hours). | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| CodeArtifactShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| ComplianceAssuranceShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| ComplianceAssuranceShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| ComplianceAssuranceShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| ComplianceAssuranceShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| CompliantCredentialShape | gx | credentialType | 1 | 1 | Type of the compliant credential. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CompliantCredentialShape |  | https://www.w3.org/2018/credentials#digestSRI | 1 | 1 | Subresource Integrity hash of the verifiable credential ensuring it has won't be modified. | <https://www.w3.org/2018/credentials#sriString> | gx_shacl.ttl |
| ComputeFunctionConfigurationShape | gx | computeFunctionSDK |  |  | SDKs provided to ease function development | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionConfigurationShape | gx | computeFunctionRuntime | 1 |  | Available runtime for executing function | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionConfigurationShape | gx | confidentialComputingTechnology |  | 1 | Details with respect to confidential computing requirements | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionConfigurationShape | gx | computeFunctionDeploymentMethod |  |  | Supported methods for importing/deploying compute function code |  | gx_shacl.ttl |
| ComputeFunctionConfigurationShape | gx | computeFunctionQuotas |  |  | Quotas available for compute functions | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionConfigurationShape | gx | computeFunctionLibrary |  |  | Library of compute function templates available | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionConfigurationShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionConfigurationShape | gx | computeFunctionTrigger |  |  | Available trigger for starting function execution | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionConfigurationShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionQuotasShape | gx | functionRequestSizeLimit |  | 1 | Maximum size for incoming request (or triggering event) for a function | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionQuotasShape | gx | functionMemoryLimit |  | 1 | Maximum amount of memory usable by a function | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionQuotasShape | gx | functionSizeLimit |  | 1 | Maximum size of a deployed function | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionQuotasShape | gx | functionStorageLimit |  | 1 | Storage limit for deployed functions | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionQuotasShape | gx | functionMaximumNumber |  | 1 | Maximum number of functions that can be created. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| ComputeFunctionQuotasShape | gx | functionConcurrencyLimit |  | 1 | Maximum number of concurrent execution of a function | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| ComputeFunctionQuotasShape | gx | functionResponseSizeLimit |  | 1 | Maximum size for a function response | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionQuotasShape | gx | functionTimeLimit |  | 1 | Maximum execution time for a function | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionRuntimeShape | gx | supportedVersion | 1 |  | Supported version for Runtime language | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionRuntimeShape | gx | supportedLanguage | 1 | 1 | Language for writing compute function |  | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | computeFunctionAllowTimeout |  | 1 | Indicates whether the service allows to define timeouts for functions | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | computeFunctionAllowAutoScaling |  | 1 | Indicates whether the service supports auto-scaling of functions | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | computeFunctionEditor |  | 1 | Indicates whether the service includes a code editor. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | computeFunctionConfiguration | 1 | 1 | Attributes configurable at service instantiation. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | computeFunctionDebugTools |  | 1 | Indicates whether the service includes debugging tools | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | computeFunctionAllowQuota |  | 1 | Indicates whether the service allows to define resource quotas for functions (typically memory) | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | computeFunctionAllowFSMount |  | 1 | Indicates whether the service supports mounting and using external file systems in functions | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | tenantSeparation |  | 1 | How compute resources of different tenants are separated. Default value = hw-virtualized. |  | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | computeFunctionAllowVersioning |  | 1 | Indicates whether the service allows code versioning for functions | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | computeFunctionName | 1 | 1 | Name of this function template | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| ComputeFunctionTemplateShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionTemplateShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | version |  | 1 | Version of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | computeFunctionDescription | 1 | 1 | Description of what the function template does | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | checkSum |  | 1 | Details on checksum of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | buildDate |  | 1 | Date and time the software was build, formated according to ISO 8601 (UTC - 24 hours). | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | computeFunctionTemplateRuntime | 1 |  | Runtime(s) available for this function template | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | signature |  | 1 | Details with respect to signature of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | patchLevel |  | 1 | Software specific patch number describing patch level of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionTemplateShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionTriggerShape | gx | triggeringEvent |  |  | Events usable to trigger execution of a ComputeFunction | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeFunctionTriggerShape | gx | triggeringService |  | 1 | Service providing the events usable to trigger execution of a ComputeFunction | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | tenantSeparation |  | 1 | How compute resources of different tenants are separated. Default value = hw-virtualized. |  | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ComputeServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConfidentialComputingShape | gx | technology | 1 | 1 | Particular confidential computing technology used by flavors as defined in... | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConfidentialComputingShape | gx | attestationServiceURI |  | 1 | indicates whether confidential server has an associated attestation service. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| ConnectivityConfigurationShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConnectivityConfigurationShape | gx | sourceIdentifierA |  | 1 | InterconnectionPointIdentifier reference of the source service access point. |  | gx_shacl.ttl |
| ConnectivityConfigurationShape | gx | destinationIdentifierZ |  | 1 | InterconnectionPointIdentifier reference of the destination service access point. |  | gx_shacl.ttl |
| ConnectivityConfigurationShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | connectivityQoS |  | 1 | Contractual performance values defined in the SLA. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | connectivityConfiguration | 1 |  | All possible provided connectivity parameters for this network connectivity service offering. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConnectivityServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| ConsentShape | gx | purpose |  |  | Purposes of the processing. It is recommended to use well know controlled vocabulary such as the Data Privacy Vocabulary:Purposes | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConsentShape | gx | dataProtectionContactPoint |  |  | ContactPoint of the Data Protection Officer or Participant responsible for the management of personal or sensitive data | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConsentShape | gx | consentWithdrawalContactPoint |  |  | ContactPoint of the Participant to whom to formulate a withdrawal consent request | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ConsentShape | gx | legalBasis | 1 | 1 | One of the reasons as detailed in the identified Personal Data Protection Regimes, formatted as a string matching <protectionRegime>:<article number> | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContactInformationShape | gx | uri |  | 1 | URI for the contact. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| ContactInformationShape | gx | postalAddress |  | 1 | Postal address of the contact. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContactInformationShape | gx | phoneNumber |  | 1 | Phone number of the contact. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContactInformationShape | gx | email |  | 1 | Email address of the contact. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerImageShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerImageShape | gx | multiQueues |  | 1 | If true, one queue is set for each virtual CPU. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ContainerImageShape | gx | buildDate |  | 1 | Date and time the software was build, formated according to ISO 8601 (UTC - 24 hours). | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| ContainerImageShape | gx | maintenance |  | 1 | Details on maintenance capabilities of vendor of image's operating system. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | gx | containerFormat | 1 | 1 | container image format |  | gx_shacl.ttl |
| ContainerImageShape | gx | secureBoot |  | 1 | If true, instances of the image are only started, if signature of software, such as firmware or operating system, are valid. Default: False. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ContainerImageShape | gx | signature |  | 1 | Details with respect to signature of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | gx | checkSum |  | 1 | Details on checksum of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | gx | patchLevel |  | 1 | Software specific patch number describing patch level of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerImageShape | gx | fileSize |  | 1 | Size of the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | gx | licenseIncluded |  | 1 | In case an image requires a commercial license to be used (No Freeware), this attribute indicates, if service usage fee includes that license (true) or customer has to bring its own commercial license (False). Default: False | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ContainerImageShape | gx | operatingSystem |  | 1 | A resolvable link to Gaia-X credential of operation system offered by this image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| ContainerImageShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerImageShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| ContainerImageShape | gx | vPMU |  | 1 | If true, a virtual performance monitoring unit (vPMU) is enable in guest. Default: False | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ContainerImageShape | gx | gpuReq |  | 1 | Details with respect to GPU capabilities required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | gx | encryption |  | 1 | Details with respect to encryption of the images. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | gx | cpuReq |  | 1 | Details with respect to CPU capabilities required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | gx | baseContainerImage | 1 | 1 | container image base software stack | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | gx | videoRamSize |  | 1 | Maximum amount of RAM for the video image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| ContainerImageShape | gx | version |  | 1 | Version of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerImageShape | gx | rootDiskReq |  | 1 | Minimal size of root disk required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | gx | ramReq |  | 1 | Minimal size of RAM required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerImageShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerImageShape | gx | updateStrategy |  | 1 | Details on provider's image update strategy of this image. An update strategy defines ... | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerResourceLimitsShape | gx | memoryLimit |  | 1 | container memory limits | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerResourceLimitsShape | gx | numberOfCoresLimit |  | 1 | limit to the number of cores usable by a container (expressed in milicore) | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| ContainerResourceLimitsShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerResourceLimitsShape | gx | confidentialComputingTechnology |  | 1 | Details with respect to confidential computing requirements | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerResourceLimitsShape | gx | memoryRequirements |  | 1 | container memory requirements | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerResourceLimitsShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerResourceLimitsShape | gx | confidential | 1 | 1 | indicates whether container is of confidential nature | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ContainerResourceLimitsShape | gx | gpuRequirements |  | 1 | number of GPUs | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerResourceLimitsShape | gx | cpuRequirements |  | 1 | CPU requirements | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerResourceLimitsShape | gx | gpuLimit |  | 1 | GPU number limit | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | instantiationReq | 1 |  | All possible provided container resource limits for this service offering | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | tenantSeparation |  | 1 | How compute resources of different tenants are separated. Default value = hw-virtualized. |  | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | codeArtifact | 1 |  | All possible provided container images for this service offering. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ContainerServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| CopyrightAndIntellectualPropertyDocumentShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| CopyrightAndIntellectualPropertyDocumentShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| CopyrightAndIntellectualPropertyDocumentShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| CopyrightAndIntellectualPropertyDocumentShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| CpuCapabilitiesShape | gx | pCPU | 1 | 1 | Hardware capabilities of phyisical CPU used by given flavor. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| CpuCapabilitiesShape | gx | overProvisioningRatio |  | 1 | A Non-negative integer (beeing equal or greater than 1) defining the amount of overprovising. 
1 means no over-provisiong.
> 1, means physical CPU/thread is over-provisioneb by factor greater 1, e.g. factor 2 means, one physical CPU is used by two virtual CPUs.
 | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| CpuCapabilitiesShape | gx | vCPUs | 1 | 1 | A Non-negative integer (beeing equal or greater than 1) defining the number of virtual CPUs availabe in given flavor. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| CustomerAuditingRightsShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| CustomerAuditingRightsShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| CustomerAuditingRightsShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| CustomerAuditingRightsShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| CustomerDataAccessTermsShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| CustomerDataAccessTermsShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| CustomerDataAccessTermsShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| CustomerDataAccessTermsShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| CustomerDataProcessingTermsShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| CustomerDataProcessingTermsShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| CustomerDataProcessingTermsShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| CustomerDataProcessingTermsShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| CustomerInstructionsShape | gx | terms | 1 |  | Terms and conditions to provide instructions for processing the data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| CustomerInstructionsShape | gx | means | 1 |  | Describes how the customer can instruct the provider with regards to the processing of data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataAccountExportShape | gx | requestType | 1 | 1 | The mean to request data retrieval: API, email, webform, unregisteredLetter, registeredLetter, supportCenter. |  | gx_shacl.ttl |
| DataAccountExportShape | gx | formatType | 1 | 1 | Type of Media Types (formerly known as MIME types) as defined by the IANA. |  | gx_shacl.ttl |
| DataAccountExportShape | gx | accessType | 1 | 1 | Type of data support: digital, physical. |  | gx_shacl.ttl |
| DataConsumerShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataConsumerShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataConsumerShape | gx | legalAddress | 1 | 1 | The full legal address of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataConsumerShape | gx | headquartersAddress | 1 | 1 | Full physical location of the headquarter of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataConsumerShape | gx | registrationNumber | 1 |  | Country's registration number, which identifies one specific entity. Valid formats are local, EUID, EORI, vatID, leiCode. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataConsumerShape | gx | subOrganisationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants with a legal mandate on this entity, e.g., as a subsidiary. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataConsumerShape | gx | parentOrganizationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants that this entity is a subOrganization of, if any. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataLicensorShape | gx | legalAddress | 1 | 1 | The full legal address of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataLicensorShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataLicensorShape | gx | subOrganisationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants with a legal mandate on this entity, e.g., as a subsidiary. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataLicensorShape | gx | parentOrganizationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants that this entity is a subOrganization of, if any. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataLicensorShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataLicensorShape | gx | headquartersAddress | 1 | 1 | Full physical location of the headquarter of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataLicensorShape | gx | registrationNumber | 1 |  | Country's registration number, which identifies one specific entity. Valid formats are local, EUID, EORI, vatID, leiCode. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataPortabilityShape | gx | legalDocument | 1 | 1 | Legal document describing the data portability agreement between the Provider and the Customer hence creating obligations. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataPortabilityShape | gx | contactInformation |  | 1 | Allows to provide a specific provider contact point for data portability. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataPortabilityShape | gx | resource | 1 | 1 | Resource of the service offering concerned by data portability. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataPortabilityShape | gx | deletionMethods | 1 |  | Methods used to delete the customer's data. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataPortabilityShape | gx | pricing | 1 | 1 | Link to the service's pricing page. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| DataPortabilityShape | gx | documentations | 1 |  | Documentations explaining how data portability can be done, in the sense of a manual. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| DataPortabilityShape | gx | means | 1 |  | Means used to transfer the customer's stored data to another provider. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataPortabilityShape | gx | formats | 1 |  | Technical formats for which the Provider will ensure support for importation or exportation processes. For example, YAML, JSON, etc. or even vendor specific formats. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataPortabilityShape | gx | deletionTimeframe | 1 | 1 | Timeframe within which the customer's data will be deleted. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProducerShape | gx | parentOrganizationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants that this entity is a subOrganization of, if any. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataProducerShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProducerShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProducerShape | gx | registrationNumber | 1 |  | Country's registration number, which identifies one specific entity. Valid formats are local, EUID, EORI, vatID, leiCode. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProducerShape | gx | legalAddress | 1 | 1 | The full legal address of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProducerShape | gx | headquartersAddress | 1 | 1 | Full physical location of the headquarter of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProducerShape | gx | subOrganisationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants with a legal mandate on this entity, e.g., as a subsidiary. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataProductShape | gx | termsAndConditions | 1 | 1 | A resolvable link to the Terms and Conditions applying to that service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | dcat | contactPoint |  | 1 | Contact to get more information | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataProductShape | gx | dataLicensors |  |  | A list of Licensors either as a free form string or participant self-description. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataProductShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductShape | gx | obsoleteDateTime |  | 1 | Date time in ISO 8601 format after which Data Product is obsolete. | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| DataProductShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | dcterms | identifier | 1 | 1 | Unique UUID4 | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | gx | dataUsageAgreements |  |  | List of authorizations from the data subjects as Natural Person when the dataset contains PII, as defined by the Trust Framework | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductShape | dcterms | license | 1 |  | A list of URIs to license documents. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| DataProductShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | odrl | hasPolicy |  | 1 | a list of policy expressed using ODRL | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| DataProductShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| DataProductShape | dcterms | title | 1 | 1 | Title of the Data Product. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| DataProductShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | gx | aggregationOf | 1 |  | DataSet Content | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | dcterms | issued |  | 1 | Publication date in ISO 8601 format | <http://www.w3.org/2001/XMLSchema#date> | gx_shacl.ttl |
| DataProductShape | dcterms | conformsTo |  | 1 | An established standard to which the described resource conforms. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| DataProductShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductUsageContractShape | gx | dataUsage | 1 | 1 | A resolvable link to Data Usage. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductUsageContractShape | gx | providedBy | 1 | 1 | A resolvable link to the Data Provider Declaration. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataProductUsageContractShape | gx | notarizedIn |  | 1 | A resolvable link to the Notarization service | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductUsageContractShape | gx | signers | 1 |  | The array identifying all required Participant signature. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductUsageContractShape | gx | consumedBy | 1 | 1 | A resolvable link to the Data Consumer Delaration. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataProductUsageContractShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductUsageContractShape | gx | dataProduct | 1 | 1 | A resolvable link to the Data Product Description Declaration (after negotiation). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProductUsageContractShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProductUsageContractShape | gx | termOfUsage | 1 | 1 | A resolvable link to the Term of Usage. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProtectionPolicyShape | gx | protectionFrequency | 1 | 1 | Frequency at which data are captured/protected. |  | gx_shacl.ttl |
| DataProtectionPolicyShape | gx | protectionRetention | 1 | 1 | How long captured/protected data are kept available. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProtectionPolicyShape | gx | protectionMethod |  | 1 | Method used to protect data, can be be full copy, incremental,... |  | gx_shacl.ttl |
| DataProtectionRegulationMeasuresShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| DataProtectionRegulationMeasuresShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| DataProtectionRegulationMeasuresShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataProtectionRegulationMeasuresShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| DataProviderShape | gx | registrationNumber | 1 |  | Country's registration number, which identifies one specific entity. Valid formats are local, EUID, EORI, vatID, leiCode. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProviderShape | gx | subOrganisationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants with a legal mandate on this entity, e.g., as a subsidiary. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataProviderShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProviderShape | gx | parentOrganizationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants that this entity is a subOrganization of, if any. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataProviderShape | gx | legalAddress | 1 | 1 | The full legal address of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataProviderShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataProviderShape | gx | headquartersAddress | 1 | 1 | Full physical location of the headquarter of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataResourceShape | gx | containsPII | 1 | 1 | Boolean for Personal Identifier Information, which is determined by the Participant owning the Data Resource. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| DataResourceShape | gx | expirationDateTime |  | 1 | Date time in ISO 8601 format after which data is expired and shall be deleted. | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| DataResourceShape | gx | producedBy | 1 | 1 | A resolvable link to participant legally enabling the data usage. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataResourceShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataResourceShape | gx | exposedThrough | 1 |  | A resolvable link to the data exchange component that exposes the Data Product. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataResourceShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| DataResourceShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataResourceShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataResourceShape | gx | obsoleteDateTime |  | 1 | Date time in ISO 8601 format after which data is obsolete. | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| DataResourceShape | gx | dataController |  |  | data controller Participant as defined in GDPR. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataResourceShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| DataResourceShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| DataResourceShape | gx | consent |  |  | list of consents covering the processing activities from the data subjects as Natural Person when the dataset contains PII. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataSetShape | gx | exposedThrough | 1 | 1 | A resolvable link to the data exchange component that exposes the Data Product. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataSetShape | dcterms | issued |  | 1 | Publication date in ISO 8601 format | <http://www.w3.org/2001/XMLSchema#date> | gx_shacl.ttl |
| DataSetShape | gx | expirationDateTime |  | 1 | Date time in ISO 8601 format after which data is expired and shall be deleted. | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| DataSetShape | dcterms | title | 1 | 1 | Title of the Dataset. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataSetShape | dcterms | distribution | 1 |  | List of distributions format of the dataset | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataSetShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataSetShape | dcterms | license |  |  | A list of URIs to license documents. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataSetShape | gx | dataUsageAgreements |  |  | List of authorizations from the data subjects as Natural Person when the dataset contains PII, as defined by the Trust Framework | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataSetShape | gx | dataLicensors |  |  | A list of Licensors either as a free form string or participant self-description. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataSetShape | dcterms | identifier | 1 | 1 | Unique UUID4 | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataSetShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataTransferShape | gx | scope | 1 | 1 | Perimeter of data that will be transferred. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataTransferShape | gx | reason | 1 | 1 | Reason for which the transfer might occur. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataUsageAgreementShape | gx | dataProduct | 1 | 1 | A resolvable link to the Data Product Description Declaration (after negotiation). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataUsageAgreementShape | gx | dataUsageAgreementTrustAnchor | 1 | 1 | A resolvable link to the Data Usage Agreement Trust Anchor. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataUsageAgreementShape | gx | licensedBy |  |  | A resolvable links to Data Licensors. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataUsageAgreementShape | gx | producedBy | 1 | 1 | A resolvable link to the Data Producer. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataUsageAgreementShape | gx | providedBy | 1 | 1 | A resolvable link to the Data Provider. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataUsageAgreementShape | gx | signers | 1 |  | The array identifying all required Participant signature. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DataUsageShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataUsageShape | gx | loggingService |  | 1 | Link to the Logging Service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataUsageShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DatacenterAllocationShape | gx | portNumber |  | 1 | The port number on the patch panel where the service can be accessed. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| DatacenterAllocationShape | gx | refersTo | 1 | 1 | Datacenter where the service can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DatacenterAllocationShape | gx | rackNumber |  | 1 | The Id of the datacenter rack number where the service can be accessed. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DatacenterAllocationShape | gx | floor |  | 1 | The floor number of the datacenter where the service can be accessed. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DatacenterAllocationShape | gx | patchPanel |  | 1 | The Id of the datacenter patch panel where the service can be accessed. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DatacenterShape | gx | energyMix |  |  | A list of information on the composition of the energy mix used by the resource, including percentages of renewable energy and carbon-free energy. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DatacenterShape | gx | maintainedBy | 1 |  | A list of resolvable links to Gaia-X Credentials of participants maintaining the resource in operational condition and thus having physical access to it. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DatacenterShape | gx | manufacturedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant manufacturing the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DatacenterShape | gx | energyUsageEfficiency |  | 1 | Information about the energy usage efficiency of the resource, including relevant certifications and metrics. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DatacenterShape | gx | location | 1 |  | A list of physical locations. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DatacenterShape | gx | ownedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant owning the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DatacenterShape | gx | aggregationOfResources | 1 |  | References those availability zones (at least one must exist) out of which a datacenter is aggregated. |  | gx_shacl.ttl |
| DatacenterShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DatacenterShape | gx | waterUsageEffectiveness |  | 1 | Information regarding the water usage effectiveness of the resource, including certifications and effectiveness measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DatacenterShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DevelopmentCycleSecurityShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| DevelopmentCycleSecurityShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DevelopmentCycleSecurityShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| DevelopmentCycleSecurityShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| DeviceShape | gx | generation |  | 1 | Vendor specific generation of the device. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DeviceShape | gx | vendor |  | 1 | Vendor of the device. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DeviceShape | gx | defaultOversubscriptionRatio |  | 1 | Over-subscription means assigning more capacity to virtual machines that the physical device has. Default over-subscription ratio defines the amount of default over-subscription as a value larger or equal to 1.0. 1.0 means no over-subscription. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| DeviceShape | gx | supportedOversubscriptionRatio |  | 1 | Over-subscription means assigning more capacity to virtual machines that the physical device has. Supported over-subscription ratio defines the amount of supported over-subscription as a value larger or equal to 1.0. 1.0 means no over-subscription. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| DiskShape | gx | vendor |  | 1 | Vendor of the device. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DiskShape | gx | defaultOversubscriptionRatio |  | 1 | Over-subscription means assigning more capacity to virtual machines that the physical device has. Default over-subscription ratio defines the amount of default over-subscription as a value larger or equal to 1.0. 1.0 means no over-subscription. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| DiskShape | gx | diskType |  | 1 | The type of storage drive. |  | gx_shacl.ttl |
| DiskShape | gx | diskSize | 1 | 1 | The size of the hard drive. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| DiskShape | gx | diskBusType |  | 1 | Type of disk controller the disk is attached to. |  | gx_shacl.ttl |
| DiskShape | gx | generation |  | 1 | Vendor specific generation of the device. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DiskShape | gx | supportedOversubscriptionRatio |  | 1 | Over-subscription means assigning more capacity to virtual machines that the physical device has. Supported over-subscription ratio defines the amount of supported over-subscription as a value larger or equal to 1.0. 1.0 means no over-subscription. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| DocumentChangeProceduresShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DocumentChangeProceduresShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| DocumentChangeProceduresShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| DocumentChangeProceduresShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| EORIShape | gx | eori | 1 | 1 | The Economic Operators Registration and Identification number (EORI). | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| EORIShape | gx | country |  | 1 | The country where the EORI is registered written in plain english. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| EUIDShape | gx | euid | 1 | 1 | The European Unique Identifier (EUID) for business located in the European Economic Area, Iceland, Liechtenstein or Norway and registered in the Business Registers Interconnection System (BRIS). This number can be found via the EU Business registers portal. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| EmployeeResponsibilitiesShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| EmployeeResponsibilitiesShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| EmployeeResponsibilitiesShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| EmployeeResponsibilitiesShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| EncryptionShape | gx | keyManagement | 1 | 1 | Define key management method. Allowed values are: managed, BYOK, HYOK |  | gx_shacl.ttl |
| EncryptionShape | gx | cipher | 1 | 1 | Supported algorithm used to encrypt. |  | gx_shacl.ttl |
| EndpointShape | gx | standardConformity | 1 |  | Provides information about applied standards. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| EndpointShape | gx | endpointURL |  | 1 | The URL of the endpoint where it can be accessed. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| EndpointShape | gx | formalDescription |  | 1 | The formal description (e.g. openAPI Description) of the endpoint. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| EnergyMixShape | gx | date | 1 | 1 | Date for which this energy mix has been attained, if the date is in the past, or is forecast to be attained, if the date is in the future. | <http://www.w3.org/2001/XMLSchema#date> | gx_shacl.ttl |
| EnergyMixShape | gx | hourlyCarbonFreeEnergy | 1 | 1 | Percentage of hourly carbon-free energy in the energy mix. | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| EnergyMixShape | gx | renewableEnergy | 1 | 1 | Percentage of renewable energy in the energy mix. | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| EnergyUsageEfficiencyShape | gx | certifications |  |  | Legal documents certifying the energy usage efficiency. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| EnergyUsageEfficiencyShape | gx | powerUsageEffectiveness | 1 | 1 | The effectiveness of power usage, represented as a float. | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| EnvironmentalImpactReportShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| EnvironmentalImpactReportShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| EnvironmentalImpactReportShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| EnvironmentalImpactReportShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| FederatorShape | gx | headquartersAddress | 1 | 1 | Full physical location of the headquarter of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FederatorShape | gx | legalAddress | 1 | 1 | The full legal address of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FederatorShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| FederatorShape | gx | parentOrganizationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants that this entity is a subOrganization of, if any. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| FederatorShape | gx | subOrganisationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants with a legal mandate on this entity, e.g., as a subsidiary. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| FederatorShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| FederatorShape | gx | registrationNumber | 1 |  | Country's registration number, which identifies one specific entity. Valid formats are local, EUID, EORI, vatID, leiCode. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageConfigurationShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| FileStorageConfigurationShape | gx | storageCompression |  |  | Available compression features. |  | gx_shacl.ttl |
| FileStorageConfigurationShape | gx | storageProtection |  |  | Available data protection features. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageConfigurationShape | gx | storageDeduplication |  |  | Deduplication features available for the storage service, such as inline or post-processing. |  | gx_shacl.ttl |
| FileStorageConfigurationShape | gx | fileSystemType |  |  | Filesystem Type  for storage  partition. Ref:https://opensource.com/article/18/4/ext4-filesystem |  | gx_shacl.ttl |
| FileStorageConfigurationShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| FileStorageConfigurationShape | gx | highLevelAccessProtocol |  |  | Underlying higher level access protocol. These mainly refer to access methods such as NFS (Network File System), Common Internet File System (CIFS) and Hadoop File System (HDFS) |  | gx_shacl.ttl |
| FileStorageConfigurationShape | gx | storageQoS |  |  | Available QoS class for storage service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageConfigurationShape | gx | blockSize |  |  | Available block size to be used. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageConfigurationShape | gx | storageRedundancyMechanism |  |  | Underlying data protection mechanism (such as RAID levels or Erasure Codes). |  | gx_shacl.ttl |
| FileStorageConfigurationShape | gx | storageEncryption | 1 |  | Available encryption features. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | storageConfiguration | 1 | 1 | Attributes that are configurable at service instantiation. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | dataViews |  | 1 | Capability to compose logical data views and present the subset of the data as a logical data entity | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | accessSemantics |  | 1 | Does I/O conform to the POSIX standard? See https://en.wikipedia.org/wiki/POSIX. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | maximumSize |  | 1 | Maximum Capacity (expressed as value + unit) supported by the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | lifetimeManagement |  | 1 | Lifetime (in hours) of data (since last access), before it is moved externally, archived or deleted and will not be accessible through the storage service. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | multipleViews |  | 1 | Capability for multiple views. For example is it possible to view Objects as Files, or the other way around | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | storageConsistency |  | 1 | Consistency model provided. See https://en.wikipedia.org/wiki/Consistency_model |  | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | versioning |  | 1 | Whether versioning is available on this storage service. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | accessAttributes |  |  | Supported access attributes (ie how the data can be accessed, read only, read-write, append-only, etc.) |  | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| FileStorageServiceOfferingShape | gx | minimumSize |  | 1 | Minimum Capacity (expressed as value + unit) supported by the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| GPSLocationShape | gx | crs |  | 1 | Coordinate Reference System identifier. Framework used to precisely measure locations on the surface of Earth as coordinates. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| GPSLocationShape | gx | longitude | 1 | 1 | Coordinate representing y horizontal position such as longitude. Negative values west of Prime Meridian and positive values east of Prime Meridian. |  | gx_shacl.ttl |
| GPSLocationShape | gx | altitude |  | 1 | For three-dimensional point locations, a value representing vertical position through either height or depth. Positive direction and units are defined by CRS identifier. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| GPSLocationShape | gx | latitude | 1 | 1 | Coordinate representing x horizontal position such as latitude. Negative number south of equator and positive north of equator. |  | gx_shacl.ttl |
| GPSUnitShape | gx | degrees | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| GPSUnitShape | gx | minutes |  | 1 |  | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| GPSUnitShape | gx | seconds |  | 1 |  | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| GPSUnitShape | gx | decimals |  | 1 |  | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| GPUShape | gx | gpuProcessingUnits |  | 1 | Number of processing units, also called compute units, execution units or streaming multiprocessors, of the GPU. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| GPUShape | gx | gpuMemory |  | 1 | Size of memory of the GPU. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| GPUShape | gx | vendor |  | 1 | Vendor of the device. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| GPUShape | gx | supportedOversubscriptionRatio |  | 1 | Over-subscription means assigning more capacity to virtual machines that the physical device has. Supported over-subscription ratio defines the amount of supported over-subscription as a value larger or equal to 1.0. 1.0 means no over-subscription. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| GPUShape | gx | defaultOversubscriptionRatio |  | 1 | Over-subscription means assigning more capacity to virtual machines that the physical device has. Default over-subscription ratio defines the amount of default over-subscription as a value larger or equal to 1.0. 1.0 means no over-subscription. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| GPUShape | gx | generation |  | 1 | Vendor specific generation of the device. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| GPUShape | gx | gpuInterconnection |  | 1 | Interconnection of multiple GPUs within a server system |  | gx_shacl.ttl |
| GPUShape | gx | gpuPassthrough |  | 1 | If true, GPU is provided via passthrough, otherwise GPU is virtualized. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| GaiaXEntityShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| GaiaXEntityShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| GovernmentInvestigationManagementShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| GovernmentInvestigationManagementShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| GovernmentInvestigationManagementShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| GovernmentInvestigationManagementShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| HypervisorShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| HypervisorShape | gx | version |  | 1 | Version of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| HypervisorShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| HypervisorShape | gx | buildDate |  | 1 | Date and time the software was build, formated according to ISO 8601 (UTC - 24 hours). | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| HypervisorShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| HypervisorShape | gx | checkSum |  | 1 | Details on checksum of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| HypervisorShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| HypervisorShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| HypervisorShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| HypervisorShape | gx | hypervisorType | 1 | 1 | The common name of the distribution of the operating system as defined in http://libosinfo.org/. |  | gx_shacl.ttl |
| HypervisorShape | gx | patchLevel |  | 1 | Software specific patch number describing patch level of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| HypervisorShape | gx | signature |  | 1 | Details with respect to signature of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| IOPSShape | gx | guaranteed |  | 1 | Minimum percentage of time where a performance-level is guaranteed to be met. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| IOPSShape | gx | metric | 1 | 1 | Input/output operations per second expressed as a data-rate. |  | gx_shacl.ttl |
| ImageShape | gx | checkSum |  | 1 | Details on checksum of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ImageShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| ImageShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ImageShape | gx | signature |  | 1 | Details with respect to signature of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ImageShape | gx | operatingSystem |  | 1 | A resolvable link to Gaia-X credential of operation system offered by this image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ImageShape | gx | fileSize |  | 1 | Size of the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ImageShape | gx | ramReq |  | 1 | Minimal size of RAM required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ImageShape | gx | cpuReq |  | 1 | Details with respect to CPU capabilities required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ImageShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ImageShape | gx | buildDate |  | 1 | Date and time the software was build, formated according to ISO 8601 (UTC - 24 hours). | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| ImageShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ImageShape | gx | version |  | 1 | Version of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ImageShape | gx | videoRamSize |  | 1 | Maximum amount of RAM for the video image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ImageShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| ImageShape | gx | patchLevel |  | 1 | Software specific patch number describing patch level of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ImageShape | gx | vPMU |  | 1 | If true, a virtual performance monitoring unit (vPMU) is enable in guest. Default: False | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ImageShape | gx | multiQueues |  | 1 | If true, one queue is set for each virtual CPU. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ImageShape | gx | maintenance |  | 1 | Details on maintenance capabilities of vendor of image's operating system. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ImageShape | gx | rootDiskReq |  | 1 | Minimal size of root disk required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ImageShape | gx | encryption |  | 1 | Details with respect to encryption of the images. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ImageShape | gx | licenseIncluded |  | 1 | In case an image requires a commercial license to be used (No Freeware), this attribute indicates, if service usage fee includes that license (true) or customer has to bring its own commercial license (False). Default: False | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ImageShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| ImageShape | gx | secureBoot |  | 1 | If true, instances of the image are only started, if signature of software, such as firmware or operating system, are valid. Default: False. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ImageShape | gx | gpuReq |  | 1 | Details with respect to GPU capabilities required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ImageShape | gx | updateStrategy |  | 1 | Details on provider's image update strategy of this image. An update strategy defines ... | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InformationSecurityOrganizationShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| InformationSecurityOrganizationShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InformationSecurityOrganizationShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| InformationSecurityOrganizationShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| InformationSecurityPoliciesShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| InformationSecurityPoliciesShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InformationSecurityPoliciesShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| InformationSecurityPoliciesShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| InformationSecurityRiskManagementShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InformationSecurityRiskManagementShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| InformationSecurityRiskManagementShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| InformationSecurityRiskManagementShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| InfrastructureServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| InstantiationRequirementShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InstantiationRequirementShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionPointIdentifierShape | gx | completeIPI | 1 | 1 | Unique label identifying structure of an IPI. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionPointIdentifierShape | gx | ipiProvider |  | 1 | The Provider of the IPI. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionPointIdentifierShape | gx | ipiType |  | 1 | Type of the interconnection point identifier. |  | gx_shacl.ttl |
| InterconnectionPointIdentifierShape | gx | ipAddress |  | 1 | The IP address required for L3 connectivity setup. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionPointIdentifierShape | gx | specificParameters |  | 1 | Type or Provider Specific Parameters, separated by colons. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionPointIdentifierShape | gx | datacenterAllocation |  | 1 | Details specific situation within the datacenter where the service can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionPointIdentifierShape | gx | macAddress |  | 1 | The mac address required for L2 connectivity setup. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | vlanConfiguration |  | 1 | VLAN configuration. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | ipVersion |  | 1 | Version of IP address supported. IPv4: only ipV4 addresses are supported. IPv6: both version iIPV4 and IPv6 are supported. |  | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | connectivityQoS |  | 1 | Contractual performance values defined in the SLA. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | connectedNetworkA |  |  | Autonomous system (AS) number (ASN) of the side A. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | interfaceType |  |  | A type of physical interface: Copper cable, 5G... | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | connectionType |  |  | The supported types of connection, preferably specified as a controlled vocabulary entry: ethernet unicast, multicast, broadcast support... | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | tenantSeparation |  | 1 | How compute resources of different tenants are separated. Default value = hw-virtualized. |  | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | prefixSetZ |  |  | CIDR Provider Identifier of network on the side Z. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | prefixSetA |  |  | CIDR Provider Identifier of network on the side A. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | connectedNetworkZ |  |  | Autonomous system (AS) number (ASN) of the side Z. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | serviceType |  | 1 | Type of Service Offering. Choose one of the following: virtual, bare-metal, mixed | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | publicIpAddressProvisioning |  | 1 | Defines how public IP address are provided. Floating: floating ips are supported. |  | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | connectivityConfiguration | 1 |  | All possible provided connectivity parameters for this network connectivity service offering. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InterconnectionServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| InternetExchangePointShape | gx | waterUsageEffectiveness |  | 1 | Information regarding the water usage effectiveness of the resource, including certifications and effectiveness measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InternetExchangePointShape | gx | location | 1 |  | A list of physical locations. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InternetExchangePointShape | gx | maintainedBy | 1 |  | ISP in charge of managing the IP transit (or internet transit) of this point of presence | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InternetExchangePointShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InternetExchangePointShape | gx | manufacturedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant manufacturing the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InternetExchangePointShape | gx | energyUsageEfficiency |  | 1 | Information about the energy usage efficiency of the resource, including relevant certifications and metrics. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InternetExchangePointShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InternetExchangePointShape | gx | interconnectionPointIdentifier | 1 | 1 | Definition of the location where resources can interconnect. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InternetExchangePointShape | gx | ownedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant owning the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InternetExchangePointShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| InternetExchangePointShape | gx | participants | 1 |  | Internet service providers interconnecting their networks through this IXP | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InternetExchangePointShape | gx | energyMix |  |  | A list of information on the composition of the energy mix used by the resource, including percentages of renewable energy and carbon-free energy. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InternetServiceProviderShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InternetServiceProviderShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InternetServiceProviderShape | gx | parentOrganizationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants that this entity is a subOrganization of, if any. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InternetServiceProviderShape | gx | registrationNumber | 1 |  | Country's registration number, which identifies one specific entity. Valid formats are local, EUID, EORI, vatID, leiCode. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InternetServiceProviderShape | gx | headquartersAddress | 1 | 1 | Full physical location of the headquarter of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InternetServiceProviderShape | gx | legalAddress | 1 | 1 | The full legal address of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| InternetServiceProviderShape | gx | subOrganisationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants with a legal mandate on this entity, e.g., as a subsidiary. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| IssuerShape | gx | gaiaxTermsAndConditions | 1 | 1 | Gaia-X terms and conditions this issuer agreed with in order to act as an issuer of Gaia-X compliant credentials. |  | gx_shacl.ttl |
| JitterShape | gx | metric | 1 | 1 | Jitter expressed as time. |  | gx_shacl.ttl |
| JitterShape | gx | guaranteed |  | 1 | Minimum percentage of time where a performance-level is guaranteed to be met. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LabelCredentialShape | gx | rulesVersion | 1 | 1 | Gaia-X compliance document version from which the validated criteria originate. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LabelCredentialShape | gx | compliantCredentials | 1 |  | Credentials validated by the compliance engine and linked to a label credential. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LabelCredentialShape | gx | engineVersion | 1 | 1 | Gaia-X compliance engine version that delivered a label credential. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LabelCredentialShape | gx | validatedCriteria | 1 |  | Gaia-X compliance document version from which the validated criteria originate. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LabelCredentialShape | gx | labelLevel | 1 | 1 | Abbreviated conformity level of the label credential (SC, L1, L2, ...). |  | gx_shacl.ttl |
| LatencyShape | gx | guaranteed |  | 1 | Minimum percentage of time where a performance-level is guaranteed to be met. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LatencyShape | gx | metric | 1 | 1 | Latency expressed as time. |  | gx_shacl.ttl |
| LatestNShape | gx | value |  | 1 |  | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| LegalDocumentShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| LegalDocumentShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| LegalDocumentShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| LegalDocumentShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| LegalPersonShape | gx | subOrganisationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants with a legal mandate on this entity, e.g., as a subsidiary. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| LegalPersonShape | gx | headquartersAddress | 1 | 1 | Full physical location of the headquarter of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LegalPersonShape | gx | parentOrganizationOf |  |  | A list of resolvable links to Gaia-X Credentials of participants that this entity is a subOrganization of, if any. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| LegalPersonShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LegalPersonShape | gx | registrationNumber | 1 |  | Country's registration number, which identifies one specific entity. Valid formats are local, EUID, EORI, vatID, leiCode. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LegalPersonShape | gx | legalAddress | 1 | 1 | The full legal address of the organization. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LegalPersonShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LegallyBindingActShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| LegallyBindingActShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| LegallyBindingActShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| LegallyBindingActShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| LegitimateInterestShape | gx | legalBasis | 1 | 1 | Reasons to process PII as detailed in your personal data protection regime. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LegitimateInterestShape | gx | dataProtectionContact | 1 | 1 | A URL pointing to a contact form or an email address. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LeiCodeShape | schema | leiCode | 1 | 1 | Unique LEI number as defined by https://www.gleif.org. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LeiCodeShape | gx | subdivisionCountryCode |  | 1 | The country subdivision (state/region) where the LEI number is registered. |  | gx_shacl.ttl |
| LeiCodeShape | gx | countryCode |  | 1 | The country where the LEI number is registered. |  | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | protocolType | 1 | 1 | Link protocol type. |  | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | connectivityQoS |  | 1 | Contractual performance values defined in the SLA. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | vlanConfiguration |  | 1 | VLAN configuration. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | connectivityConfiguration | 1 |  | All possible provided connectivity parameters for this network connectivity service offering. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| LinkConnectivityServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| LocalRegistrationNumberShape | gx | local | 1 | 1 | The state issued company number. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| MaintenanceSubscriptionShape | gx | subscriptionRequired |  | 1 | True, if cloud service user needs a maintenance subscription account from the vendor of image's operating system in order to receive fixes. Default: False. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| MaintenanceSubscriptionShape | gx | subscriptionIncluded |  | 1 | True, if cloud  service provider prepared already the image to reviece bug fixes, security fixes and (minor) function updates. Default: False | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| MaintenanceSubscriptionShape | gx | maintainedUntil |  | 1 | Date (UTC) until vendor of image's operating system promises maintenance at least. | <http://www.w3.org/2001/XMLSchema#date> | gx_shacl.ttl |
| MeasureShape | gx | legalDocuments | 1 |  | Legal documents associated with the measure. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| MeasureShape | schema | description | 1 | 1 | Description of the measure. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| MemoryCapabilitiesShape | gx | overProvisioningRatio |  | 1 | A Non-negative float (being equal or greater than 1) defining the amount of overprovisoning. 
1 means no over-provisiong.
> 1, means physical memory over-provisioned by factor greater than one, e.g. factor 2 means, available virtual RAM size is twice as big as physical RAM size. Maxium value is 3.
 | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| MemoryCapabilitiesShape | gx | memory | 1 | 1 | Amount of virtual RAM available in given flavor. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| MemoryShape | gx | generation |  | 1 | Vendor specific generation of the device. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| MemoryShape | gx | vendor |  | 1 | Vendor of the device. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| MemoryShape | gx | eccEnabled |  | 1 | Error connection code allows to detect and correct bit errors in data. True, if error-correction-code is supported by the ram, false otherwise. Default: False. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| MemoryShape | gx | defaultOversubscriptionRatio |  | 1 | Over-subscription means assigning more capacity to virtual machines that the physical device has. Default over-subscription ratio defines the amount of default over-subscription as a value larger or equal to 1.0. 1.0 means no over-subscription. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| MemoryShape | gx | memoryRank |  | 1 | Rank defines the number of memory chip banks and the buffering used to access these. |  | gx_shacl.ttl |
| MemoryShape | gx | memorySize | 1 | 1 | Memory size of RAM. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| MemoryShape | gx | memoryClass |  | 1 | DRAM technology name defined by JEDEC. |  | gx_shacl.ttl |
| MemoryShape | gx | hardwareEncryption |  | 1 | If true, encryption of memory at the hardware level is enabled. Default: False. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| MemoryShape | gx | supportedOversubscriptionRatio |  | 1 | Over-subscription means assigning more capacity to virtual machines that the physical device has. Supported over-subscription ratio defines the amount of supported over-subscription as a value larger or equal to 1.0. 1.0 means no over-subscription. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| MemorySizeShape |  | http://qudt.org/vocab/unit | 1 | 1 | Unit of physical quantity. See https://qudt.org/schema/qudt/Unit | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| MemorySizeShape |  | http://qudt.org/vocab/value | 1 | 1 | Value of physical quantity. See https://qudt.org/schema/qudt/value | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | publicIpAddressProvisioning |  | 1 | Defines how public IP address are provided. Floating: floating ips are supported. |  | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | ipVersion |  | 1 | Version of IP address supported. IPv4: only ipV4 addresses are supported. IPv6: both version iIPV4 and IPv6 are supported. |  | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | serviceType |  | 1 | Type of Service Offering. Choose one of the following: virtual, bare-metal, mixed | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | connectivityConfiguration | 1 |  | All possible provided connectivity parameters for this network connectivity service offering. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | connectivityQoS |  | 1 | Contractual performance values defined in the SLA. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | tenantSeparation |  | 1 | How compute resources of different tenants are separated. Default value = hw-virtualized. |  | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| NetworkConnectivityServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | minimumSize |  | 1 | Minimum Capacity (expressed as value + unit) supported by the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | storageConsistency |  | 1 | Consistency model provided. See https://en.wikipedia.org/wiki/Consistency_model |  | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | maximumObjectSize |  | 1 | Maximum size for objects supported by the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | accessAttributes |  |  | Supported access attributes (ie how the data can be accessed, read only, read-write, append-only, etc.) |  | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | maximumSize |  | 1 | Maximum Capacity (expressed as value + unit) supported by the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | multipleViews |  | 1 | Capability for multiple views. For example is it possible to view Objects as Files, or the other way around | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | dataViews |  | 1 | Capability to compose logical data views and present the subset of the data as a logical data entity | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | versioning |  | 1 | Whether versioning is available on this storage service. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | lifetimeManagement |  | 1 | Lifetime (in hours) of data (since last access), before it is moved externally, archived or deleted and will not be accessible through the storage service. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | objectAPICompatibility |  |  | Compatibility for third party object storage  APIs. Ref:https://docs.aws.amazon.com/AmazonS3/latest/API/Type_API_Reference.html, https://docs.microsoft.com/en-us/rest/api/storageservices/blob-service-rest-api |  | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | storageConfiguration | 1 | 1 | Attributes that are configurable at service instantiation. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| ObjectStorageServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| OperatingSystemShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| OperatingSystemShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| OperatingSystemShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| OperatingSystemShape | gx | signature |  | 1 | Details with respect to signature of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| OperatingSystemShape | gx | buildDate |  | 1 | Date and time the software was build, formated according to ISO 8601 (UTC - 24 hours). | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| OperatingSystemShape | gx | checkSum |  | 1 | Details on checksum of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| OperatingSystemShape | gx | patchLevel |  | 1 | Software specific patch number describing patch level of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| OperatingSystemShape | gx | osDistribution | 1 | 1 | The common name of the distribution of the operating system as defined in http://libosinfo.org/. |  | gx_shacl.ttl |
| OperatingSystemShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| OperatingSystemShape | gx | version |  | 1 | Version of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| OperatingSystemShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| OperatingSystemShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| OperationalSecurityShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| OperationalSecurityShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| OperationalSecurityShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| OperationalSecurityShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| PXEImageShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| PXEImageShape | gx | videoRamSize |  | 1 | Maximum amount of RAM for the video image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PXEImageShape | gx | secureBoot |  | 1 | If true, instances of the image are only started, if signature of software, such as firmware or operating system, are valid. Default: False. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| PXEImageShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PXEImageShape | gx | buildDate |  | 1 | Date and time the software was build, formated according to ISO 8601 (UTC - 24 hours). | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| PXEImageShape | gx | checkSum |  | 1 | Details on checksum of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PXEImageShape | gx | maintenance |  | 1 | Details on maintenance capabilities of vendor of image's operating system. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PXEImageShape | gx | rootDiskReq |  | 1 | Minimal size of root disk required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PXEImageShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| PXEImageShape | gx | encryption |  | 1 | Details with respect to encryption of the images. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PXEImageShape | gx | ramReq |  | 1 | Minimal size of RAM required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PXEImageShape | gx | operatingSystem |  | 1 | A resolvable link to Gaia-X credential of operation system offered by this image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PXEImageShape | gx | licenseIncluded |  | 1 | In case an image requires a commercial license to be used (No Freeware), this attribute indicates, if service usage fee includes that license (true) or customer has to bring its own commercial license (False). Default: False | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| PXEImageShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| PXEImageShape | gx | cpuReq |  | 1 | Details with respect to CPU capabilities required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PXEImageShape | gx | fileSize |  | 1 | Size of the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PXEImageShape | gx | vPMU |  | 1 | If true, a virtual performance monitoring unit (vPMU) is enable in guest. Default: False | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| PXEImageShape | gx | multiQueues |  | 1 | If true, one queue is set for each virtual CPU. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| PXEImageShape | gx | version |  | 1 | Version of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PXEImageShape | gx | signature |  | 1 | Details with respect to signature of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PXEImageShape | gx | patchLevel |  | 1 | Software specific patch number describing patch level of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PXEImageShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PXEImageShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PXEImageShape | gx | gpuReq |  | 1 | Details with respect to GPU capabilities required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PXEImageShape | gx | pxeImageDiskFormat |  | 1 | Disk format. Default "ISO". |  | gx_shacl.ttl |
| PXEImageShape | gx | updateStrategy |  | 1 | Details on provider's image update strategy of this image. An update strategy defines ... | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PacketLossShape | gx | metric | 1 | 1 | Percentage of lost packets compared to the total number of exchanged packets. |  | gx_shacl.ttl |
| PacketLossShape | gx | guaranteed |  | 1 | Minimum percentage of time where a performance-level is guaranteed to be met. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ParticipantShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ParticipantShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | interfaceType | 1 | 1 | For the chosen circuit type, one should know the interface type in case the interoperability is required. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | circuitType | 1 | 1 | Type of access medium: wired medium access or wireless medium access. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | connectivityConfiguration | 1 |  | All possible provided connectivity parameters for this network connectivity service offering. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | connectivityQoS |  | 1 | Contractual performance values defined in the SLA. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalConnectivityServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | gx | participants | 1 |  | Legal persons interconnecting their networks via this point of presence | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | gx | location | 1 |  | A list of physical locations. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | gx | interconnectionPointIdentifier | 1 | 1 | Definition of the location where resources can interconnect. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | gx | energyMix |  |  | A list of information on the composition of the energy mix used by the resource, including percentages of renewable energy and carbon-free energy. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | gx | waterUsageEffectiveness |  | 1 | Information regarding the water usage effectiveness of the resource, including certifications and effectiveness measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | gx | ownedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant owning the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | gx | manufacturedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant manufacturing the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | gx | maintainedBy | 1 |  | ISP in charge of managing the IP transit (or internet transit) of this point of presence | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| PhysicalInterconnectionPointIdentifierShape | gx | energyUsageEfficiency |  | 1 | Information about the energy usage efficiency of the resource, including relevant certifications and metrics. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalResourceShape | gx | ownedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant owning the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalResourceShape | gx | manufacturedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant manufacturing the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalResourceShape | gx | location | 1 |  | A list of physical locations. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalResourceShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| PhysicalResourceShape | gx | waterUsageEffectiveness |  | 1 | Information regarding the water usage effectiveness of the resource, including certifications and effectiveness measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalResourceShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalResourceShape | gx | energyUsageEfficiency |  | 1 | Information about the energy usage efficiency of the resource, including relevant certifications and metrics. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalResourceShape | gx | energyMix |  |  | A list of information on the composition of the energy mix used by the resource, including percentages of renewable energy and carbon-free energy. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PhysicalResourceShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalResourceShape | gx | maintainedBy | 1 |  | A list of resolvable links to Gaia-X Credentials of participants maintaining the resource in operational condition and thus having physical access to it. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalSecurityShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| PhysicalSecurityShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| PhysicalSecurityShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| PhysicalSecurityShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PointOfPresenceShape | gx | energyUsageEfficiency |  | 1 | Information about the energy usage efficiency of the resource, including relevant certifications and metrics. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PointOfPresenceShape | gx | manufacturedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant manufacturing the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PointOfPresenceShape | gx | location | 1 |  | A list of physical locations. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PointOfPresenceShape | gx | participants | 1 |  | Legal persons interconnecting their networks via this point of presence | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PointOfPresenceShape | gx | interconnectionPointIdentifier | 1 | 1 | Definition of the location where resources can interconnect. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PointOfPresenceShape | gx | ownedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant owning the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PointOfPresenceShape | gx | maintainedBy | 1 |  | ISP in charge of managing the IP transit (or internet transit) of this point of presence | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PointOfPresenceShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PointOfPresenceShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PointOfPresenceShape | gx | waterUsageEffectiveness |  | 1 | Information regarding the water usage effectiveness of the resource, including certifications and effectiveness measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| PointOfPresenceShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| PointOfPresenceShape | gx | energyMix |  |  | A list of information on the composition of the energy mix used by the resource, including percentages of renewable energy and carbon-free energy. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ProcurementManagementSecurityShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| ProcurementManagementSecurityShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| ProcurementManagementSecurityShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| ProcurementManagementSecurityShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| ProductSecurityShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| ProductSecurityShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| ProductSecurityShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| ProductSecurityShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| QoSMetricShape | gx | guaranteed |  | 1 | Minimum percentage of time where a performance-level is guaranteed to be met. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| QoSMetricShape | gx | metric | 1 | 1 | Quantity usually representing a performance level |  | gx_shacl.ttl |
| QoSShape | gx | packetLoss |  | 1 | Contractual packet loss of connection defined in the SLA agreement. If not specified, then best effort is assumed. packetLoss measured in the pseudo-unit "percent" | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| QoSShape | gx | latency |  | 1 | Contractual latency defined in the SLA. If not specified, then best effort is assumed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| QoSShape | gx | bandWidth |  | 1 | Contractual bandwidth defined in the service level agreement (SLA). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| QoSShape | gx | jitter |  | 1 | Contractual jitter defined in the SLA. If not specified, then best effort is assumed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| QoSShape | gx | roundTripTime |  | 1 | Contractual roundTrip time defined in the SLA. If not specified, then best effort is assumed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| QoSShape | gx | availability |  | 1 | Contractual availability of connection defined in the SLA agreement. Availability is measured in the pseudo-unit "percent". | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| QoSShape | gx | throughput |  | 1 | QoS metric for throughput | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| QoSShape | gx | targetPercentile |  | 1 | Contractual percentile in the SLA. Usually referred to the number of frames the SLA metrics such as availability, latency and jitter can be guaranteed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| QoSShape | gx | iops |  | 1 | QoS metric for Input/Output operations per second. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| RegionShape | gx | address |  | 1 | The physical address associated with the region. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| RegionShape | gx | aggregationOfResources | 1 |  | References those datacenters (at least one must exist) out of which a region is aggregated. |  | gx_shacl.ttl |
| RegionShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| RegionShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ReplicationPolicyShape | gx | synchronousReplication |  | 1 | Whether replication is performed in synchronous mode | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ReplicationPolicyShape | gx | replicaNumber |  |  | How many independant copies are made | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| ReplicationPolicyShape | gx | consistencyType |  | 1 | Type of consistency supported |  | gx_shacl.ttl |
| ReplicationPolicyShape | gx | protectionMethod |  | 1 | Method used to protect data, can be be full copy, incremental,... |  | gx_shacl.ttl |
| ReplicationPolicyShape | gx | geoReplication |  |  | Scope of geo-replication, cross-region, cross-dc or simply cross-az |  | gx_shacl.ttl |
| ReplicationPolicyShape | gx | protectionRetention | 1 | 1 | How long captured/protected data are kept available. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ReplicationPolicyShape | gx | protectionFrequency | 1 | 1 | Frequency at which data are captured/protected. |  | gx_shacl.ttl |
| ResourceShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ResourceShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| ResourceShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| RetentionDurationShape |  | http://qudt.org/vocab/unit | 1 | 1 | Unit of physical quantity. See https://qudt.org/schema/qudt/Unit | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| RetentionDurationShape |  | http://qudt.org/vocab/value | 1 | 1 | Value of physical quantity. See https://qudt.org/schema/qudt/value | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
| RoleAndResponsibilitiesShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| RoleAndResponsibilitiesShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| RoleAndResponsibilitiesShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| RoleAndResponsibilitiesShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| RoundTripTimeShape | gx | metric | 1 | 1 | Time taken for a round-trip. |  | gx_shacl.ttl |
| RoundTripTimeShape | gx | guaranteed |  | 1 | Minimum percentage of time where a performance-level is guaranteed to be met. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| SecurityIncidentManagementShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| SecurityIncidentManagementShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| SecurityIncidentManagementShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| SecurityIncidentManagementShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| ServerFlavorShape | gx | hwRngTypeOfFlavor |  | 1 | Type of physical phenomena hardware random number generator (RNG) of this flavor is based on. |  | gx_shacl.ttl |
| ServerFlavorShape | gx | confidentialComputing |  | 1 | Details with respect to confidential computing capabilities of the flavor. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServerFlavorShape | gx | memory | 1 | 1 | A non-negative integer, which defines how many memory given flavor provides. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServerFlavorShape | gx | gpu |  | 1 | GPU capabilities of the flavor. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServerFlavorShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServerFlavorShape | gx | bootVolume | 1 | 1 | Boot volume capabilities of boot volume of the flavor. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServerFlavorShape | gx | hypervisor |  | 1 | Hypervisor as Gaia-X software resources. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServerFlavorShape | gx | network |  | 1 | Network capabilities of the flavor. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServerFlavorShape | gx | additionalVolume |  |  | Additional volume capabilities of boot volume of the flavor. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServerFlavorShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServerFlavorShape | gx | hardwareAssistedVirtualization |  | 1 | Hardware-assisted virtualization, a.k.a. accelerated virtualization or hardware virtualization, enables full virtualization. Full virtualization means to run an unmodified guest operation system in complete isolation by emulating a complete hardware environment. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| ServerFlavorShape | gx | cpu | 1 | 1 | Capabilities of virtual CPUs available in flavor. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceAgreementOfferShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| ServiceAgreementOfferShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| ServiceAgreementOfferShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| ServiceAgreementOfferShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| ServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| ServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| ServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| ServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| ServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| ServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| SignatureCheckTypeShape | gx | legalValidity | 1 | 1 | Establish the if the Legal validity check needs to be enforced to the Signature. Possible values are Yes/No | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| SignatureCheckTypeShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SignatureCheckTypeShape | gx | participantRole | 1 | 1 | Establish a unique way to identify the participant that has to Sign(e.g. gx:providedBy is identified by Provider ). Possible values are Provider, Consumer, Licensor, Producer | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SignatureCheckTypeShape | gx | mandatory | 1 | 1 | Establish the if a Signature is mandatory or Optional. Possible values are Yes/No | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SignatureCheckTypeShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SignatureShape | gx | signatureValue | 1 | 1 | Value of the signature | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SignatureShape | gx | signatureAlgorithm | 1 | 1 | Algorithm used to create the checksum hash. |  | gx_shacl.ttl |
| SignatureShape | gx | hashAlgorithm | 1 | 1 | Algorithm used to create the checksum hash. |  | gx_shacl.ttl |
| SnapshotPolicyShape | gx | protectionRetention | 1 | 1 | How long captured/protected data are kept available. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| SnapshotPolicyShape | gx | protectionMethod |  | 1 | Method used to protect data, can be be full copy, incremental,... |  | gx_shacl.ttl |
| SnapshotPolicyShape | gx | protectionFrequency | 1 | 1 | Frequency at which data are captured/protected. |  | gx_shacl.ttl |
| SnapshotPolicyShape | gx | snapshotReplication |  |  | Snapshots replication policy, if any | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| SoftwareResourceShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| SoftwareResourceShape | gx | version |  | 1 | Version of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SoftwareResourceShape | gx | buildDate |  | 1 | Date and time the software was build, formated according to ISO 8601 (UTC - 24 hours). | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| SoftwareResourceShape | gx | patchLevel |  | 1 | Software specific patch number describing patch level of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SoftwareResourceShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SoftwareResourceShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SoftwareResourceShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| SoftwareResourceShape | gx | signature |  | 1 | Details with respect to signature of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| SoftwareResourceShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| SoftwareResourceShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SoftwareResourceShape | gx | checkSum |  | 1 | Details on checksum of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StandardConformityShape | gx | standardReference | 1 | 1 | Provides a link to schemas or details about applied standards. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| StandardConformityShape | dcterms | title | 1 | 1 | Name of the standard. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| StandardConformityShape | gx | publisher |  | 1 | Publisher of the standard. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| StorageConfigurationShape | gx | storageQoS |  |  | Available QoS class for storage service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageConfigurationShape | gx | storageCompression |  |  | Available compression features. |  | gx_shacl.ttl |
| StorageConfigurationShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| StorageConfigurationShape | gx | storageProtection |  |  | Available data protection features. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageConfigurationShape | gx | storageDeduplication |  |  | Deduplication features available for the storage service, such as inline or post-processing. |  | gx_shacl.ttl |
| StorageConfigurationShape | gx | storageRedundancyMechanism |  |  | Underlying data protection mechanism (such as RAID levels or Erasure Codes). |  | gx_shacl.ttl |
| StorageConfigurationShape | gx | blockSize |  |  | Available block size to be used. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageConfigurationShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| StorageConfigurationShape | gx | storageEncryption | 1 |  | Available encryption features. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | storageConfiguration | 1 | 1 | Attributes that are configurable at service instantiation. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | maximumSize |  | 1 | Maximum Capacity (expressed as value + unit) supported by the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| StorageServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | storageConsistency |  | 1 | Consistency model provided. See https://en.wikipedia.org/wiki/Consistency_model |  | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | minimumSize |  | 1 | Minimum Capacity (expressed as value + unit) supported by the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | multipleViews |  | 1 | Capability for multiple views. For example is it possible to view Objects as Files, or the other way around | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | lifetimeManagement |  | 1 | Lifetime (in hours) of data (since last access), before it is moved externally, archived or deleted and will not be accessible through the storage service. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | dataViews |  | 1 | Capability to compose logical data views and present the subset of the data as a logical data entity | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | versioning |  | 1 | Whether versioning is available on this storage service. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| StorageServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| SubContractorShape | gx | informationDocuments | 1 |  | Documents providing additional information about the subcontractor. |  | gx_shacl.ttl |
| SubContractorShape | gx | legalName | 1 | 1 | The legal name of the subcontractor. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SubContractorShape | gx | applicableJurisdiction | 1 | 1 | The jurisdiction under which the subcontractor operates. |  | gx_shacl.ttl |
| SubContractorShape | gx | communicationMethods | 1 |  | The method of communication with the subcontractor. |  | gx_shacl.ttl |
| SubProcessorDataTransferShape | gx | subProcessorManagement | 1 | 1 | Management means of the sub-processor. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| SubProcessorDataTransferShape | gx | scope | 1 | 1 | Perimeter of data that will be transferred. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SubProcessorDataTransferShape | gx | subProcessor |  | 1 | Sub-processor to which the data can be transferred. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| SubProcessorDataTransferShape | gx | reason | 1 | 1 | Reason for which the transfer might occur. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| TargetPercentileShape | gx | guaranteed |  | 1 | Minimum percentage of time where a performance-level is guaranteed to be met. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| TargetPercentileShape | gx | metric | 1 | 1 | Percentage of frames the SLA metrics can be guaranteed. |  | gx_shacl.ttl |
| TaxIDShape | schema | taxID | 1 | 1 | The company tax ID. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| TermsAndConditionsShape | gx | url | 1 | 1 | A resolvable link to the terms & conditions document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| TermsAndConditionsShape | gx | hash | 1 | 1 | SHA-256 hash of the document. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ThirdCountryDataTransferShape | gx | country | 1 | 1 | Country to which the data can be transferred. |  | gx_shacl.ttl |
| ThirdCountryDataTransferShape | gx | securingMechanism | 1 |  | Mechanism used to secure the data transfer. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ThirdCountryDataTransferShape | gx | scope | 1 | 1 | Perimeter of data that will be transferred. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ThirdCountryDataTransferShape | gx | reason | 1 | 1 | Reason for which the transfer might occur. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ThroughputShape | gx | guaranteed |  | 1 | Minimum percentage of time where a performance-level is guaranteed to be met. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| ThroughputShape | gx | metric | 1 | 1 | Throughput expressed as a data-rate. |  | gx_shacl.ttl |
| UpdateStrategyShape | gx | replaceFrequency |  | 1 | Frequency, in which the provider updates the image on a regular basis. Possible values are: yearly, quarterly, monthly, weekly, daily, critical_bug, and never. |  | gx_shacl.ttl |
| UpdateStrategyShape | gx | hotfixHours |  | 1 | Time in hours passed after image's distributor published a critical hot fix and cloud provider updated this image with the critical patch. A critical bug is defined as a security vulnerability with a CVSS score of 9.0 or higher. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| UpdateStrategyShape | gx | oldVersionsValidUntil |  | 1 | Defines, how long outdated and hidden images are available by its ID. Allowed values are "none" (none information are given), "notice" (outdated version is valid until deprecation notice from provider), "forever" (Outdated version will never be deleted), non-negative integer n (latest n version keep available) and date in UTC (outdated version is valid until given date). |  | gx_shacl.ttl |
| UpdateStrategyShape | gx | providedUntil |  | 1 | Details, how long the image will be provided in image catalogue. Allowed values are "none" (none information are given), "notice" (image is available until deprecation notice from provider), and date in UTC (date until the image is available). |  | gx_shacl.ttl |
| UserDocumentationMaintenanceShape | gx | involvedParties |  |  | Legal entities involved or mentioned in the legal document. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| UserDocumentationMaintenanceShape | gx | mimeTypes |  |  | The MIME types associated with the legal document. |  | gx_shacl.ttl |
| UserDocumentationMaintenanceShape | gx | governingLawCountries |  |  | Countries under whose laws the document is governed. |  | gx_shacl.ttl |
| UserDocumentationMaintenanceShape | gx | url | 1 | 1 | A resolvable link to the legal document. | <http://www.w3.org/2001/XMLSchema#anyURI> | gx_shacl.ttl |
| VLANConfigurationShape | gx | vlanType |  | 1 | The chosen types of vlan types. |  | gx_shacl.ttl |
| VLANConfigurationShape | gx | vlanTag |  | 1 | Vlan Tag ID that range between 1 and 4094. In case qinq connection type is chosen tow vlan tag, namely outer and innter should be provided. | <http://www.w3.org/2001/XMLSchema#integer> | gx_shacl.ttl |
| VLANConfigurationShape | gx | vlanEtherType |  | 1 | The ether type of the vlan in hexadecimal notation. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VMImageShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VMImageShape | gx | videoRamSize |  | 1 | Maximum amount of RAM for the video image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VMImageShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| VMImageShape | gx | licenseIncluded |  | 1 | In case an image requires a commercial license to be used (No Freeware), this attribute indicates, if service usage fee includes that license (true) or customer has to bring its own commercial license (False). Default: False | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| VMImageShape | gx | updateStrategy |  | 1 | Details on provider's image update strategy of this image. An update strategy defines ... | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VMImageShape | gx | watchDogAction |  | 1 | Define the action to be performed if server hangs. |  | gx_shacl.ttl |
| VMImageShape | gx | fileSize |  | 1 | Size of the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VMImageShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VMImageShape | gx | patchLevel |  | 1 | Software specific patch number describing patch level of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VMImageShape | gx | buildDate |  | 1 | Date and time the software was build, formated according to ISO 8601 (UTC - 24 hours). | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| VMImageShape | gx | vPMU |  | 1 | If true, a virtual performance monitoring unit (vPMU) is enable in guest. Default: False | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| VMImageShape | gx | firmwareType |  | 1 | Type of firmware which which guests are booted. |  | gx_shacl.ttl |
| VMImageShape | gx | encryption |  | 1 | Details with respect to encryption of the images. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VMImageShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VMImageShape | gx | secureBoot |  | 1 | If true, instances of the image are only started, if signature of software, such as firmware or operating system, are valid. Default: False. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| VMImageShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| VMImageShape | gx | checkSum |  | 1 | Details on checksum of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VMImageShape | gx | cpuReq |  | 1 | Details with respect to CPU capabilities required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VMImageShape | gx | multiQueues |  | 1 | If true, one queue is set for each virtual CPU. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| VMImageShape | gx | operatingSystem |  | 1 | A resolvable link to Gaia-X credential of operation system offered by this image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VMImageShape | gx | version |  | 1 | Version of the software. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VMImageShape | gx | ramReq |  | 1 | Minimal size of RAM required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VMImageShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| VMImageShape | gx | hypervisorType |  | 1 | Hypervisor type required by the image |  | gx_shacl.ttl |
| VMImageShape | gx | vmImageDiskFormat |  | 1 | Disk format og the VM inage. Default "RAW" |  | gx_shacl.ttl |
| VMImageShape | gx | maintenance |  | 1 | Details on maintenance capabilities of vendor of image's operating system. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VMImageShape | gx | signature |  | 1 | Details with respect to signature of the software. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VMImageShape | gx | hwRngTypeOfImage |  | 1 | Type of physical phenomena hardware random number generator (RNG) this image prefers. |  | gx_shacl.ttl |
| VMImageShape | gx | rootDiskReq |  | 1 | Minimal size of root disk required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VMImageShape | gx | gpuReq |  | 1 | Details with respect to GPU capabilities required to run the image. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VatIDShape | gx | vatID | 1 | 1 | The VAT identification number. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VatIDShape | gx | countryCode |  | 1 | The country where the VAT identification number is registered. |  | gx_shacl.ttl |
| VirtualInterconnectionPointIdentifierShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualInterconnectionPointIdentifierShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| VirtualInterconnectionPointIdentifierShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| VirtualInterconnectionPointIdentifierShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualInterconnectionPointIdentifierShape | gx | participants | 1 |  | Legal persons participating within a concept. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| VirtualInterconnectionPointIdentifierShape | gx | interconnectionPointIdentifier | 1 | 1 | Definition of the location where resources can interconnect. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| VirtualInterconnectionPointIdentifierShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| VirtualInterconnectionPointIdentifierShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | keyword |  |  | Keywords that describe / tag the service. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | providerContactInformation |  | 1 | The contact information where the customer can contact the provider of this service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | possiblePersonalDataTransfers |  |  | One or more data transfer documents describing if and to which extent Customer data transfers will happen. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | providedBy | 1 | 1 | A resolvable link to Gaia-X Credential of the participant providing the service. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | instantiationReq | 1 |  | Set of technical requirements or conditions to instantiate this service offering. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | dataAccountExport | 1 |  | One or more methods to export data out of the service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | subContractors |  |  | A list of sub-contractors processing customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | dataPortability |  |  | One or more data portability documents describing the data portability measures for the stored Customer data. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | servicePolicy |  |  | One or more policies expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | dependsOn |  |  | A list of resolvable links to Gaia-X Credentials of service offerings related to the service and that can exist independently of it. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | dataProtectionRegime |  |  | One or more data protection regimes applying to the service offering. |  | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | hostedOn |  |  | List of Resource references where service is hosted and can be instantiated. Can refer to availabilty zones, data centers, regions, etc. |  | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | serviceOfferingTermsAndConditions | 1 |  | One or more Terms and Conditions applying to that service. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | endpoint |  | 1 | Endpoint through which the Service Offering can be accessed. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | tenantSeparation |  | 1 | How compute resources of different tenants are separated. Default value = hw-virtualized. |  | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | requiredMeasures |  |  | One or more technical and organizational measures. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | customerInstructions |  |  | One or more customer instructions describing the Customer instructions regarding any data therein. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | codeArtifact | 1 |  | Compute Service Code Artifacts. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | provisionType |  | 1 | Provision type of the service |  | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | legalDocuments |  |  | A list of legal documents in relation to the service or the customer. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | serviceScope |  | 1 | Plain text describing the service scope. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to an entity and that can exist independently of it. |  | gx_shacl.ttl |
| VirtualMachineServiceOfferingShape | gx | cryptographicSecurityStandards |  |  | One or more cryptographic security standards protecting authenticity or integrity of the data. |  | gx_shacl.ttl |
| VirtualResourceShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| VirtualResourceShape | gx | aggregationOfResources |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| VirtualResourceShape | gx | resourcePolicy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualResourceShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| VirtualResourceShape | schema | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualResourceShape | schema | description |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| WaterUsageEffectivenessShape | gx | certifications |  |  | Legal documents certifying the water usage effectiveness. | <http://www.w3.org/ns/shacl#BlankNodeOrIRI> | gx_shacl.ttl |
| WaterUsageEffectivenessShape | gx | waterUsageEffectiveness | 1 | 1 | The effectiveness of water usage, represented as a float. | <http://www.w3.org/2001/XMLSchema#float> | gx_shacl.ttl |
