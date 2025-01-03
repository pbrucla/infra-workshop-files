# Activity 2: Communicating between Pods

In this activity, we will create a web server and allow it to access the database created in activity 1 using services.

## Part 0: Build the web server

Before we host a web server, we need to create the web server docker image first. A modified version of the same web server from before is available in the `web-server` folder - we've already built this container, available at `workshop.acmcyber.com/web-server`, but if you'd like to do it yourself, go ahead and build this container and push it to `workshop.acmcyber.com/YOUR_USERNAME` so we can use it in the cluster. Note: please make sure to build the container inside of cloud shell. If you build this locally on the wrong architecture (e.g. M1 Macs), it will not run in the cluster!

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

## Part 5: Testing

Once your app is deployed, let's test it!
- You can visit the site and see the information inside of the database in addition to the hostname, which identifies each pod. Notice how on each reload, the hostname may change, indicating how our NodePort load balances between all available pods.
- Try adding data by visiting `/add?secret=DATA`. While this may not be best practice, we should then see the data added when visiting `/`. Notice how the data is always seen regardless of frontend server, since while there are multiple web apps, they all use the same backend database, so they all appear to do the same thing. This is the basis behind horizonal scaling: split out the expensive computational work between multiple load balanced copies of the frontend server, and only the data that needs to be shared is on a shared database which itself might be distributed, but generally acts as one database.
