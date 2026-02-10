# Variables pour les chemins
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# Par défaut, on installe
all: install

# Crée l'environnement virtuel SEULEMENT s'il n'existe pas
$(VENV)/bin/activate:
	python3 -m venv $(VENV)

# Installe les dépendances via le pip du venv
install: $(VENV)/bin/activate
	$(PIP) install -e .[dev]

# Lance le linter via le venv
lint:
	$(PYTHON) -m ruff check --fix .

# Lance les tests via le venv
test:
	$(PYTHON) -m pytest tests/

# Lance le script via le venv
run:
	$(PYTHON) src/main.py

# Nettoyage (supprime aussi le venv pour repartir de zéro)
clean:
	rm -rf build dist *.egg-info
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache

.PHONY: all install lint test run clean