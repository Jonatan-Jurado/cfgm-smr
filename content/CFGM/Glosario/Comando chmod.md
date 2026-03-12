---
title: "Comando chmod"
aliases: ["Comandos chmod", "chmod"]
---
# Comando chmod
Se utiliza para cambiar los permisos de los archivos y directorios.

*   _Sintaxis general_: `chmod` seguido de los permisos para los diferentes tipos de usuarios y, después, el nombre del archivo o directorio.
*   _Formas de uso_:
    *   _Modo octal_: Los grupos de tres elementos (rwx) se convierten en una cifra octal, asignando valores: r=4, w=2, x=1. Un "1" se usa si la letra aparece y un "0" si no aparece.
    *   _Modo carácter_: Se indican los permisos para cada grupo de usuarios mediante letras.
        *   _Sintaxis_: `chmod grupo operación permisos`.
        *   _Tipo de grupo_:
            *   _u_: Usuario propietario.
            *   _g_: Grupo del usuario propietario.
            *   _o_: Resto de usuarios.
        *   _Operaciones_:
            *   _`+`_: Añadir.
            *   _`-`_: Eliminar.
            *   _`=`_: Sobreescribir al modo anterior.