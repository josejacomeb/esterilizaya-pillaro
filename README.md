# esterilizaya-pillaro

[![Super-Linter](https://github.com/josejacomeb/esterilizaya-pillaro/actions/workflows/super-linter-slim.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)

Sistema de Gestión para automatizar las tareas de Esterilización de Bajo Costo en Píllaro - Tungurahua, Ecuador

## Participantes

<a href="https://www.facebook.com/profile.php?id=61558304577721"><img align="left" src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Color/Facebook.svg" alt="Barrio Yacupamba | Facebook" height="21px"/></a>
<a href="https://www.instagram.com/yacupamba/"><img align="left" src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Color/Instagram.svg" alt="Barrio Yacupamba | Instagram" height="21px"/></a>
<a href="https://www.tiktok.com/@yacupamba"><img align="left" src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Color/Tik%20Tok.svg" alt="Yacupamba | Tiktok" height="21px"/></a>
<a href="https://instagram.com/yushi.95"><img align="left" src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Color/Youtube.svg" alt="Yu Shi | Instagram" height="21px"/></a>
</br>

- Barrio Yacupamba

<a href="https://www.facebook.com/veterinaria.animal.zoo"><img align="left" src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Color/Facebook.svg" alt="Veterinaria Animal-Zoo | Facebook" height="21px"/></a>
<a href="https://maps.app.goo.gl/B391JtNhJMbuY78J9"><img align="left" src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Google_Maps_icon_%282020%29.svg" alt="Veterinaria Animal-Zoo Píllaro | Google Maps" height="21px"/></a>
</br>

- Veterinaria AnimalZoo

<a href="https://www.facebook.com/profile.php?id=61550626997105"><img align="left" src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Color/Facebook.svg" alt="Happy Paws Píllaro | Facebook" height="21px"/></a>
<a href="https://www.instagram.com/happypaws.pillaro/"><img align="left" src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Color/Instagram.svg" alt="Happy Paws Píllar | Instagram" height="21px"/></a>
</br>

- Happy Paws Píllaro

## Herramientas Software

- [Django](https://www.djangoproject.com/) >= 5.x
- [MariaDB](https://mariadb.org/) >= 11.x
- [Bootstrap](https://getbootstrap.com/) >= 5.x
- [boostrap-autocomplete](https://bootstrap-autocomplete.readthedocs.io/en/latest/) >= 2.x
- [jQuery](https://jquery.com/) >= v3.x
- [WeasyPrint](https://weasyprint.org/) >= v63.x
- [watchfiles](https://github.com/samuelcolvin/watchfiles) >= v1.x
- [Chart.js](https://www.chartjs.org/) >= 4.5.x
- [Leaflet](https://leafletjs.com/) >= 1.9.x

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

## Servidor de forma local

Estas instrucciones pueden servir cuando se genere una campaña en un lugar que no tenga acceso de internet.

### Configuraciones Django

En caso no tengas acceso a internet, debes hacer una configuración adicional para acceder al servidor, por ejemplo puedes consultar tu dirección de Red en Linux con `ip addr show _remplazar_dispositivo_red_`, luego:

1. Añade el `hostname` y el IP en tu archivo `.env`

   ```bash
   # URLs para correr localmente
   APP_URL=www.happypawspillaro.org # Hostname como lo configuraste en tu archivo /etc/hosts
   LOCAL_URL=192.168.1.100 # IP local de tu adaptador de red
   ```

### Impresiones automáticas

Si la computadora donde corre este servidor tiene una impresora conectada, la puedes configurar en Linux para imprimir las fichas automáticamente.

Para saber cómo hacerlo por favor Instrucciones [Impresion Automática](impresion-automatica/README.md)

## Generación respaldos

### Exportar datos crudos

Para exportar los datos de las esterilizaciones, por favor use: `python manage.py  dumpdata --exclude auth.permission > Xda_campana.json`

### Respaldo de datos y contenedores

Se puede hacer el respaldo de los contenedores a través de estos comandos:

#### Respaldo

1. Reemplaza el campo `<rootpassword>` con tu contraseña de usuario `root`
   `docker exec -i esterilizaya-pillaro-db-1 mariadb-dump -u root -p~RXPf@hi^3%5ns7FtcF7 --all-databases > backup.sql`
2. Respalda el volumen que contiene la base de datos con el siguiente comando
   `docker run --rm -v esterilizaya-pillaro_maria-db:/data -v $(pwd):/backup alpine tar czf /backup/mariadb_volume_backup.tar.gz -C /data .`
3. Respalda el volumen que contiene las imágenes a través del comando.
   `docker run --rm -v esterilizaya-pillaro_media-volume:/data -v $(pwd):/backup alpine tar czf /backup/django_media_backup.tar.gz -C /data .`

##### Restaurar

1. Copia los contenedores generados anteriormente a la ruta donde está el archivo `docker-compose.yml`

2. Para los contenedores y móntalos nuevamente, si es necesario iniciar de cero, bórralos.

   ```bash
   docker compose down
   docker run --rm -v esterilizaya-pillaro_maria-db:/data -v $(pwd):/backup alpine tar xzf /backup/mariadb_volume_backup.tar.gz -C /data
   docker run --rm -v esterilizaya-pillaro_media-volume:/data -v $(pwd):/backup alpine tar xzf /backup/django_media_backup.tar.gz -C /data
   ```

3. Crea de nuevo el contenedor de la base de datos e inicializa nuevamente el mismo con:

   ```bash
   docker compose up -d db
   cat backup.sql | docker exec -i esterilizaya-pillaro-db-1 mariadb -u root -p<rootpassword>
   ```

4. Inicializa normalmente los contenedores.
   `docker-compose up -d`

_Nota_: Puede salir un mensaje de alerta que el volumen no ha sido creador por docker-compose, al final seguirá funcionando el programa.
