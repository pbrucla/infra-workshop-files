# Activity 1: Simple Deployment

Let's get started with your first deployment against a Kubernetes cluster!

## Potentially useful resources
- https://kubespec.dev: Kubernetes .yaml file specification explorer

## Part -1: Setting up the cluster

If you don't already have a cluster, you'll have to set one up yourself. K3s has a simple installation guide [on their homepage](https://k3s.io), but note that it takes up a wide range of ports, so it's not recommended to install it directly on your machine. Instead, you'll want to provision either a cloud machine, or spin up a Linux VM to install it. If you set up your own k3s cluster, then don't use the `k3s.yaml` file in this repository. Instead, pull the file from `/etc/rancher/k3s/k3s.yaml` on the machine the cluster is on, and add the line `insecure-skip-tls-verify: true` after the `server:` line.

## Part 0: Connecting to your cluster

First, we need to authenticate to the cluster. Make sure you are on google cloud shell at https://shell.cloud.google.com, and then copy the **contents** of `k3s.yaml` to the file at `~/.kube/config`, creating it if it does not exist. You will then need to edit the line `server: https://127.0.0.1:6443` and replace `127.0.0.1` with your cluster's IP address, which we should have provided you by now. **Keep the port 6443.**

Once done, try running `kubectl get namespaces`. If you connected successfully, you should see something like this:

```
$ kubectl get namespaces
NAME                    STATUS   AGE
cyber-connection-test   Active   2s
default                 Active   142m
kube-node-lease         Active   142m
kube-public             Active   142m
kube-system             Active   142m
```

## Part 1: Creating a namespace

Let's create a namespace! We can use the `kubectl create namespace <namespace>` command. Go ahead and do that - pick something appropriate, and remember it for the rest of this activity.

## Part 2: Creating a ConfigMap

If you remember from the Docker workshop, we had a `init.sql` file that we needed to mount into the container in a specific folder. In kubernetes, if you need to mount configuration files, we use the appropriately named `ConfigMap` Object! We specify as many key-value pairs as we want, and then specify in the Deployment where we want those key-value pairs to go: as a file in a volume like we did before, environment variable, etc. Since we didn't cover it very deeply, most of the ConfigMap framework is there - just fill in the blanks where comments tell you to.

More information about ConfigMaps (and the source of the ConfigMap example file) can be found at https://kubernetes.io/docs/concepts/configuration/configmap/.

## Part 3: Making your Deployment file

Time to make your first deployment! In this activity, we will be deploying a Postgres database, just like last time! A couple reminders for what we want:
- Database Name: workshop
- Username: workshop
- Password: ACMCyber
- Postgres version: 14
- Postgres runs on port 5432.
- Mounting the .sql file. This will require specifying a `volume` inside of the pod template, and mounting it inside of the container using a `volumeMount` inside of the container. Just follow the comments provided.
- Remember to specify the namespace!

Create the .yaml Deployment file. With Kubernetes, usually we don't create deployment files from scratch, but start from some template either from searching online or past deployments (or *I guess*, ChatGPT/Gemini/Claude, but for this workshop, we intend you to do it the old way so you understand what's going on). Feel free to name this file anything.
- Since this is a database, we only want **one** replica. We don't want our database to be split!
  - If we were doing this properly and wanted to save data, we would use a PersistentVolume like https://kubernetes.io/docs/concepts/storage/persistent-volumes/, but since this is presumed to be a CTF challenge, resetting the database on restart or pod crash is a feature, not a bug.
  - For LA CTF/ACM Cyber, our persistent databases actually just live outside the cluster.
- Don't forget to match the labels
- Remember to list the Postgres default port

## Part 4: Deploying your.... deployment

Now it's time to deploy! We do this using the `kubectl apply -f FILE.yaml` command. This command will either create the Kubernetes Objects specified in the yaml file, or if they already exist, modify them to match any changes you made. Get comfortable with this command, as you'll be using it over and over and over!

Once deployed, use `kubectl get deployments` and `kubectl describe deployment/NAME` to ensure that it is deployed, and take a look at the logs with the `kubectl logs` command. Remember to specify the namespace with `-n NAMESPACE` on every command!

## Part 5: Testing your deployment

Let's test that the database is actually running! Run `psql -U USERNAME -d DATABASE_NAME -h 127.0.0.1`, replacing username and database_name with the username and database names set earlier **inside the Pod** with `kubectl exec -it`. If successful, you should be able to run `select * from secrets;` inside of the psql shell and see some data. Type `\q` and hit enter to exit.

In addition, we can also try connecting to the database ourselves by using `kubectl port-forward` to forward the port inside of the pod/container to our cloud shell, and then connect through this port-forward by running `psql -U USERNAME -d DATABASE_NAME -h 127.0.0.1` in cloud shell. Note that port-forward runs in the foreground while waiting for a connection to the port locally, so it will appear to hang, and you'll need to run psql in another tab. Again, if successful, you should be able to run `select * from secrets;` inside of the psql shell and see some data. Type `\q` and hit enter to exit.

Notice how you are not prompted to enter your password: that is because for port forwarding with kubectl, it appears to the container that the traffic is coming from localhost, not from an external source.

In addition, try the following:
- Add some data into the database. This can be done using `insert into secrets values ('VALUE HERE');` (note the use of single quotes).
- Restart the database using kubectl.
- Reconnect to the database. Notice how the added data was removed, as restarting actually deletes and re-creates the pod
- Make some changes to the yaml file: add replicas, change the password, edit the configmap data, etc, and see how they apply when doing `kubectl apply`
- Delete resources using `kubectl delete`

## (Optional) Part 6: Automatically creating the namespace
Instead of running `kubectl create namespace` before running `kubectl apply`, let's just put the creation of our namespace in the file. Do a little google searching to find how to do this. Remember: kubernetes objects are created from top down, so if you reference an object in another object, you must make sure that this object is created first and placed higher up in the file!
