FROM apache/airflow:2.3.3-python3.9
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow

COPY --chown=airflow:root test_dag.py /opt/airflow/dags
