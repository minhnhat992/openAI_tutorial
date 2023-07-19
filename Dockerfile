FROM ubuntu:latest
LABEL authors="minhbui"

FROM amd64/python:3.9.9-slim AS stage_0
# Env vars
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV GOOGLE_APPLICATION_CREDENTIALS=/usr/credentials/wc-data-consolidated-gcs-user.json

FROM stage_0 AS set_up
RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get install -y --no-install-recommends \
    git \
  && apt-get clean \
  && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/*

FROM set_up AS install_dependencies
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

FROM install_dependencies AS move_files
COPY .env .env
COPY script /home/script
COPY data /home/data
