# Catalog and Search

This catalog is generated from `docs/registry.json` and is indexed by the site search. Use it to discover domains, versions, and local file paths.

## How to Search

- Use the documentation site search to find a domain or IRI.
- Query the registry locally with `jq` or Python.

Example `jq` query:

```bash
jq -r '.ontologies | to_entries[] | "\(.key)\t\(.value.latest)\t\(.value.iri)"' docs/registry.json
```

## Registry Catalog

<!-- START_REGISTRY_TABLE -->
| Domain | Latest | IRI | Ontology | SHACL | Context | Example Instance |
| --- | --- | --- | --- | --- | --- | --- |
| automotive-simulator | v1 | https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1 | artifacts/automotive-simulator/automotive-simulator.owl.ttl | artifacts/automotive-simulator/automotive-simulator.shacl.ttl |  | tests/data/automotive-simulator/valid/automotive-simulator_instance.json |
| description | v0.5 | https://w3id.org/gaia-x4plcaad/ontologies/description/v1 | artifacts/description/description.owl.ttl | artifacts/description/description.shacl.ttl |  |  |
| environment-model | v5 | https://w3id.org/ascs-ev/envited-x/environment-model/v5 | artifacts/environment-model/environment-model.owl.ttl | artifacts/environment-model/environment-model.shacl.ttl |  | tests/data/environment-model/valid/environment-model_instance.json |
| envited-x | v3 | https://w3id.org/ascs-ev/envited-x/envited-x/v3 | artifacts/envited-x/envited-x.owl.ttl | artifacts/envited-x/envited-x.shacl.ttl |  | tests/data/envited-x/valid/envited-x_instance.json |
| example | v0.5 | https://w3id.org/gaia-x4plcaad/ontologies/example/v1 | artifacts/example/example.owl.ttl | artifacts/example/example.shacl.ttl |  | tests/data/example/valid/example_instance.json |
| general | v3 | https://w3id.org/gaia-x4plcaad/ontologies/general/v3 | artifacts/general/general.owl.ttl | artifacts/general/general.shacl.ttl |  | tests/data/general/valid/general_instance.json |
| georeference | v5 | https://w3id.org/ascs-ev/envited-x/georeference/v5 | artifacts/georeference/georeference.owl.ttl | artifacts/georeference/georeference.shacl.ttl |  | tests/data/georeference/valid/georeference_instance.json |
| gx | v25.11 | https://w3id.org/gaia-x/development/ | artifacts/gx/gx.owl.ttl | artifacts/gx/gx.shacl.ttl | artifacts/gx/gx.context.jsonld | tests/data/gx/valid/gx_data_resource_instance.json |
| hdmap | v5 | https://w3id.org/ascs-ev/envited-x/hdmap/v5 | artifacts/hdmap/hdmap.owl.ttl | artifacts/hdmap/hdmap.shacl.ttl |  | tests/data/hdmap/valid/hdmap_instance.json |
| leakage-test | v2 | https://w3id.org/gaia-x4plcaad/ontologies/leakage-test/v2 | artifacts/leakage-test/leakage-test.owl.ttl | artifacts/leakage-test/leakage-test.shacl.ttl |  | tests/data/leakage-test/valid/leakage-test_instance.json |
| manifest | v5 | https://w3id.org/ascs-ev/envited-x/manifest/v5 | artifacts/manifest/manifest.owl.ttl | artifacts/manifest/manifest.shacl.ttl |  | tests/data/manifest/valid/manifest_instance.json |
| openlabel | v1.0.0 | https://openlabel.asam.net/V1-0-0/ontologies/ | artifacts/openlabel/openlabel.owl.ttl | artifacts/openlabel/openlabel.shacl.ttl |  | tests/data/openlabel/valid/openlabel_instance.json |
| ositrace | v5 | https://w3id.org/ascs-ev/envited-x/ositrace/v5 | artifacts/ositrace/ositrace.owl.ttl | artifacts/ositrace/ositrace.shacl.ttl |  | tests/data/ositrace/valid/ositrace_instance.json |
| scenario | v5 | https://w3id.org/ascs-ev/envited-x/scenario/v5 | artifacts/scenario/scenario.owl.ttl | artifacts/scenario/scenario.shacl.ttl |  | tests/data/scenario/valid/scenario_instance.json |
| service | v1 | https://w3id.org/gaia-x4plcaad/ontologies/service/v1 | artifacts/service/service.owl.ttl | artifacts/service/service.shacl.ttl |  | tests/data/service/valid/service_instance.json |
| simulated-sensor | v2 | https://w3id.org/gaia-x4plcaad/ontologies/simulated-sensor/v2 | artifacts/simulated-sensor/simulated-sensor.owl.ttl | artifacts/simulated-sensor/simulated-sensor.shacl.ttl |  | tests/data/simulated-sensor/valid/simulated-sensor_instance.json |
| simulation-model | v2 | https://w3id.org/gaia-x4plcaad/ontologies/simulation-model/v2 | artifacts/simulation-model/simulation-model.owl.ttl | artifacts/simulation-model/simulation-model.shacl.ttl |  | tests/data/simulation-model/valid/simulation-model_instance.json |
| surface-model | v6 | https://w3id.org/ascs-ev/envited-x/surface-model/v6 | artifacts/surface-model/surface-model.owl.ttl | artifacts/surface-model/surface-model.shacl.ttl |  | tests/data/surface-model/valid/surface-model_instance.json |
| survey | v6 | https://w3id.org/gaia-x4plcaad/ontologies/survey/v6 | artifacts/survey/survey.owl.ttl | artifacts/survey/survey-result-data-offering.shacl.ttl<br>artifacts/survey/survey-service-offering.shacl.ttl |  | tests/data/survey/valid/survey-result-data-offering_instance.json |
| tzip21 | v1 | https://w3id.org/ascs-ev/envited-x/tzip21/v1 | artifacts/tzip21/tzip21.owl.ttl | artifacts/tzip21/tzip21.shacl.ttl |  | tests/data/tzip21/valid/tzip21_instance.json |
| vv-report | v2 | https://w3id.org/gaia-x4plcaad/ontologies/vv-report/v2 | artifacts/vv-report/vv-report.owl.ttl | artifacts/vv-report/vv-report.shacl.ttl |  | tests/data/vv-report/valid/vv-report_instance.json |
<!-- END_REGISTRY_TABLE -->

## Regeneration

Regenerate the registry and catalogs with:

```bash
python3 -m src.tools.utils.registry_updater
```

