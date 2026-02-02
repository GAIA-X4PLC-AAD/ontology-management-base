#!/usr/bin/env python3
"""
Main SHACL validation orchestrator.

This module provides the ShaclValidator class which orchestrates the complete
SHACL validation pipeline using the modular components.
"""

import logging
import sys
import time
from dataclasses import dataclass, field
from io import StringIO
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from rdflib import Graph

from src.tools.utils.print_formatting import (
    normalize_path_for_display,
    print_validate_jsonld_against_shacl_result,
)
from src.tools.utils.registry_resolver import RegistryResolver

from .graph_loader import (
    FAST_STORE,
    extract_external_iris,
    load_fixtures_for_iris,
    load_jsonld_files,
    load_turtle_files,
)
from .inference import apply_rdfs_inference
from .schema_discovery import (
    discover_required_schemas,
    extract_rdf_types,
    get_base_ontology_paths,
)

# Try to import pyshacl
try:
    from pyshacl import validate

    PYSHACL_AVAILABLE = True
except ImportError:
    PYSHACL_AVAILABLE = False


@dataclass
class ValidationResult:
    """Result of a SHACL validation run."""

    conforms: bool
    return_code: int
    report_text: str
    report_graph: Optional[Graph] = None
    files_validated: List[str] = field(default_factory=list)
    triples_count: int = 0
    inferred_count: int = 0
    duration_seconds: float = 0.0


class ShaclValidator:
    """
    SHACL validation orchestrator using registry-based discovery.

    This class provides a clean interface for validating JSON-LD files
    against SHACL shapes, with automatic schema discovery and RDFS inference.

    Usage:
        validator = ShaclValidator(root_dir)
        result = validator.validate(jsonld_files)
        if not result.conforms:
            print(result.report_text)
    """

    def __init__(
        self,
        root_dir: Path,
        inference_mode: str = "rdfs",
        verbose: bool = True,
    ):
        """
        Initialize the SHACL validator.

        Args:
            root_dir: Repository root directory
            inference_mode: Inference mode (rdfs|owlrl|none|both)
            verbose: Whether to print progress messages
        """
        self.root_dir = Path(root_dir).resolve()
        self.resolver = RegistryResolver(root_dir)
        self.inference_mode = inference_mode
        self.verbose = verbose

    def _log(self, message: str) -> None:
        """Print message if verbose mode is enabled."""
        if self.verbose:
            print(message, flush=True)

    def _rel_path(self, path: Path) -> str:
        """Convert to repository-relative string for display."""
        return normalize_path_for_display(path, self.root_dir)

    def validate(self, jsonld_files: List[Path]) -> ValidationResult:
        """
        Run complete SHACL validation pipeline.

        Args:
            jsonld_files: List of JSON-LD files to validate

        Returns:
            ValidationResult with validation outcome and details
        """
        start_time = time.perf_counter()

        if not PYSHACL_AVAILABLE:
            return ValidationResult(
                conforms=False,
                return_code=99,
                report_text="Error: pyshacl is not installed",
                files_validated=[self._rel_path(f) for f in jsonld_files],
            )

        # Step 1: Load data
        self._log("\nStep 1: Loading JSON-LD Data Files...")
        data_graph, prefixes = self._load_data(jsonld_files)

        # Step 2: Extract types and discover schemas
        self._log("\nStep 2: Discovering Required Schemas...")
        rdf_types = extract_rdf_types(data_graph)
        ontology_graph, shacl_graph = self._load_schemas(rdf_types)

        # Step 3: Apply inference if requested
        self._log(f"\nStep 3: Applying Inference ({self.inference_mode})...")
        combined_graph, inferred_count = self._apply_inference(
            data_graph, ontology_graph
        )

        # Step 4: Run SHACL validation
        self._log("\nStep 4: Running SHACL Validation...")
        conforms, report_text, report_graph = self._run_validation(
            combined_graph, ontology_graph, shacl_graph
        )

        duration = time.perf_counter() - start_time

        return ValidationResult(
            conforms=conforms,
            return_code=0 if conforms else 210,
            report_text=report_text,
            report_graph=report_graph,
            files_validated=[self._rel_path(f) for f in jsonld_files],
            triples_count=len(combined_graph),
            inferred_count=inferred_count,
            duration_seconds=duration,
        )

    def _load_data(self, jsonld_files: List[Path]) -> Tuple[Graph, Dict[str, str]]:
        """Load JSON-LD files and resolve fixture references."""
        data_graph, prefixes = load_jsonld_files(jsonld_files, self.root_dir)

        for i, f in enumerate(jsonld_files, 1):
            self._log(f"  [{i}/{len(jsonld_files)}] Loaded: {self._rel_path(f)}")

        self._log(f"  Data triples: {len(data_graph)}")
        self._log(f"  Prefixes discovered: {len(prefixes)}")

        # Load fixtures for external references
        external_iris = extract_external_iris(data_graph)
        if external_iris:
            self._log(f"\n  Resolving {len(external_iris)} external references...")
            fixtures_loaded = load_fixtures_for_iris(
                external_iris, self.resolver, data_graph, self.root_dir
            )
            if fixtures_loaded > 0:
                self._log(f"  Fixtures loaded: {fixtures_loaded}")
                self._log(f"  Updated triples: {len(data_graph)}")

        return data_graph, prefixes

    def _load_schemas(self, rdf_types: Set[str]) -> Tuple[Graph, Graph]:
        """Load ontology and SHACL schemas based on discovered types."""
        self._log(f"  Types found: {len(rdf_types)}")
        for rdf_type in sorted(rdf_types):
            self._log(f"    {rdf_type}")

        # Discover required schemas
        ontology_paths, shacl_paths = discover_required_schemas(
            rdf_types, self.resolver
        )

        # Add base ontologies
        base_paths = get_base_ontology_paths(self.root_dir)
        all_ontology_paths = sorted(set(ontology_paths + base_paths))

        # Load ontologies
        self._log(f"\n  Loading {len(all_ontology_paths)} ontology files:")
        ontology_files = [self.resolver.to_absolute(p) for p in all_ontology_paths]
        ontology_graph = load_turtle_files(ontology_files, self.root_dir)

        for path in all_ontology_paths:
            self._log(f"    {path}")

        # Load SHACL shapes
        self._log(f"\n  Loading {len(shacl_paths)} SHACL files:")
        shacl_files = [self.resolver.to_absolute(p) for p in shacl_paths]
        shacl_graph = load_turtle_files(shacl_files, self.root_dir)

        for path in shacl_paths:
            self._log(f"    {path}")

        self._log(f"\n  Ontology triples: {len(ontology_graph)}")
        self._log(f"  SHACL triples: {len(shacl_graph)}")

        return ontology_graph, shacl_graph

    def _apply_inference(
        self, data_graph: Graph, ontology_graph: Graph
    ) -> Tuple[Graph, int]:
        """Apply RDFS inference based on configured mode."""
        if self.inference_mode == "rdfs":
            combined, inferred = apply_rdfs_inference(data_graph, ontology_graph)
            self._log(f"  Inferred {inferred} new triples")
            self._log(f"  Total triples: {len(combined)}")
            return combined, inferred
        elif self.inference_mode in ("owlrl", "both"):
            # Use pyshacl's built-in inference
            combined = Graph(store=FAST_STORE)
            combined += data_graph
            return combined, 0
        else:
            # No inference
            combined = Graph(store=FAST_STORE)
            combined += data_graph
            combined += ontology_graph
            return combined, 0

    def _run_validation(
        self,
        data_graph: Graph,
        ontology_graph: Graph,
        shacl_graph: Graph,
    ) -> Tuple[bool, str, Optional[Graph]]:
        """Run SHACL validation using pyshacl."""
        # Convert to default store if using oxigraph (pyshacl compatibility)
        if FAST_STORE == "oxigraph":
            self._log("  Converting to default store for validation...")
            validation_graph = Graph()
            validation_graph += data_graph
        else:
            validation_graph = data_graph

        try:
            conforms, results_graph, results_text = validate(
                validation_graph,
                shacl_graph=shacl_graph,
                ont_graph=(
                    ontology_graph if self.inference_mode in ("owlrl", "both") else None
                ),
                inference=(
                    self.inference_mode if self.inference_mode != "rdfs" else None
                ),
                abort_on_first=False,
                advanced=True,
                js=False,
                meta_shacl=False,
            )

            if conforms:
                self._log("  Validation PASSED")
            else:
                self._log("  Validation FAILED")

            return conforms, results_text, results_graph

        except Exception as e:
            error_msg = f"Validation error: {e}"
            self._log(f"  {error_msg}")
            return False, error_msg, None

    def format_result(self, result: ValidationResult) -> str:
        """
        Format validation result for console output.

        Args:
            result: ValidationResult to format

        Returns:
            Formatted string output
        """
        output_buffer = StringIO()
        print_validate_jsonld_against_shacl_result(
            result.conforms,
            result.files_validated,
            "" if not result.conforms else result.report_text,
            result.report_graph,
            exit_code=None,
            file=output_buffer,
        )
        return output_buffer.getvalue()


def validate_data_conformance(
    jsonld_files: List[Path],
    root_dir: Path,
    inference_mode: str = "rdfs",
    debug: bool = False,
    logfile: Optional[Path] = None,
) -> Tuple[int, str]:
    """
    Main validation entry point (backwards compatible).

    This function provides a backwards-compatible interface for the
    refactored SHACL validation system.

    Args:
        jsonld_files: List of JSON-LD files to validate
        root_dir: Repository root directory
        inference_mode: Inference mode for validation
        debug: Enable debug logging
        logfile: Optional log file path

    Returns:
        Tuple of (return_code, output_message)
    """
    # Set up logging
    if debug or logfile:
        level = logging.DEBUG if debug else logging.INFO
        handlers = []
        if logfile:
            handlers.append(logging.FileHandler(logfile))
        if debug:
            handlers.append(logging.StreamHandler(sys.stdout))
        if handlers:
            logging.basicConfig(
                level=level,
                format="%(asctime)s [%(levelname)s] %(message)s",
                handlers=handlers,
            )

    # Print header
    print("=" * 80)
    print("SHACL VALIDATION (Registry-Based)")
    print("=" * 80)

    if FAST_STORE == "oxigraph":
        print("Performance: Oxigraph (oxrdflib) is active")
    else:
        print("Performance: Using default rdflib store")

    if not PYSHACL_AVAILABLE:
        error_msg = "Error: pyshacl is not installed"
        print(error_msg, file=sys.stderr)
        return 99, error_msg

    # Initialize validator
    print(f"\nRepository Root: {root_dir}")
    validator = ShaclValidator(root_dir, inference_mode=inference_mode, verbose=True)

    info = validator.resolver.get_registry_info()
    print(f"Registry Domains: {info['domains_available']}")

    print(f"\nJSON-LD Files to Validate: {len(jsonld_files)}")
    for i, f in enumerate(jsonld_files[:5], 1):
        rel_path = normalize_path_for_display(f, root_dir)
        print(f"   {i}. {rel_path}")
    if len(jsonld_files) > 5:
        print(f"   ... and {len(jsonld_files) - 5} more")

    # Run validation
    result = validator.validate(jsonld_files)

    # Format and print output
    formatted_output = validator.format_result(result)
    print(formatted_output)

    return result.return_code, formatted_output
