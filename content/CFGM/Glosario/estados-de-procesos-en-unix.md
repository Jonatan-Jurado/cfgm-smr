---
title: "Estados de Procesos en Unix"
---
# Estados de Procesos en Unix
Además de los estados básicos, los sistemas tipo Unix gestionan estados adicionales:
- **Nuevo:** [[Proceso]] recién creado que aún no ha sido admitido para su procesamiento.
- **Terminado:** Proceso que ha finalizado su ejecución satisfactoriamente.
- **Zombie:** Proceso que ha terminado su ejecución pero cuya entrada permanece en la tabla de procesos porque no ha liberado totalmente sus recursos o su estado no ha sido leído por el Proceso padre.