#!/bin/bash

set -x

docker compose up -d --build
sleep 3
curl http://localhost:8080
docker compose exec db psql -U workshop
psql -U workshop -h 127.0.0.1
docker compose down
