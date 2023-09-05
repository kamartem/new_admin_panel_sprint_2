ARG BUILD_IMAGE=3.11-buster
ARG BASE_IMAGE=3.11-slim-buster

# modules
FROM python:${BUILD_IMAGE} as modules
WORKDIR /wheels
COPY ./src/requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache --mount=type=cache,target=/pkg pip install -U pip && pip wheel -r requirements.txt -w /pkg

### builder
FROM python:${BASE_IMAGE} as builder
RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    gettext \
    # pg_isready
    postgresql-client \
  && apt-get purge -y --auto-remove \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

COPY --from=modules /wheels /wheels
RUN --mount=type=cache,target=/pkg pip install -U pip \
       && pip install --no-index -r /wheels/requirements.txt -f /pkg \
       && rm -rf /wheels \
       && rm -rf /root/.cache/pip/*

### dev build
FROM builder as dev

ARG APP_DIR
WORKDIR ${APP_DIR}

COPY ./docker/entrypoint.sh /entrypoint.sh

# Setting up proper permissions:
RUN chmod +x '/entrypoint.sh' \
  && groupadd -r web && useradd -d ${APP_DIR} -r -g web web \
  && chown web:web -R ${APP_DIR} \
  && mkdir -p /opt/static /opt/media \
  && chown web:web /opt/static /opt/media

# Running as non-root user:
USER web

EXPOSE 8080
ENTRYPOINT ["/entrypoint.sh"]

### prod build
FROM dev AS prod
COPY --chown=web:web ./src ./
