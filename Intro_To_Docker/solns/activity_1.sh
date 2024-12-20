#!/bin/bash

docker run -p "5432:5432" -d \
    --name db \ # Not required, but used to reference in next command
    -e POSTGRES_PASSWORD=ACMCyber \
    -e POSTGRES_USER=workshop \
    -v ./secret_init.sql:/docker-entrypoint-initdb.d/test.sql \
    postgres:14 

docker exec -it db psql -U workshop
