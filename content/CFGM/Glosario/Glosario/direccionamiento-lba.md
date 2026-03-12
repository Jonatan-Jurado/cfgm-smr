---
title: "Direccionamiento LBA"
---
# Direccionamiento LBA
La técnica de direccionamiento de bloques lógicos (LBA, *Logical Block Addressing*) es el método estándar actual para el acceso a datos en discos duros. A diferencia del sistema CHS, el modo LBA enumera todos los sectores del disco de forma consecutiva y lineal. Gracias a esta simplificación, basta con conocer un único número de [[Sector]] para localizar cualquier dato. Su capacidad se calcula multiplicando el número total de sectores por el tamaño de cada Sector.