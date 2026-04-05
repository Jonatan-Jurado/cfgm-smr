---
title: Tema 4
tags:
  - Virtualización
  - Software
  - SistemaOperativo
---
# Tema 4 - Máquinas Virtuales

## MÁQUINA REAL Y MÁQUINA VIRTUAL
- **[[maquina-real|Máquina Real]]:** El Sistema informático que tenemos físicamente, tiene el S.O que es con el que trabaja el User
- **[[maquina-virtual|Máquina Virtual]]:** Software que permite instalar nuevos S.O dentro del S.O de tu máquina real sin tener que hacer particiones de disco físicas.
	- *Dos Partes*:
		- *Anfitrión/Host*: S.O de la Máquina Real
		- *Huésped/Guess*: S.O que instalamos en la Máquina Virtual
	- Tipos:
		- *De Sistema*: Permiten instalar mas de un S.O y ejecutarlos a la vez
		- *De Proceso*:
			- Virtualiza 1 proceso
			- Sin S.O
			- Se aísla su aplicación
			- Se crea cuando se lanza aplicación y cierra cuando termina
			- Requiere recursos de la Máquina Física
			- Para crear aplicaciones Multiplataforma 
			- Ejemplo: *JVM Java Virttual Machine* 

**[[escenarios-duales|Dual-Boot o Arranque Dual]]:** 
- Es otra forma de tener mas de un S.O en el pc pero sin virtualizar
- Obliga a particionar el disco duro
- Entra al S.O con uno u otro, no puedes con los dos a la vez

> A veces si tu PC no tiene activada la Virtualización es necesario antes de virtualizar activarla en la BIOS. Normalmente en la parte de Seguridad o Configuración


### VENTAJAS Y DESVENTAJAS
#### VENTAJAS
- Aislamiento
- Seguridad
- Portabilidad
- Menos Hardwarte (Es compartido)
- Guardar Estado
- Crear Sistemas con una cantidad de recursos fijos
- Compartir archivos y directorios
- Entornos de Prueba
#### DESVENTAJAS
- Ralentiza la ejecución de programas
- Ralentiza el sistema

### SOFTWARE PARA CREAR MÁQUINAS VIRTUALES

| **Software**   | **Propietario** | **SO Anfitrión**              | **SO Invitado**                        | **Licencia / Notas clave**                                        |
| -------------- | --------------- | ----------------------------- | -------------------------------------- | ----------------------------------------------------------------- |
| **VirtualBox** | Oracle          | Windows, Linux, Mac, Solaris  | Windows, Linux, FreeBSD, MS-DOS        | Gratuita (Personal) y Privativa. Muy extendido.                   |
| **VMware**     | Dell            | Windows, Linux                | Windows, Linux (Ubuntu, Red Hat, etc.) | Gratuita (Player) y Privativa. Soporta x86 (32/64 bits).          |
| **Virtual PC** | Microsoft       | Windows                       | Windows, MS-DOS                        | Gratuita. **No recomendado para Linux** (muy lento).              |
| **Parallels**  | Parallels       | Mac OS (Intel)                | Windows, Linux, Mac OS                 | Pago (Prueba gratuita). Evita usar BootCamp.                      |
| **Hyper-V**    | Microsoft       | Windows (64 bits) / Server    | Windows (hasta 3 niveles)              | Gratuito (Incluido en Windows 8/10/Server).                       |
| **QEMU**       | Software Libre  | Windows (con interfaz), Linux | Casi todos (Windows, Linux, DOS, BSD)  | **Software Libre**. Sin interfaz nativa; emula hardware completo. |


## COMO USAR VIRTUALBOX

1. Descargar VirtualBox aquí : https://www.virtualbox.org/wiki/Downloads
2. Descargar el VirtualBox Extension Pack aquí: https://download.virtualbox.org/virtualbox/7.2.6/Oracle_VirtualBox_Extension_Pack-7.2.6.vbox-extpack
3. Descargar la ISO (Imágen de Disco) que quieras instalar (Solo busca ISO WIndows, ISO Ubuntu o la que requieras en Google, entra y descarga)
4. Instala VirtualBox
5. Instala el Extensión Pack 
6. **Guest Additions (Imprescindible)** :Sin esto, no podrás redimensionar la pantalla ni compartir el portapapeles.
	- Con la MV encendida, ve al menú superior: **Dispositivos > Insertar imagen de CD de complementos del invitado.
	- Abre el explorador de archivos en la MV, entra en la unidad de CD y ejecuta el instalador.
	- Reinicia la MV.    
7. **Carpetas Compartidas**: Para pasar archivos entre tu PC real y la MV:
	- **Configuración de la MV > Carpetas compartidas**.
		- Haz clic en el icono `+` (Añadir carpeta).
		- Selecciona la ruta de tu PC real y marca **"Automontar"** y **"Hacer permanente"**.
		- En Linux:_ Recuerda que tu usuario debe estar en el grupo `vboxsf` para verla: `sudo adduser $USER vboxsf`.
8. **Portapapeles y Arrastrar/Soltar**
- Ve a **Configuración > General > Avanzado**.
- Cambia "Compartir portapapeles" y "Arrastrar y soltar" a **Bidireccional**.

**TUTORIAL INSTALACIÓN + EXTENSION PACK**
<iframe width="560" height="315" src="https://www.youtube.com/embed/NuLLlBOQ_F0?si=1cHnSQ0rwY0yvaI5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


**TUTORIAL GUESS ADITIONS**

<iframe width="560" height="315" src="https://www.youtube.com/embed/Z3n2zTIgang?si=29D_YKU6k-qk3G6X" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## REALIZACIÓN DE PRUEBAS DE RENDIMIENTO
Una vez que tenemos nuestras máquinas virtuales nos interesa monitorizar el rendimiento, porqué de esa manera podemos comprobar si le hemos asignado los recursos suficientes comprobando la RAM/CPU/DISCO DURO etc.
Para ello podemos dar a la tecla de Windows y escribir Monitor de Recursos y lo abrimos, o podemos crear un archivo .bat que se ejecute al hacer click y se abra (Más Cómodo)
Para crear el archivo bat lo haremos así:
1. Abrimos el bloc de notas
2. Escribimos el siguiente código
```
@echo off
start resmon.exe
exit
```
3. Lo guardamos con el nombre que queramos y con extension .bat (nombre.bat)
4. Cada vez que queramos acceder al monitor de recursos solo abrimos el bat y listo!

## ERRORES COMUNES
**Operating System not Found**: Suele deberse a que no se indicó bien la ruta hacia el archivo ISO
**Unable to Open Kernel Device**: Revisa el atrchivo de configuración de la VM comprueba que:
	``` vmci0.present ="TRUE" ```
**This kernel requires an X86-64 cpu**: como indica el sistema que quieres instalar es de 64bits y seguramente tengas un S.O Anfitrión de 32bits 


## DOCUMENTACIÓN DEL PROCESO DE INSTALACIÓN E INCIDENCIAS

> Este documento técnico registra las especificaciones del entorno real y virtual, asegurando la trazabilidad de la instalación y las incidencias resueltas.

### 💻 1. Especificaciones del Sistema Anfitrión (Host)

_Datos del ordenador físico donde se instala el software de virtualización._

#### 🛠️ Hardware Real

- **Procesador:** (Ej: Intel Core i5-12400 / AMD Ryzen 5)
    
- **Memoria RAM Total:** (Ej: 16 GB DDR4)
    
- **Almacenamiento Total:** (Ej: 500 GB SSD NVMe)
    

#### 💿 Software Anfitrión

- **Sistema Operativo:** (Ej: Windows 11 / Ubuntu Desktop)
    
- **Versión:** (Ej: 23H2)
    
- **Arquitectura:** (Ej: x64)
    
- **Software de Virtualización:** (Ej: VirtualBox 7.0.12 / VMware Player)
    

---

### 🔲 2. Especificaciones de la Máquina Virtual (Guest)

_Configuración asignada y datos del sistema instalado._

#### ⚙️ Hardware Virtualizado

- **RAM Asignada:** (Ej: 4096 MB)
    
- **Espacio en Disco:** (Ej: 50 GB - Reservado dinámico)
    
- **Procesadores (Cores):** (Ej: 2 núcleos)
    

#### 📀 Sistema Operativo Huésped

- **Nombre:** (Ej: Windows 10 Pro / Debian 12)
    
- **Versión:** (Ej: 22H2)
    
- **Arquitectura:** (Ej: 64 bits)
    
- **Clave de Producto:** (Si aplica o "N/A - Licencia Libre")
    
- **Fecha y Hora de Instalación:** `YYYY-MM-DD` | `HH:MM`
    
- **Usuario Administrador:** * **Contraseña:** (¡No usar contraseñas personales!)
    
- **Licencias Adicionales:** (Ej: Guest Additions instaladas)
    

---

### ⚠️ 3. Registro de Incidencias y Observaciones

_Cualquier problema surgido durante el proceso y su solución._

|**ID**|**Incidencia (Problema)**|**Solución Aplicada**|**Estado**|
|---|---|---|---|
|01|Error de virtualización VT-x desactivada|Activar "Virtualization Technology" en la BIOS|✅ Solucionado|
|02|La pantalla no se ajusta al tamaño|Instalación de las Guest Additions|✅ Solucionado|