# Documentation Structure Proposal

## Executive Summary

This document proposes a comprehensive restructuring of the Ontology Management Base documentation to clarify the dual-domain architecture (GAIA-X 4 PLC-AAD project ontologies vs. ENVITED-X post-project developments), improve discoverability, and establish clear sections for different audience segments and technical concerns.

## Current State Analysis

### Existing Documentation Coverage

The current documentation covers:

- ✅ IRI patterns and w3id resolution
- ✅ OWL imports best practices
- ✅ Individual validation tools (SHACL, target classes, JSON-LD)
- ✅ Repository structure
- ⚠️ Two ontology domains mentioned only in metadata/code (not clearly explained in docs)
- ❌ Theoretical foundation (RDF/OWL/SHACL concepts for users)
- ❌ Building and testing guidelines
- ❌ Contributing workflows
- ❌ Service Characteristics integration details
- ❌ LinkML future direction and migration path
- ❌ High-level overview of validation tools together

### Missing Information

1. **Domain Distinction**: No clear documentation explaining:
   - GAIA-X 4 PLC-AAD project scope (2021-2024): https://w3id.org/gaia-x4plcaad/ontologies/
   - ENVITED-X post-project scope (2024+): https://w3id.org/ascs-ev/envited-x/
   - Why this split exists
   - Timeline and governance implications

2. **Previous Documentation**: Unclear if README.md files existed in artifact folders pre-restructuring

3. **Theoretical Foundation**: No standalone section on RDF/OWL/SHACL concepts for new users

4. **Service Characteristics**: Submodule exists but integration approach not documented

5. **LinkML Roadmap**: Future direction mentioned but not comprehensive

---

## Proposed Documentation Structure

```
docs/
├── 1-foundations/              # [NEW] Theory & Core Concepts
│   ├── index.md               # Overview of semantic modeling
│   ├── rdf-owl-shacl.md       # RDF, OWL, SHACL fundamentals
│   ├── linked-data-principles.md # Linked Data & IRIs
│   ├── semantic-versioning.md # How we version ontologies
│   └── best-practices.md      # General best practices
│
├── 2-architecture/            # [RESTRUCTURED] System Design
│   ├── index.md               # Architecture overview
│   ├── domains.md             # [NEW] The two domains explained
│   ├── iri-patterns.md        # [REVISED] IRI structure & resolution
│   ├── ontology-discovery.md  # How tools find ontologies
│   ├── owl-imports.md         # Import strategy
│   └── w3id-publishing.md     # [NEW] w3id.org setup & redirects
│
├── 3-ontology-domains/        # [REORGANIZED] Catalog
│   ├── index.md               # Master index
│   ├── gaia-x4plcaad/         # [NEW] Project-era ontologies
│   │   ├── index.md           # Domain overview
│   │   └── ontologies.md      # List with details
│   └── envited-x/             # [NEW] Post-project ontologies
│       ├── index.md           # Domain overview
│       └── ontologies.md      # List with details
│
├── 4-getting-started/         # [RESTRUCTURED] For New Users
│   ├── quickstart.md          # 5-minute start
│   ├── installation.md        # Environment setup
│   ├── first-validation.md    # [NEW] Your first check
│   └── structure.md           # [REVISED] Folder organization
│
├── 5-building-contributing/   # [NEW] For Developers
│   ├── index.md               # Overview
│   ├── contributing.md        # [MOVED] DCO & commit guidelines
│   ├── adding-ontologies.md   # [NEW] How to add domain
│   ├── testing-workflow.md    # [NEW] Test structure & patterns
│   ├── build-process.md       # [NEW] How to build & validate
│   └── releasing.md           # [NEW] Release process
│
├── 6-validation-tools/        # [REORGANIZED] Validation Catalog
│   ├── index.md               # Overview & comparison matrix
│   ├── quick-reference.md     # [NEW] Command cheatsheet
│   ├── architecture.md        # [NEW] Tool architecture & flow
│   ├── tools/
│   │   ├── run-all-checks.md
│   │   ├── check-jsonld-shacl.md
│   │   ├── check-check-artifact-coherence.md
│   │   └── readme-generator.md
│   └── troubleshooting.md     # [NEW] Common issues & fixes
│
├── 7-service-characteristics/ # [NEW] Gaia-X Integration
│   ├── index.md               # What is Service Characteristics?
│   ├── integration.md         # How we use it
│   ├── mapping-guide.md       # [NEW] Service Char ↔ Ontology mapping
│   └── schema-reuse.md        # [NEW] How to reuse schemas
│
├── 8-linkml-future/           # [NEW] Future Direction
│   ├── index.md               # Vision & timeline
│   ├── why-linkml.md          # [NEW] Advantages & rationale
│   ├── migration-plan.md      # [EXPANDED] Detailed roadmap
│   ├── getting-started.md     # [NEW] Starting with LinkML
│   └── examples/              # [NEW] Migration examples
│       ├── simple-example.md
│       └── complex-example.md
│
├── 9-advanced/                # [NEW] Deep Dives
│   ├── iri-resolution.md      # How w3id.org redirects work
│   ├── content-negotiation.md # Turtle vs JSON-LD vs RDF/XML
│   ├── import-optimization.md # Performance tuning
│   └── ci-cd-pipeline.md      # GitHub Actions workflow
│
├── migration-notes/           # [PRESERVED] Historical Docs
│   ├── MIGRATION_SUMMARY.md
│   ├── ontology_architecture_and_migration_masterplan.md
│   ├── ontology_repo_restructuring_for_validation.md
│   ├── owl_imports_best_practices.md
│   └── iri_restructuring_pattern.md
│
├── ontologies/                # [EXISTING] Keep as-is
├── registry.json              # [EXISTING] Keep as-is
└── mkdocs.yml                 # [UPDATED] New nav structure
```

---

## Section Details

### 1. Foundations (NEW)

**Purpose**: Help new users understand RDF, OWL, and SHACL at a conceptual level.

**Files**:

- **index.md**: Overview of semantic modeling approach
- **rdf-owl-shacl.md**:
  - What is RDF? (Triples, URIs, literals)
  - What is OWL? (Classes, properties, constraints)
  - What is SHACL? (Validation shapes, constraints)
  - How they work together
- **linked-data-principles.md**:
  - Dereferenceable URIs
  - Content negotiation
  - Linked Data best practices
- **semantic-versioning.md**:
  - How we version ontologies (v1, v2, v3)
  - Breaking changes
  - Deprecation policy
- **best-practices.md**:
  - Class naming conventions
  - Property domain/range
  - Documentation standards

**Audience**: ontologists, data engineers, new contributors

---

### 2. Architecture (RESTRUCTURED)

**Purpose**: Explain system design and how components fit together.

**New file: domains.md** - The Two Ontology Domains

```markdown
# The Two Ontology Domains

## Overview

This repository maintains ontologies in two separate IRI namespaces, each with different governance and timelines:

### 1. GAIA-X 4 PLC-AAD Project Ontologies

- **IRI Namespace**: `https://w3id.org/gaia-x4plcaad/ontologies/`
- **Timeline**: 2021-2024 (Project runtime)
- **Ontologies**: automotive-simulator, environment-model, general, georeference, hdmap, leakage-test, manifest, ositrace, scenario, service, simulated-sensor, simulation-model, surface-model, survey, tzip21, vv-report
- **Maintenance**: Maintained by the project team and may enter stable/legacy status
- **Use Case**: Research and development within the project scope
- **Example IRI**:
```

https://w3id.org/gaia-x4plcaad/ontologies/hdmap/v5
https://w3id.org/gaia-x4plcaad/ontologies/general/v3

```

### 2. ENVITED-X Post-Project Ontologies
- **IRI Namespace**: `https://w3id.org/ascs-ev/envited-x/`
- **Timeline**: 2024+ (Post-project development)
- **Ontologies**: envited-x, gx, example, description, and future developments
- **Maintenance**: Actively developed within the ENVITED-X Data Space
- **Use Case**: Production systems, ENVITED-X data space participants
- **Example IRI**:
```

https://w3id.org/ascs-ev/envited-x/envited-x/v3
https://w3id.org/ascs-ev/envited-x/gx/v1

````

## Why Two Namespaces?

1. **Governance Clarity**: Clear separation between project outputs and ongoing development
2. **Backward Compatibility**: Project ontologies remain frozen or update independently
3. **Organizational Alignment**: Project under GAIA-X, post-project under ASCS-EV/ENVITED-X
4. **IRI Persistence**: w3id.org stable redirects guarantee permanent access

## Cross-Domain Imports

Ontologies from different domains can import each other:

```turtle
@prefix envited-x: <https://w3id.org/ascs-ev/envited-x/envited-x/v3/> .
@prefix hdmap: <https://w3id.org/gaia-x4plcaad/ontologies/hdmap/v5/> .

envited-x:SensorConfiguration a owl:Class ;
  rdfs:comment "Uses concepts from GAIA-X project hdmap" ;
  owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/hdmap/v5> .
````

## Finding Ontologies by Domain

- See [GAIA-X 4 PLC-AAD Ontologies](../ontology-domains/gaia-x4plcaad/index.md)
- See [ENVITED-X Ontologies](../ontology-domains/envited-x/index.md)

````

**New file: w3id-publishing.md** - How w3id.org Integration Works

```markdown
# W3ID Publishing and Resolution

## Overview

All ontologies are published through [w3id.org](https://w3id.org), a service that provides stable, permanent identifiers (Persistent IRIs).

## Architecture

### URL Structure

````

https://w3id.org/{namespace}/{domain}/{version}

````

Examples:
- `https://w3id.org/ascs-ev/envited-x/hdmap/v5`
- `https://w3id.org/gaia-x4plcaad/ontologies/general/v3`

### Resolution Process

1. **Request**: Client sends HTTP request to w3id.org URL
2. **Content Negotiation**: Client specifies desired format via Accept header
3. **Redirect**: w3id.org resolves to actual file location
4. **Response**: Server returns ontology in requested format

### Example Flow

```bash
# Request OWL in Turtle format
curl -H "Accept: text/turtle" \
  https://w3id.org/ascs-ev/envited-x/hdmap/v5

# w3id.org routes to:
# → GitHub → artifacts/hdmap/hdmap.owl.ttl
# Response: 200 OK + Turtle content
````

### Content Negotiation

| Accept Header         | File Format | Use Case               |
| --------------------- | ----------- | ---------------------- |
| `text/turtle`         | `.ttl`      | RDF editors, reasoners |
| `application/rdf+xml` | `.rdf`      | Legacy tools           |
| `application/ld+json` | `.jsonld`   | JSON-based tools       |
| (no accept)           | HTML        | Browser viewing        |

## Configuration

w3id.org configuration is stored in the repository:

- Location: `w3id.org/` directory (version controlled)
- Format: `.htaccess` files or YAML config
- Maintained via: Pull requests to w3id organization

### Adding New Ontologies

1. Create ontology in `artifacts/{domain}/`
2. Add resolution rule in `w3id.org/{namespace}/.htaccess`
3. Update `docs/registry.json` with metadata
4. Push to main branch (CI automatically updates w3id.org)

## Version Resolution

### Specific Versions

```bash
# Get v3 specifically
curl https://w3id.org/ascs-ev/envited-x/hdmap/v3
```

### Latest Version

```bash
# Get the latest version (determined by registry.json)
curl https://w3id.org/ascs-ev/envited-x/hdmap/latest
```

### Content Negotiation + Version

```bash
# Get v5 in JSON-LD format
curl -H "Accept: application/ld+json" \
  https://w3id.org/ascs-ev/envited-x/hdmap/v5
```

## CORS and APIs

- w3id.org returns proper HTTP headers for CORS
- Can be used from web browsers
- Returns `Access-Control-Allow-Origin: *`

## Troubleshooting

### "Not Found" Response

Check:

1. Domain name is correct
2. Version exists in registry.json
3. Ontology file exists in artifacts/

### "Too Many Redirects"

Check for circular redirects in `.htaccess`

### Wrong Format Returned

Verify Accept header is correct

````

---

### 3. Ontology Domains (NEW ORGANIZATION)

**Purpose**: Separate ontologies by domain/namespace for clarity.

**Structure**:
- `gaia-x4plcaad/index.md`: Overview + governance
- `gaia-x4plcaad/ontologies.md`: Detailed list with version history
- `envited-x/index.md`: Overview + governance
- `envited-x/ontologies.md`: Detailed list with version history

---

### 4. Getting Started (SIMPLIFIED)

**Purpose**: Fast onboarding for new users.

**New file: first-validation.md** - Your First Validation

```markdown
# Your First Validation

## 5-Minute Quick Start

### Step 1: Install Dependencies (1 min)

```bash
git clone https://github.com/gaia-x4plc-aad/ontology-management-base.git
cd ontology-management-base
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
````

### Step 2: Validate a Sample Instance (2 min)

```bash
# Validate all domains
python3 -m src.tools.validators.validation_suite --run all

# Or just SHACL checks
python3 -m src.tools.validators.validation_suite --run check-data-conformance
```

### Step 3: Validate Your Own Instance (2 min)

```bash
# Create test file: test-hdmap.json
{
  "@context": "https://w3id.org/ascs-ev/envited-x/hdmap/context",
  "@id": "did:web:example:hdmap:123",
  "@type": "hdmap:HDMap",
  "hdmap:hasContent": {...}
}

# Validate
python3 -m src.tools.validators.check_jsonld_against_shacl_schema \
  hdmap test-hdmap.json
```

## What Just Happened?

The tool:

1. Found the SHACL file: `artifacts/hdmap/hdmap.shacl.ttl`
2. Loaded the OWL ontology: `artifacts/hdmap/hdmap.owl.ttl`
3. Validated your JSON-LD against the shapes
4. Printed errors or "✅ Valid"

## Next Steps

- Learn about [the two domains](../architecture/domains.md)
- Explore [validation tools](../validation-tools/)
- Read [building & contributing](../building-contributing/)

````

---

### 5. Building & Contributing (NEW)

**Purpose**: Guide for contributors.

**New files**:
- **index.md**: Overview of contribution workflow
- **adding-ontologies.md**: How to add a new domain
- **testing-workflow.md**: How tests are organized
- **build-process.md**: How to build artifacts
- **releasing.md**: How to cut releases

**Example: adding-ontologies.md**

```markdown
# Adding a New Ontology Domain

## Overview

This guide walks you through adding a new ontology domain to the repository.

## Steps

### 1. Choose Namespace

Decide which domain your ontology belongs to:
- **GAIA-X 4 PLC-AAD**: For ontologies from the 2021-2024 project
  - Namespace: `https://w3id.org/gaia-x4plcaad/ontologies/`
  - Example: `https://w3id.org/gaia-x4plcaad/ontologies/{domain}/v1`

- **ENVITED-X**: For post-project developments
  - Namespace: `https://w3id.org/ascs-ev/envited-x/`
  - Example: `https://w3id.org/ascs-ev/envited-x/{domain}/v1`

### 2. Create Artifact Files

```bash
mkdir -p artifacts/{domain}
touch artifacts/{domain}/{domain}.owl.ttl
touch artifacts/{domain}/{domain}.shacl.ttl
````

### 3. Write OWL Ontology

Use the template:

```turtle
@prefix {domain}: <https://w3id.org/ascs-ev/envited-x/{domain}/v1/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .

<https://w3id.org/ascs-ev/envited-x/{domain}/v1> a owl:Ontology ;
    rdfs:label "Your Domain Ontology"@en ;
    owl:versionInfo "v1" ;
    owl:versionIRI <https://w3id.org/ascs-ev/envited-x/{domain}/v1> ;
    dcterms:created "2024-01-01" ;
    dcterms:creator "Your Name" ;
    dcterms:conformsTo <https://w3id.org/ascs-ev/envited-x/{domain}/v1/shapes> .

# Define your classes and properties
{domain}:YourClass a owl:Class ;
    rdfs:label "Your Class" .
```

### 4. Write SHACL Shapes

```turtle
@prefix {domain}: <https://w3id.org/ascs-ev/envited-x/{domain}/v1/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .

<https://w3id.org/ascs-ev/envited-x/{domain}/v1/shapes> a owl:Ontology ;
    owl:imports <https://w3id.org/ascs-ev/envited-x/{domain}/v1> .

{domain}:YourClassShape a sh:NodeShape ;
    sh:targetClass {domain}:YourClass ;
    sh:property [
        sh:path {domain}:someProperty ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
    ] .
```

### 5. Create Test Instances

```bash
mkdir -p tests/data/{domain}/valid
mkdir -p tests/data/{domain}/invalid

# Create valid instance
cat > tests/data/{domain}/valid/{domain}_instance.json << 'EOF'
{
  "@context": "https://w3id.org/ascs-ev/envited-x/{domain}/context",
  "@id": "did:web:example:{domain}:1",
  "@type": "{domain}:YourClass",
  "{domain}:someProperty": "value"
}
EOF

# Create invalid instance
cat > tests/data/{domain}/invalid/fail_missing_property.json << 'EOF'
{
  "@context": "https://w3id.org/ascs-ev/envited-x/{domain}/context",
  "@id": "did:web:example:{domain}:2",
  "@type": "{domain}:YourClass"
}
EOF
```

### 6. Test Locally

```bash
python3 -m src.tools.validators.check_jsonld_against_shacl_schema \
  {domain} tests/data/{domain}/valid/{domain}_instance.json

# Should show ✅ Valid
```

### 7. Add to Documentation

```bash
cat > docs/ontologies/{domain}.md << 'EOF'
# {Domain} Ontology

Brief description.

## IRI
`https://w3id.org/ascs-ev/envited-x/{domain}/v1`

## Classes
- {domain}:YourClass - Description

## Files
- Ontology: `artifacts/{domain}/{domain}.owl.ttl`
- SHACL: `artifacts/{domain}/{domain}.shacl.ttl`
EOF
```

### 8. Configure w3id Resolution

Edit `w3id.org/ascs-ev/envited-x/.htaccess`:

```apache
RewriteRule ^{domain}/(.*)$ https://raw.githubusercontent.com/gaia-x4plc-aad/ontology-management-base/main/artifacts/{domain/{domain}.owl.ttl [R=303,L]
```

### 9. Update Config

Edit `config/ontoenv.toml`:

```toml
[dependencies.{domain}]
uri = "https://w3id.org/ascs-ev/envited-x/{domain}/"
local = "artifacts/{domain}/{domain}.owl.ttl"
description = "Description"
```

### 10. Commit and Push

```bash
git add artifacts/{domain}/ tests/data/{domain}/ docs/ontologies/{domain}.md
git commit -m "feat: add {domain} ontology"
git push
```

CI will automatically:

1. Validate your files
2. Update registry.json
3. Deploy to w3id.org
4. Build documentation

## Checklist

- [ ] OWL file is valid Turtle
- [ ] SHACL file validates OWL ontology
- [ ] At least one valid test instance exists
- [ ] At least one invalid test instance exists
- [ ] Documentation exists
- [ ] w3id config added
- [ ] ontoenv.toml updated
- [ ] Commit is signed-off (DCO)

````

---

### 6. Validation Tools (REORGANIZED)

**Purpose**: Comprehensive guide to all validation tools.

**New file: index.md** - Validation Tools Overview

```markdown
# Validation Tools

## Quick Comparison

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| **run-all-checks** | Orchestrate all validations | Domain | Report |
| **check-jsonld-shacl** | SHACL shape validation | JSON-LD file | ✅/❌ |
| **check-check-artifact-coherence** | Class existence check | Domain | ✅/❌ |
| **readme-generator** | Generate PROPERTIES.md | SHACL files | Markdown |

## Which Tool Do I Need?

### I want to validate my JSON-LD instance
→ Use [`check-jsonld-against-shacl`](tools/check-jsonld-shacl.md)

### I want to check all domains at once
→ Use [`run-all-checks`](tools/run-all-checks.md)

### I want to ensure all SHACL target classes exist in OWL
→ Use [`check-check-artifact-coherence`](tools/check-check-artifact-coherence.md)

### I want to auto-generate documentation
→ Use [`readme-generator`](tools/readme-generator.md)

## Validation Flow

````

Your Instance (JSON-LD)
↓
[SHACL Shape Validation] ← OWL + SHACL
↓
Target Classes Check ← OWL
↓
Result: Valid/Invalid

```

See [Architecture](architecture.md) for details.
```

**New file: troubleshooting.md** - Common Issues

````markdown
# Troubleshooting Validation

## "No ontology file found"

**Problem**: Tool says it can't find the OWL file.

**Causes**:

1. Wrong domain name
2. Ontology file doesn't exist in `artifacts/{domain}/`
3. File named incorrectly (should be `{domain}.owl.ttl`)

**Solution**:

```bash
ls artifacts/{domain}/
# Check that {domain}.owl.ttl exists
```
````

## "SHACL validation failed: unknown class"

**Problem**: Target class in SHACL doesn't exist in OWL.

**Cause**: Mismatch between SHACL shape and OWL ontology.

**Solution**:

```bash
# Check if class exists in OWL
grep "a owl:Class" artifacts/{domain}/{domain}.owl.ttl | grep ClassName

# If missing, add it to OWL file
# If named differently, update SHACL
```

## "IRI not resolvable"

**Problem**: Cannot fetch ontology from w3id.org

**Causes**:

1. Domain not yet deployed
2. w3id config outdated
3. Network issue

**Solution**:

```bash
# Test local file
curl -f artifacts/{domain}/{domain}.owl.ttl

# Test w3id
curl -f https://w3id.org/ascs-ev/envited-x/{domain}/v1
```

## "Content negotiation fails"

**Problem**: Can't get Turtle format from w3id.org

**Solution**: Ensure w3id config has content negotiation rules

````

---

### 7. Service Characteristics (NEW)

**Purpose**: Explain Gaia-X service-characteristics integration.

**New file: index.md** - What is Service Characteristics?

```markdown
# Service Characteristics Integration

## Overview

The [Gaia-X Service Characteristics](https://gitlab.com/gaia-x/technical-committee/service-characteristics) project maintains a set of reusable JSON Schema definitions for describing services in the Gaia-X ecosystem.

This repository includes the service-characteristics project as a git submodule to enable:
1. Schema reuse in our ontologies
2. Alignment with Gaia-X standards
3. Semantic mapping between schemas and RDF

## What is Provided

### Core Schemas

Located in `service-characteristics/linkml/`:
- Service description schemas
- Certification schemas
- Compliance schemas
- Participant/Provider schemas

## How We Use It

### 1. Schema Analysis

We analyze service-characteristics schemas to understand what domain concepts need to be represented in our ontologies.

### 2. Ontology Alignment

Our ontologies define RDF equivalents of key service characteristics concepts:

```turtle
sc:Service owl:equivalentClass envited-x:ServiceOffering ;
    rdfs:comment "Service Characteristics 'Service' maps to our ServiceOffering" .
````

### 3. JSON-LD Context Mapping

Context files map service characteristics JSON keys to our ontology IRIs:

```jsonld
{
  "@context": {
    "serviceType": { "@id": "envited-x:hasServiceType" },
    "provider": { "@id": "envited-x:providedBy" }
  }
}
```

## Integration Points

| Service Characteristics | Our Ontology                     | Mapping                 |
| ----------------------- | -------------------------------- | ----------------------- |
| `Service`               | `envited-x:ServiceOffering`      | service.yml → ontology  |
| `Provider`              | `envited-x:Provider`             | provider.yml → ontology |
| `Certification`         | `envited-x:ServiceCertification` | cert.yml → ontology     |

## Viewing Service Characteristics

```bash
# Explore current schemas
cd service-characteristics
find linkml/ -name "*.yaml" | head

# Read a schema
cat service-characteristics/linkml/service.yaml
```

## Updating Service Characteristics

```bash
# Pull latest changes from upstream
cd service-characteristics
git fetch origin
git merge origin/main

cd ..
git add service-characteristics
git commit -m "chore: update service-characteristics submodule"
```

See [integration guide](integration.md) for technical details.

````

---

### 8. LinkML Future (NEW)

**Purpose**: Explain LinkML migration path.

**New file: index.md** - LinkML Vision

```markdown
# LinkML-Driven Architecture

## Vision

Transition from hand-crafted OWL/SHACL to **LinkML as the single source of truth**, enabling:

````

LinkML Schema (.yaml)
↓ (auto-generated)
├→ OWL Ontology (.ttl)
├→ SHACL Shapes (.ttl)
├→ JSON-LD Context (.jsonld)
├→ JSON Schema (.json)
└→ Markdown Docs (.md)

````

## Why LinkML?

| Aspect | LinkML | Manual OWL/SHACL |
|--------|--------|-----------------|
| Single Source | ✅ YAML | ❌ Multiple files |
| Consistency | ✅ Auto-generated | ⚠️ Manual sync |
| Validation | ✅ Built-in | ⚠️ Custom tools |
| Documentation | ✅ Auto-generated | ⚠️ Manual |
| Reuse | ✅ Modularity | ⚠️ Copy-paste |

## Timeline

- **Phase 1** (Now): Parallel systems
  - Keep OWL/SHACL for production
  - Start LinkML schemas

- **Phase 2** (Q3 2024): Validation
  - Validate LinkML → OWL/SHACL generation
  - Compare outputs with current

- **Phase 3** (Q4 2024): Migration
  - Switch to LinkML as source
  - Auto-generate artifacts in CI

- **Phase 4** (2025): Full adoption
  - Remove hand-crafted OWL/SHACL
  - Deprecate old format

See [migration plan](migration-plan.md) for detailed roadmap.

## Examples

```yaml
# src/linkml/envited-x.yaml
id: https://w3id.org/ascs-ev/envited-x/envited-x/v3
name: envited-x
title: ENVITED-X Ontology

classes:
  ServiceOffering:
    description: A service offered in the data space
    attributes:
      providedBy:
        range: Provider
        required: true

      hasServiceType:
        range: string
````

Gets auto-generated to:

```turtle
# artifacts/envited-x/envited-x.owl.ttl
envited-x:ServiceOffering a owl:Class ;
    rdfs:comment "A service offered in the data space" .

envited-x:providedBy a owl:ObjectProperty ;
    rdfs:domain envited-x:ServiceOffering ;
    rdfs:range envited-x:Provider ;
    sh:minCount 1 .
```

See [getting started with LinkML](getting-started.md).

````

---

### 9. Advanced (NEW)

**Purpose**: Deep technical dives.

Covers:
- IRI resolution mechanisms
- Content negotiation details
- Import performance optimization
- CI/CD pipeline

---

### 10. Migration Notes (PRESERVED)

**Purpose**: Keep historical documentation for reference.

Files:
- `MIGRATION_SUMMARY.md`
- `ontology_architecture_and_migration_masterplan.md`
- `ontology_repo_restructuring_for_validation.md`
- `owl_imports_best_practices.md`
- `iri_restructuring_pattern.md`

These become read-only reference materials.

---

## MkDocs Configuration Update

**mkdocs.yml** navigation should be:

```yaml
site_name: Ontology Management Base
site_description: GAIA-X and ENVITED-X Ontology Hub

theme:
  name: material

nav:
  - Home: index.md
  - 1. Foundations:
    - Overview: foundations/index.md
    - RDF, OWL, SHACL: foundations/rdf-owl-shacl.md
    - Linked Data: foundations/linked-data-principles.md
    - Versioning: foundations/semantic-versioning.md
    - Best Practices: foundations/best-practices.md

  - 2. Architecture:
    - Overview: architecture/index.md
    - The Two Domains: architecture/domains.md
    - IRI Patterns: architecture/iri-patterns.md
    - W3ID Publishing: architecture/w3id-publishing.md
    - Discovery Mechanism: architecture/ontology-discovery.md
    - OWL Imports: architecture/owl-imports.md

  - 3. Ontology Domains:
    - Index: ontology-domains/index.md
    - GAIA-X 4 PLC-AAD:
      - Overview: ontology-domains/gaia-x4plcaad/index.md
      - Ontologies: ontology-domains/gaia-x4plcaad/ontologies.md
    - ENVITED-X:
      - Overview: ontology-domains/envited-x/index.md
      - Ontologies: ontology-domains/envited-x/ontologies.md

  - 4. Getting Started:
    - Quick Start: getting-started/quickstart.md
    - Installation: getting-started/installation.md
    - First Validation: getting-started/first-validation.md
    - Repository Structure: getting-started/structure.md

  - 5. Building & Contributing:
    - Overview: building-contributing/index.md
    - Contributing Guidelines: building-contributing/contributing.md
    - Adding Ontologies: building-contributing/adding-ontologies.md
    - Testing Workflow: building-contributing/testing-workflow.md
    - Build Process: building-contributing/build-process.md
    - Release Process: building-contributing/releasing.md

  - 6. Validation Tools:
    - Overview: validation-tools/index.md
    - Quick Reference: validation-tools/quick-reference.md
    - Tool Architecture: validation-tools/architecture.md
    - Run All Checks: validation-tools/tools/run-all-checks.md
    - Check SHACL: validation-tools/tools/check-jsonld-shacl.md
    - Check Classes: validation-tools/tools/check-check-artifact-coherence.md
    - Generate Docs: validation-tools/tools/readme-generator.md
    - Troubleshooting: validation-tools/troubleshooting.md

  - 7. Service Characteristics:
    - Overview: service-characteristics/index.md
    - Integration: service-characteristics/integration.md
    - Mapping Guide: service-characteristics/mapping-guide.md
    - Schema Reuse: service-characteristics/schema-reuse.md

  - 8. LinkML Future:
    - Vision: linkml-future/index.md
    - Why LinkML: linkml-future/why-linkml.md
    - Migration Plan: linkml-future/migration-plan.md
    - Getting Started: linkml-future/getting-started.md

  - 9. Advanced Topics:
    - IRI Resolution: advanced/iri-resolution.md
    - Content Negotiation: advanced/content-negotiation.md
    - Performance Tuning: advanced/import-optimization.md
    - CI/CD Pipeline: advanced/ci-cd-pipeline.md

  - Reference: migration-notes/index.md
````

---

## Implementation Roadmap

### Phase 1: Structure (This Week)

1. Create new folder structure in `docs/`
2. Move existing files to new locations
3. Update mkdocs.yml
4. Create stubs for all new files

### Phase 2: Foundational Content (Week 2)

1. Write 1. Foundations section
2. Update 2. Architecture with new files
3. Create 3. Ontology Domains reorganization

### Phase 3: Contributor Focus (Week 3)

1. Write 5. Building & Contributing
2. Write 6. Validation Tools reorganization
3. Create troubleshooting guide

### Phase 4: Advanced Topics (Week 4)

1. Write 7. Service Characteristics
2. Expand 8. LinkML Future with examples
3. Write 9. Advanced Topics

### Phase 5: Polish (Week 5)

1. Add cross-references
2. Add diagrams/flowcharts
3. Test navigation
4. Peer review

---

## Key Improvements

✅ **Clarity on Domains**: Two separate namespace sections explain project vs. post-project ontologies  
✅ **Theoretical Foundation**: New foundations section helps beginners understand RDF/OWL/SHACL  
✅ **Contributor Path**: Clear guide for adding ontologies and testing  
✅ **Tool Overview**: Consolidated validation tools with comparison matrix  
✅ **Service Characteristics**: Dedicated section on integration  
✅ **LinkML Roadmap**: Comprehensive migration path with examples  
✅ **Better Navigation**: Numbered sections with clear audience targeting  
✅ **Preservation**: Historical docs kept but separated from main flow

---

## Questions for Feedback

1. **Domain Clarity**: Is the GAIA-X 4 PLC-AAD vs. ENVITED-X distinction clear enough?
2. **Audience Segmentation**: Are the sections well-targeted for their intended audiences?
3. **Depth**: Should any sections be deeper or shallower?
4. **LinkML Timeline**: Is the Phase 1-4 timeline realistic?
5. **Service Characteristics**: Is the integration level detailed enough?

---

## Notes on Previous README.md Files

Investigation shows:

- No README.md files currently exist in artifact folders
- Git history doesn't show remnants of per-ontology README files
- All documentation is centralized in `docs/`
- This is appropriate for a monolithic ontology repository

**Recommendation**: Keep documentation centralized; add ontology-specific pages in `docs/ontology-domains/{domain}/` as needed.
