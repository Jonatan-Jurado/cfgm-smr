---
title: "Salidas de un SAI"
aliases: ["Salida de un SAI"]
---
# Salidas de un SAI
Un Sistema de Alimentación Ininterrumpida (SAI) debe contener dos salidas:
- _Primera salida (señal de fallo)_: Conectada por cable al controlador, que dispone de un mecanismo para identificar que el SAI ha cambiado a la alimentación de batería debido a un fallo con la red eléctrica. Esta señal puede ser utilizada por el controlador (si está configurado) para iniciar automáticamente una secuencia de apagado segura, dirigir los comandos a estados seguros y desactivar la fuente de alimentación.
- _Segunda salida (advertencia de baja batería)_: Advertirá de la baja batería del SAI.