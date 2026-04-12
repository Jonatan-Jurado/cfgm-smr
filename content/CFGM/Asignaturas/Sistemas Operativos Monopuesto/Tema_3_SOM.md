---
title: Tema 3
tags:
  - Memoria
  - Procesos
  - SistemaArchivos
  - Almacenamiento
  - CPU
---
# Tema 3- Gestión de Archivos - Memoria - Procesos
## GESTIÓN DE ARCHIVOS
**Archivo**: 
- Conjunto de bits almacenados tratados como una sola unidad.
- Tienen una [[extension-de-archivo|Extensión]] y un Tamaño ([[unidad-de-medida-de-informacion|Byte]])
- *Operaciones:*
	- *Ceración*
	- *Apertura*
	- *Cierre*

**Directorio:** 
- Archivo que almacena otros archivos y subdirectorios
- Guarda la Ruta y atributos de un directorio

**Atributo:** Características de un Archivo

**Permisos:**  [[permiso-de-archivo|Reglas de acceso]] para las operaciones
- *lectura*
- *escritura*
- *ejecución*

## GESTIÓN DE LA MEMORIA
En los S.O multiproceso, la [[memoria-ram|RAM]] no suele tener capacidades suficiente para todos los procesos. Por eso se debe distribuir la Memoria entre varios procesos.
### SOLAPAMIENTO o OVERLAY
Divide el [[software-y-algoritmo|Programa]] Virtualmente en procesos para que se ejecuten en diferentes partes de la RAM.
Fue inviable porqué cada sistema tiene características diferentes y necesitaba una programación diferente para todas las [[aplicacion|aplicaciones]]

### GESTIÓN DINÁMICA DE LA MEMORIA
- Comprobar que el Proceso se ejecuta en una parte libre de la memoria principal.
- Los datos se comparten entre todos los procesos (Si un proceso está accediendo a uno de éstos otro proceso no puede acceder al mismo dato en ese momento)
- Resolver las *Colas de ejecución* (Que proceso entra y que proceso espera)

### TÉCNICAS DE GESTIÓN DE LA MEMORIA
#### PARTICIONES FIJAS
- La memoria se divide en [[particion-de-disco-duro|particiones]] que no podrán modificarse después.
- 1 [[particion|Partición]] -> 1 Proceso
- Problemas!
	- *[[fragmentacion-de-memoria|Fragmentación Interna]]*: procesos ocupan espacio menor que el que tienen asignado
	- *[[fragmentacion-externa|Fragmentación Externa]]*: Procesos ocupan espacio mayor y la partición queda libre
	- ![[interna.png]]
	- ![[externa.png]]

- *Asignar Procesos*: 
	- *[[cola-unica|Cola única]]*: 
	  ![[cola-unica.png]]
	- *Cola por Partición*:
	- ![[cola-por-particion.png]]
- *Asignar Memoria*:
	- Primer Proceso de la cola a un espacio según quede libre (Si proceso > Espacio libre. No se ejecuta)
	- Primer Proceso de la cola que quepa en el espacio que ha quedado libre.
	- Proceso mas grande de la cola que quepa en el espacio que ha quedado libre

#### PARTICIONES VARIABLES
Se particiona según la ejecución de los procesos, , un proceso solo ocupa en memoria el espacio que necesita.
![[part-variables.png]]


**Uso**
1. Cuando un proceso termina, se combina el hueco con el que hay disponible al lado
![[mem-var-1.png]]
2. Cuando un proceso termina, se compactan los espacios ocupados de la memoria, por lo que al principio está toda la memoria ocupada y después toda la memoria libre.
	- *[[estrategia-de-ajuste|Primer Ajuste]]*:  asigna al primer proceso de la cola el primer hueco 
	- *Siguiente Ajuste*: asignan los procesos por orden de cola
	- *Mejor Ajuste*: asigna el hueco más pequeño al proceso que mejor se adapte al espacio
	- *Peor Ajuste*: asigna el hueco más grande al primer proceso de la cola.
	![[mem-var-2.png]]
	

#### MEMORIA VIRTUAL
Se usa el [[almacenamiento-secundario|Disco duro]] como RAM.
*Programas*: Tienen 2 Capas
- *Capa Activa*: Procesos en ejecución en la memoria principal
- *Capa inactiva*: Procesos en la memoria secundaria.

*[[intercambio-de-memoria|Swapping]]*:  Mueve el proceso de la memoria principal al [[disco-duro|disco duro]] y viceversa.
Problema! Ralentiza el sistema.
![[swaping.png]]


*Técnicas para la [[tecnologia-de-virtualizacion|Virtualización]]*:
- *[[paginacion|Paginación]]*: La memoria y los procesos se dividen en unidades mas pequeñas
	- *[[pagina|Páginas]]*: Programas distribuidos en segmentos dentro de la memória principal
	- *Marcos*: Programas distribuidos en secciones d eigual tamaño que las páginas
- *[[segmentacion|Segmentación]]*: los programas también se dividen en segmentos, pero, al contrario que en la paginación, estos son de diferente tamaño.
	- *Modularidad*:cada rutina dentro de un programa permita cambios que no afecten al resto del programa. También admite la compilación de módulos por separado

## GESTIÓN DE LOS PROCESOS

*Proceso*: es un conjunto de instrucciones que se ejecutan en la [[unidad-central-de-procesamiento|CPU]]
### ESTADO DE LOS PROCESOS
Todos los procesos tienen un ID que define sus situación respecto a su funcionamiento
#### INDICADOR
- *Activo/Ejecución*: Está asignado para ejecutarse
- *Bloqueado*: Ha sido interrumpido y está a la espera de que termine la operación que lo bloqueó
- *Preparado*: Disponible para ejecutarse
- *Solo en Unix*:
	- *Nuevo*: aún no ha sido elegido para iniciar su procesamiento
	- *Terminado*: ha finalizado su ejecución
	- *[[proceso-zombie|Zombie]]*: ha finalizado su ejecución pero que no ha liberado los recursos que ha utilizado.

#### CAMBIO DE ESTADO
- *Bloqueo*: Cuando un proceso se está ejecutando y produce llama al sistema, se bloquea para evitar consumir CPU. 
	- Ejemplo: cuando requiere información y pide que se lean datos; en este caso, debe esperar a que se complete esa operación.
- *[[apropiacion|Apropiación]]*: está en ejecución y el gestor indica que debe pare, tiene que salir de la CPU hasta que pueda volver a estar activo
- *[[asignacion|Asignación]]*: cuando pasa a ejecutarse en la CPU.
- *[[fin-de-bloqueo|Fin de bloqueo]]*: está esperando a que acabe la operación que lo bloqueó


![[estado1.png]]


*Solo en Unix*
![[estado2.png]]



### PRIORIDAD Y PLANIFICACIÓN
#### ASPECTOS PRINCIPALES
- *Imparcialidad*: cada proceso tenga la fracción de tiempo de procesador que le corresponde.
- *Repetitividad*: con [[carga-de-trabajo|cargas de trabajo]] similares -> comportamientos similares
- *Predecibilidad*: tiempo y coste de procesamiento -> con cualquier carga de Trabajo
- *Eficiencia*: CPU y demás recursos trabajen el mayor tiempo posible
- *Productividad*: Cantidad de trabajo por unidad de tiempo
- *Economía*: Reducir gastos al mínimo
- *Equilibrio*: Aprovechar recursos manteniendo ocupados todos los [[componentes-del-hardware|componentes]] posibles
- *Recursos Críticos*: preferencia a aquellos procesos que están ocupando recursos críticos, para que terminen lo antes posible y los liberen.
- *Degradación progresiva*: degradación uniforme al incrementar el trabajo
- *Tiempos Aceptables*:grado de satisfacción que tienen los usuarios respecto al tiempo que deben esperar

### REFERENCIAS NUMÉRICAS
- *[[tiempo-de-ejecucion|Tiempo de ejecución]] ([[tiempo-de-retorno|t]])*: es el tiempo de [[proceso-del-sistema|Servicio]] que necesita un proceso. 
- *Tiempo de terminación o de retorno (T)*: es el tiempo entre la hora de llegada del trabajo y su hora de finalización. 
	- Mide el tiempo que un proceso está presente en el equipo
	- **T = Ht – Hn** 
- *[[tiempo-de-respuesta|Tiempo de respuesta]]*:  tiempo desde que se solicita hasta que se obtiene.
- *[[tiempo-de-espera|Tiempo de espera]] (w)*: tiempo que transcurre entre hora de llegada y la hora en que empieza a ejecutarse
	-  **W = Hc – Hn**
 - *[[tiempo-perdido|Tiempo perdido]] (M)*: diferencia del tiempo de ejecución al tiempo de finalización.
	 - **M = T – t**
- *[[indice-de-penalizacion|Índice de penalización]] ([[potencia-electrica|P]])*: cociente entre el tiempo de finalización y el tiempo de ejecución. 
	- **P = T/t** 
 - *[[indice-de-respuesta|Índice de respuesta]] (R)*: es el inverso al anterior. 
	 - **R = t/T**
- *[[tiempo-del-sistema|Tiempo del sistema]]*: tiempo que consume el S.O en ejecutar los [[criterio-de-planificacion|métodos de planificación]] establecidos.
- *[[tiempo-de-inactividad|Tiempo de inactividad]]*: tiempo que el procesador permanece desocupado cuando no hay procesos preparados para ejecutar.

### MÉTODOS DE PLANIFICACIÓN
#### NO APROPIATIVOS
Una vez asignado el procesador a un proceso, ya no se puede quitar.
##### FCFS 
**[[first-come-first-served|FCFS]]**: EL primero que llega se le asigna.
- *Trabajos*: En orden de llegada
- *Proceso*: se añade al final de la cola y se ejecuta en orden de incorporación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/nzCeLcajobs?si=C15M9xET_TBs3mHa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

##### SJF
**Shorted Job First**: Para su ejecución, selecciona el trabajo que necesita menos tiempo de entre todos los que estén listos para ejecutarse
<iframe width="560" height="315" src="https://www.youtube.com/embed/P5p9uyji2YY?si=MNYs8lEgbd7yfewR" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

#### APROPIATIVOS
##### SRT
**Short Remining [[time]] First**: proceso más corto en cada momento,  solo puede ocurrir una apropiación si llega un proceso nuevo que necesite menos tiempo del que le falta al actual
<iframe width="560" height="315" src="https://www.youtube.com/embed/yzMOAtoCDR0?si=WiThnTUYCuYgFAXF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

