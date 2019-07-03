
Create development environment
---------
Create pyenv-based dev environment
```
make env
```

Install requirements:
```
pyenv activate app
pip install -r app/requirements.txt
```

Test and run app
---------
```
make run
```

Start/stop app in docker containers
---------
Start app in docker containers
```
make start
```
Stop app in docker containers
```
make stop
```
Rebuild docker container
```
make build
```

Run quality verifiers (unit tests, coverage, linter, security checks)
---------
Run all quality checks
```
make all_checks
```

Run unit tests
```
make test
```

Run unit tests and see code coverage
```
make coverage
```

Run linter
```
make lint
```

Run security check
```
make security
```
