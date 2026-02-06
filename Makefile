# Project Chimera Control Plane

.PHONY: setup test lint clean docker-build docker-test

# --- Local Development ---

setup: ## Install dependencies using uv
	@echo "Initializing Golden Environment..."
	uv sync
	@echo "Environment ready."
spec-check: ## Verify code matches specs/technical.md
	python3 scripts/spec_check.py

test: ## Run tests locally
	@echo "Running Governor checks..."
	uv run pytest tests/ -v

lint: ## Run code quality checks
	uv run ruff check .
	uv run mypy src/

clean: ## Remove artifacts
	rm -rf .venv .pytest_cache .ruff_cache __pycache__
	find . -type d -name "__pycache__" -delete

# --- Container Operations ---

docker-build: ## Build the Chimera Agent Image
	docker build -t project-chimera:latest .

docker-test: docker-build ## Run tests inside Docker (The ultimate truth)
	docker run --rm project-chimera:latest