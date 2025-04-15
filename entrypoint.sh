#!/bin/sh

# Create directory for SQLite database if it doesn't exist
mkdir -p /app/data

# Ensure the app has write permissions to the database directory
chmod -R 777 /app/data

# Run migrations
poetry run alembic upgrade head || echo "Migration failed, but continuing..."

# Start the application
exec uvicorn app.main:app --host 0.0.0.0 --port 8000