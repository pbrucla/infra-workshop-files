#!/bin/bash
set -x
# --name isn't technically required but used to give a name for the exec command after

docker run -p "5432:5432" -d \
    --name db \
    -e POSTGRES_PASSWORD=ACMCyber \
    -e POSTGRES_USER=workshop \
    -v ./secret_init.sql:/docker-entrypoint-initdb.d/secret_init.sql \
    postgres:14 

# Give time for db to start up before attempting to connect
sleep 3

docker exec -it db psql -U workshop

psql -U workshop -h 127.0.0.1

docker rm -f db