---
title: Tema 3
tags:
  - Hardware
  - CPU
  - Memoria
  - Arquitectura
  - GPU
---
# Tema 3 - Identificación de los Bloques Funcionales de un Sistema Informático

## PRINCIPALES FUNCIONES DE CADA BLOQUE
- **[[placa-base|Placa Base]]** :
	- Anclada a [[la-caja|la caja]]
	- La componen una serie de circuitos impresos que conectan todos los elementos entre si
- **Microprocesador**: Su función principal es procesar las instrucciones que le llegan
- **[[memoria-ram|RAM]]**: Traslada la info hacía el [[unidad-central-de-procesamiento|procesador]]
- **[[tarjeta-de-expansion|Tarjetas de Expansión]]**: 
	- [[adaptador-de-red|Adaptadores de Red]]
	- [[tarjeta-grafica|Tarjeta Gráfica]]
	- Tarjeta de Audio
- [[periferico-interno|Periféricos Internos]]: 
	- [[almacenamiento-secundario|Disco Duro]]
	- [[disco-compacto|Discos compactos]]
- [[periferico-externo-de-entradasalida|Periféricos Externos]]:
	- Pantalla
	- Teclado [[directorio-etc|etc]]...

## ARQUITECTURA DE BUSES
*Función* -> Conectar: **CPU - Memoria - E/S**
*Tipos:*
- De Control
- De Datos 
- De Dirección
*Los más importantes:*
- **ISA Industri Standard Arquitecture**
	- Creador: IBM
	- [[buses-del-sistema|Bus]] de expansión Estandar
	- Está Obsoleto!
- **[[interfaz-pci|PCI]] Interconexión de [[componentes-del-hardware|Componentes]] [[periferico|Periféricos]]** 
	- PCI y [[configuracion-de-la-bios|BIOS]] interactúan
	- Estandar en las [[tarjetas-de-expansion|tarjetas de expansión]]
- **[[AGP]] Puerto de Aceleración Gráfica**
	- Tarjeta de Video
	- Para [[aplicacion|Aplicaciones]] 2D y 3D
	- Más Velocidad que PCI
- **PnP [[plug-and-play|Plug and Play]]** Configuración automática entre diferentes tarjetas de expansión 
	- *PnP* : Autoidentificar
	- *BIOS PnP*: Inicia los dispositivos cuando PC arranca
	- *[[sistema-operativo|SO]] Pnp*: sigue con el proceso de la BIOS Pnp en [[el-sistema-operativo|el Sistema Operativo]]

## LA PLACA BASE

### CARACTERÍSTICAS
- Forma
- Tamaño
- Orientación
- Conectores
- Anclaje
- [[zocalo|Zócalos]]
- Tipos de Alimentación

### FACTORES
- **ATX (Advanced Technology eXtended):** El estándar más común ($305 \times 244$ mm). Ofrece mayor espacio para expansión (PCIe), ideal para PCs de alto rendimiento o gaming.
    
- **DTX:** Variante poco común diseñada para equipos compactos. Es similar al Mini-ITX pero ligeramente más largo, permitiendo hasta dos [[ranura-de-expansion|ranuras de expansión]].
    
- **Micro ATX (mATX):** Versión reducida del ATX ($244 \times 244$ mm). Equilibrio ideal entre tamaño y funcionalidad; compatible con la mayoría de gabinetes estándar.
    
- **Mini ATX:**Es un formato extremadamente compacto ($150 \times 150$ mm) diseñado para sistemas de muy bajo consumo y espacios reducidos.
    
- **BTX (Balanced Technology eXtended):** Formato diseñado por Intel para mejorar el flujo de aire y la refrigeración. Actualmente está **obsoleto**, desplazado por la eficiencia del estándar ATX.

### PARTES
- *[[zocalo-del-microprocesador|Zócalo del Microprocesador]]*
	- *Socket*: Sitio para conectar la CPU
	- *[[ranura-del-microprocesador|Slot]]*: Vertical
- *[[ranura-ram|Ranura RAM]]*: Dependiendo del tipo será de un color u otro
- *[[ranuras-de-expansion|Ranuras de Expansión]]*
- *[[conector-de-energia|Conectores de Energía]]*
- *Conectores Internos y Externos*: SATA, USB, etc..
- *BIOS*: Basic Input/Output System
- *[[sistema-de-arranque|Sistema de Arranque]]*:
	- *Memoria CMOS [[memoria-cmos|Complementary Metal Oxide Semiconductor]]*: 
		- Se alimenta de una Pila
		- Contiene la info básica de todos los recursos que componen el sistema
	- *[[memoria-flash|Memoria Flash]]*: 
		- Contiene la BIOS y la configuración del sistema.
		- Dispone de las unidades necesarias para arrancar y poner en marcha el S.O 
- *Buses del Sistema*: 
	- *Buses Internos*: Comunica unidades del Chip
	- *Buses Externos*: Comunica unidades de la Placa Base
	- *Buses de Expansión*: Comunica placa base con unidades externas
	- *Slots*: Inserta dispositivos que serán parte del sistema

### CONFIGURACIÓN
**BIOS** 
- Conjunto de [[software-y-algoritmo|programas]] que se alojan en la memoria del PC
- Emplean Memoria Flash 'no volátil' pero permite leer y borrar datos electrónicamente
- Comprueba E/S de datos a través de los [[controlador-de-dispositivo|Drivers]]
- *POST Power On Self Test*
- Carga el S.O y lo enlaza con el [[gestor-de-arranque|Gestor de Arranque]]

![[placa base.jpg]]


## MICROPROCESADOR

*CPU* 
- *Velocidad*: MHz o [[velocidad-de-procesador|GHz]] --> 1GHz = 1000MHz
	- *Interna*: dentro del propio microprocesador
	- *Externa*: la de la CPU con la Placa Base
- *Memoria*: [[memoria-cache|caché]] L1 , L2, L3 ...
- *Alimentación*: Pilla electricidad de la placa base
	- *Voltaje Externo E/S*: permite comunicación CPU-Placa Base
	- *Voltaje Interno o de [[nucleo-del-sistema-operativo|Núcleo]]* Permite que CPU tenga temperatura interna menor
- *Sockets y Slots*: Lo visto en el punto anterior.

### CONTROL DE TEMPERATURA
- *[[sistema-de-refrigeracion|Disipador]]*: Elemento de metal (cobre o aluminio) que traspasa el calor de la CPU al Ventilador
- *Cooler*: Provoca la circulación rápida del aire caliente hacia el exterior



## RAM
**RAM** : Su función es almacenar instrucciones y datos que se estén utilizando

### CARACTERÍSTICAS
- Operaciones Escritura/Lectura
- *Volátil* (Necesita Energía sino pierde info)
- Permite acceder a un dato sin recorrer por todos los anteriores
- *Refresco*: Los datos se van borrando conforme s eva usando
- *Transferencia de Datos*: desde la memoria hasta el bus conforme marca el reloj del sistema
- *Frecuencia del Bus*: Velocidad que trabaja el reloj del sistema
- *Índice PC*: Velocidad de Transferencia entre los diferentes módulos

### TIPOS
- *DRAM [[memoria-dram|Dynamic RAM]]*:
	- Necesita Refrescar Datos
	- Más Económica
		- *SDRAM*: Sincronizada con el reloj del sistema para leer/escribir
		- *[[memoria-ddr-sdram|DDR]]-SDRAM*: Doble Velocidad, envía la info. tanto en subida como en bajada del reloj
		- *DDR2*:
			- Menos Voltaje
			- Se calienta menos
			- Más Frecuencia de Trabajo
		- *DDR3*:
			- Menos voltaje que DDR2
			- Mas frecuencia
		- *DDR4*:
			- Más Frecuencia
			- Mejor Transferencia de datos
		- *DDR5*:
			- Menos Consumo de Energia
			- Duplica el Ancho de Banda
			- Dobla su tasa de Transferencia
- *SRAM [[memoria-sram|Static RAM]]:*
	- Refresca menos vecesque la DRAM
	- Más Rápidas
	- Más [[cara-de-disco|Caras]]

## ALMACENAMIENTO

Discos de Memoria Secundaria
- Más baratos que la RAM
- Más capacidad
- Almacenamiento Permanente
- Son mas Lentos!

### HDD DISCOS DUROS MAGNÉTICOS
#### CARACTERÍSTICAS
- *Velocidad de Transferencia*
- *Tasa de Tranferencia*
- *Tiempo Medio de Lectura/Escritura*
- *Tiempo de Latencia*
- *Tiempo de Búsqueda*
- *Velocidad de Rotación*
#### COMPONENTES
- *Carcasa* cerrada con un dispositivo ultravioleta
- *Discos* que se leen por las dos caras
- *Cabezal* hace la función de lectura/escritura
- *Eje* la parte que contiene todos los discos

#### LOCALIZAR DATOS
Es necesario tener en cuenta:
- *Caras (Sides)* el dato esta en una de las 2
- *[[pista-de-disco|Pistas]] (Tracks)* los círculos concéntricos que van por todo el plato
- *Cilindro* es el conjunto de pistas que ocupan una posición determinada en todos los platos
- *[[sector-de-disco|Sectores]]* es la cantidad mínima en la que podemos dividir una cara del plato

Para Localizar un dato teniendo en cuenta lo anterior tenemos dos técnicas
##### CHS CILINDRO-CABEZAL-CILINDRO
Asigna una serie de números a los sectores y cilindro, la cara del plato también se enumera (comenzando por el 0) para localizar el dato solo hay que conocer esos 3 números.

> **CAPACIDAD DE UN DISCO** = (CILINDRO) * (CARAS) * (Nº DE SECTOR)  * (TAMAÑO DEL SECTOR)

##### LBA
Ésta Técnica enumera todos los sectores del disco de manera consecutiva

> **CAPACIDAD DE UN DISCO** = (Nº DE SECTOR) * (TAMAÑO DEL SECTOR)


#### MEMÓRIA INTERMEDIA: BUFFER O CACHÉ
Mientras se ejecuta una posición de memoria guardamos en la caché las posiciones de memoria próximas para agilizar y ser más rápidos.

### DISPOSITIVOS ÓPTICOS
Almacenan los datos de forma permanente pero en el exterior del PC

- #### [[comando-de-directorio|CD]]-ROM
	- ##### COMPONENTES
		- Cabeza lectora con haz de laser
		- Motor que acciona la cabeza
		- Motor de Rotación
		- Mecanismo de carga/BandejA
- ##### DVD
- ##### BLUE-RAY

### SSD MEMORIAS EN ESTADO SÓLIDO
Formada por elementos electrónicos 
- Mejores características
- Más Rápidas
- Más Velocidad
- Sin Ruido
- Más Vida Útil
- Más Caras
#### TIPOS
##### SDRAM
- Volátil
- Puede llevar una pequeña pila
##### EEPROM:
- No Volátil
- Lectura/Escritura ilimitadas
- Suele usarse como disco externo

#### FORMATOS
##### CF COMPACT FLASH
- Diseñado por SANDISK
- La 1ª del Mercado
- Ranura PC-CARD o [[lector-de-tarjetas|Lector de Tarjetas]]
##### MS MEmory Stick
- SONY
- Para Compatibilidad entres sus Dispositivos
##### SD Secure Digital
- La más Usada
- Gran Capacidad en tamaño reducido
##### SDHC Secure Digital High Capacity
- [[secure-digital|SD]] Mejorada con más capacidad

## TARJETA GRÁFICA
*Tarjeta Gráfica*: Permite que la info. se muestre en pantalla
### TIPOS
- *Integradas*
- *Externas*
	- Para que sea óptima hay que desactivar la integrada desde la BIOS y tendremos una mayor eficiencia al quitarnos carga en el procesador CPU

### COMPONENTES
#### GPU
 *Graphic Processing Unit*:
- Procesador Dedicado
- MEjor Calidad y Colores
- Utiliza Librerias como:
	- *OpenGraph* para 2D y 3D
	- *[[libreria-grafica|Directx]]* para Apps Multimedia

#### MEMORIA
- Capacidad [[unidad-de-medida-de-informacion|GB]]
- Tecnologia: SRAM (desde DDR a DDR5 dependiendo el modelo)
- Frecuencia: 166MHz hasta 7GHz

#### CONECTORES
- *[[conector-vga|VGA]]* 
- *[[conector-rca|RCA]]*
- *[[puerto-hdmi|HDMI]]*
#### INTERFAZ
- *[[interfaz-agp|AGP]]* (En desuso)
- *PCI y PCI-Express 


## OTRAS TARJETAS DE EXPANSIÓN
### CAPTURADORAS DE VIDEO
Capturan video en analógico y lo guardan en digital
#### CONECTORES
- *BNC* para video de pago
- *S-VIDEO* para pantallas LED, LCD o Plasma
- *RCA* Audio y Video

### SINTONIZADORAS DE TV
- Analógica
- Digital
- Híbrida
- Satélite

### TARJETA DE SONIDO
Gestiona independientemente a la CPU el audio
#### CARACTERÍSTICAS
- *Polifonía*: cantidad de voces reproducidas a la vez
- *Canales*: sonido envolvente, un canal por cada altavoz
#### COMPONENTES
- *[[bufer-de-memoria|Buffer]] de Memoria*: traspasa datos entre Tarjeta sonido <-> Placa Base
- *Sintetizador*: Procesador produce sonidos mediante códigos [[protocolo-midi|MIDI]]
- *DSP*: [[procesador-de-senal-digital|Procesador de señal digital]] que comprime y descomprime el audio
- *[[adcdac|ADC/DAC]]*: [[convertidor-adcdac|Convertidor Analógico-Digital]]
- *Mezclador*: Mezcla los canales de audio
- *Conectores*
	- *MiniJack*
	- *RCA*
	- *S/PDIF*
	- *GAMEPORT*
	- *MIDI*: Intercambio de dispositivos musicales, la info es covertida a nota musical

## LAN y WAN
### TIPOS
- *[[red-de-area-local|LAN]] Local Network Area*
	- Privada
	- Pocos Equipos
	- Gestión y Montaje Privado
- *MAN [[red-de-area-metropolitana|Metropolitan Area Network]]*
	- Pública
	- Municipios Enteros
	- Empresa Especializada
- *WAN [[red-wan|Wide Area Network]]*
	- Pública
	- Continentes incluso Mundo entero
	- Gestionan varias EMpresas
	- ç

### TARJETA DE RED
*NIC [[tarjeta-de-red-nic|Network Interface Card]]*
- Cable mediante *RJ45*
- Inalámbrica mediante *[[conexion-inalambrica|Wireless]] Antena*
- Suele venir integrada en la placa base
- Utilizan colores led para informar de su funcionamiento, conexión, velocidad
*MAC [[direccion-mac|Dirección Física]]*: cuando un equipo se conecta a un router este almacena la MAC