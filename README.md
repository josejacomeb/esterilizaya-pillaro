# esterilizaya-pillaro

[![Super-Linter](https://github.com/josejacomeb/esterilizaya-pillaro/actions/workflows/super-linter-slim.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)

Sistema de Gestión para automatizar las tareas de Esterilización de Bajo Costo en Píllaro - Tungurahua, Ecuador
 ![Esterilizaya!](/docs/images/Esteriliza-ya.png)

## Características

Destinado a funcionar en lugares *sin conexión* a internet, sólo necesitas una laptop que haga de servidor, una impresora y conectar a los voluntarios a la red del servidor.

* 📝 Gestionar inscripciones, registros incluso con fotos desde tu celular
* 🛠️ Generar fichas, carnets, recetas listas para imprimir instantáneamente
* 🥼🐾 Provee datos de las mascotas a los veterinarios en tiempo real
* 📊 Genera estadísticas de tenencia con varios filtros a elección
* 🗃️ Genera un catastro digital de mascotas

## Herramientas Software

* [Docker](https://www.docker.com/get-started/) >= 28.x
* [Django](https://www.djangoproject.com/) >= 5.x
* [MariaDB](https://mariadb.org/) >= 11.x
* [Bootstrap](https://getbootstrap.com/) >= 5.x
* [boostrap-autocomplete](https://bootstrap-autocomplete.readthedocs.io/en/latest/) >= 2.x
* [jQuery](https://jquery.com/) >= v3.x
* [WeasyPrint](https://weasyprint.org/) >= v63.x
* [watchfiles](https://github.com/samuelcolvin/watchfiles) >= v1.x
* [Chart.js](https://www.chartjs.org/) >= 4.5.x
* [Leaflet](https://leafletjs.com/) >= 1.9.x
* [easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails) >=2.x

## Instalación

Por favor, siga las instrucciones en el Archivo de [Instalación](INSTALL.md)

## Servidor de forma local

En caso de no tener una red Wifi, considera hacer un *hotspot* desde tu servidor hacia los dispositivos de tus voluntarios, luego sigue las instrucciones:

### Configuraciones Django

En caso no tengas acceso a internet, debes hacer una configuración adicional para acceder al servidor, por ejemplo puedes consultar tu dirección de Red en Linux con `ip addr show _remplazar_dispositivo_red_`, luego:

1. Añade el `hostname` y el IP de tu servidor en tu archivo `.env`

   ```bash
   # URLs para correr localmente
   APP_URL=www.happypawspillaro.org # Hostname como lo configuraste en tu archivo /etc/hosts
   LOCAL_URL=192.168.1.100 # IP local de tu servidor en la red
   ```

2. Haz efectiva tu configuración al reiniciar los contenedores con el comando

   ```bash
   docker compose -f docker-compose.yml -f docker-compose.prod.yml restart
   ```

### Impresiones automáticas

Si la computadora donde corre este servidor tiene una impresora conectada, la puedes configurar en Linux para imprimir las fichas automáticamente.

Para saber cómo hacerlo por favor Instrucciones [Impresion Automática](impresion-automatica/README.md)

## Happy Paws Píllaro

¿Deseas saber más o como contribuir? ¡Síguenos! Si te gusta nuestro trabajo, por favor considera hacer una donación.

| Facebook                                                                         | Instagram                                                          | TikTok                                                            | Youtube                                                                  |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------------|
| [Happy Paws Píllaro]( https://www.facebook.com/profile.php?id=61550626997105 ) | [@happypaws.pillaro](https://www.instagram.com/happypaws.pillaro/) | [@happypaws.pillaro]( https://www.tiktok.com/@happypaws.pillaro ) | [Happy Paws Píllaro]( https://www.youtube.com/@HappyPawsP%C3%ADllaro ) |

![Happy Paws Píllaro](app/static/images/happypaws.png)

## Desarrollo

Si quieres contribuir al proyecto, por favor revisa las instrucciones en el archivo [DEVELOPMENT.md](DEVELOPMENT.md)
