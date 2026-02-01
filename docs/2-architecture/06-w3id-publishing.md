# W3ID Publishing and IRI Resolution

This guide explains how ontologies in this repository are published through w3id.org persistent identifiers and resolved to their implementation locations.

## Overview

We use the **w3id.org** service for persistent, resolvable IRIs that point to our ontologies hosted on GitHub. This provides several benefits:

- **Persistence**: IRIs remain stable even if hosting changes
- **Content Negotiation**: Serve different formats (RDF/XML, Turtle, JSON-LD) based on client requests
- **Versioning**: Support multiple versions of ontologies simultaneously
- **Human Access**: HTML documentation alongside machine-readable formats

## IRI Structure

### GAIA-X 4 PLC-AAD Ontologies

```
https://w3id.org/gaia-x4plcaad/ontologies/{ontology}/v{major}/
```

**Example:**

```
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/
```

**Resolution Target (GitHub):**

```
https://raw.githubusercontent.com/YOUR-ORG/ontology-management-base/main/artifacts/scenario/scenario.owl.ttl
```

### ENVITED-X Ontologies

```
https://w3id.org/ascs-ev/envited-x/{ontology}/v{major}.{minor}/
```

**Example:**

```
https://w3id.org/ascs-ev/envited-x/core/v1.0/
```

**Resolution Target (GitHub):**

```
https://raw.githubusercontent.com/YOUR-ORG/ontology-management-base/main/artifacts/envited-x/envited-x.owl.ttl
```

## Content Negotiation

### Supported Formats

The w3id.org service uses HTTP Accept headers to serve the appropriate format:

| Accept Header           | Format             | Extension |
| ----------------------- | ------------------ | --------- |
| `application/rdf+xml`   | RDF/XML            | `.rdf`    |
| `text/turtle`           | Turtle             | `.ttl`    |
| `application/n-triples` | N-Triples          | `.nt`     |
| `application/ld+json`   | JSON-LD            | `.jsonld` |
| `text/html`             | HTML Documentation | `.html`   |

### Client Examples

**Retrieve Turtle format:**

```bash
curl -L -H "Accept: text/turtle" \
  https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/
```

**Retrieve JSON-LD:**

```bash
curl -L -H "Accept: application/ld+json" \
  https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/
```

**Using Protégé or other RDF tools:**
These tools automatically send appropriate Accept headers. Simply paste the IRI and the tool will fetch the correct format.

### Version Resolution

When fetching from an IRI, the actual file served depends on content negotiation:

```
https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/
  → Accept: text/turtle
    → artifacts/scenario/scenario.owl.ttl (Turtle)
  → Accept: application/ld+json
    → artifacts/scenario/scenario.context.jsonld (JSON-LD context)
  → Accept: text/html
    → Documentation page
```

## W3ID Configuration

### .htaccess Pattern (for w3id.org repository)

The w3id.org service uses `.htaccess` files in its GitHub repository to configure IRI resolution. Here's the structure:

```
w3id.org/
├── README.md
├── index.html
├── gaia-x4plcaad/
│   └── ontologies/
│       ├── .htaccess
│       ├── scenario/
│       ├── service/
│       └── ... (more ontologies)
└── ascs-ev/
    ├── envited-x/
    │   ├── .htaccess
    │   └── ... (ontologies)
    └── README.md
```

### Example .htaccess Configuration

**File: w3id.org/gaia-x4plcaad/ontologies/.htaccess**

```apache
# Enable mod_rewrite
RewriteEngine On

# Disable directory listing
Options -Indexes

# Route ontology requests to GitHub artifacts
# Handles version-specific IRIs like /scenario/v2/

RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d

# Redirect with content negotiation
RewriteRule ^([a-z-]+)/v([0-9]+)/?$ \
  https://raw.githubusercontent.com/YOUR-ORG/ontology-management-base/main/artifacts/$1/$1.owl.ttl \
  [R=303,L,NE]

# Fallback for RDF/XML
RewriteRule ^([a-z-]+)/v([0-9]+)/?\.rdf$ \
  https://raw.githubusercontent.com/YOUR-ORG/ontology-management-base/main/artifacts/$1/$1.owl.rdf \
  [R=303,L,NE]
```

**File: w3id.org/ascs-ev/envited-x/.htaccess**

```apache
RewriteEngine On
Options -Indexes

RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d

# Version-specific routing
RewriteRule ^([a-z-]+)/v([0-9]+)(?:\.([0-9]+))?/?$ \
  https://raw.githubusercontent.com/YOUR-ORG/ontology-management-base/main/artifacts/$1/$1.owl.ttl \
  [R=303,L,NE]
```

## Publishing Workflow

### Adding a New Ontology

1. **Create artifact files** (in this repository):

   ```
   artifacts/{ontology}/
   ├── {ontology}.owl.ttl          # OWL ontology
   ├── {ontology}.shacl.ttl        # SHACL shapes (optional)
   ├── {ontology}.context.jsonld   # JSON-LD context (optional)
   └── PROPERTIES.md               # Auto-generated documentation
   ```

2. **Register with w3id.org**:
   - Fork the w3id.org GitHub repository
   - Create the appropriate folder structure
   - Add `.htaccess` file (if not exists)
   - Submit pull request to w3id.org

3. **Configure imports**:

   ```turtle
   @prefix ontology: <https://w3id.org/gaia-x4plcaad/ontologies/{ontology}/v2/> .
   # Ontology content here
   ```

4. **Update registry**:
   ```bash
   python3 -m src.tools.update_registry
   ```

### Updating an Ontology

**Minor changes (patch version):**

- Update `artifacts/{ontology}/{ontology}.owl.ttl`
- Keep existing version IRI (e.g., v2)
- No w3id.org changes needed

**Major changes (new version):**

1. Update `artifacts/{ontology}/{ontology}.owl.ttl`
2. Update `owl:versionIRI` in the ontology:
   ```turtle
   <https://w3id.org/{namespace}/{ontology}/v3/>
       rdf:type owl:Ontology ;
       owl:versionIRI <https://w3id.org/{namespace}/{ontology}/v3/> ;
       owl:versionInfo "3.0"@en ;
   ```
3. Update `.htaccess` in w3id.org to route new version
4. Submit PR to w3id.org repository

## Troubleshooting

### IRI Returns 404

**Problem:** `curl https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/` returns 404

**Solutions:**

1. Verify GitHub URL is correct (check artifacts/ folder)
2. Verify `.htaccess` rule matches the IRI pattern
3. Check w3id.org repository has been updated (may take 5-10 minutes)
4. Test direct GitHub URL:
   ```bash
   curl https://raw.githubusercontent.com/YOUR-ORG/ontology-management-base/main/artifacts/scenario/scenario.owl.ttl
   ```

### Wrong Format Returned

**Problem:** Requesting JSON-LD returns Turtle instead

**Solutions:**

1. Verify Accept header is set correctly:
   ```bash
   curl -i -H "Accept: application/ld+json" https://w3id.org/...
   ```
2. Ensure `.context.jsonld` file exists in artifacts directory
3. Check .htaccess handles JSON-LD extension properly
4. Clear browser cache (w3id.org caches responses)

### Import Fails in Protégé

**Problem:** Ontology won't load in Protégé with "Could not load ontology"

**Solutions:**

1. Verify URL is accessible:
   ```bash
   curl -H "Accept: application/rdf+xml" https://w3id.org/... > test.owl
   ```
2. Ensure ontology file is valid RDF
3. Try explicit format URL with extension:
   ```
   https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/.ttl
   ```

## Best Practices

### Import Versioning

Always use version-specific IRIs in your ontologies:

```turtle
# ✅ Good: Version pinned
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/general/v2/> .

# ❌ Avoid: Unversioned
owl:imports <https://w3id.org/gaia-x4plcaad/ontologies/general/> .
```

### URL Stability

Once published, never change the meaning of an IRI. If you need breaking changes:

- Create a new major version IRI
- Keep old version available for backward compatibility
- Document migration path for users

### Documentation Links

Include persistent links in documentation:

```markdown
- [Scenario Ontology](https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/)
- [Service Ontology](https://w3id.org/gaia-x4plcaad/ontologies/service/v2/)
```

## See Also

- [Ontology Domains](05-domains.md) - Understanding GAIA-X vs ENVITED-X namespaces
- [IRI Patterns](02-iri-patterns.md) - Internal IRI design patterns
- [OWL Import Best Practices](../10-reference/owl_imports_best_practices.md) - Strategies for managing ontology imports
- [W3ID Official Documentation](https://w3id.org/) - External w3id.org service documentation
