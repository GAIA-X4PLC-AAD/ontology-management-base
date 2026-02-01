# Makefile for Ontology Management Base
# Build command center for common development tasks

.PHONY: all install install-dev lint test docs clean help

# Default target
all: lint test

# Installation targets
install:
	python3 -m pip install -e .

install-dev:
	python3 -m pip install -e ".[dev]"
	pre-commit install

# Linting and formatting
lint:
	pre-commit run --all-files

format:
	black src/
	isort src/

# Testing targets
test: test-syntax test-target-classes test-shacl test-failing

test-syntax:
	python3 -m src.tools.validators.run_all_checks_locally --check syntax

test-target-classes:
	python3 -m src.tools.validators.run_all_checks_locally --check target-classes

test-shacl:
	python3 -m src.tools.validators.run_all_checks_locally --check shacl

test-failing:
	python3 -m src.tools.validators.run_all_checks_locally --check failing-tests

# Test specific domain
test-domain:
	@if [ -z "$(DOMAIN)" ]; then \
		echo "Usage: make test-domain DOMAIN=hdmap"; \
		exit 1; \
	fi
	python3 -m src.tools.validators.run_all_checks_locally --check all --domain $(DOMAIN)

# Documentation targets
docs-generate:
	python3 -m src.tools.readme_generator

docs-serve:
	mkdocs serve

docs-build:
	mkdocs build

# Registry management
registry-update:
	@if [ -z "$(TAG)" ]; then \
		python3 -m src.tools.update_registry --release-tag main; \
	else \
		python3 -m src.tools.update_registry --release-tag $(TAG); \
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
	@echo "  make test-syntax    Run syntax checks only"
	@echo "  make test-shacl     Run SHACL validation only"
	@echo "  make test-domain DOMAIN=hdmap  Test specific domain"
	@echo ""
	@echo "Documentation:"
	@echo "  make docs-generate  Generate PROPERTIES.md files"
	@echo "  make docs-serve     Start local docs server"
	@echo "  make docs-build     Build static docs site"
	@echo ""
	@echo "Registry:"
	@echo "  make registry-update         Update registry (main branch)"
	@echo "  make registry-update TAG=v0.0.5  Update registry with tag"
	@echo ""
	@echo "Cleaning:"
	@echo "  make clean          Remove build artifacts"
	@echo "  make clean-cache    Remove cache files"
