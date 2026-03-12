---
title: "Complemento a 2"
aliases: ["Complementos a 2", "Representación de complemento a 2", "Método de complemento a 2"]
---
# Complemento a 2
Método de representación numérica utilizado actualmente por los ordenadores para los números enteros. Al igual que en el complemento a 1, se realiza una diferenciación entre los números positivos y los números negativos.

- _Números positivos_: El bit que se encuentra más a la izquierda representa el signo, y el resto de los bits corresponden al módulo del número.
- _Números negativos_: Primero se debe realizar la transformación al complemento a 1 del número positivo y, después, sumar 1 a dicho resultado. Si el último dígito de la suma tiene acarreo, se desprecia.

Con esta técnica, no se puede representar el 0 de formas diferentes; su única representación es 00000000.

_Ejemplo (para -12 en una palabra de 8 bits)_:
- Positivo: 12 → 0 0001100
- Negativo:
    - Primer paso (complemento a 1): 1 1110011
    - Segundo paso (sumar 1): + 1
    - Resultado: -12 → 1 1110100