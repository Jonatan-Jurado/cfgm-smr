---
title: Tema 9
tags:
  - Linux
---
# REALIZACIÓN DE TAREAS BÁSICAS DE CONFIGURACIÓN Y MANTENIMIENTO SOBRE SISTEMAS OPERATIVOS LIBRES
## ARRANQUE DEL SISTEMA

**Niveles de ejecución** (del 0 al 6):

- **0** - Detiene el sistema
- **1** - Modo monousuario (Administración)
- **2** - Multiusuario local con red, sin servicios
- **3** - Multiusuario completo con red
- **4** - No se utiliza
- **5** - Multiusuario completo con red e interfaz gráfica (nivel por defecto)
- **6** - Reinicio

El proceso de arranque carga código en memoria → comprueba hardware → monta ficheros → lanza el proceso `init`, que lee `/etc/inittab` para saber qué nivel ejecutar.

### Parada del sistema

Finaliza servicios, desmonta unidades y el sistema de archivos. Necesario al cambiar de nivel o ante sobrecarga.

### Sesiones

Cada usuario tiene su propio escritorio y configuración. Los recursos y permisos dependen del tipo de usuario.

---

## UTILIZACIÓN DEL S.O

Se puede usar de forma gráfica o mediante comandos:

- **Modo Gráfico**: Ventanas, interacción con ratón. Ubuntu usa **GNOME**.
- **Modo Consola**: Consume menos recursos (RAM). En Linux se prefiere por seguridad.

---

## INTERFACES DE USUARIO

Basadas en el **Sistema de ventanas X**. Tipos de entornos de escritorio:

- **GNOME**: Intuitivo, personalización de apariencia, resoluciones y temas.
- **KDE**: Altamente modificable por el usuario (menús, botones, diálogos).
- **Unity**: Para Ubuntu, escalable a móviles, corre sobre GNOME.
- **XFCE**: Gestor de ventanas, ajuste de resolución y refresco de pantalla.
- **LXDE**: Bajo consumo de energía y recursos.

### Accesibilidad (en GNOME)

- **Orca**: Para discapacidad visual, aumenta textos y permite lectura en braille/voz.
- Control de velocidad del ratón y repetición de teclas para problemas de movilidad.
- Ajuste de contraste y brillo de pantalla.
- Comandos de voz integrados para consola.

---
## COMANDOS BÁSICOS
<iframe width="560" height="315" src="https://www.youtube.com/embed/8y5bMyW9XUA?si=A7bLpBaEI1lhpIP5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## OPERACIONES CON ARCHIVOS

Los archivos tienen el formato → `nombre.extensión` — Ejemplo → `mi_archivo.txt`

### Comodines

- **`?`** → Sustituye a un único carácter.
- **`*`** → Sustituye a varios caracteres.

### Operaciones más comunes

#### Operaciones con directorios

- **Crear directorio**: `mkdir NuevaCarpeta`
- **Cambiar de directorio**: `cd /ruta/destino`
- **Listar contenido**:
    - Lista normal: `ls`
    - En modo lista: `ls -l`
    - Incluir ocultos: `ls -a`
- **Copiar directorio**: `cp`
- **Mover directorio**: `mv CarpetaOrigen RutaDestino`
- **Eliminar directorio**: `rm`

#### Operaciones con ficheros

- **Crear fichero**: `touch archivo.txt`
- **Abrir/Leer fichero**: `cat archivo.txt` o `more archivo.txt`
- **Copiar fichero**: `cp`
- **Mover fichero**: `mv`
- **Eliminar fichero**: `rm archivo.txt`

### Permisos y atributos

Tres tipos de permiso: **R** (lectura) · **W** (escritura) · **X** (ejecución)
<iframe width="560" height="315" src="https://www.youtube.com/embed/MbdJ42OKdf8?si=vAv2JnQKd4kG9sP8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Se gestionan con `chmod`. El comando `ls -l` muestra 10 dígitos: el primero indica si es directorio (`d`), los 9 siguientes se dividen en 3 bloques (propietario / grupo / resto).

**Modo octal**: R=4, W=2, X=1 → se suman. Ej: `chmod 755 archivo`
![[Pasted image 20260419205335.png]]

**Modo carácter**: `chmod u+x archivo`

- Grupos: `u` (propietario), `g` (grupo), `o` (resto)
- Operaciones: `+` añadir, `-` eliminar, `=` sobreescribir

### Estructura del árbol de directorios

Directorio raíz único: `/`

- `/bin` → Comandos básicos del sistema (`cd`, `cat`…)
- `/sbin` → Comandos de administración
- `/boot` → Ficheros de arranque
- `/dev` → Ficheros de dispositivos
- `/etc` → Ficheros de configuración
- `/home` → Carpetas personales de usuarios
- `/root` → Directorio personal del usuario root
- `/lib` → Librerías básicas
- `/mnt` y `/media` → Montaje de dispositivos (USB, CD…)
- `/proc` → Información del kernel (sistema virtual)
- `/var` → Ficheros de tamaño variable (logs…)
- `/usr` → Aplicaciones no relacionadas directamente con el S.O
- `/tmp` → Información temporal de sesión (acceso para todos)
- `/lost+found` → Ficheros recuperados tras fallo (`fsck`)
- `/opt` → Paquetes adicionales de aplicaciones
- `/srv` → Información de servicios (FTP, HTTP…)
- `/sys` → Información de dispositivos vista por el kernel

### Rutas

- **Absoluta**: Desde la raíz. Ej: `/home/usuario/documentos`
- **Relativa**: Desde la ubicación actual. Ej: `../documentos`

---

## COMPRESIÓN Y DESCOMPRESIÓN DE ARCHIVOS

Comprimir es reducir el tamaño sin perder información.

**Comando `gzip` / `gunzip`**: Comprime en formato `.gz`. No admite directorios.

- Máxima compresión: `gzip -9 archivo.txt`
- Descomprimir: `gzip -d archivo.gz`

**Comando `tar`**: Empaqueta varios archivos en uno (formato `.tar`).

- `-f` → nombre del archivo final
- `-c` → crear nuevo archivo
- `-x` → extraer contenido
- `-v` → mostrar operaciones en pantalla
- `-t` → testear contenido
- `-u` → añadir a archivo existente

---

## ACTUALIZACIÓN DEL S.O

_Consola_ (requiere permisos root):

- Comprobar actualizaciones disponibles: `sudo apt-get update`
- Aplicar actualizaciones: `sudo apt-get upgrade`

_Aplicación gráfica_: "Actualización de Software" → asistente visual. Requiere conexión a internet estable. Al finalizar puede pedir reinicio.

---

## AGREGAR / CONFIGURAR / ELIMINAR / ACTUALIZAR PROGRAMAS

El software en GNU/Linux se distribuye en **paquetes** gestionados por un gestor de paquetes.

- **RPM**: De Red Hat, usado en Fedora, Mandriva, openSUSE. Resuelve dependencias automáticamente y cifra los paquetes.
- **APT**: De Debian, usado en Debian y Ubuntu.
    - Descargar: `apt`
    - Instalar: `apt install paquete`
    - Desinstalar: `apt remove paquete`
- **Synaptic**: Gestor gráfico, se instala vía `apt`. Más información y control sobre los paquetes.

---

## CONFIGURAR PERIFÉRICOS

Linux gestiona periféricos mediante ficheros especiales en `/dev`. En Ubuntu recientes, la detección es automática (asistente al conectar el dispositivo).

Configuración manual por terminal:

1. Crear directorio: `sudo mkdir /media/usb`
2. Listar dispositivos: `ls -l /dev/sd*`
3. Montar dispositivo:
    - FAT: `mount -t vfat /dev/sde1 /media/usb`
    - NTFS: `mount -t ntfs-3g /dev/sde1 /media/usb`
4. Desmontar: `umount /media/usb`

---

## INVENTARIO DEL SOFTWARE INSTALADO

Ver todos los programas instalados:

```
dpkg --get-selections
```

Exportar a fichero de texto:

```
dpkg --get-selections > lista_programas.txt
```

Desinstalar un programa:

```
sudo apt-get remove NombrePrograma
```

---

## COMPROBAR EL FUNCIONAMIENTO DE LAS CONFIGURACIONES

Comandos de diagnóstico de hardware:

- Dispositivos PCI: `lspci`
- Dispositivos USB: `lsusb`
- Hardware resumido: `sudo lshw -short`
- Hardware completo: `sudo lshw | less`
- Particiones: `sudo fdisk -l`
- Audio: `aplay -l | grep -i tarjeta`
- Espacio en disco: `df -h`

Herramientas gráficas de diagnóstico: `hardinfo` y `sysinfo`

```
sudo apt-get install hardinfo
sudo apt-get install sysinfo
```

---

## DOCUMENTACIÓN DEL PROCESO DE CONFIGURACIÓN

Antes de instalar cualquier programa, revisar la documentación técnica del fabricante. Incluir guía de configuración del proceso de instalación y parámetros recomendados. Puede ser **Configuración Recomendada** o **Instalación Personalizada**.