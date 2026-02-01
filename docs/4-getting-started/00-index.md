# Getting Started

Welcome! This section helps you get up and running with this ontology repository.

## Quick Navigation

**I want to...**

- **Understand what's in this repo** → Start with [Quickstart](01-quickstart.md)
- **Set up development environment** → Go to [Installation](02-installation.md)
- **Validate some data** → Follow [First Validation](03-first-validation.md)
- **Learn the repository structure** → See [Repository Structure](04-repository-structure.md)

## Where Are You Coming From?

### You're a Data Engineer / Systems Developer

**Your Goal:** Integrate ontologies into your data pipeline

**Follow this path:**

1. [Quickstart](01-quickstart.md) - Understand what ontologies do
2. [First Validation](03-first-validation.md) - Try validating sample data
3. [Repository Structure](04-repository-structure.md) - Understand where files are
4. Then → [Ontology Domains](../3-ontology-domains/) to pick the right ontology
5. Then → [Validation Tools](../6-validation-tools/) for detailed reference

### You're a Semantic Web Expert

**Your Goal:** Contribute to ontology development

**Follow this path:**

1. [Repository Structure](04-repository-structure.md) - See project layout
2. Then → [Architecture](../2-architecture/) - Understand design patterns
3. Then → [Building & Contributing](../5-building-contributing/) - Contribution process

### You're New to Semantic Web / Ontologies

**Your Goal:** Learn the fundamentals

**Follow this path:**

1. [Quickstart](01-quickstart.md) - Get high-level overview
2. Then → [Foundations](../1-foundations/) - Learn semantic web basics
3. [First Validation](03-first-validation.md) - See it in action
4. Then → [Architecture](../2-architecture/) - Deeper design understanding

### You're Evaluating This Repository

**Your Goal:** Decide if it's right for you

**Follow this path:**

1. [Quickstart](01-quickstart.md) - 5-minute overview
2. [Repository Structure](04-repository-structure.md) - What's available
3. [Ontology Domains](../3-ontology-domains/) - Specific ontologies
4. [Validation Tools](../6-validation-tools/) - Quality assurance capabilities

## Five-Minute Overview

### What This Repository Contains

A comprehensive set of **ontologies** (formal specifications of concepts and relationships) for:

- Autonomous vehicles and simulation
- Service definitions and capabilities
- Scenario representation
- Validation and quality assurance
- GAIA-X governance concepts

### How It's Organized

```
Two separate namespaces:
├── GAIA-X 4 PLC-AAD (Stable, 2021-2024)
│   └── 16 production-ready ontologies
└── ENVITED-X (Active development, 2024+)
    └── 4+ innovative new ontologies
```

All published as **persistent, resolvable IRIs** (like `https://w3id.org/gaia-x4plcaad/ontologies/scenario/v2/`)

### Why You Might Use This

- **Data Integration**: Exchange data between autonomous vehicle systems
- **Validation**: Check that data conforms to standards
- **Documentation**: Formal specifications of concepts
- **Standardization**: Build on proven, peer-reviewed ontologies
- **Reasoning**: Let systems infer new facts from data

### What Technologies Are Used

| Technology   | Purpose                              |
| ------------ | ------------------------------------ |
| **RDF**      | Data representation and linking      |
| **OWL**      | Ontology definition and semantics    |
| **SHACL**    | Data validation and quality checking |
| **Turtle**   | Human-readable file format           |
| **JSON-LD**  | JSON integration format              |
| **w3id.org** | Persistent identifier resolution     |

## Next Steps

Choose your path above and start reading!

Or if you want a gentle introduction, read [Quickstart](01-quickstart.md) first.

## Common Questions

### Q: Do I need to know RDF/OWL to use this?

**A:** Not necessarily! For basic data validation, you can use ontologies without deep knowledge. For contributing to ontologies, some learning is helpful. See [Foundations](../1-foundations/) for an intro.

### Q: Can I use these ontologies in my own systems?

**A:** Yes! All ontologies are published under open licenses and IRIs. You can import them and build on them. See [Building & Contributing](../5-building-contributing/) for guidelines.

### Q: What if I find a bug or want to propose changes?

**A:** Great! See [Building & Contributing](../5-building-contributing/01-contributing.md) for the process. We welcome community input.

### Q: Which ontology should I use?

**A:** Depends on your domain:

- Autonomous vehicle simulation? → [Automotive Simulator](../3-ontology-domains/gaia-x4plcaad/01-index.md#automotive-simulator)
- Service descriptions? → [Service Ontology](../3-ontology-domains/gaia-x4plcaad/01-index.md#service)
- HD Maps? → [HD Map](../3-ontology-domains/gaia-x4plcaad/01-index.md#hd-map)

Browse [Ontology Domains](../3-ontology-domains/) for complete list.

### Q: Are there examples I can try?

**A:** Yes! See [First Validation](03-first-validation.md) for a hands-on example with sample data.

## Getting Help

- **Conceptual questions?** → Read [Foundations](../1-foundations/)
- **Architecture questions?** → Read [Architecture](../2-architecture/)
- **Tool questions?** → Read [Validation Tools](../6-validation-tools/)
- **Contributing questions?** → Read [Building & Contributing](../5-building-contributing/)
- **Bugs or feature requests?** → Open a GitHub issue

## Navigation

← [Back to Home](../index.md)
→ [Continue to Quickstart](01-quickstart.md)
