FROM python:3.7-alpine

MAINTAINER Damian Ziobro <damian@xmementoit.com>

WORKDIR /code

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["flask", "run"]
