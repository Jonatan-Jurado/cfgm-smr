---
title: "Modo Carácter de chmod"
---
# Modo Carácter de chmod
Este modo utiliza letras y operadores para definir o alterar los [[Permisos]] de forma simbólica. La sintaxis sigue la estructura: `chmod [grupo][operación][permiso]`.

*   **Grupos:** `u` (propietario), `g` ([[Grupo]]), `o` (otros) y `a` (todos).
*   **[[Operaciones]]:** `+` (añadir), `-` (eliminar) e `=` (asignar de forma exacta sustituyendo lo anterior).
*   **Permisos:** `r` (lectura), `w` (escritura) y `x` (ejecución).

Ejemplo: `chmod g+w [[Archivo]]` añade el permiso de escritura al grupo del Archivo.