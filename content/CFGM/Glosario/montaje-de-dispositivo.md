---
title: "Montaje de dispositivo"
aliases: ["Montar", "Mount", "Punto de montaje"]
---
# Montaje de dispositivo

Es el [[Proceso]] técnico mediante el cual se asocia un dispositivo físico de almacenamiento a un [[Directorio]] específico del [[Sistema de archivos]] (fichero de dispositivos) para que su contenido sea accesible. En Linux, este Proceso requiere identificar el dispositivo (ej. `/dev/sde1`) y utilizar el comando `mount` especificando el formato del Sistema de archivos (como FAT o [[NTFS]]). La operación inversa se realiza mediante el comando `umount`.