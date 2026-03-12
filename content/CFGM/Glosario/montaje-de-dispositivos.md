---
title: "Montaje de Dispositivos"
---
# Montaje de Dispositivos
El [[Proceso]] de montaje consiste en asociar el [[Sistema de Archivos]] de un dispositivo físico (como una unidad USB o un [[Disco Duro]]) a un [[Directorio]] específico dentro del árbol de [[Directorios]] del [[Sistema Operativo]] (punto de montaje, usualmente en `/media` o `/mnt`). En Linux, esto se realiza mediante el comando `mount`, especificando el formato de archivos (FAT, [[NTFS]], etc.), permitiendo así el acceso a los datos del periférico. La operación inversa se denomina desmontar y se ejecuta con el comando `umount`.