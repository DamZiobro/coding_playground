#
# Makefile
# damian, 2021-06-02 13:21
#

install-requirements:
	pip install -r requirements.txt
	touch $@

run: install-requirements
	FLASK_RUN_PORT=80 FLASK_ENV=development FLASK_APP=app.py authbind --deep flask run


