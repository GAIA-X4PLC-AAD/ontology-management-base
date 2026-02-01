# **Architectural Standards for Ontology and SHACL Shape Discovery: A Comprehensive Best Practice Report**

## **1\. Introduction: The Semantic Validation Gap**

The evolution of the Semantic Web has been characterized by a fundamental architectural tension between description and validation. For nearly two decades, the Web Ontology Language (OWL) served as the primary mechanism for modeling domain knowledge. Underpinned by the Open World Assumption (OWA), OWL was designed to facilitate data integration and inferencing—allowing systems to deduce new facts from existing information. In this paradigm, a constraint such as "a Person has exactly one name" is not a rule to reject data lacking a name, but rather a logical axiom used to infer that if two names are found, they must refer to the same entity. While powerful for knowledge discovery, this behavior proved insufficient for enterprise data quality assurance, which requires strict, closed-world validation to ensure data conforms to expected schemas before processing.1

The introduction of the Shapes Constraint Language (SHACL) as a W3C Recommendation in 2017 addressed this gap by providing a mechanism to validate RDF graphs against a set of conditions.2 However, this introduced a new architectural challenge: the decoupling of the semantic definition (the Ontology) from the validation logic (the Shapes). Unlike traditional relational database schemas, where the structure and constraints are unified, the Semantic Web now often requires two distinct artifacts to describe the same domain: an OWL file defining the vocabulary and a SHACL file defining the constraints.

This separation necessitates robust mechanisms for **referencing** and **auto-discovery**. A critical operational requirement for modern Knowledge Graph (KG) infrastructure is the ability for a system, upon encountering a dataset or an ontology, to automatically locate and apply the correct validation shapes without manual intervention. This report investigates the best practices for establishing these links through IRI naming conventions, OWL features, and registry-based discovery mechanisms. It provides a critical analysis of industry standards, examining how tools like TopBraid, Apache Jena, and LinkML interpret these links, and recommends a tiered architecture for implementation.

## **2\. Theoretical Foundations of Artifact Linkage**

To determine the optimal linking strategy, one must first understand the theoretical relationship between the artifacts being linked. The choice of mechanism—whether owl:imports, sh:shapesGraph, or metadata associations—is not merely a syntactic preference but a reflection of the intended semantic relationship between the domain model and its validation rules.

### **2.1 The Open World vs. Closed World Dichotomy**

The necessity for separate files stems from the conflicting logical assumptions of OWL and SHACL. OWL ontologies operate under the Open World Assumption (OWA), where the absence of a statement does not imply its falsehood. Conversely, data validation inherently requires a Closed World Assumption (CWA), where the system validates only what is currently known.2

If validation shapes are embedded directly within the OWL ontology file, the semantic clarity of the domain model becomes compromised. A file containing both owl:Restriction (for inference) and sh:PropertyShape (for validation) conflates two distinct phases of the data lifecycle. Furthermore, embedding shapes limits reuse; a single ontology might require different validation strictures for different contexts (e.g., "loose" validation for data ingestion vs. "strict" validation for publication).6 Therefore, the architectural best practice is to maintain shapes as separate RDF graphs that _reference_ the ontology, rather than residing within it. This separation of concerns mandates a reliable discovery mechanism to bridge the gap.

### **2.2 The Shadow Graph Concept**

In this decoupled architecture, the SHACL shapes graph effectively acts as a "shadow" or "profile" of the ontology. For every class ex:Person in the ontology, there is typically a corresponding ex:PersonShape in the shapes graph.8 The discovery mechanism must therefore support the traversal from the concept (ex:Person) or the ontology IRI (<http://example.org/ns/core>) to its corresponding shape definition (<http://example.org/ns/core/shapes>).

## **3\. Mechanisms for Linkage and Discovery**

The investigation into current standards and tool behaviors identifies three primary mechanisms for linking ontologies to shapes: the owl:imports pattern, the sh:shapesGraph predicate, and registry-based metadata.

### **3.1 The owl:imports Mechanism**

The most prevalent and robust mechanism for linking a shapes graph to its underlying ontology is the use of the owl:imports predicate within the shapes file itself. This pattern effectively treats the shapes graph as an extension of the domain ontology.

#### **3.1.1 Architectural Pattern**

In this pattern, the SHACL file is declared as an owl:Ontology and explicitly imports the domain ontology using the owl:imports property.

**Table 1: The owl:imports Linkage Pattern**

| Component     | Description                    | Example                                 |
| :------------ | :----------------------------- | :-------------------------------------- |
| **Subject**   | The IRI of the Shapes Graph    | \<<http://example.org/ns/my-shapes\>>   |
| **Predicate** | The OWL import property        | owl:imports                             |
| **Object**    | The IRI of the Domain Ontology | \<<http://example.org/ns/my-ontology\>> |

This mechanism instructs any standard RDF/OWL processor that loading the shapes graph requires strictly loading the domain ontology as well.8

#### **3.1.2 Operational Implications**

When a validation engine processes a shapes graph with an owl:imports statement, it performs an import closure. This is critical for SHACL validation because shapes often target classes defined in the ontology (using sh:targetClass). Without the ontology present in the graph, the validator would not have access to the rdfs:subClassOf hierarchy. Since SHACL validators utilize the class hierarchy to apply shapes to subclasses, the absence of the ontology can lead to false positives where data instances are not validated because their class membership is not inferred.5

For example, if sh:targetClass ex:Party is defined, and the data contains instances of ex:Person (a subclass of ex:Party), the validator needs the triple ex:Person rdfs:subClassOf ex:Party to know that the shape applies. The owl:imports statement ensures this triple is available.12

#### **3.1.3 Industry Adoption and Tool Support**

This pattern is the _de facto_ standard for major semantic web tools:

- **Apache Jena:** The Jena SHACL implementation provides specific methods like Imports.loadWithImports(url) which automatically process the owl:imports statements to construct a unified validation graph.13 This confirms that in the Java ecosystem, this mechanism is expected and supported.
- **TopBraid Composer/EDG:** TopQuadrant’s tools, which pioneered SHACL, rely heavily on owl:imports. They recommend creating a shapes file that imports the ontology, allowing the user to view shapes and classes in a unified interface. When validation is executed, the tool operates on the union of the shapes graph and its imports.15
- **Protégé:** As an OWL-centric editor, Protégé natively handles imports. When a SHACL file is opened, it loads the imported ontology, allowing the user to define shapes using the vocabulary defined in the referenced file.17

### **3.2 The sh:shapesGraph Mechanism**

While owl:imports links the _shapes_ to the _ontology_ (upstream), the sh:shapesGraph property is designed to link the _data_ to the _shapes_ (downstream). Defined in the SHACL specification, this predicate allows a dataset to self-declare the validation logic it adheres to.8

#### **3.2.1 Architectural Pattern**

This property is typically found in a manifest file or the dataset metadata itself.

**Table 2: The sh:shapesGraph Linkage Pattern**

| Component     | Description                     | Example                                   |
| :------------ | :------------------------------ | :---------------------------------------- |
| **Subject**   | The IRI of the Dataset or Graph | \<<http://example.org/data/dataset-001\>> |
| **Predicate** | The SHACL shapes graph property | sh:shapesGraph                            |
| **Object**    | The IRI of the Shapes Graph     | \<<http://example.org/ns/my-shapes\>>     |

#### **3.2.2 Limitations and Usage**

Critically, sh:shapesGraph acts as a _hint_ rather than a directive. The SHACL specification notes that tools "may" use this property to locate shapes, but it does not mandate automatic retrieval or validation.7 In practice, many command-line validators and triple stores do not automatically follow sh:shapesGraph unless explicitly configured to do so. It is most effective when used in "SHACL-DS" (SHACL Datasets) or controlled data exchange environments like BIM (Building Information Modeling) information containers, where a manifest explicitly maps data files to shape files.11

Unlike owl:imports, sh:shapesGraph is not transitive. Referencing a shapes graph via this property does not imply that the referenced graph's imports will be processed, although a compliant SHACL processor _should_ follow owl:imports once it has located the shapes graph.10

### **3.3 Registry-Based Discovery (DCAT and VoID)**

For large-scale enterprise or open-data ecosystems, embedding links directly in files is often insufficient due to versioning complexities. The emerging best practice in these contexts is the use of **Repository Registries** compliant with DCAT (Data Catalog Vocabulary) or VoID (Vocabulary of Interlinked Datasets).21

#### **3.3.1 The Registry Pattern**

In this architecture, a central registry (e.g., FAIRsharing, generic SPARQL endpoints, or internal metadata catalogs) maintains records of both ontologies and shape files. The linkage is established through metadata properties such as dcterms:conformsTo or specific profile relations.

##### Table 3: Registry Metadata Properties for Linkage

| Property           | Usage                                                                         | Context                    |
| :----------------- | :---------------------------------------------------------------------------- | :------------------------- |
| dcterms:conformsTo | Links a dataset to the SHACL shapes it validates against.                     | DCAT / General Metadata 22 |
| rdfs:isDefinedBy   | Links a Shape to the Ontology it constrains.                                  | SHACL / RDFS 20            |
| prof:isProfileOf   | (Profiles Ontology) Declares the Shapes graph as a "profile" of the Ontology. | Advanced Configuration     |

#### **3.3.2 Auto-Discovery in Repositories**

Tools like GraphDB utilize a "reserved graph" mechanism for discovery. Rather than chasing HTTP links, they expect SHACL shapes to be loaded into a specific named graph (e.g., <http://rdf4j.org/schema/rdf4j\#SHACLShapeGraph).23> In this context, "auto-discovery" is achieved by convention: the validator always looks in the reserved graph. The "link" is established by the repository administrator who ensures the correct shapes are loaded into that graph. This approach is highly efficient for performance but less flexible for decentralized web discovery.

## **4\. IRI Naming Strategies for Auto-Discovery**

In the absence of explicit metadata registries, the most reliable mechanism for auto-discovery is **Convention over Configuration** via strict IRI naming patterns. This allows agents to algorithmically predict the location of a shapes file given an ontology IRI.

### **4.1 The Suffix Pattern**

The most widely cited and robust pattern is the **Suffix Pattern**, where the shapes graph IRI is derived by appending a standard suffix to the ontology IRI.

**Pattern:** \`\` \+ /shapes (or dash:shapes, etc.)

**Examples:**

- **Ontology IRI:** <http://example.org/ns/finance>
- **Shapes IRI:** <http://example.org/ns/finance/shapes>

This pattern is intuitively traversable. If an agent dereferences the ontology IRI, the server can use HTTP Link headers or HTML \<link\> tags to point to the /shapes resource. Furthermore, tools like TopBraid encourage file naming conventions such as filename.shapes.ttl, which often maps to these IRIs in a project workspace.15

### **4.2 The "Shape" Node Naming Convention**

Within the shapes graph itself, naming conventions for the shape nodes (the subjects of the triples) are equally critical for maintenance and linking.

- **Best Practice:** Name the NodeShape by appending Shape to the Class name it targets.
  - Class: ex:Person
  - Shape: ex:PersonShape
- **Avoid Blank Nodes:** While SHACL allows blank nodes (e.g., ex:Person sh:property \[... \]), this is considered a poor practice for reusable ontologies. Blank nodes cannot be easily referenced, extended, or deactivated by downstream users. Assigning an IRI (e.g., ex:Person-nameShape for a property shape) enables fine-grained control and linking.8

### **4.3 Versioning and IRI Stability**

When using owl:imports to link shapes to ontologies, version drift becomes a risk. If shapes/v1 imports ontology/v1, but the ontology is updated to v2, the validation may break.

- **Recommendation:** Use versioned IRIs for the import statement (e.g., owl:imports \<<http://example.org/ns/finance/1.0.0\>>) to ensure the shapes are validated against the exact schema version they were designed for.
- **Registry Coordination:** In a registry context, the metadata record should explicitly pair versions (e.g., "Shapes v1.2 applies to Ontology v2.0").21

## **5\. Integrating OWL Features for Robust Linkage**

Beyond the simple owl:imports statement, sophisticated auto-discovery utilizes specific OWL and RDFS features to enrich the machine-readability of the link.

### **5.1 The sh:entailment Property**

A critical oversight in many implementations is the failure to declare the _entailment regime_. SHACL validation is performed on a data graph, but that data graph often requires inferencing to be valid (e.g., rdfs:subClassOf inference).

- **Feature:** The property sh:entailment should be included in the Shapes Graph metadata.
- **Usage:** \<<http://example.org/ns/shapes\>> sh:entailment \<<http://www.w3.org/ns/entailment/RDFS\>>.
- **Effect:** This informs the discovery agent (and the validator) that before validating, it must activate an RDFS reasoner. Without this, a validator discovering the shapes might apply them to raw data and report false violations due to missing inferred triples.10

### **5.2 rdfs:isDefinedBy and rdfs:seeAlso**

To support bi-directional navigation, the definition of the Shape should link back to the ontology class it constrains.

- **Pattern:** ex:PersonShape rdfs:isDefinedBy \<<http://example.org/ns/ontology\>>.
- **Benefit:** This provides a provenance trail. A user encountering a standalone shape file can verify which ontology it is intended to validate. It serves as a documentation link that is machine-readable.11

### **5.3 owl:Ontology Metadata**

The Shapes file itself should be typed as an owl:Ontology to support the owl:imports mechanism.

- **Statement:** \<<http://example.org/ns/shapes\>> a owl:Ontology ; owl:imports \<<http://example.org/ns/ontology\>>.
- **Critique:** Some purists argue SHACL files are not "Ontologies" in the strict OWL sense. However, practically, typing them as owl:Ontology is necessary for them to be recognized by the import management systems of Protégé, TopBraid, and Jena.12 It is a pragmatic overload of the class to facilitate tool interoperability.

## **6\. Model-Driven Architecture: The LinkML Paradigm**

The manual maintenance of separate OWL and SHACL files, and the "glue" links between them, is error-prone. A significant trend identified in the research is the shift toward **Model-Driven Architecture (MDA)**, specifically using **LinkML** (Linked Data Modeling Language).25 LinkML fundamentally alters the "referencing" discussion by generating both artifacts from a single source of truth.

### **6.1 Unified Source, Generated Artifacts**

In the LinkML workflow, the domain expert defines the schema in a YAML file. This schema contains both the structural definitions (classes, slots) and the constraints (cardinality, patterns, rules).

- **Generation:** The gen-project command is used to compile this YAML into multiple formats simultaneously: gen-owl creates the ontology, and gen-shacl creates the shapes.30
- **Auto-Linking:** Crucially, the LinkML generator can automatically inject the owl:imports statement into the generated SHACL file. The flag \--include-imports or \--mergeimports controls whether the output is a standalone file or a modular one dependent on the ontology.25

### **6.2 The gen-project Directory Structure**

LinkML standardizes discovery through a rigid directory structure created by gen-project.

- /project/owl/ \- Contains the ontology (.owl.ttl)
- /project/shacl/ \- Contains the shapes (.shacl.ttl)
- /project/json-schema/ \- Contains JSON schemas.

**Impact on Best Practice:** This eliminates the need for ad-hoc naming conventions. The discovery mechanism becomes implicit: if you have the LinkML project root, the ontology is always in /owl and the shapes are always in /shacl. This standardization is superior to manual naming conventions because it is enforced by the build tool.31

## **7\. Tool-Specific Behaviors and Implications**

A robust referencing strategy must account for the idiosyncrasies of the major tools in the Semantic Web ecosystem. "Best practice" is often defined by what works in these specific environments.

### **7.1 TopBraid EDG and Composer**

TopQuadrant's tools are strict regarding the separation of assets.

- **File Extension:** They strongly favor the .shapes.ttl extension to identify files containing constraints.
- **Import Handling:** They assume that if a file defines shapes for a class, it _must_ import the file defining that class. If the import is missing, the tool may not visualize the shapes in the context of the class hierarchy.
- **Recommendation:** When targeting TopBraid, always use owl:imports and adhere to the .shapes. naming convention.15

### **7.2 Apache Jena (Java)**

Jena’s architecture treats SHACL validation as a process applied to a Graph.

- **Import Handling:** The Imports class provides static methods to load a graph and its imports recursively. This confirms that the owl:imports pattern is the native way to assemble a validation graph in Jena.
- **Discovery:** Jena does not have a built-in "auto-discovery" agent that crawls the web; it relies on the developer to provide the URL of the shapes graph. Thus, having the shapes graph capable of self-assembling its dependencies via imports is crucial for developer ergonomics.13

### **7.3 RDF4J and GraphDB**

As noted in Section 3.3, RDF4J-based systems differ significantly.

- **Reserved Graphs:** They utilize the <http://rdf4j.org/schema/rdf4j\#SHACLShapeGraph> context.
- **Implication:** Merely having an owl:imports link in a file on the web is not enough. The deployment pipeline must explicitly _push_ the shapes into this reserved graph.
- **Discovery:** Discovery is internal. The database knows where the shapes are because they are in the reserved location. The "link" is the database configuration itself.23

## **8\. Critical Analysis of Common Approaches**

In response to the user's request to look critically at common "answers" (represented by the input patterns), we must deconstruct several prevalent but flawed approaches to linking.

### **8.1 Critique: "Embed the Shapes in the Ontology"**

A common naive approach is to simply add sh:property constraints to the owl:Class definitions in the same file.

- **Why it fails:** This violates the separation of OWA and CWA. It makes the ontology heavy and inflexible. If a user wants to reuse the term ex:Person but has different validation rules (e.g., in a historical dataset where birth dates are optional), they cannot do so without modifying the ontology itself.6
- **Corrective Action:** Always separate concerns. Use owl:imports to bring the ontology _into_ the shapes file, never the other way around.

### **8.2 Critique: "Use sh:shapesGraph in the Data"**

Advising users to rely solely on adding sh:shapesGraph to their data files is insufficient.

- **Why it fails:** As established, many validators ignore this property. It also requires modifying the _data_ to point to the _schema_, which is often impossible if the data is read-only or third-party.
- **Corrective Action:** Use sh:shapesGraph only as a supplemental hint or in dataset manifests (DCAT). Do not rely on it for the primary validation logic flow.18

### **8.3 Critique: "OWL Restrictions are Validation"**

Some practitioners assume that owl:minCardinality is equivalent to sh:minCount.

- **Why it fails:** This is a fundamental misunderstanding of OWA. An OWL cardinality restriction will not flag missing data as an error; it will simply infer that the data _exists_ somewhere (or waits for more data). SHACL is required for actual validation.1

## **9\. Conclusion and Recommendations**

The best practice for referencing and auto-discovering ontology and shape files is to adopt a **Layered Modular Architecture**. This approach prioritizes the decoupling of semantics from validation while using standard linking mechanisms to ensure they can be re-assembled by machines.

**Strategic Recommendations:**

1. **Adopt the "Shapes Import Ontology" Pattern:**
   - Create two distinct artifacts: the Ontology (pure OWL/RDFS) and the Shapes Graph (SHACL).
   - The Shapes Graph must explicitly contain \<shapes-iri\> owl:imports \<ontology-iri\>. This allows validators to access the class hierarchy for target resolution.
2. **Standardize IRIs for Heuristic Discovery:**
   - Use a predictable suffix pattern, ideally /shapes, for the Shapes Graph IRI.
   - Example: <http://example.org/ns/core> (Ontology) -> <http://example.org/ns/core/shapes> (Shapes).
3. **Leverage Registry Metadata:**
   - For enterprise discovery, register both artifacts in a DCAT-compliant catalog.
   - Use dcterms:conformsTo in dataset metadata to point to the specific Shapes Graph.
4. **Transition to Model-Driven Engineering:**
   - For new projects, use **LinkML** to define the model once and auto-generate both OWL and SHACL. This automates the referencing (via gen-project) and ensures the links are always syntactically correct and version-aligned.
5. **Tool-Specific Configuration:**
   - When deploying to **GraphDB/RDF4J**, implement a pipeline step that loads the Shapes Graph into the reserved SHACLShapeGraph.
   - When targeting **TopBraid**, ensure file naming conventions (.shapes.ttl) are respected to enable UI features.

By implementing these standards, organizations can move from brittle, manual file management to a robust, auto-discoverable Semantic Web infrastructure where data, meaning, and validation are seamlessly linked yet logically distinct.

### **Works cited**

1. SHACL-ing the Data Quality Dragon I: the Problem and the Tools | Ontotext, accessed on January 23, 2026, [https://www.ontotext.com/blog/shacl-ing-the-data-quality-dragon-i-the-problem-and-the-tools/](https://www.ontotext.com/blog/shacl-ing-the-data-quality-dragon-i-the-problem-and-the-tools/)
2. SHACL and OWL Compared \- SPIN, accessed on January 23, 2026, [https://spinrdf.org/shacl-and-owl.html](https://spinrdf.org/shacl-and-owl.html)
3. Converting RDFS schemas to SHACL constraints \- Bob DuCharme, accessed on January 23, 2026, [https://www.bobdc.com/blog/rdfs2shacl/](https://www.bobdc.com/blog/rdfs2shacl/)
4. SHACL \- Wikipedia, accessed on January 23, 2026, [https://en.wikipedia.org/wiki/SHACL](https://en.wikipedia.org/wiki/SHACL)
5. What Is SHACL | Ontotext Fundamentals, accessed on January 23, 2026, [https://www.ontotext.com/knowledgehub/fundamentals/what-is-shacl/](https://www.ontotext.com/knowledgehub/fundamentals/what-is-shacl/)
6. Why I Use SHACL For Defining Ontology Models | TopQuadrant, accessed on January 23, 2026, [https://www.topquadrant.com/resources/why-i-use-shacl-for-defining-ontology-models/](https://www.topquadrant.com/resources/why-i-use-shacl-for-defining-ontology-models/)
7. A SHACL extension to validate RDF dataset \- arXiv, accessed on January 23, 2026, [https://www.arxiv.org/pdf/2505.09198](https://www.arxiv.org/pdf/2505.09198)
8. Shapes Constraint Language (SHACL) \- W3C, accessed on January 23, 2026, [https://www.w3.org/TR/shacl/](https://www.w3.org/TR/shacl/)
9. Ontology Matching trough alignment and extension: a Best Practice \- CROW, accessed on January 23, 2026, [https://docs.crow.nl/ontology-alignment/whitepaper/](https://docs.crow.nl/ontology-alignment/whitepaper/)
10. SHACL 1.2 Core \- W3C on GitHub, accessed on January 23, 2026, [https://w3c.github.io/shacl/shacl-core/index.html](https://w3c.github.io/shacl/shacl-core/index.html)
11. Semantic validation of information containers for reliable BIM information exchange \- ResearchGate, accessed on January 23, 2026, [https://www.researchgate.net/profile/Philipp-Hagedorn/publication/377963638_Semantic_validation_of_information_containers_for_reliable_BIM_information_exchange/links/65bf9a6934bbff5ba7ec8d6b/Semantic-validation-of-information-containers-for-reliable-BIM-information-exchange.pdf](https://www.researchgate.net/profile/Philipp-Hagedorn/publication/377963638_Semantic_validation_of_information_containers_for_reliable_BIM_information_exchange/links/65bf9a6934bbff5ba7ec8d6b/Semantic-validation-of-information-containers-for-reliable-BIM-information-exchange.pdf)
12. A SHACL OWL "profile" to aid ontologies mixing SHACL and OWL · Issue \#246 · w3c/data-shapes \- GitHub, accessed on January 23, 2026, [https://github.com/w3c/data-shapes/issues/246](https://github.com/w3c/data-shapes/issues/246)
13. Index (Apache Jena SHACL), accessed on January 23, 2026, [https://jena.apache.org/documentation/javadoc/shacl/index-all.html](https://jena.apache.org/documentation/javadoc/shacl/index-all.html)
14. Imports (Apache Jena SHACL), accessed on January 23, 2026, [https://jena.apache.org/documentation/javadoc/shacl/org.apache.jena.shacl/org/apache/jena/shacl/Imports.html](https://jena.apache.org/documentation/javadoc/shacl/org.apache.jena.shacl/org/apache/jena/shacl/Imports.html)
15. SHACL Support, accessed on January 23, 2026, [https://topbraidcomposer.org/html/SHACL.htm](https://topbraidcomposer.org/html/SHACL.htm)
16. Where have all my labels gone? Topbraid owl to SHACL conversion \- Stack Overflow, accessed on January 23, 2026, [https://stackoverflow.com/questions/66136806/where-have-all-my-labels-gone-topbraid-owl-to-shacl-conversion](https://stackoverflow.com/questions/66136806/where-have-all-my-labels-gone-topbraid-owl-to-shacl-conversion)
17. Using ontologies | IDS Best Practices \- MaastrichtU-IDS, accessed on January 23, 2026, [https://maastrichtu-ids.github.io/best-practices/docs/using-ontologies/](https://maastrichtu-ids.github.io/best-practices/docs/using-ontologies/)
18. How should sh:shapesGraph be interpreted in comparison to owl:import? \- Stack Overflow, accessed on January 23, 2026, [https://stackoverflow.com/questions/73867790/how-should-shshapesgraph-be-interpreted-in-comparison-to-owlimport](https://stackoverflow.com/questions/73867790/how-should-shshapesgraph-be-interpreted-in-comparison-to-owlimport)
19. UML-to-GML Application Schema Pilot (UGAS-2020) Engineering Report, accessed on January 23, 2026, [https://docs.ogc.org/per/20-012.html](https://docs.ogc.org/per/20-012.html)
20. Semantic validation of information containers for reliable BIM information exchange, accessed on January 23, 2026, [https://www.researchgate.net/publication/377963638_Semantic_validation_of_information_containers_for_reliable_BIM_information_exchange](https://www.researchgate.net/publication/377963638_Semantic_validation_of_information_containers_for_reliable_BIM_information_exchange)
21. Vocabulary building best practices · Solid, accessed on January 23, 2026, [https://solidproject.solidcommunity.net/SPS/developers/vocabularies/create/best-practices.html](https://solidproject.solidcommunity.net/SPS/developers/vocabularies/create/best-practices.html)
22. Testbed-12 Semantic Portrayal, Registry and Mediation Engineering Report, accessed on January 23, 2026, [https://docs.ogc.org/per/16-059.pdf](https://docs.ogc.org/per/16-059.pdf)
23. SHACL validation — GraphDB 11.2 documentation, accessed on January 23, 2026, [https://graphdb.ontotext.com/documentation/11.2/shacl-validation.html](https://graphdb.ontotext.com/documentation/11.2/shacl-validation.html)
24. SHACL | Henriette Harmse, accessed on January 23, 2026, [https://henrietteharmse.com/category/inferencing/rules/shacl/](https://henrietteharmse.com/category/inferencing/rules/shacl/)
25. SHACL \- linkml documentation, accessed on January 23, 2026, [https://linkml.io/linkml/generators/shacl.html](https://linkml.io/linkml/generators/shacl.html)
26. Best Practices for Implementing FAIR Vocabularies and Ontologies on the Web \- Daniel Garijo, accessed on January 23, 2026, [https://dgarijo.com/papers/best_practices2020.pdf](https://dgarijo.com/papers/best_practices2020.pdf)
27. Shapes Constraint Language (SHACL) \- W3C, accessed on January 23, 2026, [https://www.w3.org/TR/2016/WD-shacl-20160814/](https://www.w3.org/TR/2016/WD-shacl-20160814/)
28. ISSUE-121: Should the SHACL owl:Ontology include the \# character \- RDF Data Shapes Working Group Tracker \- W3C, accessed on January 23, 2026, [https://www.w3.org/2014/data-shapes/track/issues/121](https://www.w3.org/2014/data-shapes/track/issues/121)
29. linkml generate \- linkml documentation, accessed on January 23, 2026, [https://linkml.io/linkml/cli/generate.html](https://linkml.io/linkml/cli/generate.html)
30. vladistan/linkml-qudt: Conversion of QUDT ontology to LinkML \- GitHub, accessed on January 23, 2026, [https://github.com/vladistan/linkml-qudt](https://github.com/vladistan/linkml-qudt)
31. Source code for linkml.generators.projectgen, accessed on January 23, 2026, [https://linkml.io/linkml/\_modules/linkml/generators/projectgen.html](https://linkml.io/linkml/_modules/linkml/generators/projectgen.html)
32. Imports \- linkml documentation, accessed on January 23, 2026, [https://linkml.io/linkml/schemas/imports.html](https://linkml.io/linkml/schemas/imports.html)
