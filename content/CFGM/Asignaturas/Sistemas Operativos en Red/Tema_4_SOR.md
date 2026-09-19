---
title: Tema 4
tags:
  - Linux
  - Servidores
  - Redes
---
# Tema 4 - Instalación, actualización y monitorización de sistemas operativos libres en red

En este tema se trabaja con un **sistema operativo libre y de libre distribución**, utilizando **Linux Ubuntu Server** como sistema de referencia.

El proceso completo consiste en:

1. Analizar el equipo y comprobar su compatibilidad.
2. Elegir la distribución y versión.
3. Planificar las particiones.
4. Elegir el sistema de archivos.
5. Seleccionar el método de instalación.
6. Instalar el sistema y los servicios necesarios.
7. Configurar y actualizar el servidor.
8. Monitorizar su funcionamiento.
9. Detectar y solucionar incidencias.
10. Documentar todo el proceso.

> [!important]
> Un sistema operativo de servidor no debe instalarse simplemente aceptando todas las opciones por defecto.
>
> La instalación necesita una **planificación previa**, porque el servidor gestionará recursos, comunicaciones y servicios utilizados por otros equipos de la red.


<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
  <iframe src="https://www.youtube.com/embed/BCVQqMnt8XE?si=AB5RHRGRwsnzyhgh" title="YouTube video player" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

---

# 4.1. ESTUDIO DE COMPATIBILIDAD DEL SISTEMA INFORMÁTICO

## FUNCIÓN DE UN SERVIDOR LINUX

Las distribuciones Linux destinadas a servidores están preparadas para proporcionar recursos y herramientas a los clientes de una red.

- **Servidor:** equipo encargado de gestionar la configuración y los recursos de la red.
- **Clientes:** equipos que utilizan los recursos y servicios proporcionados por el servidor.
- **Coordinación:** el servidor controla el flujo de datos y las comunicaciones entre los equipos.
- **Detección de incidencias:** los problemas deben detectarse y solucionarse lo antes posible para afectar lo mínimo posible a los clientes.
- **Multiprocesador:** el sistema está preparado para trabajar con más de un procesador.
- **Multitarea:** permite ejecutar distintas tareas simultáneamente.

---

## PLANIFICACIÓN PREVIA

Antes de instalar el sistema operativo debemos seguir tres pasos principales:

1. **Analizar el entorno:** conocer el lugar, el equipo y sus características.
2. **Elegir la versión:** seleccionar la distribución y versión de Linux que vamos a instalar.
3. **Configurar la instalación:** preparar el sistema y poner en marcha el proceso.


---

## ELECCIÓN DE LA DISTRIBUCIÓN Y VERSIÓN

Linux dispone de numerosas distribuciones de código libre.

- **Distribución:** versión de Linux preparada con determinadas herramientas, configuraciones y características.
- **Diferencias:** pueden variar el entorno gráfico, el proceso de instalación y determinadas configuraciones.
- **Comunidad:** al tratarse de software libre, existe una comunidad de usuarios que prueba y mejora el sistema en diferentes entornos.
- **Fiabilidad:** el material destaca Linux como un sistema fiable gracias a las pruebas realizadas por su comunidad.

---

## INVENTARIO DEL SISTEMA

Antes de instalar debemos conocer todos los componentes existentes.

- **Inventario hardware:** relación de todos los componentes físicos instalados.
- **Inventario software:** relación de programas disponibles en el servidor.
- **openDCIM:** herramienta mencionada en el material para realizar tareas de inventario.
- **NeDi:** otra herramienta indicada para gestionar información de los dispositivos.

---

## COMPROBACIÓN DE COMPATIBILIDAD

Debemos comprobar varios tipos de compatibilidad:

- **Hardware-sistema operativo:** los componentes físicos deben poder funcionar con Linux.
- **Software-sistema operativo:** las aplicaciones necesarias deben ser compatibles.
- **Servicios:** los servicios que instalaremos posteriormente también deben ser compatibles.
- **Controladores:** debemos comprobar que existan drivers adecuados para nuestros dispositivos.


### CONTROLADORES

El sistema operativo incluye controladores para numerosos dispositivos.

- **Driver incluido:** el dispositivo puede ser reconocido automáticamente.
- **Driver posterior al sistema operativo:** puede ser necesario instalarlo manualmente.
- **Dispositivo no reconocido:** puede indicar que falta su controlador.

---

# 4.2. PLANIFICACIÓN Y PARTICIONADO DEL DISCO

## REQUISITOS DE UBUNTU SERVER

Según el material, los requisitos mínimos son:

- **Memoria gráfica:** 512 MB.
- **Disco duro:** 4 GB, incluida la zona de intercambio.
- **Procesador:** arquitectura de 32 o 64 bits.
- **Video Graphics Array (VGA):** tarjeta gráfica compatible.

El material también recomienda una configuración superior:

- **Disco duro:** 27 GB.
    - 2 GB destinados al sistema operativo.
    - 25 GB para configuraciones de usuarios, mantenimiento y recursos compartidos.
- **Random Access Memory (RAM):** 1 GB para responder mejor a múltiples peticiones y accesos simultáneos.

---

## PARTICIONADO EN LINUX

En Linux el particionado tiene especial importancia porque el sistema utiliza varias áreas independientes.

Las principales son:

- **Partición del sistema:** almacena los datos necesarios para ejecutar el sistema operativo.
- **Partición de datos:** almacena información independientemente de la partición principal.
- **Swap:** zona de intercambio utilizada como memoria virtual.


> [!info]
> ### ESQUEMA HABITUAL DE PARTICIONADO EN LINUX
>
> Aunque el tema explica principalmente las áreas de sistema, datos y swap, en una instalación Linux puede ser habitual separar:
>
> - **`/`:** sistema operativo.
> - **`/home`:** datos y configuraciones de usuarios.
> - **`/boot`:** archivos necesarios para el arranque.
> - **`swap`:** zona de intercambio que sirve de apoyo a la RAM.
>
> El número y tipo de particiones puede variar según las necesidades del equipo o servidor.



---

## GPARTED

- **GParted:** herramienta utilizada para crear y gestionar particiones.
- **Instalador de Ubuntu:** también incorpora herramientas que permiten realizar el particionado durante la instalación.

---

# 4.3. SISTEMAS DE ARCHIVOS

Un sistema de archivos determina cómo organiza el sistema operativo el espacio utilizado para almacenar los datos.

Su objetivo es permitir un acceso:

- Rápido.
- Seguro.
- Eficiente.

## EXT3

- **Ext3:** evolución de Ext2.
- **Journaling:** característica que permite mejorar la estabilidad ante fallos.
- **Recuperación:** puede ayudar a recuperar el estado previo del sistema después de determinados incidentes.

> [!tip]
> El **journaling** funciona de forma parecida a llevar un registro de lo que se estaba haciendo.
>
> Si ocurre un fallo, el sistema dispone de información que puede utilizar para intentar recuperar el estado anterior.

---

## EXT4

- **Ext4:** evolución de Ext3.
- **Procesador:** utiliza menos recursos de procesamiento según el material.
- **Lectura y escritura:** mejora su velocidad.
- **Extents:** sustituyen al esquema anterior de bloques y mejoran el rendimiento con archivos grandes.

---

## OTROS SISTEMAS DE ARCHIVOS

- **XFS:** sistema de archivos mencionado como uno de los sistemas más novedosos.
- **ReiserFS:** otro sistema de archivos incluido en el material.

> [!important]
> ### EXT3 ≠ EXT4
>
> - **Ext3:** destaca por incorporar journaling.
> - **Ext4:** evolución de Ext3, mejora rendimiento, lectura/escritura y utiliza extents.

---

# 4.4. MÉTODOS DE INSTALACIÓN

Ubuntu Server puede instalarse mediante dos métodos principales.

## INSTALACIÓN ATENDIDA

- **Instalación atendida:** el administrador participa durante todo el proceso.
- **Configuración:** el usuario selecciona las opciones que necesita.
- **Resultado:** permite adaptar el sistema a las necesidades concretas.
- **Requisito:** el administrador debe saber qué configuración está realizando.

Puede iniciarse desde:

- DVD.
- CD.
- Disco duro.
- Pen drive.
- Imagen ISO.

### VENTAJA

- **Personalización:** permite controlar todas las decisiones de la instalación.

### INCONVENIENTE

- **Responsabilidad:** un error del administrador durante la configuración puede provocar problemas en el sistema.

---

## INSTALACIÓN DESATENDIDA

- **Instalación desatendida:** el sistema realiza automáticamente las decisiones previamente configuradas.
- **Administrador:** prepara las opciones iniciales y pone en marcha el proceso.
- **Interacción:** durante la instalación no es necesaria la participación del usuario.
- **KickStar:** herramienta mencionada en el material para automatizar instalaciones.
- **Anaconda:** otra herramienta indicada para realizar este proceso.

### VENTAJAS

- **Tiempo:** reduce el tiempo necesario.
- **Esfuerzo:** necesita menos intervención del administrador.
- **Instalaciones múltiples:** resulta especialmente útil para instalar la misma configuración en varios equipos.

> [!important]
> ### ATENDIDA ≠ DESATENDIDA
>
> - **Atendida:** el administrador participa y decide durante la instalación.
> - **Desatendida:** las decisiones se preparan previamente y el proceso se automatiza.
>
> **Atendida = mayor control.**
>
> **Desatendida = mayor automatización.**

---

# 4.5. INSTALACIÓN Y COMPROBACIÓN DEL SISTEMA

El tema realiza una instalación **atendida** de Ubuntu Server.

Puede instalarse:

- En una máquina virtual.
- Directamente sobre el equipo físico.

## PROCESO GENERAL

1. **Configurar el arranque:** establecer como primera opción el dispositivo de instalación.
2. **Reiniciar el equipo:** arrancar desde el medio correspondiente.
3. **Elegir idioma:** seleccionar el utilizado durante la instalación.
4. **Seleccionar Instalar:** frente a las opciones Reparar o Analizar.
5. **Detectar hardware:** Ubuntu identifica los dispositivos disponibles.
6. **Elegir nombre del equipo:** debe ser único dentro de la red.
7. **Particionar el disco:** utilizar particionado guiado o manual.
8. **Elegir partición:** seleccionar dónde se instalará el sistema.
9. **Crear usuario:** configurar usuario y contraseña.
10. **Elegir componentes y servicios:** instalar las funciones necesarias.
11. **Finalizar:** iniciar sesión y personalizar el servidor.

---

## PARTICIONADO GUIADO Y MANUAL

### GUIADO

- **Guiado:** el instalador crea automáticamente las particiones necesarias.
- **Tamaño:** asigna automáticamente espacio suficiente.
- **Logical Volume Manager (LVM):** puede configurarse de forma manual o automática según las opciones disponibles.

### MANUAL

- **Manual:** el administrador crea personalmente las particiones.
- **Tamaño:** debe establecer el tamaño de cada partición.
- **Sistema de archivos:** debe elegir qué sistema utilizará cada una.

> [!important]
> ### GUIADO ≠ MANUAL
>
> - **Guiado:** el programa realiza el particionado.
> - **Manual:** el administrador decide tamaño, particiones y sistemas de archivos.

---

# SERVICIOS Y COMPONENTES DEL SERVIDOR

Los servicios son prestaciones que ofrece el servidor para permitir que los clientes realicen determinadas operaciones.

## DOMAIN NAME SYSTEM (DNS) SERVER

- **DNS Server:** relaciona una dirección IP con un nombre.

> [!example]
> En lugar de tener que identificar un equipo únicamente mediante su dirección IP, DNS permite relacionarlo con un nombre más fácil de utilizar.

---

##  LAMP: LINUX, APACHE, MYSQL Y PHP 

**LAMP** es un conjunto de programas utilizado para proporcionar servicios web.

- **Linux:** sistema operativo base.
- **Apache:** servicio web.
- **MySQL:** gestor de bases de datos.
- **PHP:** lenguaje utilizado para el tratamiento de la web.

> [!important]
> ### LAMP
>
> **Linux + Apache + MySQL + PHP**

---

## OTROS SERVICIOS

- **Mail Server:** permite configurar un servidor de correo.
- **Secure Shell (SSH) mediante OpenSSH Server:** permite comunicación entre equipos y servidor.
- **PostgrSql Server:** gestor de bases de datos.
- **Samba File Server:** permite configurar funciones relacionadas con dominio y compatibilidad con Windows.
- **Print Server:** proporciona servicios relacionados con impresión.


---

# 4.6. ARRANQUE, CONFIGURACIÓN Y ACTUALIZACIÓN

## PROCESO DE ARRANQUE

El arranque de Linux sigue una secuencia.

1. **Basic Input/Output System (BIOS):** comprueba el proceso inicial.
2. **Gestor de arranque:** recibe el control después de la BIOS.
3. **Kernel:** se carga junto con los módulos necesarios.
4. **init:** continúa el proceso de inicio.
5. **Particiones:** se montan las distintas particiones.
6. **Inicio del sistema:** finalmente se presenta el entorno al usuario.

---

## KERNEL

- **Kernel:** núcleo encargado de gestionar los recursos del sistema y las peticiones realizadas al hardware.

> [!important]
> ### BIOS → GESTOR DE ARRANQUE → KERNEL → INIT → PARTICIONES → SISTEMA
>
> Este es el orden básico de arranque descrito en el tema.

---

## PROCESOS Y SERVICIOS

Como administradores debemos controlar qué programas y servicios se ejecutan.

- **Procesos activos:** deben mantenerse únicamente los necesarios para conseguir un funcionamiento eficiente.
- **init:** según el material, es el primer proceso que se ejecuta y participa en el inicio del entorno.

---

# NIVELES DE EJECUCIÓN

Los niveles de ejecución permiten iniciar el servidor de distintas maneras según la tarea que necesitemos realizar.

> [!iMPORTANT]
>- **Nivel 0:** apagado.
>- **Nivel 1:** monousuario.
>- **Nivel 2:** multiusuario sin soporte de red.
>- **Nivel 3:** multiusuario con soporte de red.
>- **Nivel 4:** no usado.
>- **Nivel 5:** multiusuario gráfico.
>- **Nivel 6:** reinicio.


---

# PERSONALIZACIÓN DEL SERVIDOR

Linux puede utilizar diferentes entornos gráficos.

- **GNOME:** entorno gráfico disponible para Linux.
- **KDE:** otro entorno gráfico con funcionalidades similares.
- **Modo texto:** en Ubuntu Server se utiliza antes de instalar el entorno gráfico.
- **sudo:** comando utilizado para ejecutar determinadas acciones con privilegios de superusuario.

Una vez instalado un entorno gráfico, al reiniciar puede iniciarse automáticamente.

Si existen varios entornos instalados, se puede seleccionar cuál utilizar.

---

# ACTUALIZACIÓN DEL SERVIDOR

Las nuevas versiones aparecen principalmente para:

- Mejorar la seguridad.
- Incorporar funcionalidades.
- Actualizar software.

- **Gestor de actualizaciones:** comprueba nuevas versiones de software y seguridad.
- **Superusuario:** determinadas actualizaciones solicitan su contraseña.
- **Repositorios:** contienen paquetes de software y actualizaciones disponibles para Linux.


---

# 4.7. MONITORIZACIÓN DEL SISTEMA

La monitorización permite detectar errores, analizar el rendimiento y descubrir por qué aparece un problema.

Puede realizarse:

- Mediante herramientas gráficas.
- Desde el terminal utilizando comandos.

---

## COMANDOS DE MONITORIZACIÓN

- **`ps`:** muestra los procesos que se están ejecutando y su estado.
- **`pstree`:** muestra los procesos de forma jerárquica.
- **`df`:** muestra el espacio libre disponible en el sistema.
- **`free`:** muestra información sobre memoria física, swap, buffer y caché.
- **`iptraf`:** muestra estadísticas de red en tiempo real.
- **`dstat`:** muestra estadísticas de Central Processing Unit (CPU), disco y estado del sistema.


### INSTALACIÓN DE HERRAMIENTAS

`iptraf` y `dstat` necesitan instalarse previamente.

```bash
sudo apt install iptraf
```
