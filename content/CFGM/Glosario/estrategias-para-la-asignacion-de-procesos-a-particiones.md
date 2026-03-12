---
title: "Estrategias para la asignación de procesos a particiones"
aliases: ["Estrategia para la asignación de procesos a particiones", "Estrategias de asignación de procesos a particiones"]
---
# Estrategias para la asignación de procesos a particiones
Métodos que utiliza el gestor de memoria para asignar un proceso a una de las particiones disponibles.
-   _Cola única_: (No se proporciona explicación en el texto).
-   _Cola por cada partición_: El usuario es el encargado de establecer estas particiones, que no tienen necesariamente el mismo espacio. El gestor de memoria controla la ejecución de los procesos, indicando en qué partición se colocará cada uno.