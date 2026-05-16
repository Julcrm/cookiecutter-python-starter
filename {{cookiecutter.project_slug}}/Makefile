.PHONY: all install add add-dev run test lint clean
# Check that uv is available
UV := $(shell command -v uv 2> /dev/null)

check_uv:
ifndef UV
	$(error "uv is not installed")
endif

install:
	uv sync

add:
	@test -n "$(lib)" || (echo "Usage: make add lib=pandas" && exit 1)
	uv add $(lib)

add-dev:
	@test -n "$(lib)" || (echo "Usage: make add-dev lib=pytest" && exit 1)
	uv add --dev $(lib)

run:
	uv run {{ cookiecutter.project_slug }}

test:
	uv run pytest tests/

lint:
	uv run ruff check --fix .

clean:
	rm -rf .venv
	rm -rf build dist
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache
