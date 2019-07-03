
CONFIG_FILE=ci/config

SHELL := /bin/bash 

include ${CONFIG_FILE}

CONCOURSE_TARGET=pipeline-${APP_NAME}
CONCOURSE_PLAN=plan-${APP_NAME}
CONCOURSE_JOB=job-${APP_NAME}

#==========================================================================
# Development Environtmen creating
env:
	pyenv install -s 3.6.0
	pyenv virtualenv -f ${APP_NAME}

#==========================================================================
# Run/Stop app in docker containers
start:
	cd ci/${APP_NAME} && docker-compose up -d 

build:
	cd ci/${APP_NAME} && docker-compose build

stop:
	cd ci/${APP_NAME} && docker-compose down


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

docker-all-checks:
	docker exec -it ${APP_DOCKER_CONTAINER} make all_checks

#==========================================================================
# Test and run
run-ci: ci-pipeline-run start
run-all: concourse-run run-ci
run-dev: all_checks start

#==========================================================================
# Clean container and pipeline
clean: ci-pipeline-destroy stop
clean-all: clean concourse-destroy


#==========================================================================
# Run Concourse-based CI environment

ci-pipeline-run: docker-registry-run
	fly -t ${CONCOURSE_TARGET} set-pipeline --non-interactive -c ci/concourse/pipeline.yml -p ${CONCOURSE_PLAN} \
		-v DOCKER_REGISTRY_ORIGIN=${DOCKER_REGISTRY_ORIGIN} \
		-v GIT_URL=${GIT_URL} \
		-v APP_NAME=${APP_NAME} \
	fly -t ${CONCOURSE_TARGET} unpause-pipeline -p ${CONCOURSE_PLAN}
	fly -t ${CONCOURSE_TARGET} trigger-job -w -j ${CONCOURSE_PLAN}/${CONCOURSE_JOB}

ci-pipeline-destroy: docker-registry-destroy
	fly -t ${CONCOURSE_TARGET} destroy-pipeline -p ${CONCOURSE_PLAN}

concourse-destroy:
	cd ci/concourse && docker-compose down

concourse-run:
	cd ci/concourse && docker-compose up -d
	fly --target ${CONCOURSE_TARGET} login --concourse-url ${CONCOURSE_URL} -u ${CONCOURSE_USER} -p ${CONCOURSE_PASS}
	fly --target ${CONCOURSE_TARGET} sync

#==========================================================================
# Run local Docker Registry which will cooperate with Concourse
docker-registry-run:
ifneq ($(shell docker inspect -f '{{.State.Running}}' ${DOCKER_REGISTRY_NAME}), true)
	docker run -d -p ${DOCKER_REGISTRY_PORT}:5000 --restart=always --name ${DOCKER_REGISTRY_NAME} registry:2
endif

docker-registry-destroy:
	docker rm -f ${DOCKER_REGISTRY_NAME}

