---
title: "Comprobador de archivos de sistema"
aliases: ["Comprobadores de archivos de sistema", "SFC.exe", "System File Checker"]
---
# Comprobador de archivos de sistema
Herramienta integrada en Windows, también conocida por su archivo ejecutable SFC.exe, que permite comprobar el estado del funcionamiento de los archivos y las funcionalidades propias del sistema.

*   _Uso_: Se utiliza cuando determinadas funcionalidades del sistema operativo no funcionan o bloquean el sistema, impidiendo la comunicación con él.
*   _Ejecución_: Se abre la terminal de Windows y se escribe el comando `sfc /scannow`.
*   _Función_: Realiza un análisis de todos los archivos del sistema y reemplaza, en caso de ser necesario, aquellos que estén dañados por otros ubicados en las copias de seguridad del sistema.
*   _Resultado_: Tras finalizar la comprobación, mostrará un informe detallado de los cambios realizados o, en caso contrario, un mensaje indicativo de que no se ha realizado modificación alguna. Este informe quedará almacenado dentro de la ruta especificada en `%windir%` en un archivo de texto.
*   _Precaución_: Este proceso realiza modificaciones de archivos de manera automática, por lo que una vez iniciado no es aconsejable detenerlo, ya que algunos archivos del sistema pueden verse dañados de manera irreparable.