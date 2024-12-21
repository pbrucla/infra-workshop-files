#!/bin/bash
set -x

docker build . -t workshop.acmcyber.com/soln:v1
docker run -dp 8080:5000 --name flask workshop.acmcyber.com/soln:v1
sleep 3
curl http://localhost:8080
# This may fail if registry is down after the workshop
docker push workshop.acmcyber.com/soln:v1
docker rm -f flask
