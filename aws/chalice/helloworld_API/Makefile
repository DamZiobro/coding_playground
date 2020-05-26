
all: deploy test

deploy:
	chalice deploy

test:
	http $(shell chalice url)
	http $(shell chalice url)/cities/Leeds

destroy: 
	chalice delete

logs:
	chalice logs

