---
title: "Algoritmo SRT"
aliases: ["SRT", "Shortest Remaining Time", "Tiempo restante más corto"]
---
# Algoritmo SRT

Es un método de planificación apropiativo que combina las ventajas del SJN con la capacidad de interrumpir procesos en ejecución. El procesador se asigna al [[Proceso]] que tenga el menor tiempo restante para finalizar; si llega un nuevo Proceso cuya carga de trabajo sea inferior al tiempo que le queda al Proceso actual, se produce una apropiación del procesador. Este método reduce las conmutaciones improductivas y mantiene la cola de procesos preparados lo más corta posible.