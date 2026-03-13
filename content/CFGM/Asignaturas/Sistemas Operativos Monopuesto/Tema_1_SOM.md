---
title: Tema 1
tags:
  - SistemaOperativo
  - Hardware
  - Software
  - CPU
  - Memoria
  - Arquitectura
---

#  Sistemas Operativos y Utilidades
## **Sistema Informático: Componentes Físicos** 
aquel que nos permite almacenar y procesar información.

### **Partes:**
- *[[hardware-y-software|Hardware]]:* lo tangible
	- *Firmware:* En la ROM - Instrucciones Pre-grabadas
		- *POST Power on Self Test:* Revisa que los Componentes esenciales funcionen
- *[[hardware-y-software|Software]]:* Parte Intangible.
- *[[cuenta-de-usuario|Usuario]]*: 
	- *Final*
	- *Admin*

### **Clasificación**
- **Uso:**
	- *Específico:* TPV/ Controladores Aéreos..
	- *General*: PC /Móvil/TV/Consola..
	 
- **Función:**
	- *[[arquitectura-mimd|MIMD]]:* Múltiples Instrucciones Múltiples Datos
	- *[[arquitectura-simd|SIMD]]:* Una Instrucción Múltiples Instrucciones
	- *[[arquitectura-sisd|SISD]]:* Una Instrucción Un Dato
	- *[[arquitectura-misd|MISD]]:* Múltiples  Instrucciones Un Dato

## **Hardware:**
- *Componentes:* Forman parte del PC
- *[[periferico|Periféricos]]:* Ajenos al Sistema, aportan funcionalidad.

### **Arquitectura de Von Neumman:** 
Para que todo funcione se sigue ésta arquitectura en la que:
- *[[unidad-central-de-procesamiento|CPU]]:* Es el cerebro que orquesta todo
	- *UC:* 'Unidad Central' Busca instrucciones en la Memoria principal, las interpreta y las ejecuta.
	- *ALU:* 'Unidad Aritmético-Lógica' ejecuta Operaciones entre datos de los [[unidad-aritmetico-logica|Unidad lógica]].

![[Pasted-image-20260311235804.png]]


### MEMORIA
Las características más importantes que las definen son su capacidad, velocidad y coste por Bit.
**Tipos:**
- *Memoria Interna:* Dentro del Pc
	- *Registros:* poca capacidad - alta velocidad de acceso.
	- *[[memoria-cache|Cache]]:* 
		- Almacena datos mas usados por el procesador. 
		- Reduce el Tiempo de acceso
		- Agiliza CPU.
		- Cuando el equipo lo requiere almacena datos en caché y en siguientes accesos comprueba si está disponible 
	- *[[memoria-ram|RAM]]:* 
		- [[extension-de-archivo|Extensión]] de la caché, si CPU no encuentra dato en caché va a la RAM
		- Son Volátiles
		- Cuando la RAM se llena el [[disco-duro|Disco duro]] destina una parte suya a cumplir sus funciones (Se nota porqué se relentiza el PC)
		- *Tipos:*
			- *Estáticas:* Mantienen los Datos
			- *Dinámicas:* Pueden perder Info

![[Pasted-image-20260311235827.png]]



### BUSES
Interconexión entre CPU y demás componentes.
**Tipos:**
- *Datos:* intercambian datos entre  CPU y el resto de los componentes del sistema.
- *Direcciones:* transportar direcciones de memoria desde CPU a memoria principal
- *Control:* transportan las órdenes de la CPU

## Software

### Según Función
- *[[software-de-aplicacion|Software de aplicación]]:* Orientado a Usuarios (Ofimática..)
- *[[software-de-programacion|Software de programación]]:*  Software Orientado a desarrolladores (IDE's, Compiladores ..)
- *[[software-de-sistema|Software de sistema]]:* Son los [[sistema-operativo|sistemas operativos]] y las diferentes [[herramientas-para-el-montaje|herramientas]] de [[monitoreo-y-optimizacion|optimización]] y diagnóstico
- *Software Base:* Controla el Hardware
	- *[[bios-y-uefi|BIOS]]:* 
		- 'Firmware' almacenado en un circuito de la [[placa-base|Placa base]] 
		- Primero que se ejecuta cuando arranca el equipo
		- Inicia el PC - Comprueba Hardware - Carga el [[gestor-de-arranque|Gestor de arranque]]
	- *[[bios-y-uefi|UEFIBIOS]]:* 
		- Moderno
		- 32-64Bits
		- Configurar '*[[secure-boot|Secure Boot]]*'
		- Agiliza el Arranque

### Sistema Operativo
Es un conjunto de ordenes y [[software-y-algoritmo|programas]] que controlan los procesos básicos del PC y permiten un funcionamiento de otros programas.
#### Elementos del S.O
- *[[nucleo-del-sistema-operativo|Kernel]]:* 
	- Control de procesos
	- Control de Memoria
- *[[interprete-de-comandos|Intérprete de comandos]] CLI:* "[[interprete-de-comandos|Shell]]" traduce órdenes que introduce el user al PC parta que haya una comunicación S.O - User
- *[[sistema-de-archivos|Sistema de archivos]]:* 
	- Almacena la información
	- Establece Jerarquias (FAT, [[sistema-de-archivos-ntfs|NTFS]], ext4..)

#### Funciones del S.O
- *Gestionar CPU:* Reparte cada Proceso que se está ejecutando
- *Gestionar RAM:*  
	- Asigna espacio de memoria a cada [[aplicacion|Aplicación]]
	- Crea [[gestion-de-la-memoria-mediante-memoria-virtual|Memoria virtual]] en el disco duro para adaptar sus funciones
- *Gestionar la Entrada/Salida:* Mediante [[controlador-de-dispositivo|Drivers]] controla la E/S de datos y acceso a programas.
- *Gestionar Procesos:* Crear, Ejecutar, Suspender, Reanudar, Matar Procesos
- *Gestionar [[permiso-de-archivo|Permisos]]:* Lectura, Escritura, Ejecución 
- *Gestionar Archivos:* Gestiona los permisos que los Usuarios tienen sobre el Archivo.
- *Gestionar Información:* Proporciona toda la info para que la máquina funcione.

#### Arquitectura del S.O

**7 Capas**
![[public/media/fr.png]]

**3 Capas**
![[fre.png]]


**Tipos:**
- *Monolítica:* 
	- S.O Un solo [[nucleo|Núcleo]]
	- Recoge todos los Servicios del Sistema
	- Todas las Peticiones en un solo Programa
	- EJ: [[sistema-operativo-linux|Linux]], Unix, MS-DOS..
- *[[micronucleo|Micronúcleo]]:* 
	- Recoge las Funciones mas básicas del S.O
	- Si quieres añadir Funciones se hace de forma Modular
	- *Ventajas:*
		- Mejor [[seguridad-y-gestion-de-identidad|Seguridad]] 
		- Mejor Portabilidad
	- *Desventajas:*
		- Peor Tiempo [[respuesta-en-ciberseguridad|Respuesta]] 
		- Menos Comunicación entre Hardware y Controladores
- *Híbrido:*
	- Mejor Comunicación entre Hardware y Controladores
	- Mejor Gestión de llamadas al Sistema
	- Ej: [[sistema-operativo-windows|Windows]], MacOS..
- *[[exonucleo|Exonúcleo]]:* 
	- Más moderno
	- El núcleo contiene una parte básica de [[gestion-de-recursos|Gestión de recursos]] 
	- El desarrollador mediante librerías, añade nuevos módulos.
	- Esto libera de carga de memoria de procesamiento al núcleo y mejora la comunicación con el software


#### Clasificación
##### Según Procesos
- *[[sistema-operativo-monotarea|Monotarea]]*
- *[[sistema-operativo-multitarea|Multitarea]]*
##### Según Usuarios
- *[[sistema-operativo-monousuario|Monousuario]]*
- *[[sistema-operativo-multiusuario|Multiusuario]]*
##### Según Recursos
- *Centralizados*
- *Doistribuidos*
##### Según Licencia
- *Propietario*
- *Libre*

#### Evolución de los S:O
- *[[memory-stick|MS]]-DOS:*
	- En los '80
	- Microsoft
	- [[nucleo-monolitico|Núcleo Monolítico]]
	- Uso mediante CLI
- *MacOS:*
	- Por Sun Microsystems
	- Basado en Unix
	- Muchas Workstations y Servers de los 90'
- *[[windows-95|Windows 95]]:* 
	- Primero con [[interfaz-grafica-de-usuario|Interfaz]] Gráfica
- *Linux:*
	- Creador: Linus Torvalds
	- Combina [[nucleo-linux|Kernel Linux]] y S.O [[gnu-linux|GNU]]
	- Escrito en 'C'

### Sistemas Transaccionales
Su función es recolectar, almacenar, modificar y recuperar la información generada por las [[transaccion|transacciones]] de una organización.
**[[test-acid|Test ACID]]**
- *Atomicidad:* La Transacción no puede quedarse a medias.
- *Consistencia:* Normas para no romper la [[blu-ray-disc|BD]]
- *Aislamiento:* Las Transacciones no interfieren unas con otras
- *Durabilidad:* No es Vulnerable sis e producen fallos

### Sistema por Lotes
Las operaciones son realizadas una a una: si una falla, el programa finaliza, pero los cambios realizados quedan operativos. 
Este tipo de sistemas son utilizados en los [[archivo-de-respuesta|Script]].

*Script:* texto plano con instrucciones para realizar en el sistema, las cuales serán ejecutadas mediante el Procesamiento por Lotes con la línea de comandos