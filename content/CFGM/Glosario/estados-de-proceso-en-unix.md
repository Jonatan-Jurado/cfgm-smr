---
title: "Estados de Proceso en Unix"
---
# Estados de Proceso en Unix
Sistemas como Unix añaden estados específicos al ciclo de vida del [[Proceso]]:
- **Nuevo:** Proceso recién creado que aún no ha sido admitido para su procesamiento.
- **Terminado:** Proceso que ha finalizado su ejecución satisfactoriamente.
- **Zombie:** Proceso que ha terminado su ejecución pero todavía figura en la tabla de procesos porque no ha liberado totalmente sus recursos o su estado no ha sido leído por el Proceso padre.