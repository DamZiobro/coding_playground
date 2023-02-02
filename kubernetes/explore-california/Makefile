
PROJECT=explorecalifornia.com

#=========================================================
# LCOAL DEV docker commands
#=========================================================

deps: ## verifies project-related dependency tools are up and running
	@docker --version || (echo "docker tool is NOT installed on your local machine" && false)

build: deps ## build project-related docker image
	docker build -t $(PROJECT) .

run: deps ## runs project-related docker container (build must be performed first)
	docker run -d --name $(PROJECT) -p 5000:80 $(PROJECT)

stop: ## stops project-related docker containers (without deleting them)
	docker stop -d --name $(PROJECT)

clean: ## removes project-related docker containers and docker images (does not remove any k8s-based deployed resources)
	docker rm -f $(PROJECT)
	docker rmi -f $(PROJECT)

#=========================================================
# LOCAL DEV kubernetes commands
#=========================================================

kind-deps: deps ## makes sure that project-related system tools are installed (ex. kind, kubectl etc.)
	@kind --version || (echo "kind tool is NOT installed on your local machine" && false)
	@kubectl > /dev/null || (echo "kubectl tool is NOT installed on your local machine" && false)

#---------------------------------
# kind-based commands
#---------------------------------

create-kind-cluster: kind-deps ## creates kind-based k8s claster for local development
	kind create cluster --name $(PROJECT)
	kubectl get nodes
	touch $@

delete-kind-cluster: kind-deps ## deletes local kind-based k8s cluster
	kind delete cluster --name $(PROJECT)

#---------------------------------
# local-docker-registry-based commands
#---------------------------------
run-local-docker-registry: deps ## runs docker container containing local docker registry (if it is not running already)
	docker start local-docker-registry || docker run --name local-docker-registry -d --restart=always -p 5000:5000 registry:2
	touch $@

delete-local-docker-registry: ## removes locally running docker registry
	docker rm -f local-docker-registry

run-local-k8s-env: create-kind-cluster run-local-docker-registry

dist-clean: delete-local-docker-registry delete-kind-cluster clean ## remove all project-related docker images, docker containers (including local kind k8s cluster and local docker registry)
