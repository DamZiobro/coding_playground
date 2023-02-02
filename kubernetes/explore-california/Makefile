
PROJECT=explorecalifornia.com

#=========================================================
# LCOAL DEV docker commands
#=========================================================
build:
	docker build -t $(PROJECT) .

run:
	docker run -d --name $(PROJECT) -p 5000:80 $(PROJECT)

build-run: build run

#=========================================================
# LOCAL DEV kubernetes commands
#=========================================================

install_kind:
	curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
	sudo install -o root -g root -m 0755 kind-linux-amd64 /usr/local/bin/kind
	touch $@

install_kubectl:
	curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
	sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
	touch $@

kind-deps:
	kind --version || make install_kind
	kubectl version || make install_kubectl

create-kind-cluster: kind-deps
	kind create cluster --name $(PROJECT)
	kubectl get nodes
	touch $@
