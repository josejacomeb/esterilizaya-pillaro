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

- [Docker](https://www.docker.com/get-started/) >= 28.x
- [Django](https://www.djangoproject.com/) >= 5.x
- [MariaDB](https://mariadb.org/) >= 11.x
- [Bootstrap](https://getbootstrap.com/) >= 5.x
- [boostrap-autocomplete](https://bootstrap-autocomplete.readthedocs.io/en/latest/) >= 2.x
- [jQuery](https://jquery.com/) >= v3.x
- [WeasyPrint](https://weasyprint.org/) >= v63.x
- [watchfiles](https://github.com/samuelcolvin/watchfiles) >= v1.x
- [Chart.js](https://www.chartjs.org/) >= 4.5.x
- [Leaflet](https://leafletjs.com/) >= 1.9.x
- [easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails) >=2.x

## Instalación

Por favor, siga las instrucciones en el Archivo de [Instalación](INSTALL.md)

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

1. Respalda el volumen que contiene la base de datos con el siguiente comando
   `docker run --rm -v esterilizaya-pillaro_maria-db:/data -v $(pwd):/backup alpine tar czf /backup/mariadb_volume_backup.tar.gz -C /data .`
2. Respalda el volumen que contiene las imágenes a través del comando.
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

## Desarrollo

Si quieres contribuir al proyecto, por favor revisa las instrucciones en el archivo [DEVELOPMENT.md](DEVELOPMENT.md)
