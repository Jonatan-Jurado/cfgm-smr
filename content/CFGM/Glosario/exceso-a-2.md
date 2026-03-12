---
title: "Exceso a 2^(n-1)"
aliases: ["Exceso a 2n-1", "Representación de exceso a 2^(n-1)", "Método de exceso a 2^(n-1)"]
---
# Exceso a 2^(n-1)
Método de representación numérica donde no hay ningún bit específico para el signo, sino que todos los bits que componen el número tienen peso en el valor total. Consiste en representar el cero como un valor intermedio, que para n bits está representado por 2^(n-1), y colocar los números negativos antes de ese valor y los positivos después de él.

Para representar los números pedidos, se les suma la cantidad de exceso (2^(n-1)).

El mayor inconveniente de esta técnica es su _complejidad_ respecto a las otras, puesto que requiere operaciones intermedias.

_Ejemplo (para una palabra de 8 bits)_:
- El exceso es 2^(8-1) = 2^7 = 128.
- 12 se representa como 12 + 128 = 140 → 10001100
- -12 se representa como -12 + 128 = 116 → 01110100