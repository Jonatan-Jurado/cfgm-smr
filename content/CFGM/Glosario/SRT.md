---
title: "SRT (Shortest Remaining Time)"
aliases: ["SRT", "Shortest Remaining Time", "Tiempo restante más corto", "Método SRT"]
---
# SRT (Shortest Remaining Time)
Es un método de planificación apropiativo que combina las ventajas de los procedimientos apropiativos con las del SJN. El procesador se adjunta al proceso más corto en cada momento, considerando el tiempo restante para terminar.
- _Apropiación_: Solo puede ocurrir una apropiación si llega un proceso nuevo que necesite menos tiempo del que le falta al proceso actualmente activo.
- _Ventajas_:
    - _Reduce las conmutaciones improductivas_ (aquellas que no se deben a operaciones de lectura/escritura).
    - _Mantiene la cola de procesos preparados lo más corta posible_, lo que reduce el valor medio del tiempo de espera.