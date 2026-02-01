# Documentation Restructuring - Executive Summary

## Overview

A comprehensive documentation restructuring proposal has been prepared to address:

1. **Domain clarity**: Distinguish GAIA-X 4 PLC-AAD (2021-2024 project) from ENVITED-X (post-2024 development)
2. **Audience segmentation**: Separate sections for theorists, developers, contributors, and operators
3. **Missing topics**: Service Characteristics integration, LinkML migration, deeper validation tool guide
4. **Navigation**: Create a logical flow from foundations → architecture → implementation → advanced

## Key Findings

### Current Documentation Status

✅ **What's Covered**:

- IRI patterns and w3id resolution
- OWL imports best practices
- Individual validation tools
- Repository structure
- Historical migration docs

❌ **What's Missing**:

- Clear explanation of two separate IRI namespaces/domains
- Foundational concepts (RDF/OWL/SHACL for newcomers)
- Service Characteristics integration details
- LinkML roadmap with concrete examples
- Comprehensive contribution guide
- Consolidated validation tool overview

### Domain Situation

The repository contains ontologies in **two separate IRI namespaces**:

| Aspect            | GAIA-X 4 PLC-AAD                                                                                                                                                                                         | ENVITED-X                             |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **IRI Namespace** | `https://w3id.org/gaia-x4plcaad/ontologies/`                                                                                                                                                             | `https://w3id.org/ascs-ev/envited-x/` |
| **Timeline**      | 2021-2024 (Project runtime)                                                                                                                                                                              | 2024+ (Post-project)                  |
| **Ontologies**    | automotive-simulator, environment-model, general, georeference, hdmap, leakage-test, manifest, ositrace, scenario, service, simulated-sensor, simulation-model, surface-model, survey, tzip21, vv-report | envited-x, gx, example, description   |
| **Governance**    | Project-era outputs                                                                                                                                                                                      | Active ENVITED-X Data Space           |
| **Use Case**      | R&D within project                                                                                                                                                                                       | Production systems                    |

**Documentation Finding**: Currently only the ENVITED-X namespace is mentioned in docs; GAIA-X domain not clearly explained.

### Previous README.md Files

**Investigation Result**: No per-ontology README.md files exist in current artifact folders. Git history shows no remnants of such files. All documentation is appropriately centralized in `/docs`.

## Proposed Structure

### 10-Section Documentation Framework

```
1. Foundations (NEW)
   └─ RDF/OWL/SHACL basics, Linked Data principles, versioning strategy

2. Architecture (REVISED)
   ├─ New: "The Two Domains" explanation
   ├─ New: "W3ID Publishing" technical details
   └─ Existing: Discovery, imports, IRI patterns

3. Ontology Domains (NEW)
   ├─ GAIA-X 4 PLC-AAD (project-era ontologies)
   └─ ENVITED-X (post-project ontologies)

4. Getting Started (SIMPLIFIED)
   ├─ Quick Start (5 min)
   └─ Installation & First Validation

5. Building & Contributing (NEW)
   ├─ How to add ontologies
   ├─ Testing workflow
   ├─ Build process
   └─ Release process

6. Validation Tools (CONSOLIDATED)
   ├─ Overview & comparison matrix
   ├─ Tool-specific guides
   └─ Troubleshooting

7. Service Characteristics (NEW)
   ├─ What is it?
   ├─ How we use it
   └─ Mapping guide

8. LinkML Future (EXPANDED)
   ├─ Vision & rationale
   ├─ Migration plan (Phase 1-4)
   └─ Examples

9. Advanced Topics (NEW)
   ├─ IRI resolution mechanisms
   ├─ Content negotiation
   └─ Performance tuning

10. Reference (PRESERVED)
    └─ Historical migration docs
```

## Key Documents to Create

**High Priority** (establish domain clarity):

- `architecture/domains.md` - Explains GAIA-X 4 PLC-AAD vs ENVITED-X
- `architecture/w3id-publishing.md` - Technical details of w3id.org setup
- `ontology-domains/gaia-x4plcaad/index.md` - Project ontologies overview
- `ontology-domains/envited-x/index.md` - Post-project ontologies overview

**Medium Priority** (improve contributor experience):

- `building-contributing/adding-ontologies.md` - Step-by-step guide
- `building-contributing/testing-workflow.md` - Test structure
- `validation-tools/troubleshooting.md` - Common issues & fixes
- `service-characteristics/index.md` - SC integration overview

**Lower Priority** (future planning):

- `foundations/` section (educational)
- `linkml-future/` section (roadmap)
- `advanced/` section (deep dives)

## Benefits

1. **Clarity**: Two-domain architecture explicitly explained
2. **Navigation**: Numbered sections with audience targeting
3. **Completeness**: No major topics left undocumented
4. **Modularity**: Sections can be updated independently
5. **Preservation**: Historical docs kept but not in critical path
6. **Discoverability**: Better search/browsing with clearer hierarchy

## Next Steps

### Phase 1: Immediate (This Week)

- [ ] Review and approve proposal
- [ ] Create folder structure
- [ ] Update mkdocs.yml navigation

### Phase 2: Foundation (Week 2)

- [ ] Write domain clarification docs (HIGH PRIORITY)
- [ ] Create ontology domain pages
- [ ] Update main index

### Phase 3: Contribution (Week 3)

- [ ] Write contributor guides
- [ ] Consolidate validation tools
- [ ] Add troubleshooting

### Phase 4: Advanced (Week 4)

- [ ] Service Characteristics section
- [ ] LinkML expanded guide
- [ ] Advanced topics

### Phase 5: Polish (Week 5)

- [ ] Cross-reference links
- [ ] Add diagrams
- [ ] Peer review & test

## Files Affected

- New: 30+ markdown files (organized by section)
- Updated: `mkdocs.yml` (new navigation structure)
- Updated: `index.md` (landing page)
- Moved: `CONTRIBUTING.md` (into section 5)
- Preserved: Historical docs (moved to reference section)

## Questions for Discussion

1. Should we add per-ontology pages in docs for commonly-used domains?
2. Is the LinkML timeline (Phase 1-4 over 6 months) realistic?
3. Should service-characteristics have deeper mapping examples?
4. Any other audience segments we're missing?

---

**Full proposal**: See [DOCUMENTATION_STRUCTURE_PROPOSAL.md](DOCUMENTATION_STRUCTURE_PROPOSAL.md)

**Status**: Ready for implementation
