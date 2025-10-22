# Desarrollo

¡Gracias por contribuir al desarollo de Esteriliza-ya! Cualquier aportación de código es bienvenida con el fin de mejorar cada vez más este proyecto.

## Antes de contribuir

Si encontraste alguna [mejora requerida](https://github.com/josejacomeb/esterilizaya-pillaro/issues/) o alguna característica nueva, por favor abre una [feature branch](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches#working-with-branches) donde puedes añadir tu contribución.

## Formato de Código

Es necesario ajustarse al formato de código usado en el proyecto, éste se divide entre código de Python y del Frontend, mira cómo configurarlo en las siguientes subsecciones:

### Python

Crea un nuevo ambiente de Python e instala los formateadores con el siguiente

```bash
python -m venv .venv
source .venv/bin/activate
pip install black flake8 isort pylint
sudo chmod +x linters.sh
```

Puedes ejecutar todos los formateadores con el script `linters.sh` y especificando como argumento tu script de Python

```bash
./linters.sh app/carpeta/codigo.py
```

### Frontend

Instala `nodejs` junto las herramientas con `npm` y `npx`, por ejemplo en Ubuntu:

```bash
sudo apt update && sudo apt install nodejs
```

Instala los formateadores necesarios, por ejemplo en Ubuntu

```bash
npm install --save-dev --save-exact @biomejs/biome prettier
```

Puedes usar los formateadores de la siguiente forma

```bash
npx prettier --write DEVELOPMENT.md
npx biome format app/static/js/file.js
npx biome lint app/static/js/file.js
```

## Opciones de Desarrollo

Una vez que hayas construido los contenedores como describe la [Instalación](INSTALL.md), puedes iniciarlos en modo de desarrollo

```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d
```

Luego, podrás explorar las páginas del servidor en tu navegador en la dirección [http://localhost:8000/](http://localhost:8000/). Esta configuración activa la [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) y sincroniza tu código local con el Contenedor.

## Envia tus cambios

¡Felicidades! Si todo funciona bien en las configuraciones de producción y debug, puedes enviar iniciar una [Solicitud de cambios](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) y solicitar una revisión, una vez terminado el proceso finalmente habrás contribuido al proyecto.
