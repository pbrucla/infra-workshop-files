# Activity 3: A full webserver

In this activity, we will properly host the webserver we created in activity 2 over HTTPS via ingresses.

## Part -1: Install an ingress controller in the cluster

Ingresses don't do anything by themselves, and need an ingress controller in order to work. Since we're using k3s, [Traefik](https://doc.traefik.io/traefik/providers/kubernetes-ingress/) is pre-installed, so we can skip this step.

## Part 0: Install cert-manager in the cluster

In order to avoid having to manually provision HTTPS certificates, we'll be installing [cert-manager](https://cert-manager.io) into the cluster. To do this, we'll be using a tool called [Helm](https://helm.sh). If you're using Google Cloud Shell, it should already be installed.

Then, run the following command to add the Helm repo:
```bash
helm repo add jetstack https://charts.jetstack.io --force-update
```

Now, you can install it into the cluster with the following command:
```bash
helm install \
    cert-manager jetstack/cert-manager \
    --namespace cert-manager \
    --create-namespace \
    --version v1.16.2 \
    --set crds.enabled=true
```

If all goes well, the command `kubectl get deployments -n cert-manager` should output something like the following:
```
NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
cert-manager              1/1     1            1           6m35s
cert-manager-cainjector   1/1     1            1           6m35s
cert-manager-webhook      1/1     1            1           6m35s
```

## Part 1: Create the cluster issuer

Since we didn't really cover cluster issuers, the one at the top of `ingress-example.yaml` is almost complete. You just need to fill in your email.

## Part 2: Create the ingress

You should've been assigned a domain that points to your cluster's IP. Edit the ingress in `ingress-example.yaml` to use this domain, and also set the correct service and port for the backend.

## Part 3: Testing

Once you've created the ingress, let's check in on how cert-manager is doing! If you run `kubectl get certs -n [YOUR_NAMESPACE]`, you should see there's a certificate with the secret name you set. Since the issuer is configured to be an http01 challenge, it should be ready pretty quickly. If the "READY" column is still False after ~20 seconds, run `kubectl describe cert/[CERT_NAME] -n [YOUR_NAMESPACE]`, and scroll down to the status and events at the bottom. You should be able to spot something abnormal.

After the certificate is ready, you can try opening `https://[YOUR_DOMAIN]` in curl or your browser, and it should show the same response as before without any HTTPS errors. You're done!
