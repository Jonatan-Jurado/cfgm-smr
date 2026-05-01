---
title: Tema 8
tags:
  - Software
  - SistemaOperativo
  - GestorArranque
---
# PUESTA EN MARCHA DEL EQUIPO
## Montaje y mantenimiento de equipos

- Después de tener ensamblado nuestro equipo informático, procedemos a la conexión de los distintos periféricos: monitor, teclado, ratón, impresora (si es el caso) y altavoces.
- **Orden de encendido:**
	1. Encendemos la fuente de alimentación.
	2. Seguidamente la pantalla.
	3. Por último, el ordenador.
- Con esto podremos comprobar:
	- Si funciona el ventilador.
	- Si se encienden los LEDs delanteros.
	- Si funciona el procesador.
	- Si hubiera algún problema con el ensamblado (en ese caso escucharíamos pitidos).
- El siguiente paso es la configuración de la BIOS.

## Configuración de la BIOS

- **BIOS Setup Utility** (también llamado **EFI**) es un programa para configurar los parámetros del equipo.
- No hay un estándar para estos programas → variarán según la marca y modelo de la placa base.
- Es conveniente tener muy cerca el **manual de la placa base** para poder consultarlo.
- **Acceso a la BIOS:**
	- Se accede pulsando la tecla indicada en la pantalla de inicio (normalmente `Suprimir` o `F2`).
	- Si la tecla no se pulsa a tiempo, el programa de arranque sigue su curso y habrá que reiniciar para intentarlo de nuevo.
- **Pantalla de menú de la BIOS:** contiene apartados como Principal, Seguridad, Arranque, Avanzado y Salir (varían según placa base, pero suelen incluir estas opciones).
- Debemos seguir las instrucciones en pantalla para desplazarnos y acceder a cada opción.

## Gestor de arranque

- Pasos después de acceder a la BIOS:
	1. Empezar a enlazar los dispositivos periféricos con el equipo.
	2. Establecer los valores de la **CMOS** (como fecha y hora).
	3. Comprobar las unidades de almacenamiento.
- **Bootstrap Loader:** programa encargado de buscar un disco duro con un sistema operativo instalado.
- **Si hay más de un disco duro o partición con más de un sistema operativo:**
	- El arranque hace elegir al usuario cuál de los sistemas operativos desea (programa **boot**).
	- Una vez elegido, accedemos al **MBR** (sector de arranque del disco).
- **Características importantes del gestor de arranque según el SO:**
	- El gestor de arranque de Linux (`LILO` o `GRUB`) **sí** es capaz de identificar que hay otro sistema operativo aparte de Linux.
	- El gestor de arranque de Windows **no** identifica otro sistema operativo.

## Realización de un informe de montaje

- Al realizar un informe de nuestro proyecto de ensamblado, debemos dejar constancia por escrito de:
	- Pasos que realizar.
	- Dificultades encontradas.
	- Soluciones implementadas.
	- Conclusión.
- Utilidad: cuando queramos consultar el procedimiento de montaje, tendremos un documento escrito que servirá como resumen de todo el proceso.