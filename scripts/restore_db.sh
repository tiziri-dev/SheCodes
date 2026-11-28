#!/bin/bash
set -e
FILE=$1
docker compose exec -T db psql -U $POSTGRES_USER $POSTGRES_DB < $FILE
echo "Restore OK depuis $FILE"  