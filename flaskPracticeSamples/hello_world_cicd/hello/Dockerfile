FROM python:3.6

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

WORKDIR "app"

CMD ./run.sh
