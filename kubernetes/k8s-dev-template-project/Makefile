PROJECT=xmementoit-k8s-development.com

APP_LOCAL_PORT=3000
DOCKER_REG_PORT=5000
DOCKER_REG_CONTAINER=local-docker-registry
DOCKER_REG_URL=localhost:$(DOCKER_REG_PORT)

#=========================================================
# LCOAL DEV docker commands
#=========================================================

deps: ## verifies project-related dependency tools are up and running
	@docker --version || (echo "docker tool is NOT installed on your local machine" && false)

build: deps ## build project-related docker images
	docker build -t $(PROJECT) .

run: deps ## runs project-related docker container (build must be performed first)
	docker run -d --name $(PROJECT) -p $(APP_LOCAL_PORT):80 $(PROJECT)
	echo "website is up-and-running on http://localhost:$(APP_LOCAL_PORT)"

stop: ## stops project-related docker containers (without deleting them)
	docker stop -d --name $(PROJECT)

clean: ## delete project-related docker containers and docker images (does not delete any k8s-based deployed resources)
	docker rm -f $(PROJECT)
	docker rmi -f $(PROJECT)


#=========================================================
# LOCAL DEV kubernetes DEV commands
#=========================================================

push: build ## pushes project-related docker images into local docker registry
	docker tag $(PROJECT) $(DOCKER_REG_URL)/$(PROJECT)
	docker push $(DOCKER_REG_URL)/$(PROJECT)

deploy: kind-deps ## deploys project using k8s
	@echo "Applying k8s deployment..."
	kubectl apply -f deployment.yaml
	@echo "Applying k8s deployment..."
	kubectl get pods

#=========================================================
# LOCAL DEV kubernetes ENV SETUP commands
#=========================================================

kind-deps: deps ## makes sure that project-related system tools are installed (ex. kind, kubectl etc.)
	@kind --version || (echo "kind tool is NOT installed on your local machine" && false)
	@kubectl > /dev/null || (echo "kubectl tool is NOT installed on your local machine" && false)

#---------------------------------
# kind-based commands
#---------------------------------

create-kind-cluster: kind-deps ## creates kind-based k8s claster for local development
	kind create cluster --name $(PROJECT) --config ./kind_config.yaml
	kubectl get nodes
	touch $@

delete-kind-cluster: kind-deps ## deletes local kind-based k8s cluster
	kind delete cluster --name $(PROJECT)

#---------------------------------
# local-docker-registry-based commands
#---------------------------------
run-local-docker-registry: deps ## runs docker container containing local docker registry (if it is not running already)
	docker start local-docker-registry 2> /dev/null || docker run --name $(DOCKER_REG_CONTAINER) -d --restart=always -p $(DOCKER_REG_PORT):5000 registry:2
	touch $@

connect-registry-to-kind-network: deps ## connects local-docker-registry to 'kind' docker network
	@docker network connect kind $(DOCKER_REG_CONTAINER) 2> /dev/null || true

connect-registry-to-kind: deps connect-registry-to-kind-network ## connects local-docker-registry to kind-based cluster
	kubectl apply -f ./kind_configmap.yaml

delete-local-docker-registry: ## delete locally running docker registry
	docker rm -f $(DOCKER_REG_CONTAINER)

#---------------------------------
#  compounded dev commands
#---------------------------------

run-full-k8s-env: create-kind-cluster run-local-docker-registry connect-registry-to-kind-network connect-registry-to-kind ## generates ALL local resources related to k8s deployment

dist-clean: delete-local-docker-registry delete-kind-cluster clean ## delete all project-related docker images, docker containers (including local kind k8s cluster and local docker registry)
