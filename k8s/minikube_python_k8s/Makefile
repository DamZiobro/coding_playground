
DOCKER_REGISTRY=localhost:5000
IMAGE_VERSION=1.0
DOCKER_IMAGE=hello-world-api:$(IMAGE_VERSION)
DOCKER_CONT=hello-world-api

build: ## build docker image for the API
	eval $(minikube docker-env) && \
	docker build -t $(DOCKER_IMAGE) .

run-local: ## run local docker container for the API
	docker run -d --name $(DOCKER_IMAGE) -p 8000:80 $(DOCKER_IMAGE)

clean-local: ## clean local api
	docker rm -f $(DOCKER_IMAGE)
	docker rmi -f $(DOCKER_IMAGE)

push: build ## push docker image into docker registry
	eval $(minikube docker-env) && \
	docker tag $(DOCKER_IMAGE) $(DOCKER_REGISTRY)/$(DOCKER_IMAGE) && \
	docker push $(DOCKER_REGISTRY)/$(DOCKER_IMAGE)

deploy: ## deploy app using k8s - deployment and service
	eval $(minikube docker-env) && \
	kubectl apply -f k8s/deployment.yaml
	kubectl apply -f k8s/service.yaml
	kubectl apply -f k8s/ingress.yaml

destroy: ## remove k8s resources
	eval $(minikube docker-env) && \
	kubectl delete deploy hello-world-api && \
	kubectl delete service hello-world-api && \
	kubectl delete ingress hello-world-api

