---
title: "Estructura del Árbol de Directorios en Linux"
---
# Estructura del Árbol de Directorios en Linux
A diferencia de otros sistemas operativos, Linux utiliza una estructura jerárquica unificada que parte de un único [[Directorio]] raíz representado por una barra inclinada (`/`). A partir de este nodo principal, cuelgan todos los dispositivos, particiones y carpetas del sistema.

Los [[Directorios]] más importantes son:
*   **/bin:** Contiene archivos ejecutables esenciales del sistema (ej. `ls`, `cat`).
*   **/sbin:** Almacena comandos de administración del sistema accesibles principalmente por el [[Superusuario]].
*   **/boot:** Archivos necesarios para el arranque del [[Sistema Operativo]].
*   **/dev:** Archivos de dispositivos ([[Hardware]]).
*   **/etc:** Contiene los ficheros de configuración del sistema y servicios.
*   **/home:** Directorios personales para los usuarios comunes.
*   **/root:** Directorio personal del administrador (superusuario).
*   **/lib:** Librerías esenciales necesarias para los binarios de `/bin` y `/sbin`.
*   **/mnt:** Punto de montaje para [[Sistemas de Archivos]] temporales o dispositivos externos.
*   **/proc:** [[Sistema de Archivos]] virtual que proporciona información sobre el [[Kernel]] y los procesos.
*   **/var:** Archivos de datos variables, como logs de sistema y colas de correo.
*   **/usr:** Programas y aplicaciones de [[Usuario]] que no son esenciales para el sistema base.
*   **/tmp:** Archivos temporales; suele incluir el "sticky [[Bit]]" para que los usuarios solo puedan borrar sus propios archivos.
*   **/lost+found:** Directorio utilizado por la utilidad `[[FSCK]]` para recuperar fragmentos de archivos tras un fallo en el sistema de ficheros.