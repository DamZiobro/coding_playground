NAMESPACE=thoughts

create-namespace:
	kubectl create namespace $(NAMESPACE) --dry-run -o yaml > /tmp/namespace.yaml
	kubectl apply -f /tmp/namespace.yaml

build:
	docker-compose build

run:
	docker-compose up -d

deploy: build create-namespace
	kubectl apply -f kubernetes/deployment.yaml
	kubectl apply -f kubernetes/service.yaml
	kubectl apply -f kubernetes/ingress.yaml

delete-deploy:
	kubectl delete -f kubernetes/deployment.yaml
	kubectl delete -f kubernetes/service.yaml
	kubectl delete -f kubernetes/ingress.yaml

