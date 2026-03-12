---
title: "Métodos para la recuperación"
aliases: ["métodos para la recuperación"]
---

# Métodos para la recuperación

del sistema operativo La opción más fácil y rápida para realizar la recuperación de un siste- ma operativo es el uso del sistema de copias de seguridad creado de nuestro disco duro y archivos más importantes. En caso de no tener realizadas estas copias, sería necesario arrancar en el modo rescate de Linux, para lo cual se deberá utilizar uno de los siguientes métodos: • Arrancar desde un CD-ROM o DVD. • Arrancar desde otros medios de arranque, como dispositivos flash USB. • Arrancar desde el DVD de Red Hat Enterprise Linux. Una vez se haya iniciado [[el sistema operativo]] en la terminal, se escribe: Linux rescue dd De esta forma, el sistema arranca descargando, en caso de ser nece- sario, el controlador del disco. Además, realizará automáticamente la búsqueda dentro del disco de una imagen estable para montarla en él y restaurar el sistema operativo. Este proceso normalmente se realiza en la ruta /mnt/sysimage. Sistemas operativos monopuesto 165 Otra de las opciones para recuperar el sistema operativo es el uso del LIVECD, que arranca el sistema operativo desde el CD para realizar una reparación o instalación nueva.