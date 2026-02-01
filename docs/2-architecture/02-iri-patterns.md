# IRI Patterns

This document describes the IRI (Internationalized Resource Identifier) patterns used in the ENVITED-X ontology ecosystem.

## Base IRI Structure

All ENVITED-X ontologies use w3id.org for stable, permanent IRIs:

```
https://w3id.org/ascs-ev/envited-x/{domain}/{version}
```

### Components

| Part | Description | Example |
|------|-------------|---------|
| `w3id.org` | W3C permanent identifier service | - |
| `ascs-ev` | Organization namespace | - |
| `envited-x` | Project namespace | - |
| `{domain}` | Ontology domain | `hdmap`, `scenario` |
| `{version}` | Semantic version | `v1`, `v2`, `v3` |

## Ontology IRIs

### Ontology Definition

```turtle
<https://w3id.org/ascs-ev/envited-x/hdmap/v5> a owl:Ontology ;
    owl:versionInfo "v5" ;
    rdfs:label "HD Map Ontology" .
```

### Class IRIs

Classes are defined within the ontology namespace:

```turtle
<https://w3id.org/ascs-ev/envited-x/hdmap/v5#HDMap> a owl:Class ;
    rdfs:label "HD Map" .
```

Pattern: `{ontology-iri}#{ClassName}`

### Property IRIs

Properties follow the same pattern:

```turtle
<https://w3id.org/ascs-ev/envited-x/hdmap/v5#hasContent> a owl:ObjectProperty ;
    rdfs:label "has content" .
```

## Instance IRIs

Instances use DID (Decentralized Identifier) format:

```
did:web:{domain}:{type}:{id}
```

### Examples

```json
{
  "@id": "did:web:envited-x.2050.2060:hdmap:12345",
  "@type": "hdmap:HDMap"
}
```

### Verifiable Credential DIDs

For credentials:
```
did:web:participant.2050.2060:credential:abc123
```

## Version Resolution

The w3id.org redirects support content negotiation and version resolution:

### Latest Version

```bash
curl -H "Accept: text/turtle" https://w3id.org/ascs-ev/envited-x/hdmap/latest
# Redirects to: .../v5/hdmap_ontology.ttl
```

### Specific Version

```bash
curl -H "Accept: text/turtle" https://w3id.org/ascs-ev/envited-x/hdmap/v3
# Redirects to: .../v3/hdmap_ontology.ttl
```

### Content Types

| Accept Header | Response |
|---------------|----------|
| `text/turtle` | Turtle format ontology |
| `application/ld+json` | JSON-LD format ontology |
| `text/html` | Documentation page |

## JSON-LD Context Usage

### Full IRI in Context

```json
{
  "@context": {
    "hdmap": "https://w3id.org/ascs-ev/envited-x/hdmap/v5#"
  }
}
```

### Using Prefix

```json
{
  "@type": "hdmap:HDMap",
  "hdmap:name": "My Map"
}
```

## Best Practices

### 1. Use Versioned IRIs

Always include version in production:

```turtle
# Good
<https://w3id.org/ascs-ev/envited-x/hdmap/v5#HDMap>

# Avoid (no version stability)
<https://w3id.org/ascs-ev/envited-x/hdmap#HDMap>
```

### 2. Use Hash URIs for Terms

Classes and properties use `#`:

```turtle
# Good - hash URI
<https://w3id.org/.../hdmap/v5#HDMap>

# Avoid - slash URI for vocabulary terms
<https://w3id.org/.../hdmap/v5/HDMap>
```

### 3. Use DIDs for Instances

Instance identifiers should be DIDs:

```json
{
  "@id": "did:web:example.com:hdmap:001",
  "@type": "hdmap:HDMap"
}
```

### 4. Consistent Prefix Naming

Use lowercase, hyphenated prefixes matching domain names:

| Domain | Prefix |
|--------|--------|
| `hdmap` | `hdmap:` |
| `environment-model` | `environment-model:` |
| `envited-x` | `envited-x:` |
