#!/bin/bash

# Usage: curl -s https://raw.githubusercontent.com/CEU-Economics-and-Business/ECBS-5147-Data-Engineering-2-Cloud-Computing/main/sync.sh | bash

echo "Syncing with template repository..."

# Update requirements files
curl -s https://raw.githubusercontent.com/CEU-Economics-and-Business/ECBS-5147-Data-Engineering-2-Cloud-Computing/main/requirements.txt > requirements.txt
curl -s https://raw.githubusercontent.com/CEU-Economics-and-Business/ECBS-5147-Data-Engineering-2-Cloud-Computing/main/requirements.in > requirements.in

# Sync serverless folder
rm -rf serverless
curl -sL https://github.com/CEU-Economics-and-Business/ECBS-5147-Data-Engineering-2-Cloud-Computing/archive/main.zip | tar -xf - --strip=1 "ECBS-5147-Data-Engineering-2-Cloud-Computing-main/serverless"

# Install requirements
pip install -r requirements.txt

echo "Sync completed! Requirements installed."
