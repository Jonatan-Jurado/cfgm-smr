---
title: Codificación de la información en los Diferentes Sistemas
tags:
  - Codificacion
  - Binario
  - Almacenamiento
---

| `000`                | **0**     |
| :------------------- | --------- |
| `001`                | **1**     |
| `010`                | **2**     |
| `011`                | **3**     |
| `100`                | **4**     |
| `101`                | **5**     |
| `110`                | **6**     |
| `111`                | **7**     |
#### BINARIO A OCTAL
Agrupar de 3 en 3 el Binario y cambiar por su correspondiente en Octal. 
**(Siempre separar de derecha a Izquierda!!)**
Ejemplo: 011101 -->  011 101 --> 35

#### OCTAL A BINARIO 
AL revés!
Ejemplo: 234 --> 010  011  100 -->>010011100

### BINARIO A HEXADECIMAL Y VICEVERSA

|**Binario (4 [[bit|bits]])**|**Hexadecimal**|**Decimal (Equivalencia)**|
|---|---|---|
|`0000`|**0**|0|
|`0001`|**1**|1|
|`0010`|**2**|2|
|`0011`|**3**|3|
|`0100`|**4**|4|
|`0101`|**5**|5|
|`0110`|**6**|6|
|`0111`|**7**|7|
|`1000`|**8**|8|
|`1001`|**9**|9|
|`1010`|**A**|10|
|`1011`|**B**|11|
|`1100`|**C**|12|
|`1101`|**D**|13|
|`1110`|**E**|14|
|`1111`|**F**|15|

#### BINARIO A HEXADECIMAL
Agrupar de 4 en 4 el Binario y reemplazar por su correspondiente en Hexadecimal.
**(Siempre separar de derecha a Izquierda!!)**
Ejemplo: 1110110001010 -->>  0001  1101  1000  1010 --> 1D8A

#### HEXADECIMAL A BINARIO
Al revés!!
Ejemplo:  ABD30 -->> 1010  1011  1101  0011  0000 -->> 10101011110100110000

### OCTAL A HEXADECIMAL Y VICEBERSA
#### OCTAL A HEXADECIMAL
- Pasar primero a Binario
- Agrupar de 4 en 4
Ejemplo 1706 -->> 001 111 000 110 -->>0011 1100 0110  (Ahora convertir a Hexadecimal con la tabla)

0011 1100 0110 --> 3 C 6 --> 3C6 

#### HEXADECIMAL A OCTAL
- Primero a Binario 
- Después a Octal
Ejemplo: 3C6 -->> 0011 1100 0110 (Ahora agrupamos de 3 en 3) -->> 001 111 000 110 (Pasamos a Octal) -->> 1 7 0 6  -->> 1706

## ARITMÉTICA BINARIA

### ADICIÓN (+)
| **Operación** | **Resultado** | **Acarreo (Llevada)** | **Nota**                                          |
| ------------- | ------------- | --------------------- | ------------------------------------------------- |
| $0 + 0$       | **0**         | 0                     |                                                   |
| $0 + 1$       | **1**         | 0                     |                                                   |
| $1 + 0$       | **1**         | 0                     |                                                   |
| 1 + 1         | **0**         | **1**                 | Se pone 0 y "te llevas 1" a la siguiente columna. |
1 1 1      <-- (Acarreos/Lo que me llevo)
      1 1 0 1    (13)
    + 0 1 1 1    (7)
    ----------
    1 0 1 0 0    (20)
#### **Explicación paso a paso (de derecha a izquierda):**

1. **Columna 1:** $1 + 1 = 0$. Pongo **0** y me llevo **1**.
    
2. **Columna 2:** $0 + 1 + 1$ (que me llevaba) $= 0$. Pongo **0** y me llevo **1**.
    
3. **Columna 3:** $1 + 1 + 1$ (que me llevaba) $= 1$. Pongo **1** y me llevo **1**.
    
4. **Columna 4:** $1 + 0 + 1$ (que me llevaba) $= 0$. Pongo **0** y me llevo **1**.
    
5. **Columna 5:** El **1** que me llevaba baja solo.
    

**Resultado: `10100`**

### SUSTRACCIÓN (-)
| **Operación** | **Resultado** | **Prestado (Borrow)** | **Nota**                                                 |
| ------------- | ------------- | --------------------- | -------------------------------------------------------- |
| $0 - 0$       | **0**         | 0                     |                                                          |
| $1 - 1$       | **0**         | 0                     |                                                          |
| $1 - 0$       | **1**         | 0                     |                                                          |
| **$0 - 1$**   | **1**         | **1**                 | El resultado es 1 y **pides prestado 1** a la izquierda. |
1 1 1      <-- (Prestados/Lo que pido a la izquierda)
       1 1 0 1    (13)
     - 0 1 1 1    (7)
     ----------
       0 1 1 0    (6)

#### **Explicación detallada (de derecha a izquierda):**

1. **Columna 1**: $1 - 1 = 0$. (Fácil, no pido nada).
2. **Columna 2**: $0 - 1$. No puedo, así que pido prestado al de la izquierda. El $0$ se vuelve $10$ ($2$ decimal). $10 - 1 = \mathbf{1}$. (Anoto que **debo 1** a la izquierda).
3. **Columna 3**: Aquí arriba tengo un $1$, pero como presté uno antes, ahora es un $0$. Me queda $0 - 1$. Pido prestado a la izquierda. El $0$ se vuelve $10$. $10 - 1 = \mathbf{1}$. (Anoto que **debo 1** a la izquierda).
4. **Columna 4**: Aquí arriba tenía un $1$, pero como presté uno, ahora es un $0$. $0 - 0 = \mathbf{0}$.


**Resultado final: `0110` (que es el 6 en decimal).**

### MULTIPLICACIÓN ( * )
| **Operación** | **Resultado** | **Nota**                   |
| ------------- | ------------- | -------------------------- |
| $0 \times 0$  | **0**         |                            |
| $0 \times 1$  | **0**         | Cualquier cosa por 0 es 0. |
| $1 \times 0$  | **0**         |                            |
| $1 \times 1$  | **1**         | Solo da 1 si ambos son 1.  |
` `             1 0 1 1   (11)
        x   1 0 1   (5)
        ---------
          1 0 1 1   
        0 0 0 0     
    + 1 0 1 1       
    -------------
      1 1 0 1 1 1   (55)`

### DIVISIÓN (/)

| **Operación** | **Resultado** | **Nota**                                             |
| ------------- | ------------- | ---------------------------------------------------- |
| $0 \div 1$    | **0**         |                                                      |
| $1 \div 1$    | **1**         |                                                      |
| $1 \div 0$    | **Error**     | No se puede dividir por cero (igual que en decimal). |
| $0 \div 0$    | **Error**     | Indeterminado.                                       |


![[division.png]]


## REPRESENTACIÓN DE NÚMEROS ENTEROS (Positivos y Negativos)

En binario, no existe el símbolo "$-$". Por eso, los ordenadores usan el Bit más a la izquierda (el **MSB** o Bit Más Significativo) para saber el signo.

### 1. Signo y Magnitud (El más simple)

- **Regla**: El primer bit es el signo (**0 = +**, **1 = -**). El resto es el número normal.
    
- **Problema**: El cero tiene dos nombres ($+0$ y $-0$), lo cual confunde a la [[unidad-central-de-procesamiento|CPU]].
    
- **Ejemplo (8 bits)**:
    
    - $+12 \rightarrow$ `0 0001100`
        
    - $-12 \rightarrow$ `1 0001100`
        

### 2. Complemento a 1 (C1)

- **Regla**: Si es negativo, **invierte** todos los bits (los 0 pasan a 1 y los 1 a 0).
    
- **Problema**: Sigue teniendo el problema del "doble cero".
    
- **Ejemplo**:
    
    - $+12 \rightarrow$ `00001100`
        
    - $-12 \rightarrow$ `11110011` (Invertido)
        

### 3. Complemento a 2 (C2)  EL QUE SE USA HOY

Es el estándar actual porque elimina el doble cero y facilita las restas a la CPU.

- **Cómo se hace (Pasos para el negativo)**:
    
    1. Escribe el número en positivo.
        
    2. Pásalo a [[complemento-a-1|Complemento a 1]] (invierte los bits).
        
    3. **Súmale 1** al resultado.
        
- **Ejemplo de $-12$**:
    
    1. $+12$: `00001100`
        
    2. Invierte: `11110011`
        
    3. Suma 1: `11110100` $\rightarrow$ **Este es el -12 oficial.**
        


### 4. Exceso a $2^{n-1}$ (Exceso a 128 en 8 bits)

Aquí no hay bit de signo. Se elige un "punto medio" (el 128) para que sea el cero.

- Si el número es mayor de 128, es positivo.
    
- Si es menor de 128, es negativo.
    
- **Cálculo**: Número $+ 128 = Resultado$ en binario.
    
    - **12** $\rightarrow 12 + 128 = 140 \rightarrow$ `10001100`
        
    - **-12** $\rightarrow -12 + 128 = 116 \rightarrow$ `01110100`