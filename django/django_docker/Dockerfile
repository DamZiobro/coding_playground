FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev build-essential \
    && pip3 install django

CMD ["django-admin", "--version"]
