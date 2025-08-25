#!/bin/bash

docker run --rm -it \
  -p 4000:8000 \
  -v "$(pwd)/app/main.py":/app/main.py \
  -w /app \
  python:3.10-slim \
  bash
