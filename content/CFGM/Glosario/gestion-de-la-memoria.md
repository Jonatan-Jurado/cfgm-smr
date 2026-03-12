---
title: "Gestión de la Memoria"
aliases: ["Gestiones de la Memoria", "Gestión de Memoria", "Gestiones de Memoria"]
---
# Gestión de la Memoria
En los sistemas operativos multiproceso, es el proceso mediante el cual el sistema operativo distribuye la memoria RAM entre los diversos procesos en ejecución, dado que la capacidad de RAM no suele ser suficiente para todos ellos.

Esta gestión implica asegurar que un proceso se ejecute en una parte libre de la memoria principal, controlar el acceso a los recursos compartidos para evitar conflictos de lectura/escritura, y resolver las colas de ejecución para que ningún proceso espere innecesariamente por una posición en memoria. Ante problemas de memoria insuficiente, surgió el mecanismo de `overlay`, pero resultó inviable, concluyendo en la necesidad de gestionar la memoria dinámicamente. En la multiprogramación, se puede realizar a través de técnicas como particiones fijas, variables y memoria virtual.