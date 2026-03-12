---
title: "Estrategia de ajuste"
aliases: ["Algoritmos de ajuste", "Primer ajuste", "Mejor ajuste", "Peor ajuste", "Siguiente ajuste"]
---
# Estrategia de ajuste

Conjunto de algoritmos utilizados por el gestor de [[Memoria]] para asignar procesos a los huecos disponibles. Las principales estrategias son:
* **Primer ajuste:** Asigna el primer hueco que sea lo suficientemente grande.
* **Siguiente ajuste:** Asigna los procesos siguiendo el orden de la cola.
* **Mejor ajuste:** Busca el hueco más pequeño que pueda albergar al [[Proceso]] para minimizar el desperdicio.
* **Peor ajuste:** Asigna el hueco más grande disponible, priorizando los procesos largos.