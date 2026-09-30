---
title: Tema 1
tags:
  - RedesLocales
  - Redes
  - LAN
  - Topologias
---

# Tema 1 - Introducción a las Redes Locales

Una red informática permite que diferentes dispositivos puedan **comunicarse, intercambiar información y compartir recursos**.

Para que exista una comunicación deben intervenir varios elementos:

- **Emisor:** dispositivo que envía la información.
- **Receptor:** dispositivo que recibe la información.
- **Canal:** medio por el que circula la información.
- **Lenguaje:** forma de representar la información para que emisor y receptor puedan interpretarla.


## 1.1. DEFINICIÓN Y TIPOS DE REDES

### RED INFORMÁTICA

- **Red informática:** conjunto de dispositivos interconectados mediante un medio físico o inalámbrico que permite compartir información.
- **Host:** dispositivo conectado a una red capaz de enviar o recibir información.

Un host no tiene por qué ser únicamente un ordenador. También puede ser un móvil, una tableta, una impresora, un televisor u otro dispositivo conectado a la red.

### FUNCIONAMIENTO DISTRIBUIDO

Las redes actuales permiten distribuir tareas entre distintos equipos.

- **Sistema distribuido:** diferentes equipos participan en la prestación o utilización de servicios.
- **Servidor:** puede almacenar aplicaciones, datos o recursos.
- **Cliente:** accede a los recursos o servicios proporcionados por otros equipos.

> [!example] Ejemplo
> Un programa puede estar instalado en un servidor y ser utilizado desde varios ordenadores clientes.
>
> El programa o los datos están centralizados, pero varios equipos pueden utilizarlos a través de la red.

### VENTAJAS DE LAS REDES LOCALES

- **Compartición de recursos:** varios equipos pueden utilizar un mismo recurso, como una impresora.
- **Archivos compartidos:** varios usuarios pueden trabajar con los mismos archivos sin mantener una copia independiente en cada equipo.
- **Administración centralizada:** muchas tareas pueden ejecutarse desde servidores.
- **Administración remota:** permite resolver determinados problemas en otros equipos a través de la red.
- **Alta velocidad de transmisión:** al abarcar distancias reducidas pueden ofrecer velocidades elevadas.
- **Baja tasa de errores:** favorece una comunicación más fiable.
- **Localización de averías:** resulta más sencillo encontrar determinados fallos al existir un número limitado de dispositivos.

### CLASIFICACIÓN SEGÚN SU EXTENSIÓN

Las redes pueden clasificarse según el área geográfica que abarcan.
#### RED DE ÁREA PERSONAL (PAN)

- **Red de área personal (PAN):** conecta dispositivos situados a pocos metros y destinados al uso de una persona.
- **Configuración:** suele ser sencilla y automática.
- **Conexión:** normalmente se realiza de forma inalámbrica.
- **Coste:** el material destaca que habitualmente no supone un coste adicional.

> [!example] Ejemplo
> - **Ratón inalámbrico:** conectado a un ordenador.
> - **Móvil:** conectado a un televisor.

#### RED DE ÁREA DOMÉSTICA (HAN)

- **Red de área doméstica (HAN):** red utilizada normalmente dentro de una vivienda.
- **Router:** suele actuar como dispositivo de conexión para los diferentes equipos.
- **Internet:** normalmente permite también conectar los dispositivos domésticos a Internet.

#### RED DE ÁREA LOCAL (LAN)

- **Red de área local (LAN):** conecta dispositivos dentro de una zona geográfica reducida.
- **Ámbito:** normalmente un edificio o instalación.
- **Gestión:** suele administrarse de forma privada.

#### RED DE ÁREA DE CAMPUS (CAN)

- **Red de área de campus (CAN):** está formada por un conjunto de LAN dentro de una misma área.
- **Ámbito:** puede conectar diferentes zonas de un edificio o varios edificios cercanos.

#### RED DE ÁREA METROPOLITANA (MAN)

- **Red de área metropolitana (MAN):** puede abarcar desde varios edificios hasta una ciudad.
- **Estructura:** se basa en la interconexión de varias LAN.

> [!example] Ejemplo
> El material utiliza como ejemplo una red de **televisión por cable** dentro de una ciudad.

#### RED DE ÁREA EXTENSA (WAN)

- **Red de área extensa (WAN):** permite interconectar ciudades o incluso países.
- **Extensión:** cubre distancias mucho mayores que una LAN.
- **Velocidad:** según el material, presenta menor velocidad de transmisión que una LAN.
- **Tasa de error:** puede ser mayor debido a la gran extensión que abarca.

### CLASIFICACIÓN SEGÚN EL ACCESO

#### RED PÚBLICA

- **Red pública:** ofrece servicios de comunicación a los usuarios que pueden acceder a ellos.
- **Disponibilidad:** el término pública hace referencia a la disponibilidad del servicio, no a que los datos transmitidos sean necesariamente públicos.

#### RED PRIVADA

- **Red privada:** es administrada por una organización determinada.
- **Direcciones IP privadas:** utiliza direcciones definidas para redes privadas.
- **Internet:** los equipos necesitan un router que permita relacionar las direcciones privadas con las públicas para acceder a Internet.


### CLASIFICACIÓN SEGÚN EL MEDIO DE TRANSMISIÓN

#### RED CABLEADA

- **Red cableada:** utiliza un medio físico para transmitir la información.
- **Cable:** conecta los dispositivos con los diferentes elementos de la instalación.

#### RED INALÁMBRICA

- **Red inalámbrica:** transmite y recibe información mediante ondas electromagnéticas.
- **Antenas:** permiten emitir y recibir las señales.


### CLASIFICACIÓN SEGÚN SU FUNCIÓN

#### ALMACENAMIENTO DAS

- **Direct Attached Storage (DAS):** sistema indicado en el material para almacenar los datos de los clientes.
- **Funcionamiento:** sencillo.
- **Uso:** relacionado en el tema con pequeñas y medianas empresas.

#### ALMACENAMIENTO NAS

- **Network Attached Storage (NAS):** almacenamiento disponible a través de la red.
- **Transmission Control Protocol/Internet Protocol (TCP/IP):** conjunto de protocolos utilizado para proporcionar este almacenamiento según el material.
- **Uso:** asociado en el tema a empresas de mayor tamaño.

#### ALMACENAMIENTO SAN

- **Storage Area Network (SAN):** red orientada al almacenamiento con una gran capacidad disponible.

> [!important] Diferencias
> **DAS ≠ NAS ≠ SAN**
>
> - **DAS:** almacenamiento de funcionamiento sencillo.
> - **NAS:** almacenamiento accesible mediante TCP/IP.
> - **SAN:** red especializada en almacenamiento de gran capacidad.

#### RED VLAN

- **Red de área local virtual (VLAN):** permite crear una red lógica dentro de una infraestructura física.
- **Separación:** permite separar lógicamente diferentes grupos aunque utilicen una misma infraestructura física.

#### RED VPN

- **Red privada virtual (VPN):** utiliza Internet para crear una red privada.
- **Seguridad:** puede cifrar los datos transmitidos entre los extremos de la red.

#### ZONA DMZ

- **Zona desmilitarizada (DMZ):** zona de la red que necesita medidas de protección frente a posibles accesos no autorizados.
- **Firewall:** el material destaca su utilización para proteger esta zona.


## 1.2. ARQUITECTURA Y TOPOLOGÍA EXISTENTE

La arquitectura indica **cómo se organizan los equipos y qué función desempeña cada uno dentro de la red**.

### ARQUITECTURA CLIENTE-SERVIDOR

- **Servidor:** equipo central que proporciona servicios o recursos.
- **Cliente:** equipo que solicita esos recursos o servicios.
- **Jerarquía:** existen funciones diferentes para servidor y clientes.
- **Inconveniente:** si el servidor falla, los clientes pueden quedarse sin los recursos que proporciona.

### ARQUITECTURA P2P

- **Peer to Peer (P2P):** arquitectura entre iguales.
- **Nodos:** todos los equipos se encuentran al mismo nivel.
- **Funciones:** un equipo puede actuar como cliente y servidor al mismo tiempo.
- **Jerarquía:** desaparece la separación estricta entre servidor y cliente.


## 1.3. ELEMENTOS DE UNA RED

Los elementos de una red pueden agruparse en:

1. **Equipos terminales:** dispositivos que envían o reciben información.
2. **Elementos de conexión:** permiten que los equipos se conecten a la red.
3. **Medios de transmisión:** transportan la información.
4. **Equipos intermedios:** gestionan, distribuyen o retransmiten las comunicaciones.

### EQUIPOS TERMINALES O HOSTS

- **Host:** dispositivo emisor o receptor conectado directamente a la red.
- **Ordenadores:** pueden actuar como clientes o servidores.
- **Periféricos de red:** impresoras, escáneres o sistemas de almacenamiento.
- **Otros dispositivos:** móviles y otros equipos conectables.

### ELEMENTOS DE CONEXIÓN

#### TARJETA DE RED

- **Tarjeta de interfaz de red (NIC):** permite conectar un dispositivo a la red.
- **Función:** interpreta las señales que circulan por los medios de transmisión.
- **Red cableada:** dispone de un conector compatible con el tipo de cable.
- **Red inalámbrica:** dispone de una antena para transmitir y recibir señales.


#### CONECTORES

- **RJ-45:** utilizado con cables de cobre de pares trenzados, especialmente UTP.
- **Bayonet Neill-Concelman (BNC):** utilizado con cable coaxial.
- **LC:** conector de fibra óptica indicado para transmisiones de alta velocidad.
- **FDDI:** conector de fibra mencionado para redes en anillo.
- **FC:** utilizado para transmisión de datos y con buena resistencia a la tracción.
- **ST:** utilizado habitualmente en terminaciones de cables.
- **SC:** utilizado, por ejemplo, en entornos industriales y centrales telefónicas.

### ANTENAS

Las antenas se utilizan en las redes inalámbricas.
- **Omnidireccional:** emite en todas las direcciones.
- **Direccional:** emite principalmente en una dirección.

### EQUIPOS INTERMEDIOS DE RED

<iframe width="560" height="315" src="https://www.youtube.com/embed/EH_PdUHKv1c?si=1R2YV-vRxkRW7g8R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


#### HUB

- **Hub o concentrador:** interconecta los equipos de una red local.
- **Funcionamiento:** cuando recibe información, la replica y la transmite al resto de equipos.
- **Ancho de banda:** consume más ancho de banda porque todos reciben la información.
- **Transmisiones:** mientras se realiza una transmisión, limita el uso simultáneo del medio.

#### BRIDGE

- **Bridge o puente:** divide una red en diferentes segmentos.
- **Objetivo:** evitar que los paquetes de un segmento colisionen con los de otro.

#### SWITCH

- **Switch o conmutador:** conecta dispositivos dentro de una red local.
- **Funcionamiento:** envía la información directamente al destinatario correspondiente.
- **Dirección Media Access Control (MAC):** permite identificar el equipo al que debe enviarse la información.
- **Comunicaciones simultáneas:** permite que distintos equipos se comuniquen al mismo tiempo.

> [!important] Importante
> **HUB ≠ SWITCH**
>
> - **Hub:** recibe los datos y los replica a todos.
> - **Switch:** dirige los datos al destinatario correspondiente.
>
> **Hub = todos reciben.**
>
> **Switch = selecciona el destino.**

> [!example] Ejemplo
> Si PC1 quiere enviar un archivo a PC4:
>
> - **Con hub:** la información también llega a los demás equipos.
> - **Con switch:** la información se dirige hacia PC4.

#### ROUTER

- **Router o enrutador:** dirige el tráfico de la red.
- **Función:** determina hacia dónde deben enviarse los datos.

#### FIREWALL

- **Firewall o cortafuegos:** gestiona la seguridad de la red.

#### GATEWAY

- **Gateway o pasarela:** permite interconectar redes que pueden utilizar protocolos diferentes.
- **Modelo Open Systems Interconnection (OSI):** aparece relacionado en el material con el funcionamiento de las pasarelas.
- **Adaptación:** puede desensamblar y volver a configurar la información en función de la red de destino.

#### REPEATER

- **Repeater o repetidor:** conecta dos segmentos de una misma red y retransmite la información.
- **Red inalámbrica:** puede utilizarse para ampliar la cobertura de la señal wifi.



## 1.4. MEDIOS DE TRANSMISIÓN: CABLES Y REDES INALÁMBRICAS

Un medio de transmisión es el soporte por el que viaja la información entre el emisor y el receptor.

### MEDIOS GUIADOS Y NO GUIADOS

- **Medios guiados:** las señales circulan por un medio físico, como un cable.
- **Medios no guiados:** las señales circulan por el aire mediante ondas electromagnéticas.

### CARACTERÍSTICAS DEL MEDIO

En una red cableada debemos considerar:

- **Velocidad de transmisión:** rapidez con la que pueden enviarse los datos.
- **Ancho de banda:** capacidad disponible para transportar información.
- **Distancia entre repetidores:** distancia que puede recorrer la señal.
- **Coste:** precio del material y de la instalación.

En los medios inalámbricos pueden influir además factores externos relacionados con el entorno.

<iframe width="560" height="315" src="https://www.youtube.com/embed/v-xFxUBb6-Q?si=7SSOMnXxCAJZ5pPf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### CABLE DE PAR SIN TRENZAR

- **Estructura:** está compuesto por dos hilos paralelos.
- **Aislamiento:** los conductores están recubiertos de material plástico.
- **Interferencias:** ofrece poca protección frente a ellas.

### CABLE DE PAR TRENZADO

Los conductores se trenzan para mejorar la protección frente a las interferencias.

#### PAR TRENZADO NO APANTALLADO (UTP)

- **UTP:** cable de par trenzado sin pantalla conductora.
- **Flexibilidad:** es bastante flexible.
- **Impedancia:** 100 ohmios según el material.
- **Interferencias:** es sensible a ellas.

#### PAR TRENZADO APANTALLADO (STP)

- **STP:** cada par está protegido mediante una malla conductora y existe además una protección general.
- **Ruido:** presenta una gran inmunidad.
- **Rigidez:** es el más rígido de los tres tipos descritos.

#### PAR TRENZADO CON PANTALLA GLOBAL (FTP)

- **FTP:** dispone de una malla conductora global que protege los pares.
- **Interferencias:** ofrece mayor protección que UTP.
- **Rigidez:** es intermedia.


### CATEGORÍAS DEL PAR TRENZADO

Las categorías se diferencian, entre otros aspectos, por sus prestaciones de transmisión.

Según los ejemplos del material:

- **Categoría 1:** utilizada para voz y con una frecuencia de 1 MHz.
- **Categoría 5:** indicada como mínimo para redes de datos en el tema y con una velocidad de 100 Mbps.

### CABLE COAXIAL

- **Conductor:** dispone de un núcleo central de cobre.
- **Aislamiento:** el conductor está rodeado por un material aislante.
- **Malla:** incorpora una malla metálica protectora.
- **Interferencias:** tiene una buena inmunidad al ruido.
- **Distancia:** permite aumentar la distancia entre repetidores.
- **Uso:** se utiliza, entre otros casos, para señales de televisión.

### FIBRA ÓPTICA

- **Fibra óptica:** está formada por fibras de vidrio muy finas.
- **Transmisión:** transporta la información mediante luz.
- **Principio:** utiliza la reflexión de la luz.

### TRANSMISIÓN INALÁMBRICA

- **Medio:** la información se transmite por el aire.
- **Ondas electromagnéticas:** permiten codificar y transportar la información.
- **Espectro electromagnético:** conjunto de ondas clasificadas según su frecuencia y longitud de onda.


## 1.5. MAPA FÍSICO Y LÓGICO DE UNA RED LOCAL. TOPOLOGÍAS

Antes de construir una red es necesario diseñar la disposición de los equipos y su forma de comunicación.

### MAPA FÍSICO

- **Mapa físico:** representa la disposición geográfica real de los equipos y dispositivos.
- **Objetivo:** muestra dónde se encuentran físicamente los elementos de la red.

### MAPA LÓGICO

- **Mapa lógico:** representa cómo están configurados y cómo se comunican los dispositivos.
- **Direcciones IP:** pueden representarse en el mapa lógico.
- **Packet Tracer:** herramienta indicada en el material para diseñar y simular redes.

> [!important] Importante
> **MAPA FÍSICO ≠ MAPA LÓGICO**
>
> - **Mapa físico:** dónde están los dispositivos.
> - **Mapa lógico:** cómo están configurados y cómo se comunican.
>
> **Físico = dónde.**
>
> **Lógico = cómo.**

### TOPOLOGÍA DE RED

La topología representa la **estructura o forma en la que está diseñada una red**.

- **Topología física:** disposición geométrica real de los equipos.
- **Topología lógica:** forma en la que los equipos acceden al medio y transmiten la información.
- **Topología mixta:** combina diferentes tipos de topología.


### TOPOLOGÍA FÍSICA

<iframe width="560" height="315" src="https://www.youtube.com/embed/_yWhL9qAR-s?si=nCQnNlQOezXGwF6y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


#### ESTRELLA

- **Estrella:** todos los equipos se conectan a un dispositivo central, como un hub o switch.
- **Ventaja:** si falla el cable de un equipo, normalmente solo ese equipo queda afectado.
- **Inconveniente:** existe dependencia del dispositivo central.
- **Cableado:** requiere una cantidad considerable de cable.

#### ESTRELLA EXTENDIDA

- **Estrella extendida:** utiliza varios dispositivos centralizadores conectados entre sí.
- **Objetivo:** evitar que toda la concentración dependa de un único dispositivo central.

#### JERÁRQUICA

- **Jerárquica:** organiza los dispositivos mediante diferentes niveles.
- **Estructura:** es similar a una estrella extendida organizada jerárquicamente.
- **Control:** normalmente un equipo se encarga del control del flujo de información.

#### BUS

- **Bus:** todos los equipos están conectados a un cable central.
- **Transmisión:** los datos circulan por el medio compartido.
- **Destinatario:** cada equipo comprueba si el mensaje está dirigido hacia él.
- **Ventaja:** resulta sencillo incorporar nuevos equipos.
- **Inconveniente:** la velocidad puede reducirse al compartir todos el mismo medio.

#### ANILLO

- **Anillo:** cada equipo está conectado con otros dos formando un circuito cerrado.
- **Centralizador:** no existe un dispositivo central.
- **Transmisión:** la información circula siguiendo el anillo.
- **Ventaja:** estructura sencilla.
- **Inconveniente:** una avería en un enlace puede afectar a la comunicación del resto de la red.

#### DOBLE ANILLO

- **Doble anillo:** incorpora un segundo anillo.
- **Sentido:** el anillo secundario puede transmitir la información en sentido contrario.

#### MALLA

- **Malla:** cada nodo dispone de diferentes caminos para comunicarse con otros.
- **Fiabilidad:** si un camino falla, la información puede utilizar otra ruta.
- **Dependencia:** el fallo de un nodo tiene menos posibilidades de interrumpir toda la comunicación.
- **Inconveniente:** su implantación resulta costosa debido al elevado número de conexiones.

#### TOTALMENTE CONEXA

- **Red totalmente conexa:** todos los nodos están interconectados directamente entre sí.


### TOPOLOGÍA LÓGICA

La topología lógica indica **de qué manera los equipos acceden a la red para transmitir información**.

#### BUS LÓGICO

- **Bus lógico:** los equipos envían sus datos al resto de dispositivos.
- **Destino:** cada dispositivo comprueba si la información está dirigida hacia él.
- **Acceso:** los equipos escuchan el medio y transmiten cuando consideran que está disponible.
- **Problema:** pueden producirse colisiones.

#### USO DE TESTIGO O TOKEN

- **Token o testigo:** concede a un equipo el derecho a transmitir.
- **Transmisión:** únicamente puede transmitir el dispositivo que posee el testigo.
- **Circulación:** el token va pasando entre los diferentes equipos.
- **Ventaja:** evita las colisiones producidas por transmisiones simultáneas.



## 1.6. ESTRUCTURAS ALTERNATIVAS

Las estructuras alternativas se diferencian por la forma en la que se establece la comunicación y se transmite la información.

### REDES CONMUTADAS O PUNTO A PUNTO

- **Red conmutada:** establece una comunicación entre una estación de origen y una estación de destino.
- **Camino:** la red habilita una ruta entre los dos equipos.
- **Rutas alternativas:** pueden existir diferentes caminos para transportar la información.

Existen tres métodos principales de conmutación.

#### CONMUTACIÓN DE CIRCUITOS

- **Circuito:** se establece un único camino entre origen y destino.
- **Reserva:** ese camino permanece asignado durante la comunicación.
- **Liberación:** al finalizar, vuelve a quedar disponible.
- **Transmisión:** la información circula entre origen y destino mediante esa ruta.


#### CONMUTACIÓN DE PAQUETES

- **Fragmentación:** la información se divide en paquetes.
- **Paquete:** contiene parte de la información y datos de control.
- **Origen y destino:** cada paquete contiene información que permite identificar ambos extremos.
- **Recepción:** el receptor debe ordenar y unir los paquetes recibidos.

> [!tip] Ejemplo
> Imagina que quieres enviar un objeto grande dividido en varias cajas.
>
> Cada caja contiene una parte y lleva indicado el destino.
>
> Cuando llegan todas, el receptor vuelve a **ordenarlas y unirlas**.

#### CONMUTACIÓN DE MENSAJES

- **Mensaje:** la información se envía completa.
- **Nodo a nodo:** el mensaje pasa de un nodo al siguiente.
- **Espera:** puede permanecer almacenado temporalmente hasta que exista un camino disponible.
- **Destino:** el proceso continúa hasta llegar al receptor final.

### REDES DE DIFUSIÓN O MULTIPUNTO

- **Difusión:** la información se envía a todos los nodos.
- **Destinatario:** cada equipo determina si el mensaje le corresponde.
- **Camino:** los nodos comparten un único medio.
- **Topologías:** el material las relaciona con bus o anillo.



## 1.7. NORMATIVA LEGAL Y TÉCNICA DE IMPLANTACIÓN DE REDES LOCALES

Para que dos dispositivos puedan comunicarse deben utilizar unas reglas comunes.

Estas reglas permiten determinar:

- **Identificación:** cómo se identifican los equipos de la red.
- **Inicio:** cómo se indica el comienzo de una transmisión.
- **Turno:** quién puede transmitir en cada momento.
- **Finalización:** cómo sabe el receptor cuándo comienza y termina la transmisión.
- **Código:** qué sistema se utiliza para representar la información.
- **Entrega:** cómo se garantiza que el mensaje llegue a su destino.
- **Errores:** cómo se comprueba si existen errores durante la comunicación.

### PROTOCOLOS Y ESTÁNDARES

- **Protocolo de comunicación:** conjunto de normas utilizadas para que los dispositivos puedan comunicarse.
- **Estándar de red:** modelo o especificación común utilizada al diseñar componentes para conseguir que sean compatibles.

### ORGANISMOS DE NORMALIZACIÓN

El tema menciona los siguientes organismos relacionados con redes, telecomunicaciones y normalización:

- **Unión Internacional de Telecomunicaciones (ITU):** organismo internacional relacionado con las telecomunicaciones.
- **Organización Internacional de Normalización (ISO):** organismo internacional de normalización.
- **Comisión Electrotécnica Internacional (IEC):** organismo relacionado con la normalización electrotécnica.
- **Instituto de Ingenieros Eléctricos y Electrónicos (IEEE):** organismo relacionado con estándares eléctricos, electrónicos y de comunicaciones.
- **Instituto Americano de Normas Nacionales (ANSI):** organismo estadounidense de normalización.
- **Asociación de la Industria de las Telecomunicaciones (TIA):** organización relacionada con las telecomunicaciones.
- **Comité Europeo de Normalización (CEN):** organismo europeo de normalización.
- **Comité Europeo de Normalización Electrotécnica (CENELEC):** organismo relacionado con la normalización electrotécnica.
- **Instituto Europeo de Estándares de Telecomunicaciones (ETSI):** organismo europeo relacionado con las telecomunicaciones.
- **Estándares Europeos (EN):** estándares europeos.
- **Comité Técnico de Normalización (CTN):** comité relacionado con tareas de normalización.
- **Asociación Española de Normalización y Certificación (AENOR):** organismo citado en el material relacionado con normalización y certificación.


## 1.8. DOCUMENTACIÓN TÉCNICA

La documentación técnica permite registrar de forma sistemática todo el trabajo realizado sobre una red.

Debe conservar información sobre la topología seleccionada y la configuración de los diferentes dispositivos.

### INFORMACIÓN QUE DEBE CONTENER

- **Cableado:** características de la instalación realizada.
- **Topología:** estructura utilizada en la red.
- **Cableado estructurado:** información sobre su organización.
- **Mapa físico:** distribución física de los dispositivos.
- **Mapa lógico:** configuración y comunicación de los equipos.
- **Dispositivos:** configuración de los diferentes elementos utilizados.

### ORGANIZACIÓN DE LA DOCUMENTACIÓN

- **Soportes:** puede almacenarse en papel, carpetas o documentos electrónicos.
- **Mapas extensos:** pueden dividirse en varias páginas.
- **Jerarquización:** permite ordenar la información según su importancia o nivel de detalle.
- **Tablas:** pueden utilizarse para representar información más detallada.

> [!important] Importante
> Una buena documentación debe permitir que otro técnico pueda saber:
>
> **qué hay → dónde está → cómo está conectado → cómo está configurado**
