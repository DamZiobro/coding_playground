XMementoIT Kubernetes Development Environment - template project for kubernetes-based DevOps-based development 
==============

## Developers - Getting started


### Install system-based prerequisites
1. [Install docker](https://docs.docker.com/engine/install/)
2. [Install kind](https://kind.sigs.k8s.io/) to generate local [Kubernetes](https://kubernetes.io/) clusters
3. [Install kubectl](https://kubernetes.io/docs/tasks/tools/) to control local kubernetes resources

### Run project-related docker container

1. Build project-related docker image: `make build`
2. Run project-related docker container based on built docker image: `make run` 
3. Make sure the website is up and running: `firefox http://localhost:3000`

### Run project inside k8s local environment

1. Run k8s local cluster and local [docker registry](https://docs.docker.com/registry/) using [kind](https://kind.sigs.k8s.io/): `make run-full-k8s-env`
2. Build project-related docker image and push to local docker registry: `make push`
3. Deploy docker image to local k8s cluster: `make deploy`
3. Make sure the website is up and running: `firefox http://xmementoit-k8s-development.com`


## Developers - all development commands

### Docker-based local development and tests

* **make build** - build project-related docker image
* **make run** - runs project-related docker container (`make build` must be performed first)
  * make sure the website is up and running at `http://localhost:3000`
* **make build run** - runs above 2 commands 'make build' and 'make run' in order
* **make stop** - stops project-related docker containers (without deleting them)
* **make clean** -  removes project-related docker containers and docker images

### Kubernetes-based local development SETUP commands


* **make create-kind-cluster** - creates kind-based k8s claster for local development
* **make run-local-docker-registry** - runs docker container containing local docker registry (if it is not running already)
* **make run-full-k8s-env** - generates ALL local resources related to k8s deployment:
  * kind-based k8s cluster
  * local docker registry

### Kubernetes-based local development DEV commands

* **make push** - pushes project-related docker images into local docker registry
* **make deploy** - deploys project using k8s
* **make deploy-status** - show status of k8s deployment (pods, services, deployments)


## Cleaning docker and k8s resources

* **make clean** - removes project-related docker containers and docker images (does not remove any k8s-based deployed resources)
* **make dist-clean** - removes ALL project-related resources:
  * kind-based k8s cluster
  * local docker registry
  * all project-related docker containers and docker-images
