
PROJECT=explorecalifornia.com

#=========================================================
# LCOAL DEV docker commands
#=========================================================
deps:
	@docker --version || (echo "Install docker on your local machine" && false)

build: deps
	docker build -t $(PROJECT) .

run: deps
	docker run -d --name $(PROJECT) -p 5000:80 $(PROJECT)

build-run: build run

#=========================================================
# LOCAL DEV kubernetes commands
#=========================================================

install_kind:
	curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
	sudo install -o root -g root -m 0755 kind-linux-amd64 /usr/local/bin/kind && rm kind-linux-amd64
	touch $@

install_kubectl:
	curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
	sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && rm kubectl
	touch $@

kind-deps: deps
	kind --version || make install_kind
	kubectl version --short || make install_kubectl

create-kind-cluster: kind-deps
	kind create cluster --name $(PROJECT)
	kubectl get nodes
	touch $@

run-local-docker-registry: kind-deps
	# run docker container if it does not exist
	docker start local-docker-registry || docker run --name local-docker-registry -d --restart=always -p 5000:5000 registry:2
	touch $@
