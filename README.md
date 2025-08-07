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

- Django
- MariaDB

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

3. Debido a que a veces el sistema no tendrá internet, es necesario descargar Boostrap >= 5 localmente para que todo el frontend funcione, es recomendable descargarlo de la página oficial con los siguientes comandos:

   ```bash
      BOOSTRAP_VERSION="5.3.7"
      wget -P app/static https://github.com/twbs/bootstrap/releases/download/v$BOOSTRAP_VERSION/bootstrap-$BOOSTRAP_VERSION-dist.zip
      mkdir -p app/static/temp_bootstrap
      unzip app/static/bootstrap-$BOOSTRAP_VERSION-dist.zip -d app/static/temp_bootstrap
      mkdir -p app/static/js && mv app/static/temp_bootstrap/bootstrap-$BOOSTRAP_VERSION-dist/js/* app/static/js
      mkdir -p app/static/css && mv app/static/temp_bootstrap/bootstrap-$BOOSTRAP_VERSION-dist/css/* app/static/css
      rm -rf app/static/temp_bootstrap
      rm app/static/bootstrap-$BOOSTRAP_VERSION-dist.zip
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

### Correr el servidor en una red local

En caso no tengas acceso a internet, debes hacer una configuración adicional para acceder al servidor, por ejemplo puedes consultar tu dirección de Red en Linux con `ip addr show _remplazar_dispositivo_red_`, luego:

1. Añade la IP donde corre el servidor local al `app/esterilizaya/settings/prod.py`

   ```bash
   ALLOWED_HOSTS = ["happypawspillaro.org", "www.happypawspillaro.org", "192.168.1.101"]
   ```

2. Añade la IP para que NGINX `config/nginx/default.conf.template`

   ```apacheconf
   server {
      listen              80;
      server_name         www.happypawspillaro.org happypawspillaro.org 192.168.1.101;
   ```

### Guardar datos

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
