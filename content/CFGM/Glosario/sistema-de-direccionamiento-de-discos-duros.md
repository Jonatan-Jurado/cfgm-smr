---
title: "Sistema de Direccionamiento de Discos Duros"
aliases: ["Sistemas de Direccionamiento de Discos Duros", "Técnicas de Direccionamiento de Discos Duros"]
---
# Sistema de Direccionamiento de Discos Duros
Se refiere a la técnica o algoritmo que emplea el cabezal magnético de un disco duro para localizar y acceder a los datos, permitiendo realizar operaciones de lectura o escritura.

Existen diferentes protocolos y técnicas:
- _Técnica Cilindro-Cabezal-Cilindro (CHS)_: Asigna números específicos a los sectores y al cilindro. La cara del plato se numera empezando por 0. Para encontrar un dato, es necesario conocer estos tres números.
- _Modo LBA (Logical Block Addressing)_: Enumera todos los sectores del disco de manera consecutiva. Con un único número LBA, se puede determinar la ubicación exacta del dato.