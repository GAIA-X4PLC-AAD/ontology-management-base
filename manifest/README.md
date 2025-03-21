# < envited-x:metadata:name >

< envited-x:metadata:description >

## Digital Assets

This is a digital asset according to the ENVITED Ecosystem Specification [EVES-003](https://ascs-ev.github.io/EVES/EVES-003/eves-003.html) for the ENVITED-X Data Space. It can be used as a template for other dataspaces as well. It contains a fully described and consistent example of a digital asset including a **`manifest_reference.json` - file** as content registry.

A complete **`digital asset`** in a specific domain includes the data itself and all necessary files for describing, evaluating, and visualizing the dataset.

## Example Asset Folder Structure

A sample **`digital asset`** can be downloaded from the [GAIA-X4PLC-AAD/hd-map-asset-example](https://github.com/ASCS-eV/hd-map-asset-example) as artifact of the lastest release (**`asset.zip`**) containing the following structure:

📁 `asset`

- 📁 `simulation-data`
  - 📄 `assetName.xodr`
  - 📄 *`assetName_offset.xodr`* <i style="color:gray;">(optional)</i>
- 📁 `documentation`
  - 📄 `assetName_Documentation.pdf`
  - 📄 *`assetName_[Name].[ext]`* <i style="color:gray;">(optional)</i>
- 📁 `metadata`
  - 📄 `simulationAsset_instance.json`
- 📁 *`validation-reports`* <i style="color:gray;">(optional)</i>
  - 📄 *`qcReport.txt`* <i style="color:gray;">(optional)</i>
- 📁 `media`
  - 📁 `3d_preview` *-> 3d preview files* <i style="color:gray;">(optional)</i>
  - 📄 `assetName_01.png` *-> eyecatcher*
  - 📄 *`assetName_[XX].png`* *-> impression* <i style="color:gray;">(optional)</i>
  - 📄 `bbox.geojson`
  - 📄 *`roadNetwork.geojson`* <i style="color:gray;">(optional)</i>
  - 📄 *`detailRoadNetwork.geojson`* <i style="color:gray;">(optional)</i>
- 📄 `README`
- 📄 `manifest.json`

### Legend

- 📁 `folder-name`: A folder in the repo.
- 📄 `assetName`: A file in the repo.
-  <i style="color:gray;">(optional)</i> : This file or folder is optional and can be added or omitted as needed.

### Description of the respective folders

- 📁 `simulation-data` : *Contains all valuble data files of the asset.*
- 📁 `documentation` : *Contains an instruction as well as technical specification of the asset.*
- 📁 `metadata` :   *Contains all metadata which are necassary to describe this asset, that includes all domain sepcific metadata from the [Ontology Management Base Repository](https://github.com/GAIA-X4PLC-AAD/ontology-management-base) (and all GAIA-X metadata form the [gaia-x-compliant-claims-example](https://github.com/GAIA-X4PLC-AAD/gaia-x-compliant-claims-example) to be compliant with the [GAIA-X Trust Framework](https://docs.gaia-x.eu/policy-rules-committee/trust-framework/22.10/). -> needs to be defined in a next step)*
- 📁 `validation-reports` :   *Contains the results provided by a validation suite.*
- 📁 `media` : *Contains all viusalization content from the asset which includes positionings decribed by a bounding box or maps as well as images and videos.*

### Description of the respective files

📄 `manifest_reference.json`:

- *This manifest file defined the link structure depending on the domain sepecific asset.zip. It includes a context section defining namespaces for various terms, an identifier (`@id`) for the asset, and a type (`@type`) indicating it is a manifest. The `manifest:links` section contains multiple entries, each specifying a type of link (e.g., license, simulation-data, media) with details such as relative paths, formats, and access roles. Optional metadata and visualization files are also included, with different access roles like `isOwner`,`isRegistered`, and `isPublic`.*

📄 `simulationAsset_instance.json` (domain metadata):

- *This JSON file describes the metadata and links associated with a simulation asset used in the Gaia-X 4 PLC-AAD project. It includes a context section defining namespaces for various terms, an identifier (@id) for the simulation asset, and a type (@type) indicating it is a simulation asset. The `DataResource` section provides details such as the name, description, and the GAIA-X metadata from the [gaia-x-compliant-claims-example](https://github.com/GAIA-X4PLC-AAD/gaia-x-compliant-claims-example) to be compliant with the [GAIA-X Trust Framework](https://docs.gaia-x.eu/policy-rules-committee/trust-framework/22.10/). The `manifest` section contains multiple entries, each specified by a category of link (e.g., simulation-data, metadata, media, documentation, validation-report) with details such as URLs and types. The `format` section specifies the type and version of the simulation asset format. The `content` section describes road types, lane types, and traffic direction. The `quantity` section provides measurements like length, elevation range, and counts of intersections, traffic lights, and signs. The `quality` section details precision and accuracy metrics. The `dataSource` section lists the data sources and measurement system used. Finally, the `georeference` section provides geolocation information, including the bounding box and geodetic reference system.*

### Create an asset

You can use the GaiaX 4 PLC-AAD [Provider Services](https://github.com/GAIA-X4PLC-AAD/provider-services) and [Provider Tools](https://github.com/GAIA-X4PLC-AAD/provider-tools) to create your own digital asset.

