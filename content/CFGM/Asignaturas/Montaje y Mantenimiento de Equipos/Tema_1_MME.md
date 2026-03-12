---
title: Medición de Parámetros Eléctricos
tags:
  - Electricidad
  - FuenteAlimentacion
  - SAI
  - Hardware
---

## ELECTRICIDAD

*[[Electricidad]]* = Flujo constante de [[Carga Eléctrica|Cargas Eléctricas]]
### **Tipos**
1. **Eléctricos**
2. **Electromagnéticos**
3. **Analógicos:** Varían / Discreta  
   ![[content/media/Pasted-image-20260304115653.png]]
4. **Digitales:** Constantes[[Directorio raíz|/]]Determinada 
   ![[content/media/Pasted-image-20260304115814.png]]

### **Análisis**
1. **Dominio del Tiempo:** Variables Temporales / [[Amplitud]], [[Frecuencia]] y Fase
2. **[[Dominio de Frecuencia]]:** Sinuidales (Fourer) / Frecuencia y Amplitud

### **Tipos de Corriente**

#### CONTINUA (C.C) o (D.C)
Flujo de Electrones siempre en la misma dirección por un canal.
![[content/media/Pasted-image-20260305102832.png]]

#### **ALTERNA (A.C)**
Va cambiando la Polaridad en los extremos del canal.
**Periodo:** Onda Cíclica que se repite
- **Frecuencia:** Intervalo hasta que pasa de nuevo por [[Economía Lineal|el]] primer punto
- **Amplitud:** Distancia entre el punto medio de la onda y el punto más alejado.
![[content/media/Pasted-image-20260305102858.png]]



## MAGNITUDES Y MEDICIÓN

*Carga eléctrica:*  exceso/falta de electrones en un objeto a causa del flujo de átomos

- **Ion Negativo:** Electrones > Protones.
- **Ion Positivo:** Protones> Electrones.Ç


### VOLTAJE

**[[Voltaje]]:** Diferencia de potencial eléctrica / La [[Intensidad|Corriente eléctrica]] es el paso de electrones de un cuerpo a otro.  
*[[Unidad de Medida]]*: V (Voltio)
*Medición:* [[Voltímetro]]

### INTENSIDAD

**Intensidad:** Cantidad de corriente que pasa por un conductor en un momento determinado
*Unidad de Medida:* A (Amperio)
*Fórmula:*     **I=V/[[Índice de respuesta|R]]** 
*Medición:* [[Amperímetro]]

### RESISTENCIA

*Unidad de Medida:* Ω (Ohmio)
*Medición:* [[Polímetro|Multímetro]]


### POTENCIA

**[[Potencia]]:**  [[Trabajo]] realizado durante el tiempo que se Necesita
*Unidad de Medida:* W (Wattios)
*Fórmula:*  **[[Índice de penalización|P]]=V * I**

## FUENTE DE ALIMENTACIÓN

*[[Fuente de Alimentación]]:* Dispositivo a través del cual nos conectamos a la red eléctrica y a la placa del PC.


**Corriente** --> **[[Transformador]]** --> **[[Rectificador]]** --> **[[Filtro]]** --> **[[Regulador]]** 

 - **Transformador:** Modifica la Tensión
	 - *Bobina Primaria:* Recibe [[Señal]].
	 - *Bobina Secundaria:* Entrega Señal Transformada.
- **Rectificador:** Convierte Señal Alterna (Positiva y Negativa) a *Solo Positiva* 
	- *Media Onda:* *1 Diodo* Transforma Ciclo Negativo en Nulo.
	- *Onda Completa:* *2 Diodos* Transforma Ciclos Negativos en Positivos.
- **Filtro:** Proporciona A.C. 1 o Varios Condensadores  Retienen Corriente y dejan pasar muy lenta. casi D.C
- **Regulador:** Estabiliza Señal y Mantiene Voltaje de Salida Constante.

## SAI: SISTEMA DE ALIMENTACIÓN ININTERRUMPIDO

Proporciona Electricidad a los que estén conectados si hay [[Apagón]] y filtra señal para que no haya fallos en los equipos.
Tiene dos Salidas: *[[Controlador]] y Bateria Baja*

 **Previene:**
 - *Apagones*
 - *Sobre/[[Bajo Voltaje]]
 - *Caidas/[[Pico de Tensión|Picos de Tensión]]*
 - *[[Ruido Eléctrico]]*

**Partes:**
- *Bateria y Cargador:* Normalmente 12V
- *Filtro:* Limpia Señal
- *[[Conversor]]:* de 12V --> D.C
- *[[Inversor]]:* de D.C --> A.C
- *[[Conmutador]]:* Circuito que Camia de Red Eléctrica a [[Sistema de Alimentación Ininterrumpida|SAI]]

### **Tipos:**
#### **SAI Standby u Offline Pasivo:** 
En Paralelo, solo se activa cuando hay Apagón o Caida de Tensión.
![[content/media/Pasted-image-20260305105250.png]]


#### **SAI Offline Interactivo:**
En Serie y Siempre Activo.
![[content/media/Pasted-image-20260305105343.png]]


#### **SAI Online de Doble Conversión**
La conversión no depende de la entrada sinó de otro inversor.
![[content/media/Pasted-image-20260305105453.png]]


### Características
- *Tiempo de autonomía*
- *Potencia*
	- Vatios (V)
	- Voltamperios(VA)
	  *[[Factor de potencia]]:* La Relación entre V y VA debe estar entre 0 y 1
- *Precio*

## CIRCUITOS
### EN SERIE
- Un único Camino
- La *intensidad total* de los elementos conectados en serie es la misma en cada una de las tensiones en cada elemento
	- **[[Prestación por Incapacidad Temporal|It]] = I1 = I2 = I3 = ...**
- La *tensión* total de los elementos conectados en serie es la suma de cada una de las tensiones en cada elemento.
	- **Vt = V1 + V2 + V3 + ...**
- La *[[Resistencia]] total* de todos los receptores conectados en serie es la suma de la resistencia de cada receptor.
	- **Rt = R1 + R2 + R3 + ...**

![[content/media/Pasted-image-20260305110642.png]]


### EN PARALELO
- Todos Conectados entre si.
- Todos los elementos o receptores conectados en paralelo están a la *misma tensión.*
	- **Vt = V1 = V2 = V3 = ...**
- La suma de la intensidad que pasa por cada uno de los receptores es la *intensidad total.*
	- **It = I1 + I2 + I3 + ...**
- La *resistencia total* o equivalente de los receptores conectados en paralelo se calcula con la siguiente fórmula:
	- **1/Rt = 1/R1 + 1/R2 + 1/R3 + ...**
![[content/media/Pasted-image-20260305111207.png]]




