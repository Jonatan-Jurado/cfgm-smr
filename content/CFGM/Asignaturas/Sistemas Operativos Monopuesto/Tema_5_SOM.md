---
title: Tema 5
tags:
  - Windows
  - Particiones
  - SistemaArchivos
  - SistemaOperativo
---
# INSTALACIÓN DE LOS SISTEMAS OPERATIVOS PROPIETARIO

## REQUISITOS
**[[requisito-minimo|Requisitos Mínimos]]**: Los necesarios para instalar el S.O
**[[requisito-recomendado|Requisitos Recomendados]]**: Los no necesarios pero recomendables para exprimir el S.O

**Win 10 32bit**
- *[[unidad-central-de-procesamiento|CPU]]*: 1Ghz
- *[[memoria-ram|RAM]]*: 1Gb
- *Espacio Libre*: 16Gb
- *Gráfica*: DirectX9 con controlador WDDM o superior  
**Win 10 64bit**
- *CPU*: 1Ghz
- *RAM*: 2Gb
- *Espacio Libre*: 20Gb
- *Gráfica*: DirectX9 con controlador WDDM o superior  

## SELECCIÓN DEL S.O
Según las necesidades del cliente:
1. Que [[aplicacion|aplicaciones]] necesita?
2. Necesita S.O Cliente o Server?
3. Version? [[directorio-home|Home]]/Pro/Enterprise/Education ?

## MÉTODOS DE INSTALACIÓN
Es necesario tener al menos 1 [[particion-de-disco-duro|partición]]
### Tipos de Particiones
- *Primaria*: S.O
- *Extendida*: Almacenamiento
- *Lógica*: Para dividir la Primaria y la Extendida
### Particiones del S.O
- *Arranque o [[directorio-boot|Boot]]*: Ficherod del [[directorios-importantes-de-windows|directorio de Windows]] para iniciar el S.O
- *System*: [[gestor-de-arranque|Gestor de arranque]] y configuración de arranque *BCD*
### Clonación
- *Reinicio y Restauración*
- *Equipamiento en nuevos PC's*
- *[[actualizacion-del-sistema|Actualización del Sistema]]*
- *[[modo-rescate|Recuperación del Sistema]]*
- *[[copias-de-seguridad|Copia de Seguridad]]*
- *[[documentacion-tecnica|Documentación]]*: [[cuaderno-de-bitacora|Cuaderno de Bitácora]]

## INSTALACIÓN DEL S.O Y CONFIGURACIÓN DE PARÁMETROS BÁSICOS
- *Planificación*: instrucciones a seguir / conocer el estado actual / Actualizar o [[formateo-de-disco|Formatear]]?
- *Preparación*: [[configuracion-de-la-bios|Configuración de la BIOS]] para el arranque
- *Instalación*: Tipo de Instalación / [[particion|Partición]] a utilizar
- *Configuración*: Aceptar Licencia / Zona Horaria, idioma, admin, [[directorio-etc|etc]]

## SELECIÓN DE APLICACIONES A INSTALAR
- Dejar el PC listo para usar
- Instalar [[controlador-de-dispositivo|Drivers]]
- Instalar [[software-y-algoritmo|programas]] requeridos por el cliente y recomendable [[Antivirus]]

## ESCENARIOS DUALES
[[escenarios-duales|Dual-Boot]]: 
- Repartir espacio físico del disco para poder usar diferentes S.O en el mismo PC
- Una vez inicia el PC, la BIOS carga el gestor de arranque y permite elegir con que S.O queremos iniciar el sistema

## GESTOR DE ARRANQUE
Es el encargado de preparar todo para iniciar el sistema y cargarlo en memoria principal
PC enciende -> BIOS comprueba Hardware -> Transfiere el control al [[registro-de-arranque-maestro|Registro de arranque maestro]] *[[master-boot-record|MBR]]* 

**Configuración**
**[[windows-xp|Windows XP]]**:
- **Gestor de arranque**: NTLDR
- **Archivo de configuración**: [[bootini|Boot.ini]]
**[[sistema-operativo-windows|Windows]] Vista / 7**:
- **Gestor de arranque**: [[BOOTMGR]]
- **Archivo de configuración**: BCD (Modificable con **BCDEDIT**)
**Windows 8 / 10 / 11**:
- **Interfaz de arranque**: **UEFI** (Sustituye a la BIOS antigua y permite el **[[secure-boot|Secure Boot]]**).
- **Gestor de arranque**: **bootmgfw.efi** (Es la versión de BOOTMGR para sistemas UEFI).
- **Archivo de configuración**: BCD (Ubicado en la partición oculta **EFI**).

## NORMAS DE USO DEL SOFTWARE PROPIETARIO
### Software Propietario
- *[[propiedad-intelectual|Propiedad Intelectual]]*: Derecho del autor en relación con el software creado
- *[[derecho-de-autor|Derechos de Autor]]*:
	- *Morales:* Definen quien a sido el creador
	- *Patrimoniales*: derecho a no permitir la distribución ni modificación además de poder cobrar por su uso

### Licencias
- *[[licencia-oem|OEM]]*: 
	- Nº de licencia vía email
	- 1 Instalación / 1 PC
- *[[licencia-oem-coa|OEM COA]]*
	- Nº de licencia en etiqueta (normalmente en el mismo PC)
	- 1 Instalación / 1 PC
- *[[licencia-oembox|OEMBOX]]*:
	- Nº de licencia en DVD
	- 1 Instalación / 1 PC
- *[[licencia-retail|RETAIL]]*
	- Nº de licencia en DVD
	- Permite varias instalaciones (pero no a la vez funcionando)
	- Permite modificaciones de hardware (desactivar, modificar y volver a activar)

