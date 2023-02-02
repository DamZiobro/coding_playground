NAMESPACE=mongo-app

create-namespace: ## create namespace if does not exist
	kubectl create namespace $(NAMESPACE) --dry-run -o yaml > /tmp/namespace.yaml
	kubectl apply -f /tmp/namespace.yaml
	touch $@

init: create-namespace ## initialize project deps: k8s secrets etc.
	@echo "System dependencies: kubectl"
	@echo " --> Initialize k8s secrets"
	kubectl apply -f k8s/secret.yaml -n $(NAMESPACE)
	@echo " --> Initialize k8s ConfigMaps"
	kubectl apply -f k8s/config.yaml -n $(NAMESPACE)
	touch $@

deploy: init ## deploy the k8s stack to the default cluster
	@echo " --> Deploying ALL microservices..."
	make -C mongodb deploy
	make -C mongo-express deploy

clean-deployment: init ## deploy the k8s stack to the default cluster
	@echo " --> Deploying ALL microservices..."
	make -C mongodb clean-deployment
	make -C mongo-express clean-deployment
