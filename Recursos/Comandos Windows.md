# 📘 Tutorial de CMD: Comandos esenciales

## Tabla de comandos, opciones y ejemplos

| Comando          | Utilidad                                                            | Opciones más importantes                                                                              | Ejemplo                                                                     |
| ---------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `dir`            | Lista archivos y carpetas del directorio actual.                    | `/w` (vista ancha), `/p` (pausa), `/s` (incluye subcarpetas), `/b` (formato simple)                   | `dir /s /p *.txt`                                                           |
| `cd`             | Cambia el directorio actual.                                        | `..` (sube un nivel), `\` (va a la raíz), `d:` (cambia de unidad)                                     | `cd C:\Windows\System32`                                                    |
| `mkdir` / `md`   | Crea un nuevo directorio.                                           | Ninguna relevante. Puedes crear rutas completas.                                                      | `mkdir "C:\Nueva Carpeta\Subcarpeta"`                                       |
| `rmdir` / `rd`   | Elimina un directorio.                                              | `/s` (elimina todo el contenido), `/q` (modo silencioso)                                              | `rd /s /q "C:\Temp\Viejo"`                                                  |
| `del` / `erase`  | Elimina archivos.                                                   | `/s` (busca en subcarpetas), `/q` (sin confirmación), `/f` (fuerza borrado solo lectura)              | `del /s /q *.tmp`                                                           |
| `copy`           | Copia uno o varios archivos.                                        | `/y` (no pregunta al sobrescribir), `/v` (verifica copia)                                             | `copy "C:\origen\*.txt" "D:\destino\"`                                      |
| `xcopy`          | Copia archivos y directorios (avanzado).                            | `/e` (copia vacías), `/h` (ocultos y sistema), `/i` (supone destino es directorio)                    | `xcopy "C:\datos" "E:\backup" /e /h /i`                                     |
| `robocopy`       | Copia robusta (reanuda, multihilo).                                 | `/mir` (refleja origen/destino), `/r:3` (3 reintentos), `/np` (sin progreso visual)                   | `robocopy "C:\origen" "D:\destino" /mir /r:2`                               |
| `move`           | Mueve archivos o directorios.                                       | Ninguna relevante.                                                                                    | `move "C:\temp\*.log" "C:\logs\"`                                           |
| `rename` / `ren` | Cambia el nombre de archivos o carpetas.                            | Ninguna.                                                                                              | `ren "foto antigua.jpg" "nueva_foto.jpg"`                                   |
| `type`           | Muestra el contenido de un archivo de texto.                        | Ninguna. Útil con tuberías.                                                                           | `type readme.txt`                                                           |
| `more`           | Muestra texto paginado (pausa por pantalla).                        | `+n` (empieza en línea n)                                                                             | `type informe.txt                                                           |
| `find`           | Busca cadenas de texto en archivos.                                 | `/i` (ignora mayúsculas), `/n` (muestra nº línea), `/c` (solo cuenta coincidencias)                   | `find /i "error" *.log`                                                     |
| `findstr`        | Versión potente de find (permite regex).                            | `/s` (recursivo), `/m` (solo nombre archivo), `/r` (usa expresiones regulares)                        | `findstr /s /m "ERROR" *.log`                                               |
| `cls`            | Limpia la pantalla (clear screen).                                  | Ninguna.                                                                                              | `cls`                                                                       |
| `echo`           | Muestra mensajes o activa/desactiva eco.                            | `off` (no muestra comandos), `on` (muestra), `>` (redirige)                                           | `echo Hola mundo` ; `echo @echo off > script.bat`                           |
| `set`            | Muestra, crea o elimina variables de entorno.                       | Sin parámetros (muestra todas), `variable=valor` (crea)                                               | `set MI_VAR=contenido` ; `set MI_VAR` ; `set /p nombre=Introduce nombre:`   |
| `path`           | Muestra o modifica la variable PATH (rutas ejecutables).            | `;` (separador), `%PATH%` (incluye la actual)                                                         | `path=%path%;C:\mis_programas`                                              |
| `start`          | Abre una nueva ventana de CMD o un programa/archivo.                | `/min` (minimizado), `/max` (maximizado), `/b` (mismo ventana)                                        | `start notepad.exe` ; `start /min cmd /k "ping 8.8.8.8 -t"`                 |
| `tasklist`       | Lista procesos en ejecución.                                        | `/v` (detallado), `/fi "STATUS eq running"` (filtro), `/fo csv` (formato)                             | `tasklist /fi "IMAGENAME eq chrome.exe"`                                    |
| `taskkill`       | Termina procesos por PID o nombre.                                  | `/f` (forzado), `/pid` (por número), `/im` (por nombre imagen)                                        | `taskkill /im notepad.exe /f`                                               |
| `systeminfo`     | Muestra información detallada del sistema.                          | `/s` (equipo remoto), `/fo csv` (formato)                                                             | `systeminfo                                                                 |
| `sfc`            | Verifica y repara archivos del sistema.                             | `/scannow` (analiza y repara), `/verifyonly` (solo analiza)                                           | `sfc /scannow`                                                              |
| `chkdsk`         | Analiza y repara errores de disco.                                  | `/f` (repara errores), `/r` (recupera sectores dañados), `/x` (desmonta)                              | `chkdsk C: /f /r`                                                           |
| `diskpart`       | Herramienta de particionado (entorno interactivo).                  | Dentro: `list disk`, `select disk`, `clean`, `create partition`, `format`                             | `diskpart` → `list disk` → `select disk 2` → `clean`                        |
| `shutdown`       | Apaga, reinicia o cierra sesión.                                    | `/s` (apaga), `/r` (reinicia), `/t` (segundos), `/a` (aborta)                                         | `shutdown /r /t 60 /c "Reinicio en 1 minuto"`                               |
| `ipconfig`       | Muestra configuración de red.                                       | `/all` (detalle completo), `/release` (libera IP), `/renew` (renueva), `/flushdns` (limpia caché DNS) | `ipconfig /all` ; `ipconfig /flushdns`                                      |
| `ping`           | Prueba conectividad hacia un host.                                  | `-t` (continuo), `-n` (número paquetes), `-l` (tamaño), `-w` (timeout ms)                             | `ping -n 10 -l 1000 8.8.8.8`                                                |
| `tracert`        | Rastrea la ruta hasta un destino.                                   | `-d` (no resuelve nombres), `-h` (máx saltos), `-w` (timeout ms)                                      | `tracert -d -w 1000 google.com`                                             |
| `nslookup`       | Consulta servidores DNS.                                            | `-type=MX` (registro MX), `-timeout=5`, modo interactivo (escribir servidor)                          | `nslookup -type=NS elpais.com`                                              |
| `netstat`        | Muestra conexiones de red, puertos, estadísticas.                   | `-a` (todas conexiones), `-n` (no resuelve nombres), `-b` (ejecutable asociado), `-o` (PID)           | `netstat -anob`                                                             |
| `arp`            | Muestra/modifica tabla ARP (direcciones IP/MAC).                    | `-a` (muestra tabla), `-d` (borra entrada), `-s` (añade estática)                                     | `arp -a ; arp -d 192.168.1.1`                                               |
| `route`          | Muestra/modifica tabla de enrutamiento.                             | `print` (muestra), `add` (añade), `delete`, `change`                                                  | `route print` ; `route add 0.0.0.0 mask 0.0.0.0 192.168.1.1`                |
| `netsh`          | Herramienta avanzada de red (wifi, firewall, interfaz).             | `wlan show profiles`, `wlan show interfaces`, `advfirewall`                                           | `netsh wlan show profiles` (ver redes WiFi guardadas)                       |
| `net user`       | Administra usuarios locales.                                        | Sin parámetros (lista), `nombre /add`, `nombre /delete`, `/active:no`                                 | `net user invitado /active:no` ; `net user usuario1 *` (cambia pass)        |
| `whoami`         | Muestra el usuario y dominio actual.                                | `/user` (solo nombre), `/groups` (grupos del usuario)                                                 | `whoami` ; `whoami /groups`                                                 |
| `icacls`         | Ver o modificar permisos ACL de archivos/carpetas.                  | `/grant` (da permiso), `/remove` (quita), `/reset` (restablece)                                       | `icacls archivo.txt /grant "Usuario:F"` ; `icacls carpeta /remove "Users"`  |
| `schtasks`       | Programa tareas (crear, eliminar, ejecutar).                        | `/create`, `/delete`, `/run`, `/tn` (nombre tarea), `/sc` (frecuencia), `/tr` (acción)                | `schtasks /create /tn "MiTarea" /tr "calc.exe" /sc daily /st 09:00`         |
| `for`            | Bucle para procesar archivos o texto.                               | `/d` (directorios), `/r` (recursivo), `/f` (archivos con tokens)                                      | `for %i in (*.txt) do echo %i` ; `for /L %i in (1,1,10) do mkdir Carpeta%i` |
| `if`             | Condicional en scripts batch.                                       | `exist` (comprueba archivo), `==` (comparar cadenas), `errorlevel`                                    | `if exist archivo.txt (echo Existe) else (echo No existe)`                  |
| `goto`           | Salta a una etiqueta en un script batch.                            | `:etiqueta` (define), `goto :eof` (fin del script)                                                    | `:menu` ; `goto menu`                                                       |
| `call`           | Llama a otro script batch desde dentro.                             | Ninguna.                                                                                              | `call otro_script.bat`                                                      |
| `pause`          | Detiene la ejecución y muestra "Presione una tecla para continuar". | Ninguna.                                                                                              | `echo Fin de proceso` ; `pause`                                             |
| `rem`            | Escribe comentarios en scripts (no se ejecutan).                    | Ninguna.                                                                                              | `rem Esto es un comentario`                                                 |
| `exit`           | Cierra la ventana de CMD o termina el script.                       | `/b` (sale del script pero no cierra CMD), `exit code` (devuelve código error)                        | `exit /b 0`                                                                 |

## 🧪 Ejemplos prácticos integrados

### 1. Crear y organizar archivos
```
mkdir Proyecto
cd Proyecto
echo Contenido > archivo1.txt
copy archivo1.txt archivo2.txt
dir
rename archivo2.txt copia.txt
del archivo1.txt
```

### 2. Buscar texto dentro de archivos recursivamente

```
findstr /s /i /m "contraseña" C:\Users\*.txt
```

### 3. Gestionar procesos

```
tasklist /fi "STATUS eq running" /fo table
taskkill /im notepad.exe /f
```


### 4. Capturar información del sistema

```
systeminfo > info_sistema.txt
ipconfig /all >> info_sistema.txt
```

### 5. Limpiar archivos temporales

```
del /s /q "%TEMP%\*" 2>nul
rd /s /q "%TEMP%" 2>nul
mkdir "%TEMP%" 2>nul
```

### 6. Bucle para crear múltiples carpetas

```
for /L %i in (1,1,10) do mkdir Carpeta_%i
```

### 7. Script simple con menú

```
@echo off
:menu
cls
echo 1. Mostrar fecha
echo 2. Mostrar hora
echo 3. Salir
set /p opcion=Elige:
if %opcion%==1 (date /t & pause & goto menu)
if %opcion%==2 (time /t & pause & goto menu)
if %opcion%==3 (exit)
echo Opción no válida & pause & goto menu
```



## 💡 Consejos finales

- **Ayuda integrada**: cualquier comando seguido de `/?`, p.ej. `xcopy /?`
    
- **Historial**: flecha arriba/abajo para recorrer comandos anteriores (o `doskey /history`)
    
- **Redirección**: `>` sobrescribe, `>>` añade, `2>` errores, `|` tubería.
    
- **Variables de entorno útiles**: `%USERPROFILE%` (carpeta usuario), `%TEMP%`, `%DATE%`, `%TIME%`
    
- **Comandos externos**: muchos exe del sistema como `ping`, `find`, `xcopy` son programas independientes.