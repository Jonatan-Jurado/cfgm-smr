---
title: Tema 3
tags:
  - Cloud
  - Virtualizacion
  - Tendencias
---
# Tema 3: Cloud. Sistemas Conectados

## Cloud
**[[la-nube|Cloud]]**: 
- [[proceso-del-sistema|Servicio]] que nos permite almacenar y gestionar datos a través de Internet.
- Es un entramado de Servidores remoto ubicado en cualquier parte del mundo
- El [[cuenta-de-usuario|usuario]] se conecta a Internet y accede a gran variedad de recursos.
- Normalmente los servidores son virtuales y gestionados por los proveedores de servicios.
### Diferentes Usos del Cloud Computing
- Almacenamiento de Datos
- Base de Datos
- Apps
- Software
- [[streaming-de-video-y-audio|Streaming]]
- Redes Sociales

<iframe width="560" height="315" src="https://www.youtube.com/embed/VR8aXePkQ5M?si=qndgbc4E9ZmZNf1Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Tipos

Por uso:
- *IaaS - [[infraestructura-como-servicio|Infraestructura como Servicio]]*
	- Nivel 1
	- Servidores
	- Redes
	- Almacenamiento
		- Ejemplos:
			- *AWS*
			- *Google [[recursos-en-la-nube|Cloud]] Platform*
			- *Microsoft Azure*
- *PaaS - [[plataforma-como-servicio|Plataforma como Servicio]]*
	- Nivel 2
	- Crear, probar desplegar
		- Ejemplos:
			- *Heroku*
			- *Google App Enginer*
			- *Microsot Azure*
- *SaaS - [[software-como-servicio|Software como Servicio]]*
	- Nivel 3
	- Se ofrece listo para usar por una subscripción al user final
		- *Google Workspace*
		- *Microsoft  Office 365*
		- *Salesfgorce*

Por Privacidad:
- *[[nube-publica|Nube Pública]]*: comparte recursos a través de internet
- *[[nube-privada|Nube Privada]]*: no se comparte recursos por internet, es red privada
- *[[nube-hibrida|Nube Híbrida]]*: Es una Mezcla

## Posibilidades de Trabajo en la Cloud

### Almacenamiento y Gestión de Datos
- Almacenamiento de archivos:
	- *Amazon S3*
	- *Google [[almacenamiento-en-la-nube|Cloud Storage]]*
	- *Microsoft Azure Blob Storage*
- Base de Datos:
	- *Amazon RDS*
	- *Google Cloud SQL*
	- *Azure SQL DataBase*
### Desarrollo y Pruebas de Software
- Desarrollo:
	- *AWS Lambda*
	- *Google Cloud Functions*
	- *Azure Functions*
- CI/[[comando-de-directorio|CD]]: automatiza el flujo de trabajo
	- *Jenkins*
	- *Github Actions*
	- *GitLab CI*

### IA y ML (Machine Learning)
- Modelado y Entrenamiento:
	- *Google [[inteligencia-artificial|AI]] Platform*
	- *AWS SageMaker*
	- *Azure [[aprendizaje-automatico|Machine Learning]]*
- [[api-de-ia|APIs de IA]]:
	- *Google Cloud*
	- *IBM Watson*
	- *Azure Cognitive Services*

### Aplicaciones Web y Móviles
- [[aplicacion|Aplicaciones]] Web:
	- *AWS Elastic Beanstalk*
	- *Google App Engine*
	- *Azure App Service*
- Backend para apps móviles:
	- *Firebase de Google*


### Infraestructura
- [[maquina-virtual|Máquinas Virtuales]]
	- *Amazon EC2*
	- *Google Compute Engine*
	- *Azure Virtual Machine*

### Plataforma
- Desarrollo de [[software-y-algoritmo|aplicaciones]]:
	- *Heroku*
	- *AWS*
	- *Elastic Beanstalk*
	- *Google App Engine*

### Herramientas para Empresas
- Productividad:
	- *Google Suite*
	- *Office 365*
	- *Slack*
- [[gestion-de-relaciones-con-clientes|CRS]] - Gestion de Relaciones con Clientes
	- *Salesforce*
	- *HubSpot*
- Backup y [[recuperacion-en-ciberseguridad|Recuperación]]
	- *AWS Backup*
	- *Google Cloud Storage*
	- *Azure Backup*
- [[seguridad-y-gestion-de-identidad|Seguridad]]: cortafuegos, [[monitorizacion|monitorización]], cifrado.
	- *AWS Shield*
	- *Google Cloud Security*
	- *Azure Security Center*
### Streaming y Multimedia
- Streming de Video y Audio:
	- *AWS Media Services*
	- *Google Cloud Media Solutions*
	- *Azure Media Services*
- Almacenamiento y distribución:
	- *CDN*: [[red-de-distribucion-de-contenido|Redes de Distribución de Contenido]]
### IoT
- Gestión de Dispositivos
	- *AWS [[internet-de-las-cosas|IoT]]*
	- *Google Cloud IoT*
	- *Azure IoT Hub*

## Aplicaciones del Cloud Computing
### Empresas y Negocios
- Almacenamiento de Datos
- Gestión de la cadena de subministro
- Contabilidad y Finanzas
- Comunicaciones
- Recursos Humanos
- [[trabajo-en-equipo|Trabajo en Equipo]]
### Desarrollo de Software y Apps
- Colaboración
- [[herramientas-de-desarrollo-y-scripting|Herramientas de Desarrollo]]
- Despliegue y Escalado de apps de forma sencilla
### Educación
- [[control-remoto|Acceso Remoto]] a recursos
- Crear, compartir contenido
- Gestionar [[sistema-de-gestion-de-aprendizaje|sistemas de gestión de aprendizaje]]
- Fácil comunicación estudiante-profesor
### Salud
- Almacenar y gestionar [[registro-del-procesador|registros]] electrónicos
- Facilitar telemedicina
- Atención Remota
- Mejorar Subministro
- Permite colaborar entre profesionales
### Investigación Científica
- Almacenar y analizar grandes conjuntos de datos
- Ejecutar simulaciones computacionales
- Colaborar en Proyectos Internacionales
### Entretenimiento
- Almacenar y [[almacenamiento-y-distribucion-de-contenido|Distribución de contenido]]
- Mejorar Streaming
- Desarrollar Apps y Juegos
### IoT
- *Domótica*: [[automatizacion-de-procesos-productivos|Automatización]] del hogar.

## Edge Computing
*[[edge-computing|Edge Computing]]:* 
- El procesamiento se lleva a cabo mucho mas cerca
- + Velocidad
- - Latencia
### Relacion entre EC y Cloud
- Edge Computing envia información a centro de datos mas cercanos y disminuye el [[tiempo-de-respuesta|tiempo de respuesta]].
- Complementa al Cloud con capacidades de procesamiento mas cercanas al user final
- Cloud para gran volúmen y largo plazo / Edge corto plazo, al momento (IoT para [[respuesta-en-ciberseguridad|respuesta]] instantánea)
- EC la info es diversificada en múltiples dispositivos , datos repartidos = menos ataques
- EC reduce la cantidad de datos así que mejora el ancho de banda al mandar menos.
## Aplicaciones del Edge Computing
- Iot
- [[smart-cities|Smart Cities]]
- [[fabricas-inteligentes|Fábricas Inteligentes]]
- [[monitoreo-y-optimizacion|Monitoreo]] de la Salud y Seguridad
- Apps de [[realidad-aumentada|Realidad Aumentada]] y [[realidad-virtual|Realidad Virtual]]
- Videojuegos

## Edge - Fog - Mist

<iframe width="560" height="315" src="https://www.youtube.com/embed/nX5DsNn01PA?si=PN3hh6t85W_ywC0X" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


| Aspecto              | **Edge Computing**                                      | **Fog Computing**                                           | **Mist Computing**                                      |
|----------------------|---------------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------|
| **Definición**       | Procesamiento cerca de donde se generan los datos (dispositivos o sensores) | Nivel intermedio entre Edge y Nube (gateways locales)      | Inteligencia artificial directamente en los dispositivos finales |
| **Ubicación**        | En el borde de la red (muy cerca del dispositivo)      | Entre los dispositivos y la nube                            | En el propio dispositivo final                          |
| **Objetivo principal** | Reducir latencia y ancho de banda                       | Procesamiento distribuido con más potencia                  | Ejecutar IA/ML en el extremo                            |
| **Beneficios clave** | - Baja latencia<br>- Mayor seguridad<br>- Velocidad     | - Tiempo real<br>- Combina múltiples fuentes                | - Funciona sin conexión continua<br>- Mínima latencia   |
| **Inconvenientes**   | Algoritmos complejos mejor en la nube                   | Infraestructura compleja y costosa                          | Recursos muy limitados (CPU, memoria)                   |
| **Aplicaciones**     | IoT, vehículos autónomos, RA, monitorización salud     | Industria 4.0, conducción autónoma, salud conectada         | IoT con conectividad intermitente, entornos remotos     |
## Ventajas de los recursos Cloud
- Rápido de implementar
- Fiabilidad
- Seguridad
- Actualización Automática
- Respaldo y Recuperación de datos
- Innovación Tecnológica
- Ahorro de Costos
- Escalabilidad
- Flexibilidad

