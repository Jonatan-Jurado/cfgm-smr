---
title: Tema 8
tags:
  - Particiones
  - SistemaArchivos
  - SistemaOperativo
  - Clonacion
  - GestorArranque
  - Linux
---
# INSTALACIÓN DE SISTEMAS OPERATIVOS LIBRES

## REQUISITOS
Los requisitos que vemos están  basados en Ubuntu Desktop 20.04 LTS.
- *CPU:* 1Ghz
- *RAM:* 1,5Gb
- *Disco Duro:* 7Gb

## SELECCIÓN DEL S.O
**Distribución Linux:** Es un conjunto de paquetes de software basados en el núcleo de Linux

A la hora de escoger el S.O debemos tener en cuanta las siguientes características:
- Estabilidad
- Administrador de Paquetes
- Necesidades
- *[[interfaz-grafica-de-usuario|GUI]]*

*Ubuntu:* 
- Basada en *Debian* 
- Buen GUI
- Entorno de escritorio [[entorno-de-escritorio-gnome|GNOME]] 

## MÉTODOS DE INSTALACIÓN Y PLANIFICACIÓN


Lo recomendable es que tenga ésta estructura:
### 📂 Esquema de Particionamiento en Ubuntu (MBR)

| Tipo de Partición | Punto de Montaje | Descripción Técnica                               | Archivos que contiene                         |
| :---------------- | :--------------- | :------------------------------------------------ | :-------------------------------------------- |
| **Primaria 1**    | `/boot`          | Partición de arranque.                            | Kernel (vmlinuz), Initrd y GRUB.              |
| **Primaria 2**    | `(Reservada)`    | Espacio para otro SO o uso del sistema.           | Archivos de sistema adicionales.              |
| **Primaria 3**    | `(Reservada)`    | Espacio para otro SO o uso del sistema.           | Archivos de sistema adicionales.              |


### 📂 Particiones Lógicas (Dentro de la Extendida)

| Nombre | Punto de Montaje | Descripción Técnica | Uso Principal |
| :--- | :--- | :--- | :--- |
| **Lógica 1** | `/` (Root) | Partición raíz del sistema operativo. | Binarios (`/bin`), Configuración (`/etc`), Librerías. |
| **Lógica 2** | `/home` | Espacio de usuario persistente. | Documentos, descargas y settings de usuario. |
| **Lógica 3** | `swap` | Área de intercambio de memoria. | Memoria virtual (no tiene sistema de archivos). |

### Cantidad de Swap Dependiendo de la Cantidad de RAM

| Cantidad de RAM en el Sistema | Cantidad recomendada de Espacio Swap |
| :--- | :--- |
| **Menos de 4 GB** | Como mínimo **2 GB** |
| **Entre 4 GB y 16 GB** | Como mínimo **4 GB** |
| **Entre 16 GB y 64 GB** | Como mínimo **8 GB** |
| **Entre 64 GB y 256 GB** | Como mínimo **16 GB** |
| **Entre 256 GB y 512 GB** | Como mínimo **32 GB** |
### Clonación
- *Reinicio y Restauración*
- *Equipamiento en nuevos PC's*
- *Actualización del Sistema*
- *Recuperación del Sistema*
- *Copia de Seguridad*

*Clonezilla:* El programa mas utilizado en Linux para Clonación.

## INSTALACIÓN DEL S.O Y CONFIGURACIÓN DE PARÁMETROS BÁSICOS
- *Planificación*: instrucciones a seguir / conocer el estado actual / Actualizar o Formatear?
- *Preparación*: Configuración de la BIOS para el arranque
- *Instalación*: Tipo de Instalación / Partición a utilizar
- *Configuración*: Aceptar Licencia / Zona Horaria, idioma, admin, etc
- *Documentación*: Cuaderno de Bitácora.


## SELECIÓN DE APLICACIONES A INSTALAR
- Dejar el PC listo para usar
- Instalar Drivers
- Instalar programas requeridos por el cliente y recomendable Antivirus (*ClaimAV*)


## ESCENARIOS DUALES
[[escenarios-duales|Dual-Boot]]: 
- Repartir espacio físico del disco para poder usar diferentes S.O en el mismo PC
- Una vez inicia el PC, la BIOS carga el gestor de arranque y permite elegir con que S.O queremos iniciar el sistema

## GESTOR DE ARRANQUE
Es el encargado de preparar todo para iniciar el sistema y cargarlo en memoria principal.
En Ubuntu los más usados son: 
- *GRUB*
- *LILO*
Para configurar el Gestor de Arranque hay que modificar el archivo que está en la siguiente ruta:
/etc/default/grub 

## NORMAS DE USO DEL SOFTWARE LIBRE
**Software Libre:** El software libre puede ser copiado, modificado, utilizado sin coste, puede tener cualquier fin y ser redistribuido.
*Características:*
- Modificar
- Estudiar
- Modificar
- Distribuir
- Mejorar y Publicar

## DOCUMENTACIÓN DEL PROCESO DE INSTALACIÓN E INCIDENCIAS

*[[cuaderno-de-bitacora|Cuaderno de Bitácora]]*: 

> Este documento técnico registra las especificaciones del entorno real y virtual, asegurando la trazabilidad de la instalación y las incidencias resueltas.

### Hardware
- Referencia del equipo
- Marca y Modelo
- CPU
- RAM
- Tarjeta Gráfica
- Tarjeta de Red
- Discos 

### Sistema Operativo
- Fecha
- Hora
- Nombre
- Versión
- Arquitectura
- User Admin
- Pass
- Licencias Instaladas
- Observaciones

Además hay que indicar que Software extra se ha instalado, antivirus, drivers, incidencias, soluciones etc.