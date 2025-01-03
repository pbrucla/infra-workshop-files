# Activity 2: Communicating between Pods

In this activity, we will create a web server and allow it to access the database created in activity 1 using services.

## Part 0: Build the web server

Before we host a web server, we need to create the web server docker image first. A modified version of the same web server from before is available in the `web-server` folder - go ahead and build this container and push it to `workshop.acmcyber.com/YOUR_USERNAME` so we can use it in the cluster. Note: please make sure to build the container inside of cloud shell. If you build this locally on the wrong architecture (e.g. M1 Macs), it will not run in the cluster!

The commands you need to build and run are available in `build.txt` if you forgot.

## Part 1: Create the web server deployment

Pretty much the same as the previous activity, but create a deployment for the web server. Consider copying/using the same file from before but adding a new deployment by placing the object after 3 dashes, similarly to how the ConfigMap and Deployment are separated to keep everything in the same file. There are new environment variables to specify (see app.py for details), and use the image you pushed to `workshop.acmcyber.com` in your deployment. Here, let's make 3 replicas of the web server. Note that the web server runs on port 5000!

## Part 2: Create a service to access the database

Create a service so that the web server can access the database! Since we are accessing the database only from within the cluster, we will want to create a service with a ClusterIP. 

Inside the database service, whatever name you give it, you can access the service from the web server using the name of the service as the hostname. For example, if you named it `postgres-db-service`, set `DB_HOST` in the web server's environment variables to `postgres-db-service`.

## Part 3: Create a service to access the web server from outside

Create another service so that we can access the web server from outside! We'll learn the proper way to do this later, but for now, just create a NodePort service that connects to the web server.

## Part 4: Deploy and pray

Now let's deploy our new services and deployment using `kubectl apply`! If everything goes well, you should be able to access http://YOUR_IP:NODE_PORT and see the data inside of the database! If not, you may need to do some debugging and fix your services and/or your deployments, reapply the changes, and try again. Note that it can take a few seconds for things to boot up, so use `kubectl get <resource_type>` in order to watch object statuses.
