#!/bin/bash

# Run tests
pytest tests/
if [ $? -ne 0 ]; then
    echo "Tests failed. Build aborted."
    exit 1
fi

# Create zip
zip pams_app_release.zip main.py models/patient.py services/patient_service.py utils/json_formatter.py requirements.txt README.md run.sh

echo "Build successful! Release artifact: pams_app_release.zip"
