---
title: "Transiciones de Estado"
---
# Transiciones de Estado
Cambios que experimenta un [[Proceso]] durante su ciclo de vida entre los distintos estados de ejecución:
- **Bloqueo:** Paso de ejecución a bloqueado por una llamada al sistema o espera de datos.
- **Apropiación:** Salida forzosa de la [[CPU]] por indicación del gestor de procesos para permitir la entrada de otro.
- **Asignación:** Paso de estado preparado a activo para iniciar la ejecución en la CPU.
- **Fin de bloqueo:** Paso de bloqueado a preparado tras completarse la operación que causó la espera.