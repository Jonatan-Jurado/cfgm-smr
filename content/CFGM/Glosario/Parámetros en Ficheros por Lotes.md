---
title: "Parámetros en Ficheros por Lotes"
---
# Parámetros en Ficheros por Lotes
Son variables que permiten a un fichero *batch* recibir información desde el exterior en el momento de su ejecución. Para capturar estos valores dentro del código del fichero, se utiliza el símbolo **%** seguido de la posición numérica que ocupa el parámetro (por ejemplo, `%1` para el primero, `%2` para el segundo). Estos valores se indican después del nombre del fichero al lanzarlo desde la línea de comandos.