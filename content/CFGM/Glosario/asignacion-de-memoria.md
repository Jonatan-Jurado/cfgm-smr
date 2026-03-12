---
title: "Asignación de memoria"
aliases: ["Asignaciones de memoria"]
---
# Asignación de memoria
Diferentes maneras en que la memoria puede ser asignada a los procesos.
-   _Asignar el primer proceso de la cola a un espacio según quede libre_: Si el proceso es mayor que el hueco disponible, no se ejecuta.
-   _Asignar el primer proceso de la cola que quepa en el espacio que ha quedado libre_: (No se proporciona explicación adicional en el texto).
-   _Asignar el proceso más grande de la cola que quepa en el espacio que ha quedado libre_: En este algoritmo, se excluye a los procesos más cortos, ya que se priorizan los largos.