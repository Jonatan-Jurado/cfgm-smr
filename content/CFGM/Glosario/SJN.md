---
title: "SJN (Shortest Job Next)"
aliases: ["SJN", "Shortest Job Next", "Trabajo más corto siguiente", "Método SJN"]
---
# SJN (Shortest Job Next)
Es un método de planificación no apropiativo que, para su ejecución, selecciona el trabajo que necesita menos tiempo de entre todos los que estén listos para ejecutarse.
- _Ventajas_:
    - _Mejora considerablemente el valor medio del tiempo de terminación_ al adelantar los procesos cortos.
    - _Reduce los valores medios_ de diversos parámetros de rendimiento.
- _Inconvenientes_:
    - _Necesita conocer con antelación el tiempo de ejecución de cada proceso_, lo que no es posible en muchas ocasiones.
    - _Perjuicio para los trabajos largos_, ya que su ejecución se retrasa en favor de los procesos más cortos.
- _Soluciones a las desventajas_:
    - _Estimación del usuario_: el usuario debe incluir una estimación del tiempo de ejecución. Sin embargo, puede generar el problema de que los usuarios intenten poner el menor valor permitido para favorecer sus trabajos.
    - _Estimaciones del sistema operativo_: el sistema calcula las estimaciones mediante aproximaciones sucesivas en las diversas ejecuciones. Se empieza con una estimación inicial del tiempo y se ejecuta el trabajo, lo que permite obtener una evaluación certera del tiempo.