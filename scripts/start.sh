#!/bin/bash

# Check prerequisites
command -v docker-compose >/dev/null 2>&1 || { echo >&2 "docker-compose is required but it's not installed. Aborting."; exit 1; }

# Start services
docker-compose up