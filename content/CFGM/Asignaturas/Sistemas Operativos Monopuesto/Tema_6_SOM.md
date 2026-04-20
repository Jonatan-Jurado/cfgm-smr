---
title: Tema 6
tags:
  - Windows
---
# TAREAS BÁSICAS DE CONFIGURACIÓN Y MANTENIMIENTO EN LOS SISTEMAS OPERATIVOS PROPIETARIO

## ARRANQUE DEL SISTEMA
*[[menu-de-opciones-avanzadas-de-arranque|Opciones Avanzadas de Arranque]]* : al iniciar el PC pulsar la tecla F9. 
Tienes varias opciones:
- **[[modo-seguro-con-funciones-de-red|Modo Seguro con Funciones de Red]]**: Incluye los controladores necesarios para conectarse a Internet o a una red local.
- **[[modo-seguro|Modo Seguro]] con Símbolo de Sistema**: Inicia el sistema directamente en una ventana de comandos (CMD) en lugar de la interfaz visual.
- **Habilitar el Registro de Arranque**: Crea un archivo de texto con la lista de todos los controladores cargados para identificar fallos.
- **Última Configuración válida conocida**: Carga el registro y los controladores que funcionaron correctamente la última vez que se inició [[sesion-de-usuario|sesión]].
- **Modo de Restauración de Servicios de directorio**: Opción para servidores que permite restaurar el [[proceso-del-sistema|servicio]] de Active Directory.
- **Modo Depuración**: Envía información técnica del sistema a otro equipo para análisis de errores avanzados.
- **Deshabilitar el Reinicio Automático**: Evita que el PC se reinicie tras un error grave para que puedas leer el código del pantallazo azul.
- **Deshabilitar uso obligatorio de controladores firmados**: Permite instalar [[controlador-de-dispositivo|drivers]] que no tienen firma digital oficial.
- **Iniciar [[sistema-operativo-windows|Windows]] Normalmente**: Intenta arrancar el sistema con todos los controladores y [[software-y-algoritmo|programas]] habituales.
### Sesiones:
Los Distintos Usuarios puede:
- Tener sus propios Directorios
- Tener sus propios Programas independientes de los otros users
- Compartir Documentos
- En el proceso de apagado se añade: Cerrar Sesión, Suspender, Hivernar

## UTILIZACIÓN DEL S.O
Se puede usar de forma gráfica o mediante comandos:
- **[[interfaz-grafica-de-usuario|GUI]]** Interfaz Gráfica: [[barra-de-tareas|Barra de tareas]], Ventanas, Conf. de escritorio, [[Accesibilidad]] para personas con discapacidades
- **[[interfaz-de-linea-de-comandos|GLI]]** Interfaz Linea de Comandos (CMD)

## OPERACIONES CON ARCHIVOS
Los archivos tienen éste formato -> nombre.[[extension-de-archivo|extensión]] -  Ejemplo -> mi_archivo.txt

### USO BÁSICO DE GLI - CMD
<iframe width="560" height="315" src="https://www.youtube.com/embed/AQXbYVPEx9c?si=SxbfSXPTDaRY9owI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


#### Comando de cambio de nombre

Para realizar esta acción en la consola se utiliza: `rename archivo_actual.txt archivo_nuevo.bat`

---

### Comodines

Se utilizan para filtrar búsquedas o aplicar comandos a varios archivos a la vez:

- **Símbolo `?`**: Sustituye a un único carácter cualquiera.
    
- **Símbolo `*`**: Sustituye a un grupo de varios caracteres.
    

---

### Operaciones más comunes

#### Operaciones con directorios

- **Crear un directorio**: Se usa `mkdir` seguido del nombre o la ruta. `mkdir NuevaCarpeta`
    
- **Cambiar de directorio**: Permite navegar por el sistema mediante [[ruta-relativa|rutas relativas]] o absolutas. `cd C:\Users\Documentos`
    
- **Listar contenido**:
    
    - De forma informativa (lista): `dir`
        
    - De forma gráfica (árbol): `tree`
        
- **Copiar directorio**: Se usa `xcopy`. Para incluir subdirectorios se añade el modificador `/e`. `xcopy CarpetaOrigen CarpetaDestino /e`
    
- **Mover directorio**: Desplaza la carpeta con todo su contenido. `move CarpetaOrigen RutaDestino`
    
- **Eliminar directorio**: Se usa `rd`. Para eliminar directorios que no están vacíos, se añade `/s`. `rd CarpetaBorrar /s`
    

#### Operaciones con ficheros

- **Crear un fichero**: Permite crear un archivo definiendo su tamaño. `fsutil file createnew archivo.txt 1000`
    
- **Abrir/Leer un fichero**: Muestra el contenido de texto en la consola. `type archivo.txt`
    
- **Copiar un fichero**: `copy nota.txt C:\Copia\nota_backup.txt`
    
- **Mover un fichero**: `move archivo.txt C:\NuevaRuta\`
    
- **Eliminar un fichero**: Se pueden usar indistintamente: `del archivo.txt` o `erase archivo.txt`
    

---

### Permisos y atributos

Los archivos y carpetas poseen permisos definidos para usuarios o grupos. En Windows, estos se gestionan gráficamente desde **Propiedades > Seguridad**, donde se pueden visualizar y editar los niveles de acceso.

---

### Estructura del árbol de directorios

Windows utiliza el [[explorador-de-archivos|Explorador de archivos]] para la [[administracion|administración]] y navegación. Los directorios críticos del sistema son:

- `C:\Windows\Boot`: Archivos para el arranque del sistema.
    
- `C:\Program Files`: Archivos de programas instalados.
    
    - `\Common Files`: Datos compartidos entre [[aplicacion|aplicaciones]].
        
- `C:\ProgramData`: Datos de programas compartidos (oculto).
    
    - `...\Start Menu`: Accesos directos del menú inicio.
        
    - `...\StartUp`: Programas que inician automáticamente con Windows.
        
- `C:\PerfLogs`: [[registro-del-procesador|Registros]] de rendimiento y aplicaciones.
    
- `C:\Users`: Carpetas personales de los usuarios (Escritorio, Documentos, [[directorio-etc|etc]].).
    
    - `\Public`: Archivos compartidos entre todos los usuarios locales.
        
- `C:\Windows`: Archivos del [[nucleo-del-sistema-operativo|núcleo del sistema operativo]].
    
    - `\Fonts`: Almacén de fuentes tipográficas.
        

---

### Rutas

Una ruta es la dirección específica de un archivo, donde cada nivel jerárquico se separa por la barra invertida `\`.

#### Tipos de rutas

- **Absoluta**: Indica la ubicación exacta partiendo desde la raíz del disco (ej. `C:\Windows\System32`).
    
- **Relativa**: Indica la ubicación partiendo desde la carpeta donde se encuentra el usuario actualmente (ej. `..\Documentos`).

## COMPRESIÓN Y DESCOMPRESIÓN DE ARCHIVOS
Comprimir es reducir el tamaño pero sin perder la información.
*GUI*: Se utiliza WinRAR o 7Zip

*GLI*: 
- *Comprimir un solo archivo*
	- Si quieres convertir un documento en un `.zip`:
		- `tar -a -c -f nombre_final.zip archivo_original.txt`
- Comprimir una carpeta completa
	- Ideal para hacer backups de tus proyectos: 
		- `tar -a -c -f copia_seguridad.zip CarpetaProyecto`
- Comprimir solo archivos de un tipo específico (Comodines)
	- Si quieres meter todos tus archivos de texto en un solo comprimido: 
		- `tar -a -c -f todos_los_textos.zip *.txt`
- Extraer todo en la carpeta actual
	- `tar -x -f archivo.zip`
- Extraer en una carpeta específica
	- Para mantener el orden y que no se mezclen los archivos en el escritorio: 
		- `tar -x -f archivo.zip -C C:\Ruta\De\Destino`
- Extraer un solo archivo de dentro del zip
	- Si el zip es gigante y solo necesitas una cosa: 
		- `tar -x -f archivo.zip documento_especifico.pdf`


## ACTUALIZACIÓN DEL S.O
3 Tipos:
- *Actualizaciones Críticas*: Necesarias / Mejoran la Seguridad
- *Service Pack*: Conjunto de Programas que mejoran el S.O (Gran Peso)
- *Drivers*: Para dar Soporte a Nuevos Dispositivos
Windows Update te permite la opción de Actualizar Automáticamente!

## AGREGAR / CONFIGURAR / ELIMINAR / ACTUALIZAR - PROGRAMAS
Para Instalar un programa necesitamos el archivo .exe que viene en el CD - USB - O hemos descargado.

Dando a la tecla de Windows+X se abre un menú -> Aplicaciones Instaladas (tenemos las Apps para eliminar comprobar y lo que requieras)

## CONFIGURAR ENTORNO DE RED Y CONECTIVIDAD

### WI-FI
Redes -> Añadir Red -> Conectar ->  Poner contraseña

### ETHERNET
#### 🛠️ Paso 1: Diagnóstico Automático
- **Inicia el solucionador**: Haz clic derecho en el icono de red (la bola del mundo o el monitor) junto al reloj y selecciona **Solucionar problemas**.
- **Sigue al asistente**: El programa "Diagnósticos de red" buscará fallos automáticamente. Elige la opción que mejor describa tu problema y deja que Windows intente repararlo solo.
#### ⚙️ Paso 2: Configuración Manual (Si el paso 1 falla)

Si sigues sin internet, toca revisar la IP manualmente:
1. **Entra en ajustes**: Haz clic derecho en el icono de red y elige **Abrir Configuración de red e internet**.
2. **Busca tu adaptador**: Haz clic en la opción **Cambiar opciones del adaptador**.
3. **Propiedades de red**: Haz clic derecho sobre tu conexión (Ethernet o Wi-Fi) y selecciona **Propiedades**.
4. **Localiza el protocolo**: Busca en la lista **Protocolo de internet versión 4 (TCP/IPv4)**, selecciónalo y dale al botón **Propiedades**.
#### 🌐 Paso 3: Configurar la IP y DNS

Dentro de esa ventana tienes dos caminos:

- **Opción A (Recomendada)**: Selecciona **Obtener una dirección IP automáticamente**. Así el router se encarga de todo.
- **Opción B (IP Fija)**: Si necesitas una IP específica, marca **Usar la siguiente dirección IP**.
    - _Recuerda_: Los tres primeros bloques de números deben ser iguales a los de tu router (ej: `192.168.1.X`), pero el último número debe ser único para tu PC.
- **Configurar DNS**: Si las webs no cargan pero tienes red, marca **Usar las siguientes direcciones de servidor DNS** y escribe los servidores de tu proveedor (o los de Google: `8.8.8.8`).
#### ✅ Paso 4: Finalizar

- **Guardar**: Pulsa **Aceptar** en todas las ventanas.
- **Comprobar**: Abre tu navegador y carga cualquier página para verificar que ya tienes conexión.

## CONFIGURAR PERIFÉRICOS
- *Plug & Play*: S.O Busca automáticamente mediante Windows Update el controlador
- *Uso de CD*: A veces tiene mas funcionalidades adicionales 

## PAQUETES DE SISTEMA Y MÓDULOS DE CÓDIGO

Todos los S.O son vulnerables. Windows provee de actualizaciones.
- *Paquetes de Actualización*: Service Pack 1,2,3
- *Módulos de Código*: Solo para Windows Server 2012 R2 y Windows Server
	- *Nativo*: Gestiona la creación de distintos sitios web alojados en el servidor gestionado por los servicios de Internet Informatic Serve IIS.
	- *Administrativo:* Comprobación de formularios de Autentificación de los usuarios.
## INVENTARIO DEL SOFTWARE INSTALADO
Realiza la comprobación de listados en 'Programas y Características'
También puedes tenerlo desde cmd con éste comando: 
`winget list --accept-source-agreements > programas.txt`

O también éste para ver los instalados por el instalador de Windows:
`wmic product get name,version > lista_programas.txt`

## COMPROBAR EL FUNCIONAMIENTO DEL DISCO
1. Navegar al Disco Duro y click derecho
2. Propiedades
3. Herramientas
4. Comprobación de errores y Desfragmentación
5. Comprobar
6. Asistente de Windows para la comprobación de errores

## DOCUMENTACIÓN DEL PROCESO DE CONFIGURACIÓN

Incluir una guía de configuración dle proceso de instalación y parámetros de configuración
Puede ser Configuración Recomendada o Instalación Personalizada.