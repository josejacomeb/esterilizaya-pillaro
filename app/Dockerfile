# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.11-alpine AS builder
EXPOSE 8000
WORKDIR /esterilizaya 
COPY requirements.txt /esterilizaya
RUN apk add --no-cache --virtual build-deps gcc=13.2.1_git20240309-r0 musl-dev=1.2.5-r0 libffi-dev=3.4.6-r0 pkgconf=2.2.0-r0 mariadb-dev=10.11.8-r0 && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-deps

FROM --platform=$BUILDPLATFORM python:3.11-alpine AS prod
WORKDIR /home/esterilizaya/code
RUN apk add --no-cache curl=8.10.1-r0  mariadb-connector-c-dev=3.3.10-r0
RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash -S esterilizaya --ingroup docker vscode
EOF

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY ./ ./
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:8000/ || exit 1
USER esterilizaya