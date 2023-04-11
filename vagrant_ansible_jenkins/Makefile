
up: ## runs vagrant VMs
	vagrant up	

stop: ## stops vagrant VMs
	vagrant halt 

clean: ## destroy vagrant VMs
	vagrant destroy -f

dist-clean: clean ## destroy vagrant VMs and remove .vagrant state dir
	vagrant destroy -f
	rm -rf .vagrant

reload: ## restart vagrant VM with re-provisioning
	vagrant reload --provision-with ansible

config: ## reprovision vagrant VM
	vagrant provision --provision-with ansible

