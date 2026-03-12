---
title: "useradd"
aliases: ["comando useradd"]
---
# useradd
Comando utilizado en Linux para añadir un nuevo usuario al sistema.
- _Sintaxis_: `useradd [opciones] nombreUsuario`
- _Opciones comunes_:
    - _-g_: Identificador del grupo al que va a pertenecer el usuario. Debe existir previamente.
    - _-d_: Carpeta home del usuario. Normalmente se encuentra en la ruta `/home/nombreUsuario`.
    - _-m_: Crea la carpeta home, si es que no existe.
    - _-s_: Referencia a la Shell del sistema operativo del usuario. Suele ser `/bin/bash`.