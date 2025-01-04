# Infra Workshop Files
These files are part of a 2 part workshop series run by ACM Cyber during Winter break of the 2024-25 school year on an Introduction to Docker and Kubernetes.

## Using the files
Note that since this workshop used our infrastructure, some parts, such as our docker registry at `workshop.acmcyber.com`, will not work as they are now offline. However, almost all of the docker portion can be done as-is, just skipping running the actual `docker push` command. The kubernetes workshop will require running a k3s cluster - this can be done in a cloud VM (remember to disable the cloud provider's firewall!) or in a virtual machine, running `curl -sfL https://get.k3s.io | sh - ` as root to install k3s (https://docs.k3s.io/quick-start), and either doing all of the kubectl commands inside of the vm which will already be configured to use the k3s cluster, or copying the `k3s.yaml` file from `/etc/rancher/k3s/k3s.yaml` (https://docs.k3s.io/cluster-access) to somewhere with kubectl and helm already installed. The web server docker image prebuild is available at `ghcr.io/pbrucla/infra-workshop-files/web-server` instead of `workshop.acmcyber.com/web-server`. You will not be able to use certmanager without a domain pointing to your k3s setup, but you can still create the ingress, just without https.

## Slides
- Introduction to Docker: https://l.acmcyber.com/w25-docker
- Introduction to Kubernetes: https://l.acmcyber.com/w25-kube
