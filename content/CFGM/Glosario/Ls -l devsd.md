---
title: "Ls -l devsd"
aliases: ["ls -l devsd"]
---

# Ls -l /dev/sd*

Una vez identificado, lo montamos: • (Formato FAT): mount -t vfat /dev/sde1 /media/usb • (Formato NTFS): mount -t ntfs-3g /dev/sde1 /media/usb Donde sde1 es el nombre que [[el sistema operativo]] utiliza para identi- ficar el dispositivo. Ahora, dentro de la carpeta /media/usb estarán todos los archivos y directorios que estén el dispositivo. También es posible realizar la operación contraria, es decir, desmontar el dispositivo. Para ello se utiliza el comando: umount /media/usb Tema 9. Realización de tareas básicas de configuración y mantenimiento sobre sistemas operativos libres 150 Donde /usb es el nombre del directorio creado para el USB. En caso de tener conectados varios USB por ejemplo, se introduce lo siguiente: mount -t vfat /dev/sde1 /media/usb2 Y para desmontar: umount /media/usb2