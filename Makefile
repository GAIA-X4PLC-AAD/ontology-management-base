# Makefile for Ontology Management Base
# Build command center for common development tasks

# Python command (override with: make PYTHON=python3)
ifeq ($(OS),Windows_NT)
PYTHON ?= python
else
PYTHON ?= python3
endif
PIP := $(PYTHON) -m pip

.PHONY: all install install-dev lint test docs clean help

# Default target
all: lint test

# Installation targets
install:
	$(PIP) install -e .

install-dev:
	$(PIP) install -e ".[dev]"
	pre-commit install

# Linting and formatting
lint:
	pre-commit run --all-files

format:
	black src/
	isort src/

# Testing targets
test: test-check-syntax test-check-artifact-coherence test-check-data-conformance test-failing

test-check-syntax:
	$(PYTHON) -m src.tools.validators.validation_suite --run check-syntax

test-check-artifact-coherence:
	$(PYTHON) -m src.tools.validators.validation_suite --run check-artifact-coherence

test-check-data-conformance:
	$(PYTHON) -m src.tools.validators.validation_suite --run check-data-conformance

test-failing:
	$(PYTHON) -m src.tools.validators.validation_suite --run check-failing-tests

# Test specific domain
test-domain:
	@if [ -z "$(DOMAIN)" ]; then \
		echo "Usage: make test-domain DOMAIN=hdmap"; \
		exit 1; \
	fi
	$(PYTHON) -m src.tools.validators.validation_suite --run all --domain $(DOMAIN)

# Documentation targets
docs-generate:
	$(PYTHON) -m src.tools.utils.properties_updater

docs-serve:
	mkdocs serve

docs-build:
	mkdocs build

# Registry management
registry-update:
	@if [ -z "$(TAG)" ]; then \
		$(PYTHON) -m src.tools.utils.registry_updater --release-tag main; \
	else \
		$(PYTHON) -m src.tools.utils.registry_updater --release-tag $(TAG); \
	fi

# Cleaning
clean:
	rm -rf build/ dist/ *.egg-info/
	rm -rf .pytest_cache/ .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

clean-cache:
	rm -f .ontology_iri_cache.json
	rm -f .repo_registry_cache.json

# Help
help:
	@echo "Ontology Management Base - Available Commands"
	@echo ""
	@echo "Installation:"
	@echo "  make install        Install package (user mode)"
	@echo "  make install-dev    Install with dev dependencies"
	@echo ""
	@echo "Linting:"
	@echo "  make lint           Run pre-commit checks"
	@echo "  make format         Format code with black/isort"
	@echo ""
	@echo "Testing:"
	@echo "  make test           Run all tests"
	@echo "  make test-check-syntax    Run check-syntax checks only"
	@echo "  make test-check-data-conformance     Run check-data-conformance validation only"
	@echo "  make test-domain DOMAIN=hdmap  Test specific domain"
	@echo ""
	@echo "Documentation:"
	@echo "  make docs-generate  Generate PROPERTIES.md files"
	@echo "  make docs-serve     Start local docs server"
	@echo "  make docs-build     Build static docs site"
	@echo ""
	@echo "Registry:"
	@echo "  make registry-update         Update registry (main branch)"
	@echo "  make registry-update TAG=v0.1.0  Update registry with tag"
	@echo ""
	@echo "Cleaning:"
	@echo "  make clean          Remove build artifacts"
	@echo "  make clean-cache    Remove cache files"
