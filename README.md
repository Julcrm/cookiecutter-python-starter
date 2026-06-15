# cookiecutter-python-starter

A Python project template for production-ready scripts and services.
Preconfigured with uv, Ruff, pytest, pre-commit, and GitHub Actions CI.
The generation hook initialises Git, installs dependencies, and checks out a `dev` branch automatically.

---

## Stack

| Tool | Role |
|---|---|
| [uv](https://github.com/astral-sh/uv) | Package and environment management |
| [Ruff](https://github.com/astral-sh/ruff) | Linter and formatter |
| [pytest](https://docs.pytest.org/) | Test framework |
| [pre-commit](https://pre-commit.com/) | Git hooks (ruff lint + format) |
| [Loguru](https://github.com/Delgan/loguru) | Structured logging |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Environment variable loading |

---

## Usage

```bash
# Generate a new project from GitHub
cookiecutter https://github.com/julcrm/cookiecutter-python-starter

# Or from a local clone
cookiecutter .

# Start working
cd my_project
make install
```

---

## Makefile commands

| Command | Description |
|---|---|
| `make install` | Install dependencies via `uv sync` |
| `make run` | Run the application |
| `make test` | Run the test suite with pytest |
| `make lint` | Check and auto-fix code with ruff |
| `make pre-commit` | Install pre-commit hooks |
| `make add lib=pandas` | Add a runtime dependency |
| `make add-dev lib=httpx` | Add a dev dependency |
| `make clean` | Remove virtualenv, caches and build artifacts |

---

## Generated project structure

```
my_project/
├── src/
│   ├── __init__.py
│   └── main.py             # entry point
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── ci.yml          # lint + format check + test on push/PR (main & dev)
├── .dockerignore
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── Dockerfile              # optional
├── Makefile
├── README.md
└── pyproject.toml
```
