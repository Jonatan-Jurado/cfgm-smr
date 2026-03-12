---
title: "SWAP"
aliases: ["Memoria SWAP", "Partición SWAP", "Espacio de intercambio"]
---
# SWAP
Es una partición o espacio de intercambio dentro del disco duro utilizado en Linux para evitar que la memoria RAM colapse y se sobrecargue, ya que Linux no tiene un sistema de paginación definido. Consiste en la creación de un espacio donde se almacenan todos los datos que no pueden alojarse en la memoria RAM, actuando como punto de carga de aplicaciones o programas. Esta asignación de espacio se realiza durante la instalación del sistema operativo.

*   _Función_: Reduce la carga en memoria RAM.
*   _Optimización_: Optimizar la memoria SWAP es una tarea importante para mejorar el rendimiento del sistema operativo.
*   _Uso recomendado_: Aunque mejora el rendimiento, su uso debe minimizarse debido a los recursos hardware limitados del equipo.
*   _Comando para consultar espacio_: `free`.
*   _Definición alternativa_: Se podría definir como una memoria caché, ya que mantiene los estados de los archivos en ejecución incluso cuando el equipo se pone en modo de hibernación.