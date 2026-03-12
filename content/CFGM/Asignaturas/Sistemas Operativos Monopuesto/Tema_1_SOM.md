---
title: Caracterización de los S.O y Aplicaciones
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
- *[[Hardware]]:* lo tangible
	- *[[Firmware]]:* En la ROM - Instrucciones Pre-grabadas
		- *[[POST]] Power on Self Test:* Revisa que los [[Componentes del Hardware|componentes]] esenciales funcionen
- *[[Software]]:* Parte Intangible.
- *[[Usuario]]*: 
	- *Final*
	- *Admin*

### **Clasificación**
- **Uso:**
	- *Específico:* TPV/ [[Controlador|Controladores]] Aéreos..
	- *General*: PC[[Directorio raíz|/]]Móvil/TV/Consola..
	 
- **Función:**
	- *[[MIMD]]:* Múltiples Instrucciones Múltiples Datos
	- *[[SIMD]]:* Una Instrucción Múltiples Instrucciones
	- *[[SISD]]:* Una Instrucción Un Dato
	- *[[MISD]]:* Múltiples  Instrucciones Un Dato

## **Hardware:**
- *Componentes:* Forman parte del PC
- *[[Periférico|Periféricos]]:* Ajenos al Sistema, aportan funcionalidad.

### **Arquitectura de Von Neumman:** 
Para que todo funcione se sigue ésta arquitectura en la que:
- *[[Microprocesador|CPU]]:* Es [[Economía Lineal|el]] cerebro que orquesta todo
	- *UC:* 'Unidad Central' Busca instrucciones en la Memoria principal, las interpreta y las ejecuta.
	- *ALU:* 'Unidad Aritmético-Lógica' ejecuta Operaciones entre datos de los [[Registros del Procesador|Registros]].

![[Pasted image 20260311235804.png]]


### MEMORIA
Las características más importantes que las definen son su [[Capacidades|capacidad]], velocidad y coste por [[Bit]].
**Tipos:**
- *Memoria Interna:* Dentro del Pc
	- *Registros:* poca capacidad - alta velocidad de acceso.
	- *[[Memoria caché|Caché]]:* 
		- Almacena datos mas usados por el procesador. 
		- Reduce el Tiempo de acceso
		- Agiliza CPU.
		- Cuando el equipo lo requiere almacena datos en caché y en siguientes accesos comprueba si está disponible 
	- *[[RAM]]:* 
		- [[Extensión de archivo|Extensión]] de la caché, si CPU no encuentra dato en caché va a la RAM
		- Son Volátiles
		- Cuando la RAM se llena el [[Disco duro]] destina una parte suya a cumplir sus funciones (Se nota porqué se relentiza el PC)
		- *Tipos:*
			- *Estáticas:* Mantienen los Datos
			- *Dinámicas:* Pueden perder Info

![[Pasted image 20260311235827.png]]



### BUSES
Interconexión entre CPU y demás componentes.
**Tipos:**
- *Datos:* intercambian datos entre  CPU y el resto de los componentes del sistema.
- *Direcciones:* transportar direcciones de memoria desde CPU a memoria principal
- *Control:* transportan las órdenes de la CPU

## Software

### Según Función
- *[[Software de aplicación]]:* Orientado a Usuarios (Ofimática..)
- *[[Software de programación]]:*  Software Orientado a desarrolladores (IDE's, Compiladores ..)
- *[[Software de sistema]]:* Son los [[Sistema operativo|sistemas operativos]] y las diferentes [[Herramientas para el montaje|herramientas]] de [[Monitoreo y optimización|optimización]] y diagnóstico
- *Software Base:* Controla el Hardware
	- *[[BIOS]]:* 
		- 'Firmware' almacenado en un circuito de la [[Placa base]] 
		- Primero que se ejecuta cuando arranca el equipo
		- Inicia el PC - Comprueba Hardware - Carga el [[Gestor de arranque]]
	- *[[UEFIBIOS]]:* 
		- Moderno
		- 32-64Bits
		- Configurar '*[[Secure Boot]]*'
		- Agiliza el Arranque

### Sistema Operativo
Es un conjunto de ordenes y [[Software y algoritmo|programas]] que controlan los [[Proceso|procesos]] básicos del PC y permiten un funcionamiento de otros programas.
#### Elementos del S.O
- *[[Núcleo del Sistema Operativo|Kernel]]:* 
	- Control de procesos
	- Control de Memoria
- *[[Intérprete de comandos]] CLI:* "[[Shell]]" traduce órdenes que introduce el user al PC parta que haya una comunicación S.O - User
- *[[Sistema de archivos]]:* 
	- Almacena la información
	- Establece Jerarquias (FAT, [[NTFS]], ext4..)

#### Funciones del S.O
- *Gestionar CPU:* Reparte cada Proceso que se está ejecutando
- *Gestionar RAM:*  
	- Asigna espacio de memoria a cada [[Aplicación]]
	- Crea [[Gestión de la memoria mediante memoria virtual|Memoria virtual]] en el disco duro para adaptar sus funciones
- *Gestionar la Entrada/Salida:* Mediante [[Drivers]] controla la E/S de datos y acceso a programas.
- *Gestionar Procesos:* Crear, Ejecutar, Suspender, Reanudar, Matar Procesos
- *Gestionar [[Permisos]]:* Lectura, Escritura, Ejecución 
- *Gestionar [[Archivo|Archivos]]:* Gestiona los permisos que los Usuarios tienen sobre el Archivo.
- *Gestionar Información:* Proporciona toda la info para que la máquina funcione.

#### Arquitectura del S.O

**7 Capas**
![[fr.png]]
**3 Capas**
![[fre.png]]


**Tipos:**
- *Monolítica:* 
	- S.O Un solo [[Núcleo]]
	- Recoge todos los [[Servicio|Servicios]] del Sistema
	- Todas las Peticiones en un solo Programa
	- EJ: [[Sistema Operativo Linux|Linux]], Unix, [[MS-DOS]]..
- *[[Micronúcleo]]:* 
	- Recoge las Funciones mas básicas del S.O
	- Si quieres añadir Funciones se hace de forma Modular
	- *Ventajas:*
		- Mejor [[Seguridad y gestión de identidad|Seguridad]] 
		- Mejor Portabilidad
	- *Desventajas:*
		- Peor Tiempo [[Respuesta en Ciberseguridad|Respuesta]] 
		- Menos Comunicación entre Hardware y Controladores
- *Híbrido:*
	- Mejor Comunicación entre Hardware y Controladores
	- Mejor Gestión de llamadas al Sistema
	- Ej: [[Windows]], MacOS..
- *[[Exonúcleo]]:* 
	- Más moderno
	- El núcleo contiene una parte básica de [[Gestión de recursos]] 
	- El desarrollador mediante librerías, añade nuevos módulos.
	- Esto libera de carga de memoria de procesamiento al núcleo y mejora la comunicación con el software


#### Clasificación
##### Según Procesos
- *[[Sistema operativo monotarea|Monotarea]]*
- *[[Sistema operativo multitarea|Multitarea]]*
##### Según Usuarios
- *[[Sistema operativo monousuario|Monousuario]]*
- *[[Sistema operativo multiusuario|Multiusuario]]*
##### Según Recursos
- *Centralizados*
- *Doistribuidos*
##### Según Licencia
- *Propietario*
- *Libre*

#### Evolución de los S:O
- *[[Memory Stick|MS]]-DOS:*
	- En los '80
	- Microsoft
	- [[Núcleo Monolítico]]
	- Uso mediante CLI
- *MacOS:*
	- Por Sun Microsystems
	- Basado en Unix
	- Muchas Workstations y Servers de los 90'
- *[[Windows 95]]:* 
	- Primero con [[Interfaz]] Gráfica
- *Linux:*
	- Creador: Linus Torvalds
	- Combina [[Núcleo Linux|Kernel Linux]] y S.O [[GNU]]
	- Escrito en 'C'

### Sistemas Transaccionales
Su función es recolectar, almacenar, [[Modding|modificar]] y recuperar la información generada por las [[Transacción|transacciones]] de una organización.
**[[Test ACID]]**
- *Atomicidad:* La Transacción no puede quedarse a medias.
- *Consistencia:* Normas para no romper la [[Blu-ray Disc|BD]]
- *Aislamiento:* Las Transacciones no interfieren unas con otras
- *Durabilidad:* No es Vulnerable sis e producen fallos

### Sistema por Lotes
Las operaciones son realizadas una a una: si una falla, el programa finaliza, pero los cambios realizados quedan operativos. 
Este tipo de sistemas son utilizados en los [[Script|scripts]].

*Script:* texto plano con instrucciones para realizar en el sistema, las cuales serán ejecutadas mediante el Procesamiento por Lotes con la línea de comandos