Chapter 6
=======

The code in this chapter includes the three microservices for the example, Thoughts Backend, Users Backend and Frontend, each in its own subdirectory.

On each of the subdirectories, there's a `docker-compose.yaml` file to operate the service, and a `kubernetes` subdirectory with the configuration for each microservice.

Connecting of microservices
========

![Connecting of microservices](docs/connecting_services.png)


Run kubernetes deployment locally
=======

1. Make sure you have kubectl and minicube installed on your computer.
2. Run minikube kubernetes cluster
```
make run-k8s-cluster
```
3. Build and run microservices:
```
make local-deploy
```

4. Check status of running microservices
```
make local-deploy-status
```
5. Fetch URLs of the services in the minikube cluster:
```
minikube service -n thoughts users-service --url
minikube service -n thoughts thoughts-service --url
minikube service -n thoughts frontend-service --url
```

5. Open the fetched URLs the in the web browser:
```
firefox http://192.168.49.2:30604
```
