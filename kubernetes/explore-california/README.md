Explore California - template project for kubernetes-based development 
==============

Developers - Getting started
------

## Install system-based prerequisites
1. [Install docker](https://docs.docker.com/engine/install/)
2. [Install kind](https://kind.sigs.k8s.io/) to generate local kubernetes clusters
3. [Install kubectl](https://kubernetes.io/docs/tasks/tools/) to control local kubernetes resources

Docker-based local development and tests
------

* **make build** - build project-related docker image
* **make run** - runs project-related docker container (build must be performed first)
* **make build run** - runs above 2 commands 'make build' and 'make run' in order
* **make stop** - stops project-related docker containers (without deleting them)
* **make clean** -  removes project-related docker containers and docker images

Kubernetes-based local development, deployment and tests
------

* **make create-kind-cluster** - creates kind-based k8s claster for local development
* **make run-local-docker-registry** - runs docker container containing local docker registry (if it is not running already)
* **make run-local-k8s-env** - generates all local resources related to k8s deployment:
  * kind-based k8s cluster
  * local docker registry


Cleaning resources in case of issues
------
* **make clean** - removes project-related docker containers and docker images (does not remove any k8s-based deployed resources)
* **make dist-clean** - removes ALL project-related resources:
  * kind-based k8s cluster
  * local docker registry
  * all project-related docker containers and docker-images
