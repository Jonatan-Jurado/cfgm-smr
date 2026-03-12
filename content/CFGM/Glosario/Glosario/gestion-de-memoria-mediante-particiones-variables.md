---
title: "Gestión de memoria mediante particiones variables"
aliases: ["Gestión de la memoria mediante particiones variables", "Particiones variables"]
---
# Gestión de memoria mediante particiones variables
Método en el que la memoria se particiona según la ejecución de los procesos, de modo que un proceso solo ocupa en memoria el espacio que necesita. El número de particiones, su tamaño y posición cambian dinámicamente según se utiliza la memoria.

Se puede utilizar de dos formas:
- _Cuando un proceso termina, se combina el hueco que deja libre con el que hay disponible al lado_.
- _Cuando un proceso termina, se compactan los espacios ocupados de la memoria_, resultando al principio toda la memoria ocupada y después toda la memoria libre.

Estrategias para gestionar los procesos:
- _De primer ajuste_: se asigna al primer proceso de la cola el primer hueco que le sirva.
- _De siguiente ajuste_: se asignan los procesos por orden de cola.
- _De mejor ajuste_: se asigna el hueco más pequeño al proceso que mejor se adapte al espacio.
- _De peor ajuste_: se asigna el hueco más grande al primer proceso de la cola.