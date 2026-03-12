title: "[[Proceso]] init"
aliases: ["init", "PID 1", "Sistema de inicio"]
---
# Proceso init

Primer proceso que se ejecuta en el espacio de usuario tras el arranque del kernel en sistemas operativos tipo Unix/Linux. Su función principal es leer el fichero `/etc/inittab` (o su equivalente en sistemas modernos) para determinar el nivel de ejecución por defecto (generalmente el nivel 5). Actúa como el padre de todos los demás procesos del sistema y es responsable de orquestar la carga de servicios según el estado solicitado.