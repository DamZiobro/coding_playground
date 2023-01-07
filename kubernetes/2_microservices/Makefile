NAMESPACE=thoughts

run-k8s-cluster:
	# Run k8s cluster in minikube if not started already
	minikube status | grep -q "Running" || minikube start
	# Build docker images inside minikube
	eval $(minikube docker-env)

build:
	# build docker images for microservices
	make -C thoughts_backend build
	make -C users_backend build
	make -C frontend build

local-deploy: build
	# deploy microservices using kubernetes
	make -C thoughts_backend local-deploy
	make -C users_backend local-deploy
	make -C frontend local-deploy

delete-local-deploy:
	# deploy microservices kubernetes-based deployment
	make -C thoughts_backend delete-local-deploy
	make -C users_backend delete-local-deploy
	make -C frontend delete-local-deploy

local-deploy-status:
	# deploy kubernetes deployment status
	@echo "============== K8S DEPLOYMENTS ==================="
	kubectl get deployments -n $(NAMESPACE)
	@echo "============== K8S PODS ==================="
	kubectl get pods -n $(NAMESPACE)
	@echo "============== K8S SERVICES ==================="
	kubectl get service -n $(NAMESPACE)
	@echo "============== K8S INGRESSES ==================="
	kubectl get ingress -n $(NAMESPACE)
