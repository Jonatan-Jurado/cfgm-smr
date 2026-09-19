---
title: Tema 1
tags:
  - SistemaOperativo
  - Servidores
  - Hardware
  - Redes
---
# Tema 1 - Introducción a los Sistemas Operativos en Red

## SISTEMAS OPERATIVOS EN RED

Un **sistema operativo** es el software encargado de gestionar los componentes hardware de un equipo informático.

Cuando los equipos necesitan comunicarse entre sí mediante una red, se utilizan **sistemas operativos en red**, normalmente instalados en el equipo que actúa como **servidor**.

- **Sistema operativo en red:** software preparado para administrar equipos y ofrecer servicios dentro de una red.
- **Servidor:** máquina que gestiona el flujo y la conexión de información en la red y proporciona servicios a los equipos clientes.
- **Cliente:** equipo que solicita servicios o recursos al servidor.
- **Comunicación cliente-servidor:** los clientes realizan peticiones y el servidor responde a dichas peticiones.

> [!important]
> El funcionamiento del modelo cliente-servidor se basa en:
>
> **CLIENTE → Petición → SERVIDOR → Respuesta → CLIENTE**

### OBJETIVOS DE UN SISTEMA OPERATIVO EN RED

- **Compartir recursos:** permite utilizar recursos propios del servidor y de otros equipos de la red.
- **Soportar varios usuarios:** puede atender simultáneamente a diferentes usuarios.
- **Ofrecer servicios:** proporciona servicios a los equipos clientes conectados a la red.
- **Gestión centralizada:** permite administrar desde el servidor los usuarios y recursos de los equipos clientes.

---

## 1.1. CARACTERÍSTICAS DE LOS SISTEMAS OPERATIVOS EN RED

Dentro de una red existen equipos que cumplen funciones diferentes.

- **Servidor:** proporciona recursos y servicios a otros equipos.
- **Cliente:** utiliza los recursos o servicios ofrecidos por el servidor.
- **Sistema operativo:** puede ser diferente en clientes y servidores porque realizan funciones distintas.

El sistema operativo instalado en el **servidor** está especialmente preparado para administrar usuarios, recursos, comunicaciones y servicios de red.

> [!info]
> Un servidor no es simplemente un ordenador más potente. Su función principal es **proporcionar y administrar servicios para otros equipos de la red**.

---

## 1.2. FUNCIONES DE UN SISTEMA OPERATIVO

El sistema operativo es el software encargado de gestionar los diferentes componentes y recursos del ordenador.

### GESTIÓN DE PROCESOS

- **Gestión de procesos:** organiza los procesos que deben ejecutarse en el sistema.
- **Multitarea:** permite ejecutar varios procesos aparentemente al mismo tiempo.
- **Multiusuario:** permite atender a varios usuarios simultáneamente.
- **Despachador:** se encarga de gestionar el turno de ejecución de los diferentes procesos.

Cuando llegan más procesos de los que el procesador puede ejecutar directamente, el sistema operativo decide **cuándo se ejecuta cada uno**.

### GESTIÓN DE MEMORIA

- **Gestión de memoria:** asigna espacio de memoria a los procesos que se están ejecutando.
- **Asignación:** cada proceso necesita una zona determinada de memoria para poder funcionar.
- **Administración:** el sistema operativo controla cómo se utiliza y distribuye la memoria disponible.

La gestión de memoria está directamente relacionada con la gestión de procesos.

### GESTIÓN DE ARCHIVOS

- **Gestión de archivos:** administra cómo se organizan los datos dentro de los dispositivos de almacenamiento.
- **Sistema de ficheros:** determina cómo se almacenan y organizan los archivos.
- **Espacio libre y ocupado:** controla qué zonas del disco están disponibles.
- **Archivos y directorios:** permite crearlos, modificarlos, eliminarlos y organizarlos.

### GESTIÓN DE DISPOSITIVOS DE ENTRADA/SALIDA

- **Gestión de dispositivos:** permite al sistema operativo controlar los diferentes dispositivos conectados al equipo.
- **Drivers:** controladores que permiten que el sistema operativo reconozca y utilice correctamente cada dispositivo.

### GESTIÓN DE LA RED

- **Gestión de red:** controla las comunicaciones entre los diferentes equipos.
- **Protocolos:** establecen las reglas que deben seguir los dispositivos para comunicarse.
- **Tarjeta de red:** necesita sus correspondientes controladores para funcionar correctamente.
- **Comunicación cliente-servidor:** permite gestionar las peticiones de los clientes y las respuestas del servidor.

### PROTECCIÓN Y SEGURIDAD

- **Protección:** permite que el sistema continúe funcionando correctamente ante posibles fallos.
- **Seguridad:** controla que únicamente los usuarios autorizados puedan acceder a determinados recursos.
- **Permisos:** determinan qué acciones puede realizar cada usuario.
- **Roles:** permiten establecer diferentes niveles de acceso según el tipo de usuario.

> [!important]
> **PROTECCIÓN ≠ SEGURIDAD**
>
> - **Protección:** evita que un fallo provoque que el sistema deje de funcionar.
> - **Seguridad:** evita que usuarios no autorizados accedan a información o recursos.

---

## 1.3. CARACTERÍSTICAS DIFERENCIADORAS DE LOS SISTEMAS OPERATIVOS EN RED

Los sistemas operativos orientados a servidores presentan características específicas para gestionar correctamente una red.

### MULTIPROCESAMIENTO SIMÉTRICO

- **Multiprocesamiento simétrico:** permite repartir las tareas de forma equilibrada entre los recursos de procesamiento disponibles.
- **Objetivo:** aprovechar mejor la capacidad del sistema y distribuir las cargas de trabajo.

### MODELO CLIENTE-SERVIDOR

- **Modelo cliente-servidor:** sistema de comunicación en el que los clientes realizan peticiones a un servidor.
- **Cliente:** solicita un recurso o servicio.
- **Servidor:** recibe la petición, la procesa y devuelve una respuesta.

```text
CLIENTE
   │
   │ Petición
   ▼
SERVIDOR
   │
   │ Respuesta
   ▼
CLIENTE
```
