---
title: "Sintaxis para la Programación de Tareas"
aliases: ["Sintaxis de programación de tareas", "Sintaxis de cron", "Programación de tareas"]
---
# Sintaxis para la Programación de Tareas
Es la estructura de comandos utilizada para especificar la frecuencia con la que se ejecutará una tarea en un sistema operativo.

- _Formato_: `[minuto] [hora] [día] [mes] [día_de_la_semana] [rutaScript]`
- _Días de la semana_: Se realizan de forma numérica, tomando el domingo como 0, el lunes como 1, y así sucesivamente.
- _Ejemplo_: `0 12 * * 1 /Escritorio/script.sh` ejecuta el script todos los lunes a las doce del mediodía.