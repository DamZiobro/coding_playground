Chapter 6
=======

The code in this chapter includes the three microservices for the example, Thoughts Backend, Users Backend and Frontend, each in its own subdirectory.

On each of the subdirectories, there's a `docker-compose.yaml` file to operate the service, and a `kubernetes` subdirectory with the configuration for each microservice.

Connecting of microservices
========

![Connecting of microservices](docs/connecting_services.png)


Deploy kubernetes locally
=======

1. Make sure you have kubectl and minicube installed on your computer.
2. Run minikube kubernetes cluster
```
make run-k8s-cluster
```
3. Build and run microservices:
```
make deploy
```

4. Check status of running microservices
```
make deploy-status
```
5. If deployed successfully open the service in the web browser:
```
firefox http://localhost:8000
```
