---
title: "Proceso de arranque del sistema (Linux)"
aliases: ["Procesos de arranque del sistema (Linux)", "Arranque del sistema (Linux)"]
---
# Proceso de arranque del sistema (Linux)
Procedimiento que inicia el sistema operativo Linux. Previamente, el sistema debe estar en estado de parada (nivel de ejecución 0). Al ejecutar el arranque, se carga una pequeña parte del código en memoria, lo que da inicio al sistema operativo.

Una vez iniciado el sistema, se realizan las siguientes tareas:
- Distintas comprobaciones de hardware.
- Montaje de todos los ficheros del sistema y dispositivos.
- Lanzamiento del proceso `init`, que es el primero en ejecutarse durante el arranque. Sus tareas incluyen comprobar el fichero `/etc/inittab` para determinar el nivel de ejecución a ejecutar, o realizar el nivel por defecto (nivel de ejecución 5).