FROM python:3.7.16-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /var/www/server

RUN set -ex \
    export DEBIAN_FRONTEND=noninteractive \
    ; apt-get update \
    ; apt-get install -y --no-install-recommends --allow-unauthenticated \
    make \
    libpq-dev

COPY src/Makefile /var/www/server/Makefile
COPY src/requirements /var/www/server/requirements

ARG MODE
RUN make venv.create && \
    make venv.install mode="$MODE"