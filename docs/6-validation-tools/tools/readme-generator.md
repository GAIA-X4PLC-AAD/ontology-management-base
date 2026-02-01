# Documentation Generator

**Module:** `src.tools.readme_generator`

This tool automatically generates `PROPERTIES.md` documentation files from SHACL shape definitions.

## Purpose

For each SHACL file in `artifacts/{ontology}/`, the generator extracts property definitions and creates a markdown table documenting:

- Shape names
- Property paths
- Cardinality constraints
- Datatypes and node kinds
- Descriptions

## Usage

### Command Line

```bash
python3 -m src.tools.readme_generator
```

### Output Location

Generated files are placed in:

```
artifacts/{domain}/PROPERTIES.md
```

For example:

```
artifacts/hdmap/PROPERTIES.md
artifacts/scenario/PROPERTIES.md
artifacts/envited-x/PROPERTIES.md
```

## Output Format

### Example PROPERTIES.md

```markdown
# Properties of SHACL Files for hdmap

## Prefixes

- hdmap: <https://w3id.org/.../hdmap/>
- schema: <http://schema.org/>

## List of SHACL Properties

| Shape      | Property prefix | Property    | MinCount | MaxCount | Description         | Datatype/NodeKind | Filename        |
| ---------- | --------------- | ----------- | -------- | -------- | ------------------- | ----------------- | --------------- |
| HDMapShape | hdmap           | name        | 1        | 1        | The name of the map | <xsd:string>      | hdmap_shacl.ttl |
| HDMapShape | schema          | dateCreated | 1        |          | Creation date       | <xsd:dateTime>    | hdmap_shacl.ttl |
```

## How It Works

### 1. Discover SHACL Files

Scans `artifacts/{ontology}/` for files matching `{ontology}.shacl.ttl`.

### 2. Parse RDF Graph

Uses rdflib to parse each Turtle file.

### 3. SPARQL Query

Extracts property details using:

```sparql
PREFIX sh: <http://www.w3.org/ns/shacl#>

SELECT ?shape ?path ?minCount ?maxCount ?description ?datatype ?nodeKind ?in
WHERE {
  ?shape a sh:NodeShape .
  ?shape sh:property ?property .
  ?property sh:path ?path .
  OPTIONAL { ?property sh:minCount ?minCount }
  OPTIONAL { ?property sh:maxCount ?maxCount }
  OPTIONAL { ?property sh:description ?description }
  OPTIONAL { ?property sh:datatype ?datatype }
  OPTIONAL { ?property sh:nodeKind ?nodeKind }
  OPTIONAL { ?property sh:in ?in }
}
```

### 4. Generate Markdown

Creates a markdown table with prefix-resolved property names.

## CI Integration

The generator runs as part of the CI pipeline:

```yaml
- name: Run Generator
  run: python3 -m src.tools.readme_generator

- name: Commit changes
  run: |
    if [[ -n $(git status --porcelain "artifacts/docs/*/PROPERTIES.md") ]]; then
      git add artifacts/docs/*/PROPERTIES.md
      git commit -m "docs: auto-generate PROPERTIES.md [skip ci]"
      git push
    fi
```

## Customization

To modify the output format, edit the `main()` function in `src/tools/properties_md_generator.py`.

Key customization points:

- Table columns (line ~70)
- Prefix handling (line ~80)
- File naming (line ~35)
