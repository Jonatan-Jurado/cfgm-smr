---
title: "Optimización de la memoria"
aliases: ["optimización de la memoria"]
---

# Optimización de la memoria

y del funcionamiento de los [[dispositivos de almacenamiento]] Optimizar la memoria es una de las tareas de mejora del rendimiento necesarias durante la ejecución de un sistema operativo. La más im- portante ya ha sido comentada en un apartado anterior, es la que se conoce como SWAP. Linux no tiene un sistema de paginación definido, por lo que, para evitar que [[la memoria RAM]] colapse y se sobrecargue, se emplea este mecanismo. Consiste en la creación de un espacio de intercambio dentro del disco duro, donde se almacenarán todos los datos que no se pueden alojar dentro de la memoria RAM. Esta asignación de espacio en Linux se realiza durante la instalación del sistema operativo. Aunque es algo que para el sistema Linux supone una mejora notable en el rendimiento, hemos de tener en cuenta que este uso de memoria se debe minimizar. El equipo tiene unos recursos hardware limitados porque esto necesita una serie de librerías que intercambien informa- ción con la memoria RAM. Para consultar el espacio asignado en memoria se utiliza el comando free. Este es el espacio de memoria que mantiene los estados de los archivos en ejecución también cuando se pone el equipo en modo de hiberna- ción, por lo que la memoria SWAP se podría definir como una memoria caché.