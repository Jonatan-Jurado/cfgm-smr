---
title: Tema 5
tags:
  - Windows
  - Particiones
---
# INSTALACIÓN DE LOS SISTEMAS OPERATIVOS PROPIETARIO

## REQUISITOS
**Requisitos Mínimos**: Los necesarios para instalar el S.O
**Requisitos Recomendados**: Los no necesarios pero recomendables para exprimir el S.O

**Win 10 32bit**
- *CPU*: 1Ghz
- *RAM*: 1Gb
- *Espacio Libre*: 16Gb
- *Gráfica*: DirectX9 con controlador WDDM o superior  
**Win 10 64bit**
- *CPU*: 1Ghz
- *RAM*: 2Gb
- *Espacio Libre*: 20Gb
- *Gráfica*: DirectX9 con controlador WDDM o superior  

## SELECCIÓN DEL S.O
Según las necesidades del cliente:
1. Que aplicaciones necesita?
2. Necesita S.O Cliente o Server?
3. Version? Home/Pro/Enterprise/Education ?

## MÉTODOS DE INSTALACIÓN
Es necesario tener al menos 1 partición
### Tipos de Particiones
- *Primaria*: S.O
- *Extendida*: Almacenamiento
- *Lógica*: Para dividir la Primaria y la Extendida
### Particiones del S.O
- *Arranque o Boot*: Ficherod del directorio de Windows para iniciar el S.O
- *System*: Gestor de arranque y configuración de arranque *BCD*
### Clonación
- *Reinicio y Restauración*
- *Equipamiento en nuevos PC's*
- *Actualización del Sistema*
- *Recuperación del Sistema*
- *Copia de Seguridad*

## INSTALACIÓN DEL S.O Y CONFIGURACIÓN DE PARÁMETROS BÁSICOS
- *Planificación*: instrucciones a seguir / conocer el estado actual / Actualizar o Formatear?
- *Preparación*: Configuración de la BIOS para el arranque
- *Instalación*: Tipo de Instalación / Partición a utilizar
- *Configuración*: Aceptar Licencia / Zona Horaria, idioma, admin, etc

## SELECIÓN DE APLICACIONES A INSTALAR
- Dejar el PC listo para usar
- Instalar Drivers
- Instalar programas requeridos por el cliente y recomendable Antivirus

## ESCENARIOS DUALES
[[escenarios-duales|Dual-Boot]]: 
- Repartir espacio físico del disco para poder usar diferentes S.O en el mismo PC
- Una vez inicia el PC, la BIOS carga el gestor de arranque y permite elegir con que S.O queremos iniciar el sistema

## GESTOR DE ARRANQUE
Es el encargado de preparar todo para iniciar el sistema y cargarlo en memoria principal
PC enciende -> BIOS comprueba Hardware -> Transfiere el control al Registro de arranque maestro *[[registro-de-arranque-maestro|MBR]]* 

**Configuración**
**Windows XP**:
- **Gestor de arranque**: NTLDR
- **Archivo de configuración**: Boot.ini
**Windows Vista / 7**:
- **Gestor de arranque**: BOOTMGR
- **Archivo de configuración**: BCD (Modificable con **BCDEDIT**)
**Windows 8 / 10 / 11**:
- **Interfaz de arranque**: **UEFI** (Sustituye a la BIOS antigua y permite el **Secure Boot**).
- **Gestor de arranque**: **bootmgfw.efi** (Es la versión de BOOTMGR para sistemas UEFI).
- **Archivo de configuración**: BCD (Ubicado en la partición oculta **EFI**).

## NORMAS DE USO DEL SOFTWARE PROPIETARIO
### Software Propietario
- *Propiedad Intelectual*: Derecho del autor en relación con el software creado
- *Derechos de Autor*:
	- *Morales:* Definen quien a sido el creador
	- *Patrimoniales*: derecho a no permitir la distribución ni modificación además de poder cobrar por su uso

### Licencias
- *OEM*: 
	- Nº de licencia vía email
	- 1 Instalación / 1 PC
- *OEM COA*
	- Nº de licencia en etiqueta (normalmente en el mismo PC)
	- 1 Instalación / 1 PC
- *OEMBOX*:
	- Nº de licencia en DVD
	- 1 Instalación / 1 PC
- *RETAIL*
	- Nº de licencia en DVD
	- Permite varias instalaciones (pero no a la vez funcionando)
	- Permite modificaciones de hardware (desactivar, modificar y volver a activar)

