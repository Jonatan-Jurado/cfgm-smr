---
title: "Paginación"
aliases: ["Técnica de paginación", "Paginaciones"]
---
# Paginación
Una de las técnicas principales para usar la memoria secundaria como memoria virtual. Tanto la propia memoria como los procesos se dividen en unidades más pequeñas.

En esta técnica:
- Los programas están distribuidos en segmentos dentro de la memoria principal, denominadas _unidades lógicas_ o _páginas_.
- La memoria se divide en diferentes secciones o partes de igual tamaño que las páginas, conocidas como _marcos de página_.

Esta técnica minimiza la fragmentación interna y evita la fragmentación externa, ya que, cuando la memoria y los segmentos de los procesos tienen el mismo tamaño, no se desperdicia memoria RAM por cada partición, sino solamente en la última página de un programa.