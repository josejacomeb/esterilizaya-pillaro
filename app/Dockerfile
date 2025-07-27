# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.12-alpine AS builder
EXPOSE 8000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /esterilizaya
COPY ./app/requirements.txt /esterilizaya
RUN apk add --no-cache --virtual build-deps gcc=~14 musl-dev=~1 libffi-dev=~3 pkgconf=~2 mariadb-dev=~11 && \
  pip install --no-cache-dir -r requirements.txt && \
  apk del build-deps

FROM --platform=$BUILDPLATFORM python:3.12-alpine AS prod
WORKDIR /home/esterilizaya/code
RUN apk add --no-cache curl=~8 mariadb-connector-c-dev=~3 weasyprint=~64
RUN adduser -S -G www-data www-data
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/
COPY ./app/ ./
COPY ./config/uwsgi/uwsgi.ini /home/esterilizaya/config/uwsgi/uwsgi.ini
# Crear los directorios iniciales
RUN mkdir -p /home/esterilizaya/code/media
# Cambiar los permisos de los archivos copiados
RUN chown -R www-data:www-data /home/esterilizaya/code /home/esterilizaya/code/media
USER www-data
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:8000/ || exit 1
