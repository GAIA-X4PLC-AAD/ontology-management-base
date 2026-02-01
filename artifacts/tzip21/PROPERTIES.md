# Properties of SHACL Files for tzip21

## Prefixes

- tzip21: <https://w3id.org/ascs-ev/envited-x/tzip21/v1/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AssetShape | tzip21 | name | 0 | 1 | A UTF-8 string giving a display name to the token. (Highly recommended from TZIP-012) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AssetShape | tzip21 | symbol | 0 | 1 | A UTF-8 string for the short identifier of the token (e.g. XTZ, EUR, etc.). (Highly recommended from TZIP-012) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AssetShape | tzip21 | decimals | 1 | 1 | An integer defining the position of the decimal point in token balances for display purposes. (Required by TZIP-012) | <http://www.w3.org/2001/XMLSchema#integer> | tzip21.shacl.ttl |
| AssetShape | tzip21 | description | 0 | 1 | General notes, abstracts, or summaries about the contents of an asset. (Optional) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AssetShape | tzip21 | minter | 0 | 1 | The tz address responsible for minting the asset. Expected format: tzaddress. (Recommended for semi‑fungible and NFT tokens) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AssetShape | tzip21 | creators | 0 |  | Array of unique strings representing the primary creators of the asset. (Recommended for semi‑fungible and NFT tokens) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AssetShape | tzip21 | contributors | 0 |  | Array of unique strings representing those who made substantial creative contributions. (Optional) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AssetShape | tzip21 | publishers | 0 |  | Array of unique strings representing those primarily responsible for distributing the asset. (Optional) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AssetShape | tzip21 | date | 0 | 1 | A date associated with the creation or availability of the asset, per JSON Schema. (Optional) | <http://www.w3.org/2001/XMLSchema#dateTime> | tzip21.shacl.ttl |
| AssetShape | tzip21 | blockLevel | 0 | 1 | Chain block level associated with the asset. (Optional) | <http://www.w3.org/2001/XMLSchema#integer> | tzip21.shacl.ttl |
| AssetShape | tzip21 | type | 0 | 1 | A broad definition of the content type of the asset. (Optional) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AssetShape | tzip21 | tags | 0 |  | Array of unique strings that describe the subject or content of the asset. (Recommended for Multimedia NFTs) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AssetShape | tzip21 | genres | 0 |  | Array of unique strings that describe the genres of the asset. (Optional) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AssetShape | tzip21 | language | 0 | 1 | The language of the asset’s intellectual content (per RFC 1766). (Optional) | <http://www.w3.org/2001/XMLSchema#language> | tzip21.shacl.ttl |
| AssetShape | tzip21 | identifier | 0 | 1 | Links to the specific envited-x:SimulationAsset (e.g., hdmap:HdMap) that this TZIP21 service offering represents. |  | tzip21.shacl.ttl |
| AssetShape | tzip21 | rights | 0 | 1 | A statement about the asset rights. (Optional) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AssetShape | tzip21 | rightsUri | 0 | 1 | A URI linking to a statement of rights. Format: uri-reference. (Optional) | <http://www.w3.org/2001/XMLSchema#anyURI> | tzip21.shacl.ttl |
| AssetShape | tzip21 | artifactUri | 0 | 1 | A URI to the asset. Format: uri-reference. (Recommended for semi‑fungible and NFT tokens) | <http://www.w3.org/2001/XMLSchema#anyURI> | tzip21.shacl.ttl |
| AssetShape | tzip21 | displayUri | 0 | 1 | A URI to an image of the asset for display purposes. Format: uri-reference. (Recommended for semi‑fungible and NFT tokens) | <http://www.w3.org/2001/XMLSchema#anyURI> | tzip21.shacl.ttl |
| AssetShape | tzip21 | thumbnailUri | 0 | 1 | A URI to a scaled-down image for wallets/clients (max recommended size: 350x350px). Format: uri-reference. (Recommended for fungible and NFT tokens) | <http://www.w3.org/2001/XMLSchema#anyURI> | tzip21.shacl.ttl |
| AssetShape | tzip21 | externalUri | 0 | 1 | A URI with additional information about the asset. Format: uri-reference. (Optional) | <http://www.w3.org/2001/XMLSchema#anyURI> | tzip21.shacl.ttl |
| AssetShape | tzip21 | isTransferable | 0 | 1 | Indicates if tokens are transferable. Default is true. | <http://www.w3.org/2001/XMLSchema#boolean> | tzip21.shacl.ttl |
| AssetShape | tzip21 | isBooleanAmount | 0 | 1 | Indicates whether an account’s balance can only be 0 or 1. Default is false. (Recommended for nonfungible tokens) | <http://www.w3.org/2001/XMLSchema#boolean> | tzip21.shacl.ttl |
| AssetShape | tzip21 | shouldPreferSymbol | 0 | 1 | Indicates if a symbol should be shown instead of a name. Default is false. | <http://www.w3.org/2001/XMLSchema#boolean> | tzip21.shacl.ttl |
| AssetShape | tzip21 | ttl | 0 | 1 | Time-to-live (in seconds) for metadata caching. Default is 0 (indefinite caching). If used, it is advised not to set below 600 seconds. | <http://www.w3.org/2001/XMLSchema#integer> | tzip21.shacl.ttl |
| AssetShape | tzip21 | formats | 0 |  | An array of format objects describing various representations of the asset. (Optional) |  | tzip21.shacl.ttl |
| AssetShape | tzip21 | attributes | 0 |  | An array of attribute objects providing custom properties. Attribute names must be unique within the array. (Optional) |  | tzip21.shacl.ttl |
| AssetShape | tzip21 | assets | 0 |  | An array of asset objects for describing collections or composite resources. (Optional) |  | tzip21.shacl.ttl |
| FormatShape | tzip21 | uri | 1 | 1 | A URI to the asset in this format. Format: uri-reference. (Recommended) | <http://www.w3.org/2001/XMLSchema#anyURI> | tzip21.shacl.ttl |
| FormatShape | tzip21 | hash | 0 | 1 | Checksum hash of the asset content in this format. (Optional) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| FormatShape | tzip21 | mimeType | 0 | 1 | Media (MIME) type as registered by IANA. (Optional) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| FormatShape | tzip21 | fileSize | 0 | 1 | Size in bytes of the asset content in this format. (Optional) | <http://www.w3.org/2001/XMLSchema#integer> | tzip21.shacl.ttl |
| FormatShape | tzip21 | fileName | 0 | 1 | Display filename for the asset in this format. (Optional) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| FormatShape | tzip21 | duration | 0 | 1 | Time duration of the asset content in this format. Format: time. (Optional) | <http://www.w3.org/2001/XMLSchema#time> | tzip21.shacl.ttl |
| FormatShape | tzip21 | dimensions | 0 | 1 | Dimensions of the asset content (e.g. ‘512x512’ with unit ‘px’). |  | tzip21.shacl.ttl |
| FormatShape | tzip21 | dataRate | 0 | 1 | Data rate at which the asset content was captured (e.g. 320 kbps). |  | tzip21.shacl.ttl |
| AttributeShape | tzip21 | name | 1 | 1 | Name of the attribute. Must be unique within the attributes array. | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AttributeShape | tzip21 | value | 1 | 1 | Value of the attribute. | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| AttributeShape | tzip21 | type | 0 | 1 | Type of the attribute value (e.g. number, integer, percentage) for display purposes. (Optional) | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| OntologyConformanceAttributeShape | tzip21 | name | 1 | 1 | Reverse domain notation identifier for the ontology (e.g., 'com.github.ascs-ev.ontology-management-base.hdmap.ontology'). | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| OntologyConformanceAttributeShape | tzip21 | value | 1 | 1 | The w3id.org URI of the ontology that the simulation asset conforms to (e.g., 'https://w3id.org/ascs-ev/envited-x/hdmap/v5/'). | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| OntologyConformanceAttributeShape | tzip21 | type | 1 | 1 | Must be 'uri' for ontology conformance attributes. | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| DataRateShape | tzip21 | value | 1 | 1 | Numeric value of the data rate. | <http://www.w3.org/2001/XMLSchema#integer> | tzip21.shacl.ttl |
| DataRateShape | tzip21 | unit | 1 | 1 | Unit for the data rate (e.g. 'kbps'). | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| DimensionsShape | tzip21 | value | 1 | 1 | The dimensions value (e.g. '512x512'). | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
| DimensionsShape | tzip21 | unit | 1 | 1 | The unit of measurement for the dimensions (e.g. 'px'). | <http://www.w3.org/2001/XMLSchema#string> | tzip21.shacl.ttl |
