#!/bin/bash
set -x
kubectl get namespaces
kubectl create namespace myapp
kubectl get namespaces
kubectl apply -f act_1_soln.yaml
kubectl get deployments -n myapp
sleep 10
kubectl get deployments -n myapp
kubectl logs deployment/db
kubectl exec -it deployment/db -n myapp -- psql -U workshop -d workshop -h 127.0.0.1 -c 'SELECT * from secrets;'
kubectl port-forward deployment/db -n myapp 5432:5432&
psql -U workshop -d workshop -h 127.0.0.1 -c 'SELECT * from secrets;'
