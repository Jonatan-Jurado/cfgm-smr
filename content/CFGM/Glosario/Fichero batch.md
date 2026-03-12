---
title: "Fichero batch"
aliases: ["Ficheros batch", "fichero .bat", "ficheros .bat", "fichero ejecutable", "ficheros ejecutables", "batch file", "batch files"]
---
# Fichero batch
Un fichero ejecutable en Windows con extensión .bat, creado para facilitar la tarea del administrador y automatizar procesos.

*   _Creación_:
    -   _Crear un fichero con extensión .bat._
    -   _Abrirlo con un editor de texto plano (puede ser el Bloc de notas)._
    -   _Comenzar escribiendo echo off._
    -   _Escribir el resto de las órdenes._
    -   _Normalmente, se efectúa una pausa como último comando y se muestra un mensaje para ver la ejecución (ejemplo: `@pause Presione una tecla para continuar`)._
*   _Ejecución_: Es posible ejecutarlo con el entorno gráfico (como cualquier otra aplicación) o mediante comandos. Para ello, se introduce en el Símbolo del sistema el nombre del fichero batch.
*   _Variables por parámetro_: Permiten la ejecución con variables recibidas por parámetro. Los parámetros se indican después del nombre del fichero a la hora de la ejecución. Dentro del fichero, para recoger estos parámetros, se utiliza el símbolo `%` seguido de la posición del parámetro (por ejemplo, `%3`, para hacer referencia al tercer parámetro).