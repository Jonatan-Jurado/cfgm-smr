---
title: Tema 10
tags:
  - Automatizacion
  - Linux
  - Software
  - SistemaOperativo
  - SistemaArchivos
---
# ADMINISTRACIÓN DE LOS SISTEMAS OPERATIVOS LIBRES
## Creación y gestión de los usuarios y grupos

**Gestión de perfiles de usuarios y grupos locales**
- Las tareas de administración en Linux solo las puede realizar el usuario **root**.
- Para cualquier comando es necesario estar identificado como root o poner `sudo` delante.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6jQDaGy-TJo?si=j0NKBmLwZo5iX1C7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Usuarios
- Las cuentas de usuario controlan los archivos y programas a los que tendrán permiso de acceso y qué acciones podrán realizar.

**`useradd`** : Añadir usuario
Sintaxis: `useradd [opciones] nombreUsuario`
- **Opciones principales:**
	- `-g` → identificador del grupo al que pertenece el usuario (debe existir previamente)
	- `-d` → carpeta home del usuario (normalmente `/home/nombreUsuario`)
	- `-m` → crea la carpeta home si no existe
	- `-s` → shell del sistema operativo del usuario (suele ser `/bin/bash`)

**Otros comandos de gestión:**
- `usermod` → modificar información del usuario
- `userdel` → eliminar un usuario

### Grupos

**`groupadd`** : Añadir grupo
Sintaxis: `groupadd nombreGrupo`

**`groupmod`** : Modificar grupo
Sintaxis: `groupmod -g identificador nombreGrupo`
- La modificación se realiza mediante el identificador (GID) del grupo. Con el comando anterior se cambia el nombre del grupo.

**`groupdel`** : Eliminar grupo
Sintaxis: `groupdel nombreGrupo`
- En caso de que exista un usuario con este grupo como principal, **no será posible eliminarlo**.

**`adduser`** : Añadir usuario a un grupo
Sintaxis: `adduser nombreUsuario nombreGrupo`

### Contraseñas

**`passwd`** : Establecer contraseña
Sintaxis: `passwd nombreUsuario`
- Un usuario puede establecer **su propia** contraseña, pero no la del resto.
- Hay que ser **root** para cambiar contraseñas de otros usuarios.
- Se debe establecer **dos veces** por motivos de seguridad.

### Permisos
- Una vez definidos todos los usuarios y grupos, se gestionan los permisos para definir qué recursos cada usuario o grupo podrá **ver**, **modificar** o **eliminar**.

## Gestión del sistema de archivos

### Herramientas gráficas
- En Linux existen **tres tipos de ficheros**:
	- **Carpetas o directorios** → permiten la organización jerárquica del sistema de ficheros.
	- **Ficheros regulares u ordinarios** → archivos con los que se trabaja.
		- Linux contiene sistemas de ficheros basados en discos: `ext2`, `ext3`, `ext4`, `FAT`, `FAT32`, `NTFS`.
		- Sistemas de ficheros para comunicación en red: `NFS` (compartir recursos entre equipos Linux).
		- **SWAP** → partición dentro del disco duro utilizada como punto de carga de aplicaciones y para reducir la carga en RAM.
	- **Ficheros especiales** → usados para la comunicación con los distintos periféricos.

### Consola
- En Linux podemos gestionar y navegar por el sistema de archivos desde la consola integrada.
- El intérprete de comandos se llama **Shell** (en Linux es **bash**).
- La Shell permite ejecutar programas mediante comandos escritos en una consola en modo texto.

## Gestión de los procesos del sistema y del usuario

**Activación y desactivación de los servicios**
- Los servicios de Linux son procesos que se ejecutan de forma continua. Reciben el nombre de **demonios**.
- Los demonios son scripts que se localizan en el directorio `/etc/init.d`

**Comandos para gestionar demonios:** `root ruta/nombreServicio estado`
- **Iniciar un servicio:** `root /etc/init.d/demonio start`
- **Detener un servicio:** `root /etc/init.d/demonio stop`
- **Reiniciar un servicio:** `root /etc/init.d/demonio restart`
- Los demonios se ejecutan en **segundo plano**, no forman parte del control del usuario y **no tienen interfaz gráfica**.

## Optimización de la memoria y del funcionamiento de los dispositivos de almacenamiento

- **SWAP** es la tarea más importante para optimizar la memoria.
- Linux no tiene un sistema de paginación definido.
- Para evitar que la RAM colapse, se emplea **SWAP** → espacio de intercambio en el disco duro donde se almacenan datos que no caben en la RAM.
- Esta asignación se realiza **durante la instalación** del sistema operativo.
- El uso de SWAP se debe minimizar (recursos hardware limitados).
- Para consultar el espacio asignado en memoria se usa el comando `free`.
- La memoria SWAP mantiene los estados de los archivos en ejecución en modo **hibernación** → se define como **memoria caché**.

## Rendimiento del sistema

- Linux tiene un monitor en algunas distribuciones para consultar de forma gráfica y en tiempo real el rendimiento.

**Comandos para consultar rendimiento en consola:**
- `uptime` → monitorizar la carga del sistema
- `time` → tiempo de ejecución de un programa
- `top` → actividad de los procesos
- `vmstat` → actividad de la memoria

### Herramientas del sistema de seguimiento y monitorización

**Monitor del sistema (Ubuntu)** → permite:
- Observar el rendimiento de los procesos en ejecución.
- Porcentaje de CPU utilizado por cada proceso.
- Uso de recursos hardware (RAM y CPU).
- Espacio ocupado en discos duros.

**Monitorización de red:**
- **TCPDUMD** → analizador de paquetes que captura todos los paquetes TCP que circulan por una interfaz específica mediante `tcpdump`.
- Muestra estadísticas de red entrantes y salientes y conexiones activas.

## Compartición de recursos

Opciones para gestionar recursos compartidos:
- **SAMBA** → implementación del protocolo SMB de Microsoft en Linux. Permite configurar directorios para compartirlos en red con permisos de acceso (lectura/escritura).
- **NFS** → requiere instalar el paquete `nfs-utils` en los equipos que necesitan acceder a la carpeta compartida. Se habilita el servicio y se establecen permisos de acceso.
- **Transferencia de archivos** → mediante órdenes como `SSH` o `SCP`.

## Interpretación de datos de configuración y comportamiento del sistema operativo

### Hardware instalado

Herramienta integrada: **`lshw`**
- `sudo lshw` → listado completo del hardware instalado.
- `sudo lshw -html > nombreArchivo.html` → copiar resultado a un archivo HTML.
- `sudo lshw -C disk` → mayor detalle de dispositivos (ej. discos).
- `sudo lshw-gtk` → visualizar información con interfaz gráfica.

### Aplicaciones

- `dpkg -l` → listado completo de paquetes instalados (software).
- `cat /etc/issue.net` → mostrar nombre de la distribución Linux instalada.
- `lsb_release -a` → mayor detalle: módulos y descripción del SO.

### Técnicas de mantenimiento del software de aplicación

**Actualizaciones del sistema:**
- `sudo apt-get update`
- `sudo apt-get dist-upgrade`
- → Descarga e instala todas las actualizaciones disponibles (SO y aplicaciones)

### Copias de seguridad
- Buena práctica dentro del mantenimiento → hacer copias de seguridad de los archivos más importantes.

### Archivos temporales
- Acceder a la carpeta `/tmp`. Linux realiza esta limpieza de **manera automática**.

### Programas que no se utilizan
- `sudo apt-get purge [paquete]` → desinstalar programa **junto con sus configuraciones**.
- `sudo apt-get remove [paquete]` → desinstalar programa **dejando las configuraciones**.

### Desfragmentación de discos
- En Linux **no es necesario desfragmentar** el sistema de archivos.
- Existe la herramienta `FSCK` para **reparación** del sistema de archivos.

## Automatización de tareas

- **`cron`** → servicio para automatizar procesos. Ruta: `/etc/cron.d`

**Tres ficheros dentro de esta ruta:**
- `crontab` → especificación de todas las tareas.
- `cron.allow` → usuarios con permisos para ejecutar tareas.
- `cron.deny` → usuarios sin permisos para ejecutar tareas.

**`crontab -e`** : modificar cron del usuario en uso.

**Sintaxis para especificar una tarea:** `[minuto] [hora] [día] [mes] [día_de_la_semana] [rutaScript]`
- Ejemplo: `0 12 * * 1 /Escritorio/script.sh` → ejecuta el script **todos los lunes a las 12:00**.
- Los días de la semana se indican con números: **domingo = 0**, **lunes = 1**, etc.

<iframe width="560" height="315" src="https://www.youtube.com/embed/d2Q0NiyVO5M?si=IDGlO11tq64JoiMg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Ejecución de programas y guiones administrativos

**Tipos de archivos ejecutables en Linux:**
- `.bin` y `.run` → archivos de instalación de aplicaciones.
- `.sh` → scripts que se ejecutan desde la consola.

- Linux bloquea la ejecución de programas que no tienen los permisos necesarios.

**Para ejecutar un archivo:**
1. Navegar a la carpeta donde está el archivo.
2. Escribir `./nombreArchivo`.
3. Para instalar como administrador: `sudo ./nombreArchivo`.

## Métodos para la recuperación del sistema operativo

- La opción más fácil y rápida → **sistema de copias de seguridad** del disco duro y archivos importantes.

**Si no hay copias de seguridad → arrancar en modo rescate mediante:**
- Arrancar desde **CD-ROM o DVD**.
- Arrancar desde **dispositivos flash USB**.
- Arrancar desde el **DVD de Red Hat Enterprise Linux**.

**Comando una vez iniciado en modo rescate:** `Linux rescue dd`
- El sistema arranca descargando el controlador del disco y busca una imagen estable para montarla y restaurar el SO (normalmente en `/mnt/sysimage`).

**Otra opción:** **LIVECD** → arranca el SO desde el CD para realizar reparación o instalación nueva.

## Comprobación del correcto funcionamiento del sistema

**Mantenimiento del inventario del software utilizado y seguimiento de cambios**
- `dpkg -l` → muestra el listado completo de paquetes instalados en el sistema.
- **Linux Mint** incluye un administrador de actualizaciones que gestiona actualizaciones automáticas y puede hacer copias de seguridad de programas instalados.

## Documentación de las tareas de administración y las incidencias aparecidas con sus soluciones. Interpretación de la documentación técnica

- Todo sistema operativo Linux incluye una sección con la **documentación necesaria** para cualquier tipo de gestión.
- Contiene apartados relacionados con **incidencias encontradas por otros usuarios** y sus soluciones.
- Si la incidencia no aparece solucionada → **contactar con el fabricante** y explicar el problema con detalle.