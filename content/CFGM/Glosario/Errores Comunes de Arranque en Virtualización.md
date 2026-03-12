title: "Errores Comunes de Arranque en [[Virtualización]]"
---
# Errores Comunes de Arranque en Virtualización
Durante el proceso de inicio de una máquina virtual, pueden surgir diversos fallos técnicos:
- **Operating System not found:** Indica que la ruta a la imagen ISO o al disco virtual no se ha definido correctamente, impidiendo la carga del sistema.
- **Unable to open kernel device:** Error de configuración que suele requerir la edición del archivo de la máquina virtual para habilitar parámetros de comunicación (como vmci0.present = "TRUE").
- **This kernel requires an x86-64 CPU:** Error de arquitectura que ocurre cuando se intenta ejecutar un sistema de 64 bits en un procesador de 32 bits o cuando las funciones de virtualización del procesador no están habilitadas en la BIOS/UEFI.