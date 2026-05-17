# 📚 Lista completa de comandos Windows y Linux para CFGM

> Ampliación y mejora de tu lista básica. Formato para Obsidian con ejemplos prácticos y ejercicios.

---

## 🪟 Comandos de Windows (CMD)

### 📁 Operaciones con archivos y directorios

| Comando                                  | Descripción                                    | Ejemplo                                   |
| ---------------------------------------- | ---------------------------------------------- | ----------------------------------------- |
| `mkdir [nombre]`                         | Crea un directorio                             | `mkdir "Mi Carpeta"`                      |
| `cd [ruta]`                              | Cambia de directorio                           | `cd ..` (subir nivel), `cd \` (raíz)      |
| `dir`                                    | Lista contenido del directorio actual          | `dir /w` (vista ancha), `dir /p` (pausa)  |
| `dir /s`                                 | Lista recursivamente incluyendo subdirectorios | `dir /s *.txt`                            |
| `tree`                                   | Muestra estructura de árbol                    | `tree /f` (incluye archivos)              |
| `rename [viejo] [nuevo]`                 | Renombra archivos                              | `rename foto.jpg imagen.jpg`              |
| `copy [origen] [destino]`                | Copia archivos                                 | `copy archivo.txt D:\backup\`             |
| `xcopy [origen] [destino] /e`            | Copia directorios completos                    | `xcopy C:\datos D:\copia /e /h`           |
| `robocopy [origen] [destino]`            | Copia robusta (reanuda, múltiples hilos)       | `robocopy C:\orig D:\dest /MIR`           |
| `move [origen] [destino]`                | Mueve o renombra                               | `move datos.txt ..\`                      |
| `del [archivo]`                          | Elimina archivos                               | `del *.tmp /s` (borra todos .tmp)         |
| `erase [archivo]`                        | Sinónimo de `del`                              | `erase temp.log`                          |
| `rd [directorio]`                        | Elimina directorio vacío                       | `rd basura`                               |
| `rd /s [directorio]`                     | Elimina directorio con todo su contenido       | `rd /s viejo`                             |
| `type [archivo]`                         | Muestra contenido de texto                     | `type readme.txt`                         |
| `more [archivo]`                         | Muestra contenido página por página            | `more informe.log`                        |
| `fsutil file createnew [nombre] [bytes]` | Crea archivo de tamaño exacto                  | `fsutil file createnew vacio.bin 1048576` |

### 🧠 Gestión del sistema y diagnóstico

| Comando                     | Descripción                                  | Ejemplo                                    |
| --------------------------- | -------------------------------------------- | ------------------------------------------ |
| `msinfo32`                  | Información detallada del hardware/software  | `msinfo32`                                 |
| `systeminfo`                | Configuración del SO, parches, RAM, red      | `systeminfo > info.txt`                    |
| `tasklist`                  | Muestra procesos en ejecución                | `tasklist /v` (detalles)                   |
| `taskkill /PID [num] /F`    | Termina un proceso por ID                    | `taskkill /PID 1234 /F`                    |
| `taskkill /IM [nombre.exe]` | Termina proceso por nombre                   | `taskkill /IM notepad.exe`                 |
| `sfc /scannow`              | Verifica y repara archivos del sistema       | `sfc /scannow`                             |
| `chkdsk [unidad:] /f`       | Analiza y repara errores del disco           | `chkdsk C: /f /r`                          |
| `diskpart`                  | Administra particiones (entorno interactivo) | `list disk`, `select disk 0`               |
| `shutdown /s /t 0`          | Apaga el equipo inmediatamente               | `shutdown /r /t 30` (reinicio con retardo) |
| `bcdedit`                   | Configuración de arranque                    | `bcdedit /enum` (ver entradas)             |
| `driverquery`               | Lista todos los controladores instalados     | `driverquery /v`                           |

### 🌐 Red y conectividad

| Comando               | Descripción                           | Ejemplo                                             |
| --------------------- | ------------------------------------- | --------------------------------------------------- |
| `ipconfig`            | Muestra configuración de red          | `ipconfig /all` (detalles completos)                |
| `ping [dirección]`    | Comprueba conectividad                | `ping 8.8.8.8 -t` (continuo)                        |
| `tracert [dirección]` | Rastro de saltos hasta destino        | `tracert google.com`                                |
| `nslookup [dominio]`  | Consulta DNS                          | `nslookup elpais.com`                               |
| `netstat -an`         | Muestra conexiones y puertos abiertos | `netstat -b` (programa asociado)                    |
| `arp -a`              | Tabla ARP (direcciones MAC/IP)        | `arp -a`                                            |
| `route print`         | Tabla de enrutamiento                 | `route add 192.168.1.0 mask 255.255.255.0 10.0.0.1` |
| `netsh`               | Herramienta avanzada de red           | `netsh wlan show profiles` (ver WiFi guardadas)     |

### 👥 Usuarios y permisos

| Comando                | Descripción                        | Ejemplo                                    |
| ---------------------- | ---------------------------------- | ------------------------------------------ |
| `net user`             | Lista usuarios del sistema         | `net user usuario1 *` (cambiar contraseña) |
| `whoami`               | Muestra el usuario actual          | `whoami`                                   |
| `runas /user:[nombre]` | Ejecuta programa como otro usuario | `runas /user:admin cmd`                    |
| `icacls [archivo]`     | Ver/modificar permisos de archivos | `icacls documento.txt /grant usuario:F`    |

### 🛠️ Ayuda y utilidades

| Comando                | Descripción                            |                        |
| ---------------------- | -------------------------------------- | ---------------------- |
| `comando /?`           | Muestra ayuda de cualquier comando     |                        |
| `help`                 | Lista todos los comandos disponibles   |                        |
| `cls`                  | Limpia la pantalla                     |                        |
| `echo [texto]`         | Muestra mensaje o activa/desactiva eco |                        |
| `set`                  | Muestra / define variables de entorno  |                        |
| `find "texto" archivo` | Busca cadenas en archivos              | `find "error" log.txt` |

---

## 🐧 Comandos de Linux (Bash)

### 📁 Operaciones con archivos y directorios

| Comando                           | Descripción                            | Ejemplo                                                       |
| --------------------------------- | -------------------------------------- | ------------------------------------------------------------- |
| `mkdir [nombre]`                  | Crea directorio                        | `mkdir -p proyecto/subcarpeta` (crea padres)                  |
| `ls`                              | Lista contenido                        | `ls -la` (todos, formato largo), `ls -lh` (tamaños legibles)  |
| `cd [ruta]`                       | Cambia directorio                      | `cd ~` (home), `cd -` (directorio anterior)                   |
| `pwd`                             | Muestra directorio actual              | `pwd`                                                         |
| `touch [archivo]`                 | Crea archivo vacío o actualiza fecha   | `touch nuevo.txt`                                             |
| `cat [archivo]`                   | Muestra contenido completo             | `cat file1 file2 > union.txt`                                 |
| `less [archivo]`                  | Visualiza con paginación y búsqueda    | `less -N script.sh`                                           |
| `head -n [archivo]`               | Muestra primeras líneas                | `head -20 /var/log/syslog`                                    |
| `tail -f [archivo]`               | Muestra últimas líneas y sigue cambios | `tail -f /var/log/nginx/access.log`                           |
| `cp [origen] [destino]`           | Copia                                  | `cp -r carpeta1 carpeta2` (recursivo)                         |
| `mv [origen] [destino]`           | Mueve o renombra                       | `mv viejo.txt nuevo.txt`                                      |
| `rm [archivo]`                    | Elimina                                | `rm -rf directorio` (¡peligroso!), `rm -i archivo` (pregunta) |
| `rmdir`                           | Elimina directorio vacío               | `rmdir carpeta_vacia`                                         |
| `find [ruta] [criterio]`          | Busca archivos                         | `find . -name "*.conf" -size +1M`                             |
| `grep [patrón] [archivo]`         | Busca texto dentro de archivos         | `grep -r "error" /var/log/` (recursivo)                       |
| `chmod [permisos] [archivo]`      | Cambia permisos                        | `chmod 755 script.sh` (rwxr-xr-x), `chmod u+x archivo`        |
| `chown [usuario:grupo] [archivo]` | Cambia propietario                     | `sudo chown www-data:www-data index.html`                     |
| `ln -s [origen] [destino]`        | Crea enlace simbólico                  | `ln -s /usr/bin/python3 python`                               |

### 🧠 Procesos y sistema

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `ps aux` | Lista procesos con detalles | `ps aux --sort=-%cpu` (orden por CPU) |
| `top` | Monitor interactivo en tiempo real | `top -u usuario` (filtra por usuario) |
| `htop` | Versión mejorada de top (instalar aparte) | `htop` |
| `kill [PID]` | Termina proceso | `kill -9 1234` (forzado), `kill -15 1234` (suave) |
| `pkill [nombre]` | Mata por nombre | `pkill firefox` |
| `jobs` | Muestra tareas en segundo plano | `jobs -l` |
| `bg` / `fg` | Reanuda tarea en background/foreground | `fg %1` |
| `nohup [comando] &` | Ejecuta comando que no muere al cerrar terminal | `nohup python server.py &` |
| `systemctl [acción] [servicio]` | Gestiona servicios (systemd) | `systemctl start ssh`, `enable`, `status` |
| `journalctl -xe` | Logs del sistema | `journalctl -u nginx -f` (logs de un servicio) |

### 💾 Almacenamiento y discos

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `df -h` | Espacio en discos (formato legible) | `df -i` (inodos) |
| `du -sh [carpeta]` | Tamaño de una carpeta | `du -sh * | sort -h` (ordenar) |
| `lsblk` | Muestra dispositivos de bloque | `lsblk -f` (incluye sistemas de archivos) |
| `fdisk -l` | Lista particiones (requiere sudo) | `sudo fdisk -l /dev/sda` |
| `mount` / `umount` | Monta/desmonta sistemas de archivos | `sudo mount /dev/sdb1 /mnt/usb` |
| `tar -czvf archivo.tar.gz carpeta/` | Comprime con tar y gzip | `tar -xzvf archivo.tar.gz` (descomprimir) |
| `gzip [archivo]` | Comprime archivo (reemplaza original) | `gunzip archivo.gz` |
| `zip -r [nombre.zip] [carpeta]` | Comprime en ZIP | `unzip archivo.zip` |

### 🌐 Red y conectividad

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `ip a` | Muestra interfaces de red | `ip route show` (tabla de rutas) |
| `ping -c 4 [destino]` | Envía 4 paquetes ICMP | `ping -c 10 google.es` |
| `traceroute [destino]` | Ruta de paquetes | `traceroute -n 8.8.8.8` (sin DNS) |
| `netstat -tulpn` | Puertos abiertos y programas | `ss -tulpn` (alternativa moderna) |
| `ss -tulpn` | Socket statistics (más rápido) | `ss -tulpn` |
| `curl [URL]` | Transfiere datos desde/hacia servidor | `curl -O https://ejemplo.com/archivo.zip` |
| `wget [URL]` | Descarga archivos | `wget -c http://...` (reanuda) |
| `ssh usuario@host` | Conexión remota segura | `ssh -p 2222 user@192.168.1.10` |
| `scp [origen] [destino]` | Copia segura por SSH | `scp -r carpeta/ user@host:/ruta/` |

### 👥 Usuarios y permisos

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `whoami` | Usuario actual | `whoami` |
| `id` | UID, GID y grupos del usuario | `id -u` (solo UID) |
| `sudo [comando]` | Ejecuta como superusuario | `sudo !` (repite último comando con sudo) |
| `passwd [usuario]` | Cambia contraseña | `passwd` (cambia la propia) |
| `useradd` / `adduser` | Crea usuario | `sudo adduser juan` |
| `usermod -aG [grupo] [usuario]` | Añade usuario a grupo | `sudo usermod -aG docker juan` |
| `groups [usuario]` | Muestra grupos del usuario | `groups root` |

### 🛠️ Ayuda y mantenimiento

| Comando | Descripción |
|---------|-------------|
| `man [comando]` | Manual completo | `man ls` |
| `comando --help` | Ayuda resumida | `grep --help` |
| `whatis [comando]` | Descripción breve | `whatis mkdir` |
| `apt update && apt upgrade` | Actualiza repositorios y paquetes (Debian/Ubuntu) | `sudo apt update` |
| `apt search [paquete]` | Busca paquete | `apt search nginx` |
| `apt install [paquete]` | Instala software | `sudo apt install htop -y` |
| `clear` | Limpia pantalla | `clear` (o Ctrl+L) |
| `history` | Muestra historial de comandos | `!100` (repite línea 100) |
| `alias` | Crea atajos | `alias ll='ls -la'` |

---
## 💡 Consejos para practicar

- **Ayuda integrada**: Windows → `comando /?` ; Linux → `man comando` o `comando --help`.
    
- **Historial**: Usa flecha arriba/abajo para reutilizar comandos.
    
- **Comodines**: `*` (cualquier cadena), `?` (un carácter), `[a-z]` (rango).
    
- **Redirecciones**: `>` (sobrescribe), `>>` (añade), `|` (tubería entre comandos).
    
- **Seguridad**: En Linux evita `rm -rf /` o `chmod 777` sin entenderlo.
    
- **Máquinas virtuales** o WSL (Windows Subsystem for Linux) para practicar Linux sin riesgo.



## 📝 Ejercicios prácticos ampliados

### Ejercicio 1: Estructura de proyectos (Windows + Linux)

**Windows:**
1. Crea una carpeta `CFGM_Ejercicios` en el escritorio (usa `cd` y `mkdir`).
2. Dentro crea `Modulo1`, `Modulo2`, y dentro de cada uno `practicas` y `examenes`.
3. Usa `fsutil` para crear un archivo de 5 KB llamado `oculto.bin` dentro de `Modulo1/practicas`.
4. Cambia su nombre a `datos.dat` y muévelo a `Modulo2/practicas\examenes`.
5. Muestra toda la estructura con `tree /f`.

**Linux:**
1. Desde tu home, crea `~/proyectos/{src,doc,bin}` en un solo comando (`mkdir -p`).
2. Usa `touch` para crear `leeme.txt` en `doc`, y `script.sh` en `bin`.
3. Escribe en `leeme.txt` las líneas "Esto es una práctica" usando `echo >>`.
4. Busca todos los archivos `.txt` dentro de `proyectos` con `find`.
5. Muestra los permisos de `script.sh` y cámbialos a `rwxr-x---` (750) con `chmod`.

### Ejercicio 2: Monitorización de sistema (Linux)

1. Abre dos terminales. En una ejecuta `top` y observa procesos.
2. En la segunda, lanza un proceso en segundo plano que consuma CPU: `dd if=/dev/zero of=/dev/null &`
3. Encuentra el PID del proceso `dd` con `ps aux | grep dd`.
4. Usa `kill` para detenerlo y verifica que desaparece de `top`.
5. Registra en un archivo `monitor.log` el estado de memoria con `free -h` y espacio en disco con `df -h`.

### Ejercicio 3: Administración de redes básica

**Windows:**
1. Abre CMD como administrador.
2. Muestra tu configuración IP completa con `ipconfig /all`.
3. Averigua la puerta de enlace predeterminada (Default Gateway).
4. Haz un ping a esa puerta de enlace durante 10 paquetes (`ping -n 10`).
5. Guarda el resultado de `tracert 8.8.8.8` en un archivo `ruta.txt`.

**Linux:**
1. Muestra las interfaces de red con `ip a`.
2. Usa `ss -tulpn` para ver qué servicios están escuchando puertos.
3. Haz un ping a `google.com` limitado a 5 paquetes con `-c`.
4. Descarga el archivo `robots.txt` de `https://www.example.com/robots.txt` usando `wget`.
5. Ejecuta `sudo systemctl status ssh` (si tienes SSH instalado) y entiende la salida.

### Ejercicio 4: Permisos y seguridad comparado

1. **Windows:**
   - Crea un archivo `secreto.txt` con `echo "confidencial" > secreto.txt`.
   - Usa `icacls secreto.txt` para ver permisos.
   - Quita permisos de lectura al grupo "Usuarios" con `icacls secreto.txt /remove "Users"`.
   - Comprueba que no puedes leerlo con `type secreto.txt` (debería dar error).

2. **Linux:**
   - Crea `privado.txt` y escribe "solo root".
   - Dale permisos `600` (solo propietario lectura/escritura).
   - Crea otro usuario temporal (`sudo useradd prueba`) y cambia a él (`su - prueba`).
   - Intenta leer `privado.txt` → debe fallar.
   - Vuelve a tu usuario y usa `sudo` para leerlo.

### Ejercicio 5: Automatización con tuberías y redirecciones (Linux)

1. Lista todos los archivos de `/etc` que contengan la palabra "net" con `ls /etc | grep net`.
2. Cuenta cuántos procesos tiene el usuario root con `ps aux | grep root | wc -l`.
3. Guarda las 10 últimas líneas del log de sistema en `ultimos_logs.txt`: `tail -10 /var/log/syslog > ultimos_logs.txt` (en sistemas Debian/Ubuntu).
4. Usa `find` para localizar todos los archivos `.conf` modificados en las últimas 24 horas: `find /etc -name "*.conf" -mtime -1`.

---

## ✅ Solucionario de ejercicios

### Solución Ejercicio 1 (Windows)

```
cd C:\Users\%USERNAME%\Desktop
mkdir CFGM_Ejercicios
cd CFGM_Ejercicios
mkdir Modulo1 Modulo2
mkdir Modulo1\practicas Modulo1\examenes
mkdir Modulo2\practicas Modulo2\examenes
fsutil file createnew Modulo1\practicas\oculto.bin 5120
rename Modulo1\practicas\oculto.bin datos.dat
move Modulo1\practicas\datos.dat Modulo2\examenes\
tree /f
```

### Solución Ejercicio 1 (Linux)
```
cd ~
mkdir -p proyectos/{src,doc,bin}
touch proyectos/doc/leeme.txt
touch proyectos/bin/script.sh
echo "Esto es una práctica" >> proyectos/doc/leeme.txt
find proyectos -name "*.txt"
chmod 750 proyectos/bin/script.sh
ls -l proyectos/bin/script.sh

```

### Solución Ejercicio 2 (Linux)

```
# Terminal 1
top
# Terminal 2
dd if=/dev/zero of=/dev/null &
ps aux | grep dd
kill <PID>   # sustituir por el PID real
# Volver a terminal 1 para verificar
free -h > monitor.log
df -h >> monitor.log
```

### Solución Ejercicio 3 (Windows)

```
ipconfig /all
ping -n 10 192.168.1.1   # cambiar IP por tu puerta de enlace
tracert 8.8.8.8 > ruta.txt
type ruta.txt
```

### Solución Ejercicio 3 (Linux)

```
ip a
ss -tulpn
ping -c 5 google.com
wget https://www.example.com/robots.txt
sudo systemctl status ssh
```

### Solución Ejercicio 4 (Windows)

```
echo confidencial > secreto.txt
icacls secreto.txt
icacls secreto.txt /remove "Users"
type secreto.txt   # debe dar error
```

### Solución Ejercicio 4 (Linux)

```
echo "solo root" > privado.txt
chmod 600 privado.txt
sudo useradd prueba
su - prueba
cat /home/tu_usuario/privado.txt   # falla
exit
sudo cat privado.txt
sudo userdel -r prueba   # limpieza
```

### Solución Ejercicio 5 (Linux)

```
ls /etc | grep net
ps aux | grep root | wc -l
tail -10 /var/log/syslog > ultimos_logs.txt
find /etc -name "*.conf" -mtime -1
```