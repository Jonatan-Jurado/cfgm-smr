---
title: "Transiciones entre Estados"
---
# Transiciones entre Estados
Cambios producidos en el estado de un [[Proceso]] durante su ciclo de vida:
- **Bloqueo:** Paso de ejecución a bloqueado al realizar una llamada al sistema o requerir datos.
- **Apropiación:** Paso de ejecución a preparado cuando el gestor de procesos decide detenerlo para dar paso a otro.
- **Asignación:** Paso de preparado a activo cuando el Proceso entra en la [[CPU]].
- **Fin de bloqueo:** Paso de bloqueado a preparado tras completar la operación que originó la espera.