#!/bin/bash

# Pull the latest changes
ssh user@server "cd /path/to/app && git pull"

# Build and restart services
ssh user@server "cd /path/to/app && docker-compose -f docker-compose.yml -f docker-compose.prod.yml pull && docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build"

# Run migrations
ssh user@server "/path/to/app/scripts/migrate.sh"