---
title: "MFT"
aliases: ["MFTs", "Tabla Maestra de Archivos", "Master File Table"]
---
# MFT
Tabla que mantiene la información de todos los ficheros y directorios de un volumen NTFS. Cada fila, de longitud variable, describe un archivo o directorio en un volumen.
_Almacenamiento de ficheros_:
- Si el fichero es pequeño, se ubica al completo en una fila de la MFT.
- Si el fichero es grande, la parte que sobrepasa el espacio se almacena en una zona libre del área de almacenamiento.