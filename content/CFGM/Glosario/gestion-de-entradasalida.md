---
title: "Gestión de Entrada/Salida"
aliases: ["Gestión de Entrada y Salida"]
---
# Gestión de Entrada/Salida
Una de las funciones del sistema operativo para controlar la comunicación y los recursos asociados a los dispositivos de entrada y salida con la memoria principal.

Se puede realizar de tres formas diferentes:
- _Por sondeo_: el gestor del dispositivo de entrada/salida realiza comprobaciones periódicas del estado del dispositivo.
- _Por interrupciones_: una interrupción es una señal que proviene del dispositivo de entrada/salida y que notifica al procesador que requiere atención.
- _Híbrida_: es una combinación de las anteriores. En general, se trata la gestión de entrada/salida mediante interrupciones, pero, en momentos de carga alta, se atienden en bloques cada cierto tiempo para evitar que un dispositivo sature al procesador. Se utiliza en los sistemas modernos.