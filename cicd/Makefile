
env:
	pyenv install -s 3.6.0
	pyenv virtualenv -f app


test:
	python -m unittest discover tests

coverage:
	coverage run --source app --branch -m unittest discover -v
	coverage report -m
	coverage html

