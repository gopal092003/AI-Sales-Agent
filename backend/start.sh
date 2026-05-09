#!/usr/bin/env bash

set -o errexit

echo "Starting AI Sales Intelligence Agent Backend..."

uvicorn app.main:app \
  --host 0.0.0.0 \
  --port ${PORT:-8000}