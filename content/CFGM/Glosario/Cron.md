---
title: "Cron"
aliases: []
---
# Cron
Utilidad de Linux para la automatización de procesos o servicios, ubicada en la ruta `/etc/cron.d`. Su configuración y permisos son editables.
Dentro de esta ruta, se encuentran los siguientes ficheros relacionados:
- _crontab_: especificación de todas las tareas a ejecutar.
- _cron.allow_: lista de usuarios con permisos para ejecutar cada una de las tareas.
- _cron.deny_: lista de usuarios que no tienen permisos para ejecutar alguna tarea.
Las tareas especificadas dentro del archivo `crontab` se ejecutan en el tiempo y frecuencia indicados. Para modificar los cron del usuario en uso se utiliza el comando `crontab -e`.