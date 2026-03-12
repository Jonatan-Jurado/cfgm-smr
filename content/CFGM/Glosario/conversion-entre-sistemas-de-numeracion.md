---
title: "Conversión entre Sistemas de Numeración"
aliases: ["Conversiones entre Sistemas de Numeración", "Paso de Decimal a Binario", "Paso de Decimal a Octal", "Paso de Decimal a Hexadecimal"]
---
# Conversión entre Sistemas de Numeración
La conversión entre sistemas de numeración es el proceso de transformar la representación de un número de un sistema a otro. Para realizar este tipo de conversiones, es necesario separar la parte decimal de la parte entera del número, pues la operación se lleva a cabo de distinta forma.

- _Paso de decimal a cualquier otra base_:
    - _Parte entera_: Se divide el número original (en decimal) entre la base del sistema de numeración de destino, hasta obtener un resto menor que el divisor (es decir, sin decimales). Después, se forma el número en la base de destino con el último cociente y los restos obtenidos, leídos en orden inverso.
        - _Ejemplo (23 a Binario)_: 23 ÷ 2 = 11 (resto 1), 11 ÷ 2 = 5 (resto 1), 5 ÷ 2 = 2 (resto 1), 2 ÷ 2 = 1 (resto 0), 1 ÷ 2 = 0 (resto 1). Resultado: 10111.
        - _Ejemplo (23 a Octal)_: 23 ÷ 8 = 2 (resto 7). Resultado: 27.
        - _Ejemplo (897 a Hexadecimal)_: 897 ÷ 16 = 56 (resto 1), 56 ÷ 16 = 3 (resto 8). Resultado: 381.
    - _Parte decimal_: Se multiplica la parte decimal por la base a la que se va a transformar el número hasta que no haya parte decimal. Después, se escogen las cifras de la parte entera que resultan de cada operación, leídas en orden directo.
        - _Ejemplo (0,375 a Binario)_: 0,375 × 2 = 0,75; 0,75 × 2 = 1,5; 0,5 × 2 = 1,0. Resultado: 0,011.
        - _Ejemplo (0,625 a Octal)_: 0,625 × 8 = 5,0. Resultado: 0,5.