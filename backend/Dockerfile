FROM pypy:3.7

ENV PYTHONUNBUFFERED=1

WORKDIR /var/www/server

RUN set -ex \
    export DEBIAN_FRONTEND=noninteractive \
    ; apt-get update \
    ; apt-get install -y --no-install-recommends --allow-unauthenticated \
    libpq-dev \
    net-tools

COPY src/Makefile /var/www/server/Makefile
COPY src/requirements /var/www/server/requirements

ARG MODE
RUN make venv.create && \
    make venv.install mode="$MODE"