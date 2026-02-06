# Catalog and Search

This catalog is generated from `docs/registry.json` and is indexed by the site search. Use it to discover domains, versions, and ontology files. Each domain links to a dedicated page with class hierarchy and definitions, and the file columns link to raw files hosted under the documentation site.

## How to Search

- Use the documentation site search to find a domain, class name, or IRI.
- Open a domain page to browse class hierarchy and definitions.
- Query the registry locally with `jq` or Python.

Example `jq` query:

```bash
jq -r '.ontologies | to_entries[] | "\(.key)\t\(.value.latest)\t\(.value.iri)"' docs/registry.json
```

## Registry Catalog

<!-- START_REGISTRY_TABLE -->
|Domain|Latest|IRI|Ontology|SHACL|Context|Properties|Example Instance|
|---|---|---|---|---|---|---|---|
|automotive-simulator|v1|[IRI](https://w3id.org/gaia-x4plcaad/ontologies/automotive-simulator/v1)|[automotive-simulator.owl.ttl](../artifacts/automotive-simulator/v1/automotive-simulator.owl.ttl)|[automotive-simulator.shacl.ttl](../artifacts/automotive-simulator/v1/automotive-simulator.shacl.ttl)||[automotive-simulator Properties](properties/automotive-simulator.md)|[automotive-simulator_instance.json](../artifacts/automotive-simulator/v1/automotive-simulator_instance.json)|
|description|v0.5|[IRI](https://w3id.org/gaia-x4plcaad/ontologies/description/v1)|[description.owl.ttl](../artifacts/description/v0.5/description.owl.ttl)|[description.shacl.ttl](../artifacts/description/v0.5/description.shacl.ttl)||[description Properties](properties/description.md)||
|environment-model|v5|[IRI](https://w3id.org/ascs-ev/envited-x/environment-model/v5)|[environment-model.owl.ttl](../artifacts/environment-model/v5/environment-model.owl.ttl)|[environment-model.shacl.ttl](../artifacts/environment-model/v5/environment-model.shacl.ttl)||[environment-model Properties](properties/environment-model.md)|[environment-model_instance.json](../artifacts/environment-model/v5/environment-model_instance.json)|
|envited-x|v3|[IRI](https://w3id.org/ascs-ev/envited-x/envited-x/v3)|[envited-x.owl.ttl](../artifacts/envited-x/v3/envited-x.owl.ttl)|[envited-x.shacl.ttl](../artifacts/envited-x/v3/envited-x.shacl.ttl)||[envited-x Properties](properties/envited-x.md)|[envited-x_instance.json](../artifacts/envited-x/v3/envited-x_instance.json)|
|example|v0.5|[IRI](https://w3id.org/gaia-x4plcaad/ontologies/example/v1)|[example.owl.ttl](../artifacts/example/v0.5/example.owl.ttl)|[example.shacl.ttl](../artifacts/example/v0.5/example.shacl.ttl)||[example Properties](properties/example.md)|[example_instance.json](../artifacts/example/v0.5/example_instance.json)|
|general|v3|[IRI](https://w3id.org/gaia-x4plcaad/ontologies/general/v3)|[general.owl.ttl](../artifacts/general/v3/general.owl.ttl)|[general.shacl.ttl](../artifacts/general/v3/general.shacl.ttl)||[general Properties](properties/general.md)|[general_instance.json](../artifacts/general/v3/general_instance.json)|
|georeference|v5|[IRI](https://w3id.org/ascs-ev/envited-x/georeference/v5)|[georeference.owl.ttl](../artifacts/georeference/v5/georeference.owl.ttl)|[georeference.shacl.ttl](../artifacts/georeference/v5/georeference.shacl.ttl)||[georeference Properties](properties/georeference.md)|[georeference_instance.json](../artifacts/georeference/v5/georeference_instance.json)|
|gx|v25.11|[IRI](https://w3id.org/gaia-x/development#)|[gx.owl.ttl](../artifacts/gx/v25.11/gx.owl.ttl)|[gx.shacl.ttl](../artifacts/gx/v25.11/gx.shacl.ttl)|[gx.context.jsonld](../artifacts/gx/v25.11/gx.context.jsonld)|[gx Properties](properties/gx.md)|[gx_data_resource_instance.json](../artifacts/gx/v25.11/gx_data_resource_instance.json)|
|hdmap|v5|[IRI](https://w3id.org/ascs-ev/envited-x/hdmap/v5)|[hdmap.owl.ttl](../artifacts/hdmap/v5/hdmap.owl.ttl)|[hdmap.shacl.ttl](../artifacts/hdmap/v5/hdmap.shacl.ttl)||[hdmap Properties](properties/hdmap.md)|[hdmap_instance.json](../artifacts/hdmap/v5/hdmap_instance.json)|
|leakage-test|v2|[IRI](https://w3id.org/gaia-x4plcaad/ontologies/leakage-test/v2)|[leakage-test.owl.ttl](../artifacts/leakage-test/v2/leakage-test.owl.ttl)|[leakage-test.shacl.ttl](../artifacts/leakage-test/v2/leakage-test.shacl.ttl)||[leakage-test Properties](properties/leakage-test.md)|[leakage-test_instance.json](../artifacts/leakage-test/v2/leakage-test_instance.json)|
|manifest|v5|[IRI](https://w3id.org/ascs-ev/envited-x/manifest/v5)|[manifest.owl.ttl](../artifacts/manifest/v5/manifest.owl.ttl)|[manifest.shacl.ttl](../artifacts/manifest/v5/manifest.shacl.ttl)||[manifest Properties](properties/manifest.md)|[manifest_instance.json](../artifacts/manifest/v5/manifest_instance.json)|
|openlabel|v1.0.0|[IRI](https://openlabel.asam.net/V1-0-0/ontologies/)|[openlabel.owl.ttl](../artifacts/openlabel/v1.0.0/openlabel.owl.ttl)|[openlabel.shacl.ttl](../artifacts/openlabel/v1.0.0/openlabel.shacl.ttl)||[openlabel Properties](properties/openlabel.md)|[openlabel_instance.json](../artifacts/openlabel/v1.0.0/openlabel_instance.json)|
|ositrace|v5|[IRI](https://w3id.org/ascs-ev/envited-x/ositrace/v5)|[ositrace.owl.ttl](../artifacts/ositrace/v5/ositrace.owl.ttl)|[ositrace.shacl.ttl](../artifacts/ositrace/v5/ositrace.shacl.ttl)||[ositrace Properties](properties/ositrace.md)|[ositrace_instance.json](../artifacts/ositrace/v5/ositrace_instance.json)|
|scenario|v5|[IRI](https://w3id.org/ascs-ev/envited-x/scenario/v5)|[scenario.owl.ttl](../artifacts/scenario/v5/scenario.owl.ttl)|[scenario.shacl.ttl](../artifacts/scenario/v5/scenario.shacl.ttl)||[scenario Properties](properties/scenario.md)|[scenario_instance.json](../artifacts/scenario/v5/scenario_instance.json)|
|service|v1|[IRI](https://w3id.org/gaia-x4plcaad/ontologies/service/v1)|[service.owl.ttl](../artifacts/service/v1/service.owl.ttl)|[service.shacl.ttl](../artifacts/service/v1/service.shacl.ttl)||[service Properties](properties/service.md)|[service_instance.json](../artifacts/service/v1/service_instance.json)|
|simulated-sensor|v2|[IRI](https://w3id.org/gaia-x4plcaad/ontologies/simulated-sensor/v2)|[simulated-sensor.owl.ttl](../artifacts/simulated-sensor/v2/simulated-sensor.owl.ttl)|[simulated-sensor.shacl.ttl](../artifacts/simulated-sensor/v2/simulated-sensor.shacl.ttl)||[simulated-sensor Properties](properties/simulated-sensor.md)|[simulated-sensor_instance.json](../artifacts/simulated-sensor/v2/simulated-sensor_instance.json)|
|simulation-model|v2|[IRI](https://w3id.org/gaia-x4plcaad/ontologies/simulation-model/v2)|[simulation-model.owl.ttl](../artifacts/simulation-model/v2/simulation-model.owl.ttl)|[simulation-model.shacl.ttl](../artifacts/simulation-model/v2/simulation-model.shacl.ttl)||[simulation-model Properties](properties/simulation-model.md)|[simulation-model_instance.json](../artifacts/simulation-model/v2/simulation-model_instance.json)|
|surface-model|v6|[IRI](https://w3id.org/ascs-ev/envited-x/surface-model/v6)|[surface-model.owl.ttl](../artifacts/surface-model/v6/surface-model.owl.ttl)|[surface-model.shacl.ttl](../artifacts/surface-model/v6/surface-model.shacl.ttl)||[surface-model Properties](properties/surface-model.md)|[surface-model_instance.json](../artifacts/surface-model/v6/surface-model_instance.json)|
|survey|v6|[IRI](https://w3id.org/gaia-x4plcaad/ontologies/survey/v6)|[survey.owl.ttl](../artifacts/survey/v6/survey.owl.ttl)|[survey-result-data-offering.shacl.ttl](../artifacts/survey/v6/survey-result-data-offering.shacl.ttl)<br>[survey-service-offering.shacl.ttl](../artifacts/survey/v6/survey-service-offering.shacl.ttl)||[survey Properties](properties/survey.md)|[survey-result-data-offering_instance.json](../artifacts/survey/v6/survey-result-data-offering_instance.json)|
|tzip21|v1|[IRI](https://w3id.org/ascs-ev/envited-x/tzip21/v1)|[tzip21.owl.ttl](../artifacts/tzip21/v1/tzip21.owl.ttl)|[tzip21.shacl.ttl](../artifacts/tzip21/v1/tzip21.shacl.ttl)||[tzip21 Properties](properties/tzip21.md)|[tzip21_instance.json](../artifacts/tzip21/v1/tzip21_instance.json)|
|vv-report|v2|[IRI](https://w3id.org/gaia-x4plcaad/ontologies/vv-report/v2)|[vv-report.owl.ttl](../artifacts/vv-report/v2/vv-report.owl.ttl)|[vv-report.shacl.ttl](../artifacts/vv-report/v2/vv-report.shacl.ttl)||[vv-report Properties](properties/vv-report.md)|[vv-report_instance.json](../artifacts/vv-report/v2/vv-report_instance.json)|
<!-- END_REGISTRY_TABLE -->

## Regeneration

Regenerate the registry and catalogs with:

```bash
python3 -m src.tools.utils.registry_updater
```

