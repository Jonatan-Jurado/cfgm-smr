---
title: "Lshw"
aliases: []
---
# Lshw
Herramienta integrada en Linux que permite conocer con detalle el listado de hardware que tiene instalado el equipo.
Modos de uso:
- `lshw`: ejecuta desde la terminal para obtener un listado completo del sistema.
- `sudo lshw -html > nombreArchivo.extension`: copia el resultado directamente en un archivo generado con formato HTML.
- `sudo lshw -C [dispositivo]`: permite conocer un mayor detalle de dispositivos específicos, por ejemplo, `sudo lshw -C disk` para discos.
- `sudo lshw-gtk`: visualiza la información mediante una interfaz gráfica.