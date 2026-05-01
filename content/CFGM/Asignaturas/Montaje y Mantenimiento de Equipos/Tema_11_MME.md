---
title: Tema 11
tags:
  - Software
  - SistemaArchivos
  - GestorArranque
---
# INSTALACIÓN DE PROGRAMAS
## Tipos de instalaciones

- **Instalación estándar o completa:** desde cero con CD/DVD instalador.
	1. Configurar BIOS para arrancar desde la unidad.
	2. Particionar el disco y elegir partición de instalación.
	3. Actualizar drivers de los dispositivos.
- **Sistemas preinstalados con partición de recuperación:**
	- Crear una imagen (copia) almacenada en una partición del disco.
	- Agiliza la instalación en múltiples equipos.
- **Instalaciones desatendidas:**
	- Automatizadas, sin intervención del usuario.
	- Usan un **archivo de respuesta** (script) con todos los parámetros.
	- Si el programa no responde, muestra pantallas para selección manual.

## Instalaciones masivas

Pasos:
1. Crear una imagen de un disco duro.
2. Restaurar esa imagen en varios equipos a la vez mediante red.
- Ejemplo de software: **Symantec Ghost Corporate Edition** (Norton Ghost).
	1. Generar un archivo de respuestas para instalación desatendida.
	2. Crear la imagen.
	3. Almacenar imagen y archivo en un recurso compartido.

## Preinstalación

Herramientas que permiten personalizar la instalación del SO:
- Personalizar interfaz (fondo, tema, gadgets, opciones de escritorio).
- Añadir nuevos ajustes.
- Deshabilitar servicios.
- Eliminar elementos no necesarios.
- Colocar actualizaciones, drivers o aplicaciones al instalar.
- **Ejemplo:** `RT7 Lite` → crea imágenes desde una ISO estándar, alcanzando un nivel similar a una instalación clonada.

## Particionado de disco

- Un disco duro nuevo suele venir sin formato.
- Para crear un **sistema de archivos** necesitamos una partición.
- El sistema de archivos permite buscar, guardar y acceder a datos. Diferentes sistemas ofrecen distinto rendimiento.

### Particiones

Dos formas de particionar:
- **MBR (Master Boot Record):**
	- Máximo 4 particiones por disco.
	- Una debe ser **primaria** (para arranque). Las primarias se formatean directamente.
	- Las **extendidas** actúan como contenedores (no se formatean directamente).
- **EFI (Extensible Firmware Interface) - GPT:**
	- Hasta 128 particiones por disco.
	- Menús gráficos, acceso remoto, facilita solución de problemas.

### Operaciones con particiones

- **Creación:** indicar tipo (primaria, extendida, lógica) y tamaño.
	- Desde CD de instalación, `fdisk` (MS-DOS/Linux), administrador de discos de Windows/Ubuntu, o utilidades como `Partition Magic`, `Partition Master`, `Gparted`.
- **Eliminación:** se pierden todos los datos de la partición.
- **Redimensionamiento:** modificar tamaño sin perder datos (requiere espacio suficiente).
- **Ocultar/mostrar:** para particiones a las que no se accede desde el arranque.

### Software de gestión de particiones

- Algunos integrados en el SO, otros externos (intuitivos y fáciles de usar).

## Creación de imágenes y restauración

- **Imagen:** archivo (ej. ISO) con copia exacta y comprimida del contenido de un CD/DVD.
- Proceso: descargar imagen → grabar en soporte físico.

### Creación de imágenes

**En Windows:**
1. Insertar CD en la grabadora.
2. Doble clic en la imagen ISO → se abre el programa (Nero, Clone CD...).
3. Elegir grabadora y seleccionar "Grabar".

**En Ubuntu Linux:** usar paquetes como `ISO Master` o `Furius ISO Mount`.
Pasos con ISO Master:
1. Archivo → Nuevo.
2. Seleccionar archivos/carpetas → Agregar.
3. Si hay error → Eliminar.
4. Crear nuevo directorio si es necesario.
5. Guardar: Archivo → Guardar como.
6. Para ver contenido: doble clic en la imagen.
7. Para extraer: clic en Extraer.

### Restauración del sistema

Dos formas:
- **Clonar el disco duro:** copia exacta (datos, programas, configuración). Se usa para restaurar en otros equipos con mismas características. Software: `Clonezilla` o `Gparted`.
- **Punto de restauración:** retorna el equipo a un estado anterior (fecha indicada). Se crea cuando el equipo está funcionando perfectamente. Se gestiona desde Panel de Control → Restaurar sistema.

## Opciones de arranque de un equipo

- En la BIOS, apartado **BOOT** → configurar orden de búsqueda del SO.
- Dispositivos desde los que arrancar:
	- **CD-ROM:** se puede crear un CD con la imagen del SO y programas.
	- **Live CD:** distribución de SO en CD autoejecutable, interfaz visual.
	- **Memoria USB:** útil cuando no hay CD-ROM (ej. portátiles).
		- En Windows: requiere programa informático.
		- En Linux: se puede crear por secuencias de comandos.