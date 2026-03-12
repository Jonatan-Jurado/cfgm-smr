---
title: "Errores comunes de arranque de sistema operativo en máquina virtual"
aliases: ["Errores de inicio de SO en MV", "Problemas de arranque de sistema operativo huésped", "Fallas de arranque de máquina virtual", "Errores en arranque de MV"]
---
# Errores comunes de arranque de sistema operativo en máquina virtual
Fallos que pueden aparecer durante el proceso normal de arranque del sistema operativo dentro de una máquina virtual.
- _Operating System not found_: Indica un error al cargar el sistema operativo, generalmente porque la ruta de acceso al archivo de imagen no se ha especificado correctamente o no se pudo instalar.
- _Unable to open kernel device_: Para solucionarlo, es necesario revisar el archivo de configuración de la máquina virtual y comprobar que la opción `vmci0.present = “TRUE”` está habilitada.
- _This kernel requires an x86-64 CPU_: Puede deberse a que el sistema operativo es de 64 bits y el procesador de la máquina real es de 32 bits (se debe usar una imagen de SO de 32 bits), o a que el procesador físico no permite la virtualización.