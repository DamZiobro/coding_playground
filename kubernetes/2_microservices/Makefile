NAMESPACE=thoughts

run-k8s-cluster:
	# Run k8s cluster in minikube if not started already
	minikube status | grep -q "Running" || minikube start
	# Build docker images inside minikube
	eval $(minikube docker-env)

build:
	make -C thoughts_backend build
	make -C users_backend build
	make -C frontend build

deploy: build
	make -C thoughts_backend deploy
	make -C users_backend deploy
	make -C frontend deploy

delete-deploy:
	make -C thoughts_backend delete-deploy
	make -C users_backend delete-deploy
	make -C frontend delete-deploy

deploy-status:
	@echo "============== K8S DEPLOYMENTS ==================="
	kubectl get deployments -n $(NAMESPACE)
	@echo "============== K8S PODS ==================="
	kubectl get pods -n $(NAMESPACE)
	@echo "============== K8S SERVICES ==================="
	kubectl get service -n $(NAMESPACE)
	@echo "============== K8S INGRESSES ==================="
	kubectl get ingress -n $(NAMESPACE)
