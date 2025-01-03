#!/bin/bash
set -x
kubectl apply -f act_1_soln.yaml
kubectl get deployments -n myapp
sleep 10
kubectl get deployments -n myapp
kubectl logs deployment/db -n myapp
kubectl exec -it deployment/db -n myapp -- psql -U workshop -d workshop -h 127.0.0.1 -c 'SELECT * from secrets;'
kubectl port-forward deployment/db -n myapp 5432:5432&
sleep 3
psql -U workshop -d workshop -h 127.0.0.1 -c 'SELECT * from secrets;'

# Extra testing
kubectl exec -it deployment/db -n myapp -- psql -U workshop -d workshop -h 127.0.0.1 -c "INSERT INTO secrets VALUES ('test');"
sleep 1
kubectl exec -it deployment/db -n myapp -- psql -U workshop -d workshop -h 127.0.0.1 -c 'SELECT * from secrets;'
kubectl rollout restart -n myapp deployment/db
sleep 10
kubectl exec -it deployment/db -n myapp -- psql -U workshop -d workshop -h 127.0.0.1 -c 'SELECT * from secrets;'
kubectl delete -f act_1_soln.yaml
