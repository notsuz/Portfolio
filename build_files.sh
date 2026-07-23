#!/bin/bash
echo "Building project..."


python3 -m pip install -r requirements.txt


python3 -m django makemigrations --noinput
python3 -m django migrate --noinput
python3 -m django collectstatic --noinput --clear

echo "Build complete."