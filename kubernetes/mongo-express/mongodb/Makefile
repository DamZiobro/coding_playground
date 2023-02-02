NAMESPACE=mongo-app

deploy: ## deploy the k8s stack to the default cluster
	@echo " --> Deploying k8s for $(shell basename)..."
	kubectl apply -f k8s/deployment.yaml -n $(NAMESPACE)
	kubectl apply -f k8s/service.yaml -n $(NAMESPACE)

clean-deployment: ## deploy the k8s stack to the default cluster
	@echo " --> DELETING k8s for $(shell basename)..."
	kubectl delete -f k8s/service.yaml -n $(NAMESPACE)
	kubectl delete -f k8s/deployment.yaml -n $(NAMESPACE)
