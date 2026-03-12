---
title: "Gestión de la memoria mediante memoria virtual"
aliases: ["Memoria virtual", "Gestión de memoria virtual"]
---
# Gestión de la memoria mediante memoria virtual
Técnica de gestión de memoria donde el gestor utiliza el disco duro o un espacio secundario de almacenamiento como si formara parte de la memoria principal del sistema. Permite trabajar con una memoria RAM de mayor almacenamiento que la físicamente disponible.

En esta técnica, un programa se divide en:
- _Capas activas_: procesos que están en ejecución en la memoria principal.
- _Capas inactivas_: procesos que se localizan en la memoria secundaria.

El usuario percibe que el programa se localiza en la memoria RAM, pero en ella solo está realmente la parte que se está ejecutando, mientras que el resto del programa se encuentra en la memoria virtual esperando a ser necesario. Los procesos pueden cambiarse de memoria mediante la técnica de _swapping_.

Problemas principales de esta técnica:
- _Ralentización del sistema_: debido al constante intercambio de información entre la memoria RAM y el disco duro.
- _Fallo de página_: ocurre si un proceso hace referencia a otro que todavía no se encuentra en la memoria principal.