# imports/schema — Local Modification

This folder contains a local copy of the schema.org OWL ontology (`schema.owl.ttl`).

## Modification: `schema:name rdfs:subPropertyOf rdfs:label`

The upstream schema.org ontology declares:

```turtle
schema:name rdfs:subPropertyOf rdfs:label .
```

This triple has been **commented out** in our local copy. The reason is an
interaction between RDFS inference and Gaia-X 25.11 closed SHACL shapes.

### The problem

1. GX 25.11 shapes like `gx:SoftwareResourceShape` and `gx:ServiceOfferingShape`
   use `sh:closed true`, which rejects any property not explicitly listed.
2. These shapes explicitly allow `schema:name` via `sh:path schema:name`.
3. However, `sh:ignoredProperties` does **not** include `rdfs:label`.
4. pySHACL applies RDFS inference before validation. The `rdfs:subPropertyOf`
   declaration causes the reasoner to infer an `rdfs:label` triple for every
   node that has `schema:name`.
5. The inferred `rdfs:label` is not in the closed shape's allowlist, so
   validation fails.

### Why this is not a pySHACL bug

pySHACL correctly implements the SHACL specification. The `sh:closed`
constraint requires that every property on a focus node is either listed in
`sh:property` paths or in `sh:ignoredProperties`. Since `rdfs:label` appears
in neither, the violation is correctly reported.

### Why this is a GX design oversight

- GX OWL (`gx.owl.ttl`) itself does **not** declare
  `schema:name rdfs:subPropertyOf rdfs:label` — this relationship comes
  solely from the upstream schema.org ontology.
- GX imports schema.org but does not account for the RDFS entailment in its
  closed shapes.
- The fix on the GX side would be to add `rdfs:label` to
  `sh:ignoredProperties` on all closed shapes that allow `schema:name`.

### Restoring the original

If GX updates their shapes to handle `rdfs:label` (e.g. by adding it to
`sh:ignoredProperties`), this comment-out can be reverted by restoring:

```turtle
rdfs:subPropertyOf rdfs:label ;
```

on the `schema:name` definition (around line 15465).
