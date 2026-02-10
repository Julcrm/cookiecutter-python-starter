{% if cookiecutter.include_docker == 'yes' %}
FROM python:{{ cookiecutter.python_version }}-slim

WORKDIR /app

# Optimisation du cache Docker
COPY pyproject.toml .
RUN pip install -e .

COPY . .

CMD ["python", "src/main.py"]
{% endif %}