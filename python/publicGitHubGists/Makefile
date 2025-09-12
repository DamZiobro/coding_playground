# virtualenv-based tools to install deps and run script inside automatically created virtualenv
VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PYTEST := $(VENV)/bin/pytest

.venv: ## create virtual env (idempotent)
	@echo "---> Creating the virtualenv"
	python -m venv $(VENV)

.deps: .venv ## install dependencies into the virtualenv  (idempotent)
	@echo "---> Installing python deps inside virtualenv"
	$(PIP) install -r requirements.txt
	@touch $@ #create the .deps file to make command idempotent 

run: .venv .deps ## run the scripts for getting public gists (venv will be created and deps installed automatically)
	@$(PYTHON) get_public_gists.py $(GITHUB_USER)

test: .venv .deps ## run unit tests
	@$(PYTEST) tests_get_public_gists.py

clean: ## clean the virtualenv and start from scratch
	@echo "---> Cleaning the virtualenv and deps"
	rm -rf $(VENV) .deps recent_run_file.txt __pycache__ .pytest_cache
