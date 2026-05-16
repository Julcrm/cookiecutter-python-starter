FROM python:{{ cookiecutter.python_version }}-slim

# Install uv from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Cache dependencies layer separately from source code
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . .

CMD ["uv", "run", "{{ cookiecutter.project_slug }}"]
