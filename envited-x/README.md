# < envited-x:DataResource:name >

< envited-x:DataResource:description >

## Digital Asset Overview

This digital asset adheres to the ENVITED Ecosystem Specification [EVES-003](https://ascs-ev.github.io/EVES/EVES-003/eves-003.html) and the Gaia-X Trust Framework.
It follows a structured ontology framework (`envited-x`, `manifest`, `and others`) to ensure interoperability and consistent documentation.
A complete ENVITED-X Simulation Asset contains structured metadata, relevant resource details, and comprehensive manifest references, enabling standardized integration, evaluation, and visualization.

## Asset Package Structure (`asset.zip`)

An ENVITED-X simulation asset follows a standardized file structure and a sample **`digital asset`** can be downloaded from the [GAIA-X4PLC-AAD/scenario-asset-example](https://github.com/ASCS-eV/scenario-asset-example) as artifact of the lastest release (**`asset.zip`**):

📁 `asset`

- 📁 `simulation-data`
  - 📄 `assetName.[ext]`
  - 📄 _`assetName_addition.[ext]` (optional)_
- 📁 `documentation`
  - 📄 `assetName_documentation.[ext]`
  - 📄 _`assetName_[Name].[ext]` (optional)_
- 📁 `metadata`
  - 📄 `[assetType]_instance.json`
- 📁 _`validation-reports` (optional)_
  - 📄 _`qcReport.[ext]` (optional)_
- 📁 `media`
  - 📁 _`3d_preview` -> e.g. 3d preview files (optional)_
  - 📄 `assetName_01.png` _-> eyecatcher_
  - 📄 _`assetName_[XX].png` -> impression (optional)_
  - 📄 _`assetName_other.[ext]` (optional)_
  - 📄 _`assetName_birdview.[ext]` (optional)_
- 📄 `README.md` -> this README
- 📄 `manifest_reference.json`

### Legend

- 📁 `folder-name`: Folder names are lower case and separated by hyphen.
- 📄 `assetName`: File names are lower camelCase.
- _* italic *_: Optional but recommended elements are italic in this README.

## Folder Descriptions

- 📁 **simulation-data**  
  Contains primary simulation files (e.g., OpenSCENARIO `.xosc` files or other domain-specific formats).

- 📁 **documentation**  
  Includes descriptive materials, technical instructions, and other supportive documentation.

- 📁 **metadata**  
  Holds structured metadata files (`simulationAsset_instance.json`), including:

  - Asset identification and descriptive information
  - Detailed metadata conforming to ENVITED-X ontologies and Gaia-X-specific metadata standards.

- 📁 **validation-reports** _(recommended)_  
  Stores quality check results generated by validation tools, such as quality assurance reports (`.txt`, `.xqar`).

- 📁 **media**  
  Contains visual assets for quick inspection, previews, or presentations, including:
  - Images (e.g., `.png` files)
  - Optional 3D previews or additional visualization media.

## File Descriptions

### 📄 `manifest_reference.json`

A structured manifest serving as a registry of all contained files and external references. It defines:

- **@context**: Defines namespace references for semantic clarity.
- **@id**: A unique identifier for the asset`s manifest.
- **@type**: Specifies the type as `envited-x:Manifest`.
- **License Information**: Clearly identifies license terms (e.g., MPL-2.0) along with direct links.
- **manifest:links**: A list of links describing files and external references. Each link includes:
  - **File Metadata**: File path or URL, MIME type, file size, and filename.
  - **Access Roles**: Defines file visibility (`isPublic`, `isRegistered`, `isOwner`), controlling accessibility.
  - **Artifact Categories**: Clearly categorizes linked assets (e.g., documentation, simulation data, media, licenses).

## Metadata Description (`simulationAsset_instance.json`)

The metadata instance file (`simulationAsset_instance.json`) fully describes the asset and integrates:

- **Core Metadata (envited-x:DataResource)**

  - **Name**: Human-readable asset name.
  - **Description**: Brief description of the asset’s purpose.

- **Data Resource Extensions** _(envited-x:DataResourceExtension)_  
  Enriches the asset metadata with details such as:
  - **Format**: Simulation format and version (e.g., "ASAM OpenSCENARIO 1.1").
  - **Content**: Information like abstraction level (e.g., Logical), scenario timestamp, simulation aim, and movement descriptions.
  - **Quantity**: Information about asset scope, including the number of traffic objects and controllers.
  - **Quality**: Quality-related information (accuracy, precision, etc.), if available.
  - **Data Source**: Information about the origin of the data, sensors, or measurement systems used.
  - **Optionally more (e.g. Georeference Information)**  
    Specifies geographical context including:
    - Project location (country, region, city, related area)
    - Geodetic reference system (EPSG code)
    - Bounding box coordinates for spatial referencing.

## Ontological Standards and Compliance

This simulation asset is aligned with a set of standardized ontologies to guarantee semantic consistency and interoperability:

- **ENVITED-X Ontology**: [envited-x](https://ontologies.envited-x.net/envited-x/v2/ontology#)
- **Manifest Ontology**: [manifest ontology v4](https://ontologies.envited-x.net/manifest/v5/ontology#)
- **Scenario Ontology**: [scenario ontology v4](https://ontologies.envited-x.net/scenario/v4/ontology#)
- **Georeference Ontology**: [georeference ontology v3](https://ontologies.envited-x.net/georeference/v3/ontology#)
- **Gaia-X Shape**: [gx](https://registry.lab.gaia-x.eu/development/api/trusted-shape-registry/v1/shapes/jsonld/trustframework#)
- **Gaia-X Trust Framework**: [version 22.10](https://docs.gaia-x.eu/policy-rules-committee/trust-framework/22.10/)

## Creating a Digital Asset

Use the [Gaia-X 4 PLC-AAD Provider Services](https://github.com/GAIA-X4PLC-AAD/provider-services) and [Provider Tools](https://github.com/GAIA-X4PLC-AAD/provider-tools) to generate and validate your own digital asset packages. Further guidance can be found in the [Ontology Management Base Repository](https://github.com/GAIA-X4PLC-AAD/ontology-management-base).
