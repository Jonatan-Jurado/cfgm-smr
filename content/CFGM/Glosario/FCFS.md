---
title: "FCFS (First Come First Served)"
aliases: ["FCFS", "First Come First Served", "Primer llegado, primer servido", "Método FCFS"]
---
# FCFS (First Come First Served)
Es un método de planificación no apropiativo que asigna un recurso al primer proceso que llega. Es el procedimiento más sencillo y se emplea en la planificación de trabajos y de procesos.
- _Usos_:
    - _De trabajos_: los trabajos se ejecutan en el orden de llegada.
    - _De procesos_: un proceso se añade al final de la cola y se ejecuta según el orden de incorporación.
- _Ventajas_:
    - _Fácil de programar_.
    - _Necesita pocos recursos_.
    - _Consume muy poco tiempo de procesador_.
- _Inconvenientes_:
    - _Los índices de funcionamiento no son buenos_.
    - _Índice de penalización elevado para trabajos cortos_: un trabajo corto que llega poco después de uno largo tiene un índice de penalización grande. Este método se utiliza poco, aunque es frecuente encontrarlo combinado con otros.