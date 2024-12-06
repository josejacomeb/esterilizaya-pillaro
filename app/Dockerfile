# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.12-alpine AS builder
EXPOSE 8000
WORKDIR /esterilizaya
COPY requirements.txt /esterilizaya
RUN apk add --no-cache --virtual build-deps gcc=~13 musl-dev=~1 libffi-dev=~3 pkgconf=~2 mariadb-dev=~10 && \
  pip install --no-cache-dir -r requirements.txt && \
  apk del build-deps

FROM --platform=$BUILDPLATFORM python:3.12-alpine AS prod
WORKDIR /home/esterilizaya/code
RUN apk add --no-cache curl=~8 mariadb-connector-c-dev=~3 weasyprint=~62
RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash -S esterilizaya --ingroup docker vscode
EOF

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY ./ ./
# Crear los directorios iniciales
RUN mkdir -p /home/esterilizaya/code/media
# Cambiar los permisos de los archivos copiados
RUN chown -R esterilizaya:docker /home/esterilizaya/code
HEALTHCHECK --interval=5m --timeout=3s \
CMD curl -f http://localhost:8000/ || exit 1
#USER esterilizaya TODO: Arreglar los permisos
