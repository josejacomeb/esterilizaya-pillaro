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
3. Descargue los contenedores con el siguiente commando: `docker compose build`.
Por favor ejecute las migraciones de la base de datos a través del siguiente comando: `docker compose -f docker-compose.yml -f docker-compose.migrate.yml up`.
4. Por favor, cree un nuevo superusuario del sistema, con el siguiente comando: `docker compose -f docker-compose.yml -f docker-compose.superuser.yml up`.
5. Inicie el sistema con `docker compose up -d --build`.