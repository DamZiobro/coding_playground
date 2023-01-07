run-k8s-cluster:
	# Run k8s cluster in minikube if not started already
	minikube status | grep -q "Running" || minikube start

run: run-k8s-cluster
	kubectl apply -f example_pod.yml
	kubectl get pods -n example -o wide #checking pods in namespace 'example'
