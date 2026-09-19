---
title: Tema 2
tags:
  - Windows
  - Servidores
  - SistemaOperativo
  - Redes
---
# Tema 2 - Instalación, actualización y monitorización de sistemas operativos en red propietarios

Este tema estudia el proceso completo para poner en funcionamiento un sistema operativo de servidor propietario, utilizando **Windows Server** como referencia.

El proceso general comprende:

1. Comprobar la compatibilidad del equipo.
2. Planificar la instalación.
3. Elegir el sistema de archivos y los componentes.
4. Instalar el sistema operativo.
5. Configurar y personalizar el servidor.
6. Actualizarlo.
7. Comprobar la conectividad.
8. Monitorizar su funcionamiento.
9. Documentar todo el proceso y las incidencias.

<iframe
  width="100%"
  height="500"
  src="https://www.youtube.com/embed?listType=playlist&list=PLThkZy_SrhoUyN24kzmjo01a03vYqKXdx"
  title="Curso completo - Windows Server 2019"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen>
</iframe>


[▶ Ver curso completo en YouTube](https://www.youtube.com/playlist?list=PLThkZy_SrhoUyN24kzmjo01a03vYqKXdx)




---

## 2.1. ESTUDIO DE COMPATIBILIDAD DEL SISTEMA INFORMÁTICO

Antes de instalar un sistema operativo de servidor hay que comprobar que el equipo cumple las condiciones necesarias.

### VERSIONES DE WINDOWS SERVER

El material utiliza **Windows Server** como sistema operativo propietario de referencia y menciona las siguientes versiones:

- **Windows Server 2008:** una de las versiones anteriores del sistema.
- **Windows Server 2012:** versión posterior que incorpora mejoras respecto a las anteriores.
- **Windows Server 2016:** evolución de Windows Server.
- **Windows Server 2019:** versión utilizada como referencia para explicar sus diferentes ediciones.

### EDICIONES DE WINDOWS SERVER 2019

- **Datacenter:** orientada a servidores de gran escala y permite virtualización.
- **Standard:** edición indicada en el tema como la más utilizada; dispone de un número limitado de conexiones, suficiente según el material para una empresa mediana.
- **Essentials:** orientada a pequeñas empresas, con un máximo de **25 usuarios y 50 dispositivos**.


---

## PASOS PREVIOS A LA INSTALACIÓN

### 1. INVENTARIO DEL HARDWARE

El primer paso consiste en conocer los componentes físicos instalados en el equipo.

- **Inventario hardware:** relación de todos los componentes físicos disponibles.
- **Everest:** programa mencionado en el material para realizar seguimiento de cambios en los sistemas.
- **Hardware Component List (HCL):** lista utilizada para comprobar la compatibilidad entre el hardware y el sistema operativo.

### 2. COMPROBACIÓN DE COMPATIBILIDAD

Hay que estudiar tanto la compatibilidad del hardware como la del software.

- **Compatibilidad hardware:** comprueba que los componentes físicos puedan funcionar correctamente con el sistema operativo.
- **Compatibilidad software:** comprueba que los programas que vamos a utilizar puedan ejecutarse en el sistema.
- **Controladores o drivers:** software necesario para que el sistema operativo pueda utilizar correctamente determinados dispositivos.


Los controladores pueden instalarse:

- Durante la instalación del sistema operativo.
- Después de finalizar la instalación.

Si necesitamos información sobre un componente, también podemos consultar las especificaciones proporcionadas por el fabricante.

---

## 2.2. PLANIFICACIÓN DE LA INSTALACIÓN

Antes de instalar debemos decidir:

- Dónde se instalará el sistema operativo.
- Qué sistema de archivos utilizaremos.
- Qué componentes y funciones necesitaremos.
- Qué controladores deberán instalarse.

### REQUISITOS DEL EQUIPO

Según los requisitos indicados en el material para Windows Server:

- **Procesador:** arquitectura de 64 bits y frecuencia de 1,4 GHz.
- **Random Access Memory (RAM):** mínimo de 512 MB, aunque se aconsejan 2 GB.
- **Disco duro:** mínimo de 32 GB de espacio.
- **Adaptador Ethernet:** debe disponer del rendimiento necesario y puede utilizar arquitectura Peripheral Component Interconnect Express (PCI Express).
- **Digital Versatile Disc (DVD):** necesario si se utiliza este medio físico para realizar la instalación.

---

## PARTICIONADO DEL DISCO

El sistema operativo puede instalarse:

- **Disco completo:** utilizando toda la unidad.
- **Partición:** utilizando solamente una parte del disco.

Una partición permite dividir el disco en diferentes espacios independientes.

Se recomienda utilizar:

- **Partición del sistema:** para instalar el sistema operativo.
- **Partición de datos:** para programas y almacenamiento de información.

> [!example]
> ### EJEMPLO
>
> Imaginemos un disco dividido en dos:
>
> - **Partición C:** Windows Server.
> - **Partición D:** programas y datos.
>
> Si es necesario formatear la partición del sistema operativo, los datos almacenados en la otra partición permanecen separados.

> [!important]
> Separar **sistema operativo y datos** facilita el mantenimiento del servidor.

---

## ELECCIÓN DEL SISTEMA DE ARCHIVOS

Para Windows Server 2012 y Windows Server 2016, el material indica la utilización de **New Technology File System (NTFS)**.

- **NTFS:** sistema de archivos con características relacionadas con la seguridad.
- **Permisos:** permite administrar los permisos del sistema operativo.
- **Cuentas de usuario:** permite aplicar características asociadas a usuarios, como límites de espacio.

> [!important]
> NTFS es especialmente relevante en un servidor porque permite gestionar **permisos y características asociadas a las cuentas de usuario**.

---

## ELECCIÓN DE COMPONENTES Y UTILIDADES

Los sistemas operativos en red se diferencian especialmente por los servicios y funciones que pueden proporcionar.

Aquí aparece una diferencia especialmente importante.

> [!important]
> ### ROL ≠ SERVICIO
>
> - **Rol o función del servidor:** conjunto de aplicaciones que permite realizar una tarea específica en la red.
> - **Servicio:** programa que proporciona esa función.
>
> **Ejemplos de roles indicados en el tema:** DHCP, DNS o servidor web.
>
> **Rol = qué función realiza el servidor.**
>
> **Servicio = programa que permite proporcionar esa función.**

### EJEMPLOS DE FUNCIONES DE RED

- **Dynamic Host Configuration Protocol (DHCP):** aparece en el tema como una posible función o rol del servidor.
- **Domain Name System (DNS):** aparece como otra función que puede proporcionar el servidor.
- **Servidor web:** permite que el servidor desempeñe una función relacionada con servicios web.

---

## 2.3. MÉTODOS DE INSTALACIÓN

Un sistema operativo de servidor puede instalarse principalmente mediante dos métodos:

### INSTALACIÓN ATENDIDA

- **Instalación atendida:** el usuario interviene durante todo el proceso y realiza los diferentes pasos de instalación.
- **Interacción:** requiere que una persona vaya tomando decisiones durante la instalación.

Puede realizarse mediante:

- **DVD:** soporte físico de instalación.
- **Universal Serial Bus (USB):** dispositivo desde el que puede iniciarse la instalación.
- **Recurso compartido:** ubicación disponible a través de la red.
- **Máquina virtual:** entorno virtualizado donde puede instalarse el sistema sin modificar directamente el equipo físico.


### INSTALACIÓN DESATENDIDA

- **Instalación desatendida:** el proceso se configura previamente y posteriormente se ejecuta automáticamente sin necesitar la interacción continua del usuario.
- **Automatización:** las respuestas y opciones necesarias se preparan antes de comenzar.
- **Kit de instalación:** conjunto de programas que Microsoft proporciona para automatizar este tipo de instalaciones.


---

## MÁQUINAS VIRTUALES

Una máquina virtual permite instalar el sistema operativo sin realizar cambios directamente sobre el equipo físico.

- **Ventaja:** permite realizar pruebas fácilmente.
- **Flexibilidad:** puede adaptarse a diferentes necesidades.
- **Inconveniente indicado en el material:** puede disponer de menos recursos y reducir el rendimiento.
- **Uso recomendado en el tema:** especialmente útil para realizar pruebas.

> [!example]
> Si queremos aprender a instalar Windows Server sin modificar nuestro ordenador real, podemos hacerlo primero en una **máquina virtual**.

---

## 2.4. CONFIGURACIÓN Y PERSONALIZACIÓN DEL SERVIDOR

Una vez terminada la instalación comienza la configuración del servidor.

La configuración debe adaptarse a:

- Las necesidades de la empresa.
- Las características de la red.
- Los servicios que deberá proporcionar.

El material utiliza la ventana de **Tareas de configuración inicial** como punto de partida.

---

## INFORMACIÓN Y CONFIGURACIÓN DEL SERVIDOR

Entre las primeras tareas encontramos:

- **Cuenta del administrador:** configuración de la cuenta encargada de administrar el servidor.
- **Dominio:** configuración de la pertenencia del servidor a un dominio.
- **Zona horaria:** establece la hora correspondiente a la ubicación del equipo.
- **Red:** configura las conexiones y adaptadores de red.

### CONFIGURACIÓN DE RED

Desde los adaptadores de red podemos consultar información como:

- **Estado:** indica la situación actual del adaptador.
- **Velocidad:** muestra la velocidad de la conexión.
- **Datos transmitidos y recibidos:** muestra información sobre el tráfico del adaptador.
- **Internet Protocol (IP):** dirección utilizada para identificar el equipo en la red.
- **Máscara de red:** información utilizada para determinar la red a la que pertenece el equipo.
- **Domain Name System (DNS):** configuración relacionada con la resolución de nombres.
- **Nombre del equipo:** identifica al ordenador dentro de la red.
- **Dominio:** indica el dominio al que pertenece el servidor.

> [!important]
> El **nombre del equipo debe ser único dentro de la red** para evitar confusiones.

---

## CONFIGURACIÓN DEL DOMINIO

El servidor puede:

- **Unirse a un dominio:** incorporarse a un dominio que ya existe.
- **Crear un dominio:** establecer uno nuevo desde el propio servidor.

La gestión de dominios será especialmente importante posteriormente para administrar equipos, usuarios y recursos de forma centralizada.

---

## PERSONALIZACIÓN DEL SERVIDOR

Desde las opciones de personalización podemos agregar o quitar funciones.

- **Agregar funciones:** permite incorporar nuevos roles al servidor.
- **Eliminar funciones:** permite retirar funciones que ya no sean necesarias.
- **Rol del servidor:** determina qué función desempeñará el equipo.

Algunos ejemplos indicados en el tema son:

- Servidor de archivos.
- Gestor de dominios.
- Servidor de aplicaciones web.

> [!tip]
> Piensa en un servidor como una persona dentro de una empresa:
>
> Su **rol** determina qué trabajo tiene asignado.
>
> Un mismo servidor puede configurarse para realizar determinadas funciones dependiendo de las necesidades de la red.

---

## CONFIGURACIÓN DE LA CONECTIVIDAD

Uno de los elementos de seguridad que debemos configurar es el cortafuegos.

- **Firewall o cortafuegos:** mecanismo encargado de controlar determinadas comunicaciones de red.
- **Firewall de Windows:** herramienta utilizada para configurar el cortafuegos del servidor.
- **Configuración avanzada:** permite acceder a opciones adicionales del firewall.

### COMPROBACIÓN DE CONECTIVIDAD

El tema utiliza el comando:

`ping`

- **ping:** comando empleado para comprobar la conectividad entre equipos de la red.

El material indica realizar una comprobación desde el servidor hacia el cliente.

> [!example]
> Si queremos saber si el servidor puede comunicarse con un cliente, podemos ejecutar:
>
> `ping DIRECCION_IP_DEL_CLIENTE`
>
> Si existe comunicación, recibiremos respuestas desde el equipo de destino.

> [!important]
> El material indica deshabilitar el cortafuegos durante esta comprobación de conectividad y utilizar `ping` entre servidor y cliente.

### CONFIGURACIÓN DEL CLIENTE

La tarjeta de red del cliente puede configurarse:

- **Manualmente:** introduciendo directamente su configuración.
- **Mediante DHCP:** obteniendo automáticamente parte de la configuración de red.

Entre los parámetros utilizados encontramos:

- Dirección IP.
- Máscara de red.
- Configuración del dominio.
- DHCP.

---

## ACTUALIZACIÓN DEL SERVIDOR

La actualización aparece en distintos puntos del tema, pero forma parte del mismo proceso de mantenimiento.

- **Actualización:** descarga e instala las versiones más recientes disponibles.
- **Objetivo:** mantener el servidor actualizado y seguro.
- **Actualización automática:** el sistema gestiona automáticamente las actualizaciones.
- **Actualización manual:** el administrador selecciona qué actualización desea instalar.
- **Informe de errores:** permite enviar información a Microsoft sobre errores producidos en el equipo.

> [!important]
> Antes de poner definitivamente el servidor en funcionamiento es recomendable actualizar tanto el sistema como los servicios instalados.

---

# 2.5. FALLOS Y MONITORIZACIÓN DEL SISTEMA

Una vez instalado y configurado el servidor debemos comprobar que funciona correctamente.

## POSIBLES FALLOS DURANTE LA INSTALACIÓN

### PROBLEMAS DE LICENCIA

Windows Server es un sistema operativo propietario y necesita una licencia válida.

- **Licencia válida:** permite utilizar correctamente el producto adquirido.
- **Licencia inexistente o no válida:** puede provocar que se utilice una versión de prueba.
- **Versión de prueba:** el material indica una duración de 60 días, ampliable hasta un máximo de 180 días.

### PROBLEMAS EN MÁQUINAS VIRTUALES

- **Flexibilidad:** permiten adaptar fácilmente el entorno a las necesidades.
- **Recursos:** necesitan memoria y capacidad de procesamiento.
- **Rendimiento:** según el material, una máquina virtual puede reducir el rendimiento si no dispone de suficientes recursos.
- **Pruebas:** resultan especialmente apropiadas para realizar instalaciones de prueba.

### PROBLEMAS DE RED

- **Falta de conexión:** puede provocar problemas importantes porque el servidor está diseñado para comunicarse con otros equipos.
- **Conectividad:** debe comprobarse que el servidor pueda comunicarse correctamente con la red.

### PROBLEMAS DE CONTROLADORES

- **Driver ausente:** un dispositivo puede no ser reconocido si no dispone del controlador adecuado.
- **Solución:** instalar el driver correspondiente al dispositivo.

---

## MONITORIZACIÓN DEL SISTEMA

La **monitorización** consiste en observar el funcionamiento del servidor para detectar fallos, errores o problemas de rendimiento y averiguar sus causas.

Windows Server incorpora herramientas propias para realizar esta tarea.

> [!important]
> La monitorización debe realizarse **periódicamente**, no únicamente cuando aparece un problema.

### HERRAMIENTAS DE MONITORIZACIÓN

- **Visor de eventos:** registra información, alertas y errores producidos en el sistema.
- **Monitor de recursos:** muestra el rendimiento de diferentes componentes del equipo.
- **Monitor de rendimiento:** permite generar alertas mediante los contadores seleccionados.
- **Monitor de confiabilidad:** muestra información sobre la estabilidad del equipo y mantiene un historial de problemas.
- **Administrador de tareas de Windows:** permite observar en tiempo real los procesos, servicios y utilización de recursos.

### MONITOR DE RECURSOS

Permite consultar especialmente:

- **Central Processing Unit (CPU):** utilización del procesador.
- **Memoria:** consumo de memoria del sistema.
- **Disco:** actividad del almacenamiento.
- **Red:** estado y utilización de las comunicaciones.

> [!important]
> ### NO CONFUNDIR LAS HERRAMIENTAS
>
> - **Visor de eventos:** registros, alertas y errores.
> - **Monitor de recursos:** CPU, memoria, disco y red.
> - **Monitor de rendimiento:** contadores y alertas.
> - **Monitor de confiabilidad:** estabilidad e historial de problemas.
> - **Administrador de tareas:** procesos, servicios y recursos en tiempo real.

> [!example]
> Si queremos saber por qué un servidor está funcionando lentamente:
>
> - Consultamos el **Monitor de recursos** para comprobar CPU, memoria, disco y red.
> - Consultamos el **Visor de eventos** para comprobar si se han registrado errores.
> - Podemos utilizar el **Administrador de tareas** para observar qué procesos están consumiendo recursos en ese momento.

---

# 2.6. DOCUMENTACIÓN DEL PROCESO DE INSTALACIÓN

Una vez finalizada la instalación es recomendable crear un documento donde quede registrado todo el procedimiento.

La documentación permite:

- Repetir posteriormente el proceso.
- Conocer cómo estaba configurado inicialmente el equipo.
- Consultar las modificaciones realizadas.
- Resolver incidencias.
- Facilitar el trabajo de otros administradores.

## INFORMACIÓN QUE DEBE DOCUMENTARSE

### ANTES DE LA INSTALACIÓN

- **Hardware instalado:** componentes físicos existentes.
- **Software instalado:** programas disponibles inicialmente.
- **Particiones:** distribución inicial del disco.
- **Drivers:** controladores instalados.
- **Usuarios:** cuentas existentes y configuradas.

### DURANTE Y DESPUÉS DE LA INSTALACIÓN

- **Pasos realizados:** procedimiento seguido durante la instalación.
- **Configuraciones:** cambios efectuados en el servidor.
- **Errores:** problemas encontrados.
- **Soluciones:** acciones utilizadas para resolver cada incidencia.
- **Modificaciones posteriores:** cambios realizados después de finalizar la instalación.

> [!important]
> Una buena documentación no explica únicamente **qué se hizo**, sino también:
>
> **qué problema apareció → qué se hizo para solucionarlo → cuál fue el resultado.**

### UTILIDAD PARA OTROS ADMINISTRADORES

La documentación permite que otro administrador pueda conocer:

- El estado actual del servidor.
- Cómo fue instalado.
- Qué problemas aparecieron.
- Cómo se resolvieron.
- Qué modificaciones se realizaron posteriormente.

---

## GESTIÓN DE INCIDENCIAS

Cuando aparece un problema podemos consultar la documentación de incidencias anteriores.

- **Incidencia presencial:** determinados problemas pueden resolverse directamente sobre el servidor.
- **Gestión remota:** otros problemas pueden resolverse sin encontrarse físicamente delante del equipo.
- **Soporte técnico:** los productos con licencia pueden disponer de soporte proporcionado por el fabricante.
- **Foros:** el material menciona los foros no oficiales como fuente de ayuda en el caso del software libre.

---

# PROCESO COMPLETO DEL TEMA

> [!tip]
> 
>
> Imagina que te entregan un servidor vacío y tienes que dejarlo funcionando en una empresa.
>
> **1. ¿Puede funcionar?**
> → Compruebas hardware, software y compatibilidad.
>
> **2. ¿Cómo lo voy a instalar?**
> → Planificas particiones, sistema de archivos y componentes.
>
> **3. ¿Quién hará la instalación?**
> → Atendida o desatendida.
>
> **4. ¿Qué necesita el servidor después?**
> → Configuras red, dominio, nombre, roles y seguridad.
>
> **5. ¿Está actualizado?**
> → Instalas las actualizaciones disponibles.
>
> **6. ¿Se comunica con la red?**
> → Compruebas la conectividad, por ejemplo con `ping`.
>
> **7. ¿Funciona correctamente?**
> → Monitorizas CPU, memoria, disco, red, procesos y errores.
>
> **8. ¿Cómo sabremos qué hicimos dentro de seis meses?**
> → Documentas todo el proceso y las incidencias.

---

# RESUMEN RÁPIDO

- **Compatibilidad:** debe comprobarse antes de instalar el sistema operativo.
- **HCL:** permite comprobar compatibilidad entre hardware y sistema operativo.
- **Drivers:** permiten que el sistema operativo utilice correctamente los dispositivos.
- **Requisitos mínimos:** procesador de 64 bits a 1,4 GHz, 512 MB de RAM y 32 GB de disco según el material.
- **Particiones:** permiten separar el sistema operativo de otros datos.
- **NTFS:** sistema de archivos utilizado por Windows Server con características de seguridad y permisos.
- **Rol:** función que desempeña el servidor.
- **Servicio:** programa que proporciona dicha función.
- **Instalación atendida:** necesita la intervención del usuario.
- **Instalación desatendida:** se configura previamente y se automatiza.
- **Máquina virtual:** permite realizar instalaciones de prueba sin modificar directamente el equipo físico.
- **Nombre del servidor:** debe ser único dentro de la red.
- **Dominio:** el servidor puede unirse a uno existente o crear uno.
- **Firewall:** controla determinadas comunicaciones del servidor.
- **ping:** permite comprobar la conectividad entre equipos.
- **Actualización:** debe realizarse antes de poner definitivamente en servicio el servidor.
- **Monitorización:** permite detectar problemas y analizar el rendimiento.
- **Visor de eventos:** muestra registros, alertas y errores.
- **Monitor de recursos:** muestra CPU, memoria, disco y red.
- **Monitor de rendimiento:** trabaja con contadores y alertas.
- **Monitor de confiabilidad:** muestra estabilidad e historial de problemas.
- **Administrador de tareas:** muestra procesos, servicios y recursos en tiempo real.
- **Documentación:** registra instalación, configuración, incidencias y soluciones.



> [!important]
> ### SECUENCIA GENERAL
>
> **Compatibilidad → planificación → instalación → configuración → actualización → conectividad → monitorización → documentación**

