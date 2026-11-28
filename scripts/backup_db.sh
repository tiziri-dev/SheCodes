#!/bin/bash
set -e
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p backup
docker compose exec -T db pg_dump -U $POSTGRES_USER $POSTGRES_DB > backup/edt_$DATE.sql
echo "Backup OK: backup/edt_$DATE.sql"