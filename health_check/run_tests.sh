#!/bin/bash

echo "Starting FastAPI server..."

uvicorn app.main:app --host 0.0.0.0 --port 8000 &

sleep 5

echo "Running health test..."

python tests/test_health.py