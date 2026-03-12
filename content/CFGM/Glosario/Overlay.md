---
title: "Overlay"
aliases: ["Solapamiento", "Overlays", "Solapamientos"]
---
# Overlay
Es un mecanismo diseñado para solucionar el problema de cuando la cantidad de memoria requerida para ejecutar un programa es mayor que la disponible. Permite dividir el programa virtualmente en procesos para que se ejecuten en diferentes partes de la memoria RAM, residiendo una parte del programa en el disco duro y otra en ejecución en memoria.

A pesar de solucionar el problema de memoria, esta técnica presentaba dificultades de programación, ya que el programador debía realizar las llamadas al sistema para las divisiones, lo cual era inviable debido a las diferentes características de cada sistema y la necesidad de una programación específica para cada aplicación. También resultó inútil para sistemas multiusuario, llevando a la necesidad de una gestión de memoria dinámica.