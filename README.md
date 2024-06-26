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
- `cp .env.example .env`
- Cree los archivos de las credenciales
```bash
    mkdir database/credenciales
    echo ejemplo_contraseña_root_secreto > database/credenciales/root_password.txt
    echo ejemplo_contraseña_user_secreto > database/credenciales/user_password.txt
    echo ejemplo_contraseña_admin > database/credenciales/admin_password.txt

```
- `docker compose up -d --build`