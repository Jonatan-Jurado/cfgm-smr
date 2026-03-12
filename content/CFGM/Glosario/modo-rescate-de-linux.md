---
title: "Modo Rescate de Linux"
aliases: ["Modo rescate Linux", "Linux rescue mode"]
---
# Modo Rescate de Linux
Un modo especial de arranque en Linux utilizado para recuperar el sistema operativo cuando no se tienen copias de seguridad.

- _Métodos de arranque_:
    - _Arrancar desde un CD-ROM o DVD_.
    - _Arrancar desde otros medios de arranque_: como dispositivos flash USB.
    - _Arrancar desde el DVD de Red Hat Enterprise Linux_.
- _Comando en terminal_: Una vez iniciado el sistema operativo en la terminal, se escribe `Linux rescue dd`.
- _Proceso automático_: El sistema arranca descargando controladores si es necesario, busca una imagen estable en el disco para montarla y restaura el sistema operativo.
- _Ruta común de restauración_: `/mnt/sysimage`.