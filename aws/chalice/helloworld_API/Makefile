
all: deploy test

deploy:
	chalice deploy

test:
	http $(shell chalice url)

destroy: 
	chalice delete

