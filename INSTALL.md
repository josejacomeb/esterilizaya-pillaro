# Instalación
## Prerequisitos
1. Por favor, sigue las instrucciones de [instalación](https://docs.docker.com/engine/install/) de Docker
2. Configura Docker para que corra em modo [rootless](https://docs.docker.com/engine/security/rootless/#install)

## Instrucciones
1. Por favor, copie las variables de entorno para iniciar el sistema `cp .env.example .env`, luego se pueden cambiar a discreción
2. Cree los archivos con la información sensible en la carpeta `credenciales`, por ejemplo en Linux:

   ```bash
       mkdir credenciales & mkdir credenciales/database
       echo ejemplo_contraseña_root_secreto > credenciales/database/root_password.txt
       echo ejemplo_contraseña_user_secreto > credenciales/database/user_password.txt
       echo ejemplo_contraseña_admin > credenciales/database/admin_password.txt
       mkdir credenciales/superuser
       echo ejemplo_contraseña_superuser > credenciales/superuser/password.txt

   ```

3. Debido a que a veces el sistema no tendrá internet, es necesario descargar `bootstrap` >= 5 y `bootstrap-autocomplete` localmente para que todo el frontend funcione, es recomendable descargarlo de la página oficial con los siguientes comandos:

   ```bash
      # Descarga Bootstrap
      BOOTSTRAP_VERSION="5.3.7"
      wget -P app/static https://github.com/twbs/bootstrap/releases/download/v$BOOTSTRAP_VERSION/bootstrap-$BOOTSTRAP_VERSION-dist.zip
      mkdir -p app/static/temp_bootstrap
      unzip app/static/bootstrap-$BOOTSTRAP_VERSION-dist.zip -d app/static/temp_bootstrap
      mkdir -p app/static/js && mv app/static/temp_bootstrap/bootstrap-$BOOTSTRAP_VERSION-dist/js/* app/static/js
      mkdir -p app/static/css && mv app/static/temp_bootstrap/bootstrap-$BOOTSTRAP_VERSION-dist/css/* app/static/css
      rm -rf app/static/temp_bootstrap
      rm app/static/bootstrap-$BOOTSTRAP_VERSION-dist.zip
      # Descarga Bootstrap Icons
      BOOTSTRAP_ICONS_VERSION="1.13.1"
      wget -P app/static/css https://cdn.jsdelivr.net/npm/bootstrap-icons@$BOOTSTRAP_ICONS_VERSION/font/bootstrap-icons.min.css
      wget -P app/static/css/fonts https://cdn.jsdelivr.net/npm/bootstrap-icons@$BOOTSTRAP_ICONS_VERSION/font/fonts/bootstrap-icons.woff
      wget -P app/static/css/fonts https://cdn.jsdelivr.net/npm/bootstrap-icons@$BOOTSTRAP_ICONS_VERSION/font/fonts/bootstrap-icons.woff2
      # Descarga boostrap-autocomplete
      wget -P app/static/js/ https://cdn.jsdelivr.net/gh/lekoala/bootstrap5-autocomplete@master/autocomplete.js
      # Descarga jQuery
      JQUERY_VERSION="3.7.1"
      wget https://code.jquery.com/jquery-$JQUERY_VERSION.min.js -O app/static/js/jquery.min.js
      # Descargar Chart.js
      CHART_JS_VERSION="4.5.0"
      wget https://cdnjs.cloudflare.com/ajax/libs/Chart.js/$CHART_JS_VERSION/chart.umd.min.js -O app/static/js/chart.umd.min.js
      wget https://cdnjs.cloudflare.com/ajax/libs/Chart.js/$CHART_JS_VERSION/chart.umd.js.map -O app/static/js/chart.umd.js.map
      # Descargar Leaflet
      LEAFLET_VERSION="1.9.4"
      wget -P app/static/css https://unpkg.com/leaflet@$LEAFLET_VERSION/dist/leaflet.css
      wget -P app/static/js https://unpkg.com/leaflet@$LEAFLET_VERSION/dist/leaflet.js
      wget -P app/static/images https://unpkg.com/leaflet@$LEAFLET_VERSION/dist/images/marker-icon.png
      wget -P app/static/images https://unpkg.com/leaflet@$LEAFLET_VERSION/dist/images/marker-shadow.png
   ```

4. Descargue los contenedores con el siguiente comando: `docker compose build`.
   Por favor ejecute las migraciones de la base de datos a través del siguiente comando: `docker compose -f docker-compose.yml -f docker-compose.migrate.yml up`.
5. Por favor, cree un nuevo superusuario del sistema, con el siguiente comando: `docker compose -f docker-compose.yml -f docker-compose.superuser.yml up`.
6. Inicie el sistema con `docker compose up -d --build`, con el cual por defecto se podrá iniciar el desarrollo.

### Configuración servidor local de producción en Linux

1. Para poder usar un dominio reconocible, por favor añadir en tu archivo `/etc/hosts` la siguiente línea:

   ```text
   127.0.0.1 happypawspillaro.org www.happypawspillaro.org
   ```

2. Crea una nueva carpeta en `mkdir app/ssl` y genera el certificado SSL

   ```bash
   mkdir app/ssl/
   openssl req -x509 -newkey rsa:2048 -sha256 -days 3650 -nodes \
       -keyout app/ssl/happypaws.key -out app/ssl/happypaws.crt \
       -subj '/CN=*.happypawspillaro.org' \
       -addext 'subjectAltName=DNS:*.happypawspillaro.org'
   ```

3. Por favor cambia los permisos de tu carpeta de código, en Alpine Linux, el usuario y grupo `www-data` es diferente al de Debian/Ubuntu, en tal caso, usa la siguiente línea para modificar los permisos:

   ```bash
   sudo chown -R 82:82 app/
   ```

4. Inicie el servidor de producción con el siguiente comando

   ```bash
      docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
   ```

5. Colecciona los archivos estáticos de tu directorio con el siguiente comando

   ```bash
   docker compose exec web python /home/esterilizaya/code/manage.py collectstatic
   ```

## Preguntas frecuentes
### Cambiar permisos de los volumenes
En caso de que no tengas permiso donde `100` es el user ID y `82` es el group ID del contenedor web.
```bash
  docker run --rm \
    -v esterilizaya-pillaro_media-volume:/data \
    alpine \
    chown -R 100:82 /data
```
