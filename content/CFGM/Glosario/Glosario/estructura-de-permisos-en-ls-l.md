---
title: "Estructura de permisos en ls -l"
aliases: ["Bloque de permisos", "Visualización de permisos", "Permisos con ls -l"]
---
# Estructura de permisos en ls -l
Cuando se utiliza el comando `ls -l`, el primer bloque de la información mostrada corresponde a los permisos del archivo o directorio.

*   _Formato_: Consta de diez dígitos.
    *   _Primer dígito_: Puede ser `d` (indica que es un directorio) o `—` (indica que es un archivo).
    *   _Nueve dígitos siguientes_: Se dividen en tres bloques de tres elementos.
        *   _Primer grupo_: Muestra los permisos para el usuario propietario del archivo.
        *   _Segundo grupo_: Muestra los permisos para el grupo al que pertenece el propietario.
        *   _Tercer grupo_: Muestra los permisos del resto de usuarios.
    *   _Valores_: Pueden ser `r`, `w`, `x` (indicando el tipo de permiso) o `—` (si ese grupo de usuarios no tiene permisos sobre el fichero).