---
title: Tema 7
tags:
  - Automatizacion
  - Hardware
  - Software
  - Windows
---
# ADMINISTRACIÓN DE LOS SISTEMAS OPERATIVOS PROPIETARIOS

## 7.1. Creación y Gestión de Usuarios y Grupos

Los usuarios y grupos permiten definir permisos y accesos al sistema de archivos.

### Tipos de Usuarios

- **Administrador:** Control total. Obligatorio (al menos uno). Uso: instalaciones y cambios críticos.
- **Estándar:** Usuario habitual del equipo.
- **Invitado:** Para uso ocasional. Se recomienda mantenerla **desactivada**.

### Gestión de Cuentas (Panel de Control)

|**Acción**|**Ruta / Procedimiento**|
|---|---|
|**Crear Usuario**|Inicio → Panel de Control → Cuentas de usuario → Administrar cuentas → Agregar.|
|**Cambiar Tipo**|Administrar cuentas → Seleccionar cuenta → Propiedades → Pertenencia a grupos.|
|**Contraseñas**|Los usuarios estándar pueden crear/cambiar la suya. La del administrador **nunca** debe desactivarse.|

### Grupos de Usuarios

Son colecciones de usuarios con los mismos derechos de seguridad.

- **Crear Grupo:** Ejecutar `mmc` → Archivo → Agregar complemento → Usuarios y grupos locales → Grupos → Acción → Grupo nuevo.

![[Pasted image 20260428163936.png]]

## 7.2. Gestión del Sistema de Archivos

Es la estructura que organiza los datos en el disco duro.

### Comparativa de Sistemas de Archivos

- **FAT32:** * _Ventaja:_ Alta compatibilidad (móviles, USB, Windows antiguos).
	- _Límite:_ Archivos de máximo 4 GB y particiones de hasta 8 TB.

- **NTFS (Windows 10):**
    - _Ventaja:_ Mayor seguridad (cifrado) y copias de seguridad instantáneas.
    - _Estructura:_ * **Sector:** Unidad mínima física (512 bytes).
	    - **Clúster:** Conjunto de sectores (potencia de 2).
        - **Volumen:** Partición del disco (hasta $2^{64}$ bytes).



## 7.3. Gestión de Procesos y Servicios

- **Administrador de tareas (`Ctrl+Alt+Supr`):** Informa sobre procesos, rendimiento y aplicaciones de inicio. Útil para forzar el cierre de apps bloqueadas.
- **Servicios:** Procesos en segundo plano que dan funcionalidad (ej. cola de impresión). Se gestionan desde la pestaña "Servicios".


## 7.4. Optimización y Diagnóstico

### Memoria RAM

- **Diagnóstico:** Herramienta "Diagnóstico de memoria de Windows" (requiere reinicio).
- **Optimización:** Para evitar el exceso de paginación (compactación), se puede desactivar `RunFullMemoryDiagnostic` en el Programador de tareas.

### Almacenamiento

- **Desfragmentación:** Reagrupar fragmentos dispersos de archivos para que sean consecutivos, acelerando la lectura.
- **Formateo:** Restablece el disco al estado de fábrica.
    - **Físico (Bajo nivel):** Borrado total e irrecuperable.
    - **Lógico (Alto nivel):** Borrado de índices; datos recuperables con software especial.



## 7.5. Rendimiento del Sistema

- **Monitorización nativa:** Administrador de tareas.
- **Software externo:**
    - **CPU-Z:** Características detalladas de componentes.
    - **SpeedFan:** Monitorización de temperaturas.

![[Pasted image 20260428164032.png]]

![[Pasted image 20260428164120.png]]


## 7.6. Compartición de Recursos

- **Grupo Hogar:** Permite compartir música, imágenes o documentos en una red local.
- **Requisito:** Configurar ubicación de red (doméstica/trabajo) y usar la contraseña generada por el sistema.



## 7.7. Configuración y Mantenimiento de Software

### Identificación de Hardware

- **Información del sistema:** Ejecutar `msinfo32` (muestra lista completa y estado).
- **Administrador de dispositivos:** Listado de elementos y sus controladores.
![[Pasted image 20260428164144.png]]

### Ciclo de Mantenimiento

1. Análisis.
2. Diseño.
3. Desarrollo.
4. Implementación.
5. Pruebas.
6. **Mantenimiento** (Corrección de errores y mejoras).

## 7.8. Automatización de Tareas

Se usa el **Programador de tareas** (requiere permisos de administrador).

- **Pasos:** Acción → Crear tarea básica → Configurar disparador (diario, semanal, etc.) → Elegir acción/programa → Finalizar.



## 7.9. Guiones Administrativos (Ficheros Batch)

Archivos con extensión `.bat` para automatizar comandos.

- **Estructura básica:**
    1. `@echo off` (oculta los comandos ejecutados).
    2. Lista de órdenes.
    3. `@pause` (mantiene la ventana abierta al finalizar).
- **Parámetros:** Se usan variables como `%1`, `%2`, `%3` para recoger datos pasados al ejecutar el archivo.



## 7.10. Recuperación del Sistema

- **Puntos de restauración:** Devuelven el sistema a un estado anterior estable sin perder necesariamente archivos de usuario, pero sí cambios de configuración y apps recientes.
- **Ruta:** Equipo → Propiedades → Protección del sistema → Crear.


## 7.11. Comprobación del Funcionamiento

- **SFC (System File Checker):** Repara archivos dañados del sistema.
- **Comando:** `sfc /scannow` (ejecutar en terminal como administrador).
- **Windows Update:** Gestión de parches de seguridad y mejoras.
- **Windows Defender:** Protección y bloqueo de amenazas en tiempo real.


## 7.12. Documentación e Incidencias

- Es fundamental documentar las tareas y soluciones encontradas
- Windows incluye documentación técnica y foros de ayuda para incidencias comunes.
- En caso de error persistente, contactar con el soporte técnico del fabricante.