---
title: "proceso de arranque"
---

title: "[[Proceso]] de arranque"
aliases: ["Arranque del sistema", "Boot", "Secuencia de inicio"]
---
# Proceso de arranque

Secuencia de operaciones que se inicia cuando el sistema se encuentra en estado de parada (nivel 0) y se activa la máquina. El proceso comienza cargando una pequeña porción de código en la memoria RAM que inicia el núcleo del sistema operativo. Posteriormente, se realizan comprobaciones de hardware, se montan los sistemas de archivos y dispositivos, y finalmente se lanza el proceso `init`, que es el primer proceso de ejecución encargado de establecer el nivel de ejecución definido en el fichero de configuración correspondiente.