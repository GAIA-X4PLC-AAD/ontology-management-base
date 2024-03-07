# Variables of SHACL Files in this folder

## Prefixes

- environment-model: <https://github.com/GAIA-X4PLC-AAD/ontology-management-base/tree/main/environment-model/>

## List of SHACL Properties

| Shape | Property prefix | Property | MinCount | MaxCount | Description | Datatype/NodeKind | Filename |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Asset_Shape | environment-model | environment-model_quality_texture_resolution | 0 | 1 | real texture resolution in meter (max?) | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_project_creation_version | 1 | 1 | tool for the creation of the data | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_quality_detail_level | 1 | 1 | category of the level of detail (High - highest level of detail with additional object enrichment, Med - directly from data sources, with environment, Low - topological representation). | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_quantity_geometry_count | 1 | 1 | Total number of all geoemtries, instances are considered only once | <http://www.w3.org/2001/XMLSchema#int> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_quantity_tile_size | 0 | 1 | tile size in meter | <http://www.w3.org/2001/XMLSchema#float> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_data_format | 1 | 1 | format type for visual system | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_project_version | 1 | 1 | version of visual system | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_quantity_tile_count_x | 0 | 1 | number of tiles as row | <http://www.w3.org/2001/XMLSchema#int> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_project_creation_source | 1 | 1 | tool for the creation of the data | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_data_version | 1 | 1 | nan | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_project_software_vendor | 1 | 1 | name of software vendor | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_quality_features | 0 | 1 | description of quality features | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_quantity_tile_count_y | 0 | 1 | number of tiles as column | <http://www.w3.org/2001/XMLSchema#int> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_quantity_texture_material_count | 1 | 1 | number of textures | <http://www.w3.org/2001/XMLSchema#unsignedInt> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_quantity_triangle_count | 1 | 1 | Total number of all triangles, instances are considered only once | <http://www.w3.org/2001/XMLSchema#int> | environment-model_shacl.ttl |
| Asset_Shape | environment-model | environment-model_project_software_name | 1 | 1 | name of the visual system | <http://www.w3.org/2001/XMLSchema#string> | environment-model_shacl.ttl |
