---
title: "Complemento a 1"
aliases: ["Complementos a 1", "Representación de complemento a 1", "Método de complemento a 1"]
---
# Complemento a 1
Método de representación numérica que establece una diferenciación entre los números positivos y los números negativos.

- _Números positivos_: El bit que se encuentra más a la izquierda representa el signo, y el resto de los bits corresponden al módulo del número.
- _Números negativos_: Se parte del número positivo, pero después se debe cambiar cada uno de los dígitos, de tal forma que todos los ceros pasan a ser unos y viceversa.

La desventaja de este método es la _doble representación del 0_ (por ejemplo, +0 como 00000000 y -0 como 11111111).

_Ejemplo (en una palabra de 8 bits)_:
- 12 se representa como 0 0001100
- -12 se representa como 1 1110011