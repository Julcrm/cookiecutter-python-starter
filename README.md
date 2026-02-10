# Cookiecutter Python Starter

![Cookiecutter](https://raw.githubusercontent.com/cookiecutter/cookiecutter/main/logo/cookiecutter_medium.png)

Un modèle de projet Python, conçu pour démarrer rapidement avec les meilleures pratiques.

Ce template utilise :
- **[uv](https://github.com/astral-sh/uv)** : Gestionnaire de package et d'environnement (remplace pip, poetry, venv).
- **[Ruff](https://github.com/astral-sh/ruff)** : Linter et formateur Python.
- **[Pytest](https://docs.pytest.org/)** : Framework de tests.
- **[Makefile](https://www.gnu.org/software/make/)** : Commandes raccourcies pour l'automatisation.
- **[Loguru](https://github.com/Delgan/loguru)** : Logging simplifié.
- **[Python-dotenv](https://github.com/theskumar/python-dotenv)** : Gestion des variables d'environnement.

---

## >>> Fonctionnalités

- **Structure claire** : `src/` pour le code source, `tests/` pour les tests.
- **Environment Management** : Configuration automatique de l'environnement virtuel avec `uv sync`.
- **Installation Python** : Installation automatique de la version Python demandée si elle n'est pas présente sur le système (via `uv`).
- **Git Ready** : Initialisation automatique du dépôt Git et premier commit.
- **Docker Optionnel** : Choix d'inclure ou non un `Dockerfile`.
- **Qualité du code** : Configuration stricte de Ruff pour un code propre et sécurisé.

## [!] Pré-requis

- **Python 3.9+**
- **Uv**.
- **Cookiecutter** : `pip install cookiecutter`.

## --> Utilisation

### 1. Générer un nouveau projet

Lancez la commande suivante dans votre terminal :

```bash
cookiecutter https://github.com/julcrm/cookiecutter-python-starter
```
*(Remplacez l'URL par le chemin local si vous testez en local)*

```bash
cookiecutter .
```

### 2. Répondre aux questions

Le script vous demandera :
- `project_name` : Nom de votre projet.
- `project_slug` : Nom du dossier (généré automatiquement).
- `author_name` : Votre nom.
- `python_version` : Version de Python à utiliser (sera installée par `uv` si nécessaire).
- `include_docker` : Voulez-vous un Dockerfile ?

### 3. Démarrer

Une fois le projet généré :

```bash
cd mon_nouveau_projet
make install   # Installe les dépendances avec uv
make run       # Lance l'application
make test      # Lance les tests
make lint      # Vérifie et corrige le code
```

### Commandes du Makefile

| Commande | Description |
|---|---|
| `make install` | Installe les dépendances du projet via `uv sync`. |
| `make run` | Lance l'application (`src/main.py`). |
| `make test` | Lance la suite de tests avec `pytest`. |
| `make lint` | Analyse et corrige le code avec `ruff`. |
| `make add lib=pandas` | Ajoute une dépendance (ex: pandas). |
| `make add-dev lib=black` | Ajoute une dépendance de dev. |
| `make clean` | Nettoie les fichiers temporaires et caches. |

---