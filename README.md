# DICOM Metadata API

A FastAPI application to store and retrieve metadata from DICOM files.

## Features

- Upload DICOM files and extract metadata
- Store metadata in SQLite database
- Query stored metadata by various fields
- Dockerized for easy deployment

## Requirements

- Python 3.9+
- Poetry for dependency management
- Docker and Docker Compose (optional)

## Installation

### Using Poetry

```bash
pip install poetry

poetry install --no-root

poetry run alembic upgrade head

poetry run uvicorn app.main:app --reload
```

### Using Docker

```bash
docker compose up --build
```