---
title: "Visualización de Permisos con ls -l"
---
# Visualización de Permisos con ls -l
Al ejecutar el comando `ls -l`, el primer bloque de información representa el tipo de [[Archivo]] y sus [[Permisos]]. Consta de diez caracteres:
*   El primer carácter indica el tipo de Archivo (por ejemplo, `d` para [[Directorios]] o `-` para archivos regulares).
*   Los nueve caracteres restantes se dividen en tres grupos de tres:
    1.  **Primer grupo:** Permisos del propietario (rwx).
    2.  **Segundo grupo:** Permisos del grupo al que pertenece el Archivo (rwx).
    3.  **Tercer grupo:** Permisos para el resto de usuarios del sistema (rwx).

Un guion (`-`) en cualquier posición indica la ausencia del [[Permiso]] correspondiente.