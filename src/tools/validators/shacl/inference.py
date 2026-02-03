#!/usr/bin/env python3
"""
RDFS inference engine with optimized SPARQL.

This module provides RDFS inference using iterative SPARQL updates,
which is faster than the owlrl library for typical ontology sizes.

Key optimizations:
  - Uses iterative approach instead of transitive closure operators
  - Avoids O(N³) worst case for deep hierarchies
  - Stops early when no new triples are inferred
"""

from typing import Tuple

from rdflib import Graph

from src.tools.core.logging import get_logger

# Module logger
logger = get_logger(__name__)

# Try to import performance optimization
try:
    import oxrdflib  # noqa: F401

    FAST_STORE = "oxigraph"
except ImportError:
    FAST_STORE = "default"

# Maximum iterations to prevent infinite loops
MAX_ITERATIONS = 10

# RDFS inference rules using single-step (non-transitive) patterns
# These are applied iteratively until fixpoint
RDFS_RULES_ITERATIVE = [
    # Rule: rdfs:subClassOf (single step, iterated for transitivity)
    """
    INSERT { ?x a ?superClass }
    WHERE {
        ?x a ?class .
        ?class rdfs:subClassOf ?superClass .
        FILTER(?class != ?superClass)
    }
    """,
    # Rule: rdfs:subPropertyOf (single step, iterated for transitivity)
    """
    INSERT { ?subject ?superProperty ?object }
    WHERE {
        ?subject ?property ?object .
        ?property rdfs:subPropertyOf ?superProperty .
        FILTER(?property != ?superProperty)
    }
    """,
    # Rule: rdfs:domain
    """
    INSERT { ?subject a ?class }
    WHERE {
        ?subject ?property ?object .
        ?property rdfs:domain ?class .
    }
    """,
    # Rule: rdfs:range (only for IRI objects)
    """
    INSERT { ?object a ?class }
    WHERE {
        ?subject ?property ?object .
        ?property rdfs:range ?class .
        FILTER(isIRI(?object))
    }
    """,
]

# Single-pass rules that don't need iteration (not transitive)
RDFS_RULES_SINGLE_PASS = [
    # Rule: rdfs:domain
    """
    INSERT { ?subject a ?class }
    WHERE {
        ?subject ?property ?object .
        ?property rdfs:domain ?class .
    }
    """,
    # Rule: rdfs:range (only for IRI objects)
    """
    INSERT { ?object a ?class }
    WHERE {
        ?subject ?property ?object .
        ?property rdfs:range ?class .
        FILTER(isIRI(?object))
    }
    """,
]


def apply_rdfs_inference(
    data_graph: Graph,
    ontology_graph: Graph,
    iterate_to_fixpoint: bool = True,
    max_iterations: int = MAX_ITERATIONS,
) -> Tuple[Graph, int]:
    """
    Apply RDFS inference rules to data combined with ontology.

    This uses iterative SPARQL updates instead of transitive closure
    operators (rdfs:subClassOf+) which can be slow for deep hierarchies.

    Args:
        data_graph: Data graph to infer on
        ontology_graph: Ontology graph with class/property definitions
        iterate_to_fixpoint: If True, iterate rules until no new triples
        max_iterations: Maximum iterations to prevent infinite loops

    Returns:
        Tuple of (combined_graph, inferred_count)
    """
    # Create combined graph for inference
    combined = Graph(store=FAST_STORE)
    combined += data_graph
    combined += ontology_graph

    initial_count = len(combined)
    total_inferred = 0

    if iterate_to_fixpoint:
        # Iterative approach for transitive closure
        for iteration in range(max_iterations):
            count_before = len(combined)

            # Apply subClass and subProperty rules (need iteration)
            for rule in RDFS_RULES_ITERATIVE[:2]:
                try:
                    combined.update(rule)
                except Exception as e:
                    logger.debug("RDFS rule skipped: %s", e)

            count_after = len(combined)
            new_triples = count_after - count_before

            if new_triples == 0:
                logger.debug("RDFS fixpoint reached after %d iterations", iteration + 1)
                break

            logger.debug("RDFS iteration %d: +%d triples", iteration + 1, new_triples)

        # Apply domain/range rules once (they don't need iteration)
        for rule in RDFS_RULES_SINGLE_PASS:
            try:
                combined.update(rule)
            except Exception as e:
                logger.debug("RDFS rule skipped: %s", e)
    else:
        # Single-pass rules only (faster but incomplete for deep hierarchies)
        for rule in RDFS_RULES_ITERATIVE:
            try:
                combined.update(rule)
            except Exception as e:
                logger.debug("RDFS rule skipped: %s", e)

    total_inferred = len(combined) - initial_count

    return combined, total_inferred


def apply_rdfs_inference_transitive(
    data_graph: Graph,
    ontology_graph: Graph,
) -> Tuple[Graph, int]:
    """
    Apply RDFS inference using transitive closure operators.

    This is the original approach using rdfs:subClassOf+ which may be
    slower for deep hierarchies but is simpler to understand.

    Use apply_rdfs_inference() with iterate_to_fixpoint=True for better
    performance on larger ontologies.

    Args:
        data_graph: Data graph to infer on
        ontology_graph: Ontology graph with class/property definitions

    Returns:
        Tuple of (combined_graph, inferred_count)
    """
    combined = Graph(store=FAST_STORE)
    combined += data_graph
    combined += ontology_graph

    initial_count = len(combined)

    # Transitive closure rules
    transitive_rules = [
        """
        INSERT { ?x a ?superClass }
        WHERE {
            ?x a ?class .
            ?class rdfs:subClassOf+ ?superClass .
        }
        """,
        """
        INSERT { ?subject ?superProperty ?object }
        WHERE {
            ?subject ?property ?object .
            ?property rdfs:subPropertyOf+ ?superProperty .
        }
        """,
        """
        INSERT { ?subject a ?class }
        WHERE {
            ?subject ?property ?object .
            ?property rdfs:domain ?class .
        }
        """,
        """
        INSERT { ?object a ?class }
        WHERE {
            ?subject ?property ?object .
            ?property rdfs:range ?class .
            FILTER(isIRI(?object))
        }
        """,
    ]

    for rule in transitive_rules:
        try:
            combined.update(rule)
        except Exception as e:
            logger.debug("RDFS transitive rule skipped: %s", e)

    total_inferred = len(combined) - initial_count

    return combined, total_inferred
