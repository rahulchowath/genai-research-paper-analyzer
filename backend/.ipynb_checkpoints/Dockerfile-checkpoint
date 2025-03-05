FROM python:3.10.2-slim-bullseye

ENV HOME=/root \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_CACHE_DIR=/tmp/poetry_cache \
  POETRY_VIRTUALENVS_IN_PROJECT=1 \
  POETRY_VIRTUALENVS_CREATE=1

# System deps:
RUN pip install poetry==1.8.2

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY pyproject.toml /app/

# initialise empty package to keep poetry happy
COPY src/__init__.py /app/src/__init__.py

# Project initialization:
RUN poetry install --no-interaction --no-ansi && rm -rf $POETRY_CACHE_DIR

# Creating folders, and files for a project:
COPY src/ /app/src/

CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "src.app:app", "--port", "8080"]
