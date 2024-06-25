# Variables of SHACL Files in this folder

## Prefixes

- gx: <https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DataResourceShape | gx | obsoleteDateTime | 0 | 1 | date time in ISO 8601 format after which data is obsolete. | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| DataResourceShape | gx | policy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataResourceShape | gx | containsPII | 1 | 1 | Whether the service contains Personal Identifiable Informations. | <http://www.w3.org/2001/XMLSchema#boolean> | gx_shacl.ttl |
| DataResourceShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| DataResourceShape | gx | producedBy | 1 | 1 | a resolvable link to the participant self-description legally enabling the data usage. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataResourceShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| DataResourceShape | gx | exposedThrough | 1 |  | A resolvable link to the data exchange component that exposes the data resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| DataResourceShape | gx | aggregationOf |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| DataResourceShape | gx | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataResourceShape | gx | description |  | 1 | A free text description of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataResourceShape | gx | expirationDateTime | 0 | 1 | date time in ISO 8601 format after which data is expired and shall be deleted. | <http://www.w3.org/2001/XMLSchema#dateTime> | gx_shacl.ttl |
| GaiaXTermsAndConditionsShape | gx | termsAndConditions | 1 |  |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| InstantiatedVirtualResourceShape | gx | hostedOn | 1 | 1 | A resource where the process is located (physical server, datacenter, availability zone, …). |  | gx_shacl.ttl |
| InstantiatedVirtualResourceShape | gx | instanceOf | 1 | 1 | A virtual resource (normally a software resource) this process is an instance of. |  | gx_shacl.ttl |
| InstantiatedVirtualResourceShape | gx | serviceAccessPoint | 1 |  | A list of Service Access Point which can be an endpoint as a mean to access and interact with the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InstantiatedVirtualResourceShape | gx | maintainedBy | 1 |  | A list of participant maintaining the resource in operational condition. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| InstantiatedVirtualResourceShape | gx | tenantOwnedBy |  |  | A list of participant with contractual relation with the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| LegitimateInterestShape | gx | dataProtectionContact | 1 | 1 | an URL pointing to a contact form or an emailaddress. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| LegitimateInterestShape | gx | legalBasis | 1 | 1 | Reasons to process PII as detailed in your personal data protection regime | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalResourceShape | gx | aggregationOf |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| PhysicalResourceShape | gx | description |  | 1 | A free text description of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalResourceShape | gx | locationAddress | 0 |  | A list of physical locations. |  | gx_shacl.ttl |
| PhysicalResourceShape | gx | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| PhysicalResourceShape | gx | ownedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant owning the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalResourceShape | gx | maintainedBy | 1 |  | A list of resolvable links to Gaia-X Credentials of participants maintaining the resource in operational condition and thus having physical access to it. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalResourceShape | gx | manufacturedBy |  |  | A list of resolvable links to Gaia-X Credentials of participant manufacturing the resource. | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PhysicalResourceShape | gx | location | 0 |  | a list of physical GPS in ISO 6709:2008/Cor 1:2009 format. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceAccessPointShape | gx | host |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceAccessPointShape | gx | version |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceAccessPointShape | gx | openAPI |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceAccessPointShape | gx | name |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceAccessPointShape | gx | protocol |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceAccessPointShape | gx | port |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceOfferingLabelShape | gx | assignedTo | 1 | 1 | a resolvable link to the service offering self-description to which label level is assigned to. |  | gx_shacl.ttl |
| ServiceOfferingLabelShape | gx | criteria | 1 | 1 | Gaia-X Policy Rules and Labelling Criteria for Providers |  | gx_shacl.ttl |
| SoftwareResourceShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| SoftwareResourceShape | gx | aggregationOf |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| SoftwareResourceShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| SoftwareResourceShape | gx | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SoftwareResourceShape | gx | description |  | 1 | A free text description of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SoftwareResourceShape | gx | policy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualResourceShape | gx | license | 1 |  | A list of SPDX identifiers or URL to document. |  | gx_shacl.ttl |
| VirtualResourceShape | gx | name |  | 1 | A human readable name of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualResourceShape | gx | copyrightOwnedBy | 1 |  | A list of copyright owners either as a free form string or as resolvable link to Gaia-X Credential of participants. A copyright owner is a person or organization that has the right to exploit the resource. Copyright owner does not necessarily refer to the author of the resource, who is a natural person and may differ from copyright owner. |  | gx_shacl.ttl |
| VirtualResourceShape | gx | description |  | 1 | A free text description of the entity. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualResourceShape | gx | policy | 1 |  | A  list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, ...). If there is no specified usage policy constraints on the VirtualResource, the  policy should express a simple default: allow intent | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| VirtualResourceShape | gx | aggregationOf |  |  | A resolvable link of resources related to the resource and that can exist independently of it. |  | gx_shacl.ttl |
| legalRegistrationNumberShape | gx | EORI |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| legalRegistrationNumberShape | gx | vatID |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| legalRegistrationNumberShape | gx | EUID |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| legalRegistrationNumberShape | gx | taxID |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| legalRegistrationNumberShape | gx | leiCode |  |  |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| http://www.w3.org/2006/vcard/ns#AddressShape |  | http://www.w3.org/2006/vcard/ns#postal-code |  | 1 | String of a street-address | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| http://www.w3.org/2006/vcard/ns#AddressShape | gx | countryCode | 1 | 1 | Country code in ISO 3166-1 alpha2, alpha-3 or numeric format. |  | gx_shacl.ttl |
| http://www.w3.org/2006/vcard/ns#AddressShape |  | http://www.w3.org/2006/vcard/ns#locality |  | 1 | The v:locality property specifies the locality (e.g., city) of a postal address. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| http://www.w3.org/2006/vcard/ns#AddressShape |  | http://www.w3.org/2006/vcard/ns#street-address |  | 1 | the street address of a postal address | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| http://www.w3.org/2006/vcard/ns#AddressShape | gx | gps |  | 1 | GPS in ISO 6709:2008/Cor 1:2009 format. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CriteriaEvidenceShape | gx | website |  | 1 | Link to website to complete evidence information | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| CriteriaEvidenceShape | gx | pdf |  | 1 | Link to attestation PDF to complete evidence information | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataAccountExportShape | gx | formatType | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataAccountExportShape | gx | accessType | 1 | 1 | type of data support: digital, physical. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| DataAccountExportShape | gx | requestType | 1 | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SOTermsAndConditionsShape | gx | hash | 1 | 1 | sha256 hash of the above document. | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| SOTermsAndConditionsShape | gx | URL | 1 | 1 | a resolvable link to document | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.20 | 1 | 1 | Product safety and security: Provide appropriate mechanisms for cloud customers to enable product safety and security. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.2.2 | 1 | 1 | The Provider shall ensure there are provisions governing the rights of the parties to use the service and any Customer Data therein. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.1.3 | 1 | 1 | The Provider shall clearly define the technical and organizational measures in accordance with the roles and responsibilities of the parties, including an adequate level of detail. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.15 | 1 | 1 | Incident Management: Ensure a consistent and comprehensive approach to the capture, assessment, communication and escalation of security incidents. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.1.2 | 1 | 1 | The Provider shall define the roles and responsibilities of each party. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P5.1.5 | 0 | 1 | For Label Level 3, Shareholders in the Provider, whose registered head office, headquarters and main establishment are not established in a Member State of the EU/EEA shall not, directly or indirectly, individually or jointly, hold control of the CSP. Control is defined as the ability of a natural or legal person to exercise decisive influence directly or indirectly on the CSP through one or more intermediate entities, de jure or de facto. (cf. Council Regulation No 139/2004 and Commission Consolidated Jurisdictional Notice under Council Regulation (EC) No 139/2004 for illustrations of decisive control). |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.10 | 1 | 1 | Communication Security: Ensure the protection of information in networks and the corresponding information processing systems. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.2.7 | 1 | 1 | The Provider shall communicate to the Customer where the applicable jurisdiction(s) of subcontractors will be. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.1.3 | 1 | 1 | The Provider shall clearly identify for which parties the legal act is binding. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.3 | 1 | 1 | Risk Management: Ensure that risks related to information security are properly identified, assessed, and treated, and that the residual risk is acceptable to the CSP. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.2 | 1 | 1 | Information Security Policies: Provide a global information security policy, derived into policies and procedures regarding security requirements and to support business requirements. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.6 | 1 | 1 | Physical Security: Prevent unauthorised physical access and protect against theft, damage, loss and outage of operations. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.3.3 | 1 | 1 | Service Offering must provide a conformant self-description. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.2.3 | 1 | 1 | The Provider shall clearly define if and to which extent third country transfer will take place. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.3.1 | 1 | 1 | In case of a joint controllership, the Provider shall ensure an arrangement pursuant to Art. 26 (1) GDPR is in place. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.3.4 | 1 | 1 | Self-Description attributes need to be consistent across linked Self-Descriptions. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.1 | 1 | 1 | Organization of information security: Plan, implement, maintain and continuously improve the information security framework within the organisation. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.14 | 1 | 1 | Procurement Management: Ensure the protection of information that suppliers of the CSP can access and monitor the agreed services and security requirements. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.2.8 | 1 | 1 | The Provider shall include in the contract the contact details where Customer may address any queries regarding the Service Offering and the contract. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.1.1 | 1 | 1 | The Provider shall offer the ability to establish a legally binding act. This legally binding act shall be documented. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P5.2.1 | 1 | 1 | The Provider shall not access Customer Data unless authorized by the Customer or when the access is in accordance with EU/EEA/Member State law. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.8 | 1 | 1 | Identity, Authentication and access control management: Limit access to information and information processing facilities. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.19 | 1 | 1 | Dealing with information requests from government agencies: Ensure appropriate handling of government investigation requests for legal review, information to cloud customers, and limitation of access to or disclosure of Customer Data. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.17 | 1 | 1 | Compliance: Avoid non-compliance with legal, regulatory, self-imposed or contractual information security and compliance requirements. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P4.1.1 | 1 | 1 | The Provider shall implement practices for facilitating the switching of Providers and the porting of Customer Data in a structured, commonly used and machine-readable format including open standard formats where required or requested by the Customer. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.2.9 | 1 | 1 | The Provider shall adopt the Gaia-X Trust Framework, by which Customers may verify Provider’s Service Offering. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.3.2 | 1 | 1 | In case of a joint controllership, at a minimum, the Provider shall ensure that the very essence of such agreement is communicated to data subjects. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.3.1 | 1 | 1 | Service Offering shall include a policy using a common Domain-Specific Language (DSL) to describe Permissions, Requirements and Constraints. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.4 | 1 | 1 | Human Resources: Ensure that employees understand their responsibilities, are aware of their responsibilities with regard to information security, and that the organisation’s assets are protected in the event of changes in responsibilities or termination. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P5.1.4 | 0 | 1 | For Label Level 3, the Provider’s registered head office, headquarters and main establishment shall be established in a Member State of the EU/EEA. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.3.5 | 1 | 1 | The Provider shall ensure that the Consumer uses a verified identity provided by the Federator. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.2.7 | 1 | 1 | The Provider shall define the audit rights for the Customer. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.9 | 1 | 1 | Cryptography and Key management: Ensure appropriate and effective use of cryptography to protect the confidentiality, authenticity or integrity of information. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P5.1.6 | 0 | 1 | For Label Level 3, in the event of recourse by the Provider, in the context of the services provided to the Customer, to the services of a third-party company - including a subcontractor - whose registered head office, headquarters and main establishment is outside of the European Union or who is owned or controlled directly or indirectly by another third-party company registered outside the EU/EEA, the third-party company shall have no access over the Customer Data nor access and identity management for the services provided to the Customer. The Provider, including any of its sub-processor, shall push back any request received from non-European authorities to obtain communication of Customer Data relating to European Customers, except if request is made in execution of a court judgment or order that is valid and compliant under Union law and applicable Member States law as provided by Article 48 GDPR. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.2.6 | 1 | 1 | The Provider shall clearly define if and to the extent sub-processors will be involved, and the measures that are in place regarding sub-processors management. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.1.4 | 1 | 1 | The Provider shall ensure that the legally binding act covers the entire provision of the Service Offering. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P5.1.7 | 0 | 1 | For Label Level 3, the Provider must maintain continuous operating autonomy for all or part of the services it provides. The concept of operating autonomy shall be understood as the ability to maintain the provision of the cloud computing service by drawing on the provider’s own skills or by using adequate alternatives |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.3.3 | 1 | 1 | In case of a joint controllership, the Provider shall publish a point of contact for data subjects. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.1.2 | 1 | 1 | The Provider shall have an option for each legally binding act to be governed by EU/EEA/Member State law. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.2.2 | 1 | 1 | The Provider shall clearly define how Customer may instruct, including by electronic means such as configuration tools or APIs. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.3.2 | 1 | 1 | Service Offering requires being operated by Service Offering Provider with a verified identity. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P5.1.2 | 0 | 1 | For Label Level 3, the Provider shall process and store all Customer Data exclusively in the EU/EEA. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.5 | 1 | 1 | Asset Management: Identify the organisation’s own assets and ensure an appropriate level of protection throughout their lifecycle. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P5.1.1 | 0 | 1 | For Label Level 2, the Provider shall provide the option that all Customer Data are processed and stored exclusively in EU/EEA. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.1.1 | 1 | 1 | The Provider shall offer the ability to establish a contract under Union or EU/EEA/Member State law and specifically addressing GDPR requirements. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.2.10 | 1 | 1 | The Provider shall provide transparency on the environmental impact of the Service Offering provided |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.2.5 | 1 | 1 | The Provider shall declare the location of the processing of any Customer Data at urban area level. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.2.6 | 1 | 1 | The Provider shall explain how information about subcontractors and related Customer Data localization will be communicated. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.2.3 | 1 | 1 | The Provider shall ensure there are provisions governing changes, regardless of their kind. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.2.4 | 1 | 1 | The Provider shall clearly define if and to the extent third country transfers will take place, and by which means of Chapter V GDPR these transfers will be protected. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.2.1 | 1 | 1 | The Provider shall ensure there are specific provisions regarding service interruptions and business continuity (e.g., by means of a service level agreement), Provider’s bankruptcy or any other reason by which the Provider may cease to exist in law. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P4.1.2 | 1 | 1 | The Provider shall ensure pre-contractual information exists, with sufficiently detailed, clear and transparent information regarding the processes of Customer Data portability, technical requirements, timeframes and charges that apply in case a professional user wants to switch to another Provider or port Customer Data back to its own IT systems. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.2.1 | 1 | 1 | The Provider shall be ultimately bound to instructions of the Customer. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.7 | 1 | 1 | Operational Security: Ensure proper and regular operation, including appropriate measures for planning and monitoring capacity, protection against malware, logging and monitoring events, and dealing with vulnerabilities, malfunctions and failures. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P1.2.4 | 1 | 1 | The Provider shall ensure there are provisions governing aspects regarding copyright or any other intellectual property rights. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.18 | 1 | 1 | User documentation: Provide up-to-date information on the secure configuration and known vulnerabilities of the cloud service for cloud customers. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.12 | 1 | 1 | Change and Configuration Management: Ensure that changes and configuration actions to information systems guarantee the security of the delivered cloud service. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.11 | 1 | 1 | Portability and Interoperability: The CSP shall provide a means by which a customer can obtain their stored customer data, and provide documentation on how (where appropriate, through documented API’s) the CSC can obtain the stored data at the end of the contractual relationship and shall document how the data will be securely deleted from the Cloud Service Provider in what timeframe. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.16 | 1 | 1 | Business Continuity: Plan, implement, maintain and test procedures and measures for business continuity and emergency management. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P5.1.3 | 0 | 1 | For Label Level 3, where the Provider or subcontractor is subject to legal obligations to transmit or disclose Customer Data on the basis of a non-EU/EEA statutory order, the Provider shall have verified safeguards in place to ensure that any access request is compliant with EU/EEA/Member State law. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P2.2.5 | 1 | 1 | The Provider shall clearly define if and to which extent sub-processors will be involved. |  | gx_shacl.ttl |
| ServiceOfferingCriteriaShape | gx | P3.1.13 | 1 | 1 | Development of Information systems: Ensure information security in the development cycle of information systems. |  | gx_shacl.ttl |
| LegalParticipantShape | gx | subOrganization |  |  |  |  | gx_shacl.ttl |
| LegalParticipantShape | gx | headquarterAddress | 1 |  |  |  | gx_shacl.ttl |
| LegalParticipantShape | gx | legalAddress | 1 |  |  |  | gx_shacl.ttl |
| LegalParticipantShape | gx | parentOrganization |  |  |  |  | gx_shacl.ttl |
| LegalParticipantShape | gx | legalRegistrationNumber | 1 |  |  | <http://www.w3.org/ns/shacl#IRI> | gx_shacl.ttl |
| PostalAddressShape | gx | countrySubdivisionCode | 1 |  |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceOfferingShape | gx | termsAndConditions | 1 |  | a resolvable link to the service offering self-description related to the service and that can exist independently of it. |  | gx_shacl.ttl |
| ServiceOfferingShape | gx | dataProtectionRegime |  |  | a list of data protection regime | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceOfferingShape | gx | providedBy | 1 | 1 | a resolvable link to the participant self-description providing the service. |  | gx_shacl.ttl |
| ServiceOfferingShape | gx | policy | 1 |  | a list of policy expressed using a DSL (e.g., Rego or ODRL) (access control, throttling, usage, retention, …). | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
| ServiceOfferingShape | gx | dataAccountExport | 1 |  | list of methods to export data from your user’s account out of the service |  | gx_shacl.ttl |
| CriteriaResponseShape | gx | evidence |  | 1 |  |  | gx_shacl.ttl |
| CriteriaResponseShape | gx | response | 1 | 1 |  |  | gx_shacl.ttl |
| CriteriaResponseShape | gx | reason |  | 1 |  | <http://www.w3.org/2001/XMLSchema#string> | gx_shacl.ttl |
