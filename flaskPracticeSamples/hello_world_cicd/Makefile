#
# Makefile

include .env

all: run

run: all_checks start

clean: stop

#==========================================================================
# Development Environtmen creating
env:
	pyenv install -s 3.6.0
	pyenv virtualenv 3.6.0 ${APP_NAME}

#==========================================================================
# Run/Stop app in docker containers
start: build
	docker-compose up -d 

#build app's docker image
build:
	docker-compose build

stop:
	docker-compose down


#==========================================================================
# Test and verify quality of the app
test: 
	python -m unittest discover ${TEST_DIR}

coverage:
	coverage run --source ${APP_NAME} --branch -m unittest discover -v 
	coverage report -m
	coverage html

lint:
	pylint ${APP_NAME}

security:
	bandit ${APP_NAME}

all_checks: lint security test coverage

docker-all-checks: build
	docker exec -it ${APP_NAME} make all_checks

