APP_NAME=xmementoit-k8s-development-website

APP_LOCAL_PORT=3000
DOCKER_REG_PORT=5000
DOCKER_REG_CONTAINER=local-docker-registry
DOCKER_REG_URL=localhost:$(DOCKER_REG_PORT)
DOCKER_IMAGE_NAME=
DOCKER_IMAGE_NAME=xmementoit-k8s-development.com

#=========================================================
# LCOAL DEV docker commands
#=========================================================

deps: ## verifies project-related dependency tools are up and running
	@docker --version || (echo "docker tool is NOT installed on your local machine" && false)

build: deps ## build project-related docker images
	docker build -t $(DOCKER_IMAGE_NAME) .

run: deps ## runs project-related docker container (build must be performed first)
	docker run -d --name $(DOCKER_IMAGE_NAME) -p $(APP_LOCAL_PORT):80 $(APP_NAME)
	echo "website is up-and-running on http://localhost:$(APP_LOCAL_PORT)"

stop: ## stops project-related docker containers (without deleting them)
	docker stop -d --name $(APP_NAME)

clean: ## delete project-related docker containers and docker images (does not delete any k8s-based deployed resources)
	docker rm -f $(APP_NAME)
	docker rmi -f $(DOCKER_IMAGE_NAME)


#=========================================================
# LOCAL DEV kubernetes DEV commands
#=========================================================

push: build ## pushes project-related docker images into local docker registry
	docker tag $(DOCKER_IMAGE_NAME) $(DOCKER_REG_URL)/$(DOCKER_IMAGE_NAME)
	docker push $(DOCKER_REG_URL)/$(DOCKER_IMAGE_NAME)

deploy: push kind-deps ## deploys project using k8s
	helm upgrade --atomic --install $(APP_NAME) ./helm

undeploy: kind-deps ## deletes project using k8s
	helm uninstall $(APP_NAME) || true
	
status-deploy: kind-deps ## show status of k8s deployment
	@echo "============== K8S DEPLOYMENTS ==================="
	helm status $(APP_NAME)
	kubectl get all -l app=$(APP_NAME)

#=========================================================
# LOCAL DEV kubernetes ENV SETUP commands
#=========================================================

kind-deps: deps ## makes sure that project-related system tools are installed (ex. kind, kubectl etc.)
	@kind --version || (echo "kind tool is NOT installed on your local machine" && false)
	@kubectl > /dev/null || (echo "kubectl tool is NOT installed on your local machine" && false)

helm-deps: deps ## make sure helm-related resources are in place
	@helm --version || (echo "helm tool is NOT installed on your local machine" && false)

#---------------------------------
# kind-based commands
#---------------------------------

create-kind-cluster: kind-deps ## creates kind-based k8s claster for local development
	kind create cluster --name $(APP_NAME) --config ./kind_config.yaml
	kubectl get nodes
	touch $@

delete-kind-cluster: kind-deps ## deletes local kind-based k8s cluster
	kind delete cluster --name $(APP_NAME)

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
# nginx-based ingress controller commands
#---------------------------------
run-ingress-controller: kind-deps ## install ingress nginx controller
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

delete-ingress-controller: kind-deps ## delete ingress nginx controller resources
	kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

status-ingress-controller: kind-deps ## get status of ingress-controller 
	kubectl get all -n ingress-nginx
#---------------------------------
#  compounded dev commands
#---------------------------------

run-full-k8s-env: create-kind-cluster run-local-docker-registry connect-registry-to-kind-network connect-registry-to-kind run-ingress-controller ## generates ALL local resources related to k8s deployment

dist-clean: undeploy delete-local-docker-registry delete-ingress-controller delete-kind-cluster clean ## delete all project-related docker images, docker containers (including local kind k8s cluster and local docker registry)
