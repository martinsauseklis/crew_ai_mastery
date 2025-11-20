#!/bin/bash

echo "Extracting platform code from markdown files..."
echo ""
python utils/extract_platform_code.py
echo ""
echo "Done! Platform code is in artifacts/demo/platform_code/"
echo ""
echo "To run the platform:"
echo "  cd artifacts/demo/platform_code"
echo "  cp .env.example .env"
echo "  docker-compose up"
