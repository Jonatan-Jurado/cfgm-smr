---
title: "Directorios Principales del Sistema"
---
# Directorios Principales del Sistema
Los sistemas Linux organizan sus archivos siguiendo un estándar de jerarquía. Los [[Directorios]] más relevantes son:

*   **/bin:** Comandos básicos ejecutables del sistema para todos los usuarios.
*   **/sbin:** Comandos esenciales para la administración del sistema ([[Superusuario]]).
*   **/boot:** Archivos necesarios para el arranque del sistema ([[Kernel]], [[Gestor de Arranque]]).
*   **/dev:** Archivos de dispositivos que representan el [[Hardware]] del equipo.
*   **/etc:** Ficheros de configuración del sistema y de los servicios instalados.
*   **/home:** Directorios personales para los usuarios comunes.
*   **/root:** [[Directorio]] personal exclusivo del [[Administrador del Sistema]] (root).
*   **/lib:** Librerías esenciales compartidas por los programas de /bin y /sbin.
*   **/mnt:** Punto de montaje temporal para [[Sistemas de Archivos]] externos.
*   **/proc:** [[Sistema de Archivos]] virtual que proporciona información sobre el Kernel y los procesos.
*   **/var:** Archivos de datos variables, como archivos de registro (logs) o bases de datos.
*   **/usr:** Contiene aplicaciones y archivos de lectura para los usuarios.
*   **/tmp:** Archivos temporales de la sesión. Suele incluir el *sticky [[Bit]]* para que solo el propietario de un [[Archivo]] pueda borrarlo.
*   **/lost+found:** Directorio utilizado por la utilidad `[[FSCK]]` para recuperar fragmentos de archivos tras un fallo en el Sistema de Archivos.