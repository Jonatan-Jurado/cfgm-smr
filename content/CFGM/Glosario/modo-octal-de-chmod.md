---
title: "Modo Octal de chmod"
---
# Modo Octal de chmod
Este método utiliza una representación numérica basada en el [[Sistema Octal]] para asignar [[Permisos]]. Cada tipo de permiso tiene un valor asociado:
*   **Lectura (r):** 4
*   **Escritura (w):** 2
*   **Ejecución (x):** 1

Al sumar estos valores, se obtiene una cifra para cada [[Grupo de Usuarios]]. Por ejemplo, una combinación de lectura y escritura sumaría 6 (4+2), mientras que el acceso total sumaría 7 (4+2+1). El comando se ejecuta con tres dígitos (ejemplo: `chmod 755 [[Archivo]]`), que corresponden secuencialmente al propietario, al grupo y a otros usuarios.