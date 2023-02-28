
terraform:
	terraform --version || (echo "ERROR: Please install terraform!" && false)
	terraform workspace new dev
	terraform workspace new prod
	terraform workspace select dev
	terraform workspace list
	touch $@

apply: terraform
	terraform apply -auto-approve

plan: terraform
	terraform plan

destroy: terraform
	terraform destroy -auto-approve

workspaces: terraform
	terraform workspace list

clean:
	rm -f main.zip terraform
