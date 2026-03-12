---
title: "Parámetro de ejecución"
aliases: ["Parámetros", "Argumentos de comandos", "simbolo-porcentaje"]
---
# Parámetro de ejecución

Un parámetro de ejecución es una variable de entrada que se transfiere a un programa o [[Script]] en el momento de invocarlo desde la línea de comandos. En los sistemas [[Windows]], estos valores se indican después del nombre del [[Archivo]] ejecutable|Archivo ejecutable]]. Dentro de los scripts (como los ficheros .bat), estos datos son capturados dinámicamente utilizando el carácter especial % seguido de la posición que ocupa el dato en la instrucción de llamada (del %1 al %9), permitiendo que un mismo Script realice acciones diferentes según los datos recibidos.