# 🖥️ NAS Casera — Guía Completa Paso a Paso


```insta-toc
---
title:
  name: INDEX
  level: 2
  center:
exclude:
style:
  listType:
omit:
levels:
  min: 1
  max: 2
---

## INDEX

- 🖥️ NAS Casera — Guía Completa Paso a Paso
    - Preparación
    - Instalar DEBIAN + OMV
    - Primeras configuraciones en OMV
    - Discos
    - Usuarios
    - Carpetas
    - Compartir en red (SMB)
    - Conectar desde Windows
    - Docker y Compose (La Base)
    - Herramientas de Gestión (Local)
    - Infraestructura de Red y Proxy
    - Instalación de Aplicaciones
    - Pruebas, Solución de Problemas y Conexión
    - Resúmenes y Credenciales
```


---

## Preparación

> Esta guía cubre TODOS los pasos desde cero hasta tener una NAS funcionando con apps, proxy inverso, HTTPS y acceso remoto. Sigue el orden exacto. No te saltes ningún paso.

### Requisitos antes de empezar

**Hardware:**

- Portátil viejo + HDD 1TB en caddy + dock con 2 discos
- Cable Ethernet conectado del portátil NAS al router
- USB de 4GB+ para la instalación
- Tu PC principal (para controlar todo)

**Descargas (en tu PC principal):**

- ISO Debian 13 netinstall: https://www.debian.org/distrib/netinst → amd64
- Balena Etcher: https://etcher.balena.io

> ⚠️ **Usa Balena Etcher para grabar el USB, NO Rufus.** Rufus puede modificar la estructura de la ISO y provocar errores de instalación (debootstrap). Balena Etcher graba la ISO tal cual y es lo que recomienda Debian.

**Cuentas:**

- Crear cuenta en https://www.duckdns.org (se necesita para el acceso remoto)

---

## Instalar DEBIAN + OMV

### Paso 1 — Crear USB bootable

**Dónde:** En tu PC principal
**Herramienta:** Balena Etcher

1. Abrir Balena Etcher
2. "Flash from file" → seleccionar la ISO de Debian
3. "Select target" → seleccionar tu USB
4. "Flash!" → esperar a que termine **Y que verifique**
5. Listo, no toques el USB

> ⚠️ **No uses Rufus.** Puede causar errores de "debootstrap" al instalar Debian.

### Paso 2 — Instalar Debian

> ⚠️ **El portátil debe estar conectado al router por cable Ethernet ANTES de empezar.** La instalación necesita internet para descargar paquetes.

Teclas comunes del menú de arranque por marca: HP = F9, Dell = F12, Lenovo = F12, Acer = F2, Asus = F8/ESC

1. Pinchar el USB en el portátil NAS
2. Encender → pulsar la tecla del menú de arranque → seleccionar USB
3. Aparece el instalador de Debian → seleccionar **"Install"** (no Graphical Install)
4. Seguir el asistente:

| Pantalla | Qué elegir |
|---|---|
| Idioma | Español |
| Ubicación | España |
| Teclado | Español |
| Hostname | `nas` (o el nombre que quieras) |
| Dominio | (dejar vacío, pulsar Enter) |
| Contraseña root | Poner una segura → **APUNTARLA** |
| Nombre completo usuario | Tu nombre |
| Nombre de usuario | Tu nombre en minúsculas |
| Contraseña usuario | Poner otra segura → **APUNTARLA** |
| Zona horaria | Madrid |
| Particionado | "Guiado - utilizar todo el disco" |
| Disco | **Seleccionar el SSD** (NO el HDD del caddy) |
| Esquema | "Todos los ficheros en una partición" |
| Confirmar | "Finalizar el particionado y escribir cambios" → Sí |
| Mirror de red | España → deb.debian.org |
| Proxy | (dejar vacío, pulsar Enter) |
| Participar en encuesta | No |
| **Selección de software** | **DESMARCAR TODO excepto:** ☑ SSH server ☑ Standard system utilities (NO marcar entorno de escritorio, NO marcar GNOME) |
| GRUB | Sí, instalar en el disco principal → seleccionar el SSD |

> ⚠️ **En la selección de software:** usa la **barra espaciadora** para marcar/desmarcar. **Enter** confirma y continúa, NO desmarca. Si le das a Enter sin querer, se instalará con escritorio GNOME y tendrás que reinstalar.

5. Esperar a que termine → reiniciar → **quitar el USB**

### Paso 3 — Primer login en Debian

1. Aparece: `nas login:`
2. Escribir tu nombre de usuario → Enter
3. Escribir tu contraseña → Enter (no se ve lo que escribes, es normal)

### Paso 4 — El truco del jefe: su vs su -

Tu usuario normal no tiene permisos de administrador. Necesitas cambiar a root:

```bash
su -
```

Te pide la **contraseña de root**. La escribes → Enter.

Ahora ves: `root@nas:~#` (la `#` en vez de `$` significa que eres root)

> 💡 **¿Por qué `su -` y no `su`?** El guion carga el entorno completo de root. Sin él, muchos comandos no se encontrarán.

### Paso 5 — Preparar los permisos (sudo)

```bash
usermod -aG sudo TU_USUARIO
reboot
```

### Paso 6 — Instalar OpenMediaVault

```bash
su -
wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | bash
```

> 💡 **Si el pipe `|` no funciona por el teclado:**
> ```bash
> wget https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install -O install.sh
> bash install.sh
> ```

> ⚠️ **Es NORMAL ver letras rojas** sobre NTP. Ignóralas. Cuando termine verás: `Done. rc=0`

### Paso 7 — Obtener la IP de la NAS

```bash
ip addr show
```

Busca `inet 192.168.X.XX` → **APÚNTALA**

> 💡 También puedes ver la IP desde el panel del router → dispositivos conectados.

### Paso 8 — Configurar que no se apague al cerrar la tapa

> ⚠️ **OBLIGATORIO.** Sin esto, al cerrar la tapa la NAS se suspende.

```bash
su -
sed -i 's/#HandleLidSwitch=suspend/HandleLidSwitch=ignore/' /etc/systemd/logind.conf
sed -i 's/#HandleLidSwitchDocked=ignore/HandleLidSwitchDocked=ignore/' /etc/systemd/logind.conf
systemctl restart systemd-logind
```

### Paso 9 — Cerrar el portátil y dejarlo trabajando

1. Cierra la tapa del portátil NAS
2. Déjalo conectado: Ethernet ✅ Cargador ✅ Dock ✅
3. **A partir de ahora NUNCA MÁS tocas el portátil NAS directamente**
4. Todo lo controlas desde tu PC

---

## Primeras configuraciones en OMV

1. Cambiar a IP Fija → Panel del router → DHCP estático → `192.168.X.10` (elige tu IP)
2. Entrar al panel de OMV → cambiar contraseña (usuario: `admin` / contraseña: `openmediavault`)
3. Actualizaciones → Sistema → Gestión de actualizaciones → Instalar todas
4. Cambiar DNS → Red → Interfaces → "Dirección IP de los servidores DNS" → `1.1.1.1` y activar SSL
5. Servicios → SMB/CIFS → Activar → Configuración → "Opciones adicionales" → pegar:

```
vfs objects = fruit streams_xattr
ea support = yes
map acl inherit = yes
smb3 directory leases = no
```

---

## Discos

### Limpiar discos

Almacenamiento → Discos → Borrar (Quick) los 3 discos de datos

### Montar disco del caddy

Sistema de archivos → Crear → ext4 → Montar

### Instalar OMV Extras

Primero activar `_ssh` en Usuarios → Usuarios → Editar → Grupos.
De paso añadir: `adm`, `sudo`, `docker`, `sambashare`

> 💡 Si ya instalaste antes, borra el fingerprint:
> ```bash
> ssh-keygen -R TU_IP_NAS
> ```

```bash
ssh TU_USUARIO@TU_IP_NAS
su -
wget -O - https://github.com/OpenMediaVault-Plugin-Developers/packages/raw/master/install | bash
```

### Hacer que el PC nunca se apague

```bash
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
```

### Instalar plugin de RAID

Sistema → Plugins → `openmediavault-md` → Instalar

### Crear mirror (RAID 1)

Múltiples Dispositivos → + Crear → RAID1 o ESPEJO

**Si no te salen los discos, aplicar por SSH:**

```bash
ssh TU_USUARIO@TU_IP_NAS
su -

# Crear el RAID 1 (Mirror) - Escribe 'y' cuando pregunte
mdadm --create --verbose /dev/md0 --level=1 --raid-devices=2 /dev/sdc /dev/sdd

# Obligar a OMV a leer la configuración
mdadm --detail --scan >> /etc/mdadm/mdadm.conf
update-initramfs -u
```

**REINICIAR** la NAS después.

### Montar el mirror

Sistema de Archivos → seleccionar md0 → Montar → ext4

---

## Usuarios

Crear nuevos usuarios si necesitamos (recomendado):
- Grupos: `users`
- Shell: `/usr/bin/bash`

---

## Carpetas

Añadir en Almacenamiento → Carpetas compartidas

### Estructura

```
DISCO CADDY (lo descargable/reemplazable):
├── Media          ← compartir por SMB
│   ├── Peliculas  ← subcarpeta desde Windows
│   ├── Series
│   └── Musica
├── Descargas      ← compartir por SMB
├── Software       ← compartir por SMB
├── appdata        ← NO compartir (config Docker)
├── compose        ← NO compartir (archivos compose)
├── data           ← NO compartir (datos apps)
└── docker         ← NO compartir (instalación Docker)

DISCO MIRROR (lo que NO puedes perder):
├── Personal       ← compartir por SMB
│   ├── Fotos_Familia
│   ├── Documentos_Familia
│   └── Videos_Familia
├── Profesional    ← compartir por SMB
│   ├── Estudios
│   ├── Certificaciones
│   ├── Scripts
│   └── YouTube
├── Backups        ← compartir por SMB
│   ├── Moviles
│   └── PCs
└── backup         ← NO compartir (backup configs Docker)
```

### Crear permisos

Usuarios → Seleccionar user → Permisos de carpeta compartida → Dar permiso a los usuarios para cada carpeta que se desee

---

## Compartir en red (SMB)

### Activar SMB

Servicios → SMB/CIFS → Configuración → **Habilitado**
Habilitar ACL y Permisos heredados

### Compartir carpetas

Servicios → SMB/CIFS → Compartidos → Crear → seleccionar carpeta → Añadir
Heredar ACL y Permisos

**REINICIAR** después de configurar.

---

## Conectar desde Windows

```
\\TU_IP_NAS\CARPETA
```

> 💡 **Si no te entra:**
> ```
> net use * /delete /y
> net stop lanmanworkstation /y
> net start lanmanworkstation
> ```

---

## Docker y Compose (La Base)

### Preparar Docker

Sistema → OMV-Extras → Activar **Docker** → pulsar **Apt Clean**

### Compose

Sistema → Plugins → buscar `compose` → Instalar

En Usuarios → Usuarios → Editar → Grupos → En el usuario `admin` → Primero activar.

Servicios → Compose → Configuración:
- Carpeta compartida: `compose` (Poner de propietario a tu usuario y grupo `users`)
- Datos: `appdata`
- Respaldo: `backup`
- Propietario: tu usuario → Grupo: `users` / permisos lectura y escritura propietario y grupo

> **Las carpetas Docker:**
> - **Compose**: Los planos de nuestras apps
> - **AppData**: El corazón y configuración de las apps
> - **Backup**: Una copia de seguridad de nuestros planos, alojada en el RAID 1 para máxima seguridad
> - **Docker**: Donde va instalado Docker

### Instalar apps desde Compose

Servicios → Compose → Archivos → Crear o importar desde ejemplos

**Para cada app editar 3 cosas:**

1. **Rutas (Volumes):** reemplazar `/CHANGE/ME` por tus rutas absolutas. Las encuentras en Almacenamiento → Carpetas Compartidas → columna "Ruta absoluta". Cópialas en un bloc de notas.
2. **Permisos (PUID/PGID):** verificar en Usuarios → UID y GID (normalmente `1000` y `100`).
3. **Puerto:** que no esté en uso por otra app.

---

## Herramientas de Gestión (Local)

### FileBrowser

#### YAML

```yaml
services:
  filebrowser:
    image: filebrowser/filebrowser:latest
    container_name: filebrowser
    user: 1000:100
    environment:
      - PUID=1000
      - PGID=100
      - UMASK=000
    ports:
      - "8080:80"
    volumes:
      # Carpetas del CADDY (cambia el UUID por el tuyo)
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/Media:/srv/Media
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/Descargas:/srv/Descargas
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/Software:/srv/Software
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata:/srv/appdata
      # Carpetas del MIRROR (cambia el UUID por el tuyo)
      - /srv/dev-disk-by-uuid-TU_UUID_MIRROR/Personal:/srv/Personal
      - /srv/dev-disk-by-uuid-TU_UUID_MIRROR/Profesional:/srv/Profesional
      - /srv/dev-disk-by-uuid-TU_UUID_MIRROR/Backups:/srv/Backups
      # Config de FileBrowser
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/filebrowser/database:/database
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/filebrowser/config:/config
    restart: always
```

**Acceder:**
Usuarios → permisos → dar permisos a tu usuario.
Abrir: `http://TU_IP_NAS:8080`
La contraseña la primera vez → seleccionar filebrowser → herramientas → **logs** → cambiar la pass una vez logueado.

> 💡 **Falta de Permisos:**
> Si no te entra por falta de permisos, prueba en Carpetas compartidas → seleccionar `appdata` → poner como propietario al usuario → dar permisos y ACL → y después quitar. A veces el server lo crea como root y hay que forzar. Si no funciona, por SSH:
> ```bash
> sudo chown -R 1000:100 /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/
> ```

#### Lo que verás en FileBrowser

```
/
├── Media/
├── Descargas/
├── Software/
├── appdata/
├── Personal/
├── Profesional/
└── Backups/
```

---

## Infraestructura de Red y Proxy

### Cambiar puerto de OMV (Crucial antes de NPM)

Desde el panel de OMV:
- Sistema → Área de trabajo → Puerto → cambiar de `80` a `8888`
- Guardar → Aplicar cambios

> ⚠️ Perderás la conexión. Espera 30 segundos y entra con: `http://TU_IP_NAS:8888`

### Abrir puertos en el router

Panel del router → Internet → Redirección de puertos:

| Servicio | Puerto público | Puerto LAN | IP destino | Protocolo |
|---|---|---|---|---|
| NAS-HTTP | 80 | 80 | TU_IP_NAS | TCP |
| NAS-HTTPS | 443 | 443 | TU_IP_NAS | TCP |

**APLICAR CAMBIOS**

> ⚠️ **SOLO estos 2 puertos. NADA más.**

### DuckDNS

#### Crear cuenta y dominio

Ir a https://www.duckdns.org → crear cuenta → crear dominio → copiar token.

#### Configurar script para sincronizar IP automáticamente

```bash
ssh TU_USUARIO@TU_IP_NAS
su -
mkdir -p ~/duckdns
apt install curl -y
nano ~/duckdns/duck.sh
```

Pegar esto en el archivo (cambia TU_DOMINIO y TU_TOKEN):

```bash
#!/bin/bash
# Script para actualizar DuckDNS

DOMAIN="TU_DOMINIO.duckdns.org"    # Cambia por tu dominio
TOKEN="TU_TOKEN_AQUI"              # Cambia por tu token real

curl -k -s "https://www.duckdns.org/update?domains=${DOMAIN}&token=${TOKEN}&ip=" > ~/duckdns/duck.log
cat ~/duckdns/duck.log
```

Guardar (Ctrl+O → Enter → Ctrl+X) y ejecutar:

```bash
chmod 700 ~/duckdns/duck.sh
./duckdns/duck.sh
cat ~/duckdns/duck.log
```

¿Dice OK? → **Automatizar:**

```bash
crontab -e
```

(Si pregunta qué editor, elige `1` para nano). Añadir al final:

```
*/5 * * * * ~/duckdns/duck.sh >/dev/null 2>&1
```

Guardar (Ctrl+O → Enter → Ctrl+X → exit dos veces).

### Nginx Proxy Manager (NPM)

#### YAML

Servicios → Compose → Archivos → Crear → Levantar servicio

```yaml
services:
  npm:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    ports:
      - "80:80"
      - "443:443"
      - "81:81"
    volumes:
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/npm:/data
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/npm-letsencrypt:/etc/letsencrypt
    restart: unless-stopped
```

Después para y arranca Nginx Proxy Manager:
- Servicios → Compose → selecciona `nginx-proxy-manager` → ⬛ Down → ▶ Up

**Acceder:**
Abrir: `http://TU_IP_NAS:81`
Login: `admin@example.com` / `changeme` → Te obliga a cambiar email y contraseña.

### Certificado HTTPS (Wildcard)

En Nginx Proxy Manager (`http://TU_IP_NAS:81`):

1. SSL Certificates → Add SSL Certificate → **Let's Encrypt**
2. Domain Names (añadir los dos, pulsar Enter después de cada uno):
   - `TU_DOMINIO.duckdns.org`
   - `*.TU_DOMINIO.duckdns.org`
3. Activar **"Use a DNS Challenge"**
4. DNS Provider: **DuckDNS**
5. En `dns_duckdns_token=` → pegar tu token de DuckDNS
6. Aceptar términos → Save

> 💡 Si no lo crea, poner 120 o más segundos de propagación para que le de tiempo.

---

## Instalación de Aplicaciones

### Jellyfin

#### Preparar

Crear carpetas `Peliculas`, `Series`, `Musica` dentro de `Media` (desde Windows o FileBrowser).

#### YAML

Servicios → Compose → Crear → Levantar servicio

```yaml
services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin
    user: "1000:100"
    environment:
      - PUID=1000
      - PGID=100
      - TZ=Europe/Madrid
    ports:
      - "8096:8096"
    volumes:
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/jellyfin:/config
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/Media/Peliculas:/media/peliculas
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/Media/Series:/media/series
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/Media/Musica:/media/musica
    restart: unless-stopped
```

**Acceder:**
Abrir: `http://TU_IP_NAS:8096`
Configurar idioma, crear usuario, añadir bibliotecas. Cuando añadas pelis → Panel de control → Bibliotecas → Escanear todo.

> 💡 **Problema de permisos en Jellyfin:**
> Si no te entra por falta de permisos, prueba en Carpetas compartidas → seleccionar `appdata` → poner como propietario al usuario → dar permisos y ACL → y después quitar. Si aún así no entra, ir por SSH:
> ```bash
> sudo chown -R 1000:1000 /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/*
> sudo chmod -R 775 /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/*
> ```

#### Conectar Jellyfin desde fuera de la red local

En Nginx Proxy Manager → **Proxy Hosts** → **Add Proxy Host**:

| Campo | Valor |
|---|---|
| Domain Names | `jellyfin.TU_DOMINIO.duckdns.org` |
| Forward Hostname/IP | `TU_IP_NAS` |
| Forward Port | `8096` |
| Pestaña SSL | Seleccionar certificado wildcard → **Force SSL** ✅ |

En la pestaña **Advanced** pegar:

```
client_max_body_size 512M;

location / {
    proxy_pass $forward_scheme://$server:$port;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Protocol $scheme;
    proxy_set_header X-Forwarded-Host $http_host;

    # Buffering off es vital para streaming de vídeo (Jellyfin)
    proxy_buffering off;
}
```

### Nextcloud

#### YAML

Servicios → Compose → Añadir → Levantar servicio

```yaml
services:
  nextcloud-db:
    image: mariadb:10.11
    container_name: nextcloud-db
    environment:
      MYSQL_ROOT_PASSWORD: TU_ROOT_PASSWORD_SEGURA
      MYSQL_DATABASE: nextcloud
      MYSQL_USER: nextcloud
      MYSQL_PASSWORD: TU_PASSWORD_NEXTCLOUD
    volumes:
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/nextcloud-db:/var/lib/mysql
    restart: unless-stopped

  nextcloud:
    image: nextcloud:latest
    container_name: nextcloud
    ports:
      - "8082:80"
    environment:
      MYSQL_HOST: nextcloud-db
      MYSQL_DATABASE: nextcloud
      MYSQL_USER: nextcloud
      MYSQL_PASSWORD: TU_PASSWORD_NEXTCLOUD
    volumes:
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/nextcloud:/var/www/html
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/Media:/mnt/Media:rw
      - /srv/dev-disk-by-uuid-TU_UUID_CADDY/Descargas:/mnt/Descargas:rw
      - /srv/dev-disk-by-uuid-TU_UUID_MIRROR/Personal:/mnt/Personal:rw
      - /srv/dev-disk-by-uuid-TU_UUID_MIRROR/Profesional:/mnt/Profesional:rw
    restart: unless-stopped
```

> ⚠️ **Cambia las contraseñas** por unas reales (sin arrobas ni caracteres raros). Tienen que ser diferentes entre sí.

**Lo que hace cada volumen:**
- `Personal` → tus fotos y docs familia (mirror, protegido)
- `Profesional` → tus proyectos y estudios (mirror, protegido)
- `Media` y `Descargas` → contenido descargable (caddy)
- `appdata/nextcloud` → configuración de Nextcloud (caddy)
- `appdata/nextcloud-db` → base de datos MariaDB (caddy)

#### SI NO TE CONECTA!!
1. Sino te conecta haz esto por SSH
```
nano /etc/docker/daemon.json
```

2. Copia y pega exactamente esto (pon tu UIID de Disco):
```
{
  "data-root": "/srv/dev-disk-by-uuid-TU_UUID_CADDY/docker",
  "log-driver": "json-file",
  "log-opts": {
    "max-file": "3",
    "max-size": "50m"
  },
  "storage-driver": "overlay2",
  "dns": ["8.8.8.8", "1.1.1.1"],
  "ipv6": false,
  "iptables": false,
  "ip6tables": false,
  "registry-mirrors": ["https://mirror.gcr.io", "https://dockerhub.azk8s.cn"]
}
```

Guarda (Ctrl+O → Enter → Ctrl+X).

3. Aplica los cambios:

```
systemctl restart docker
sleep 10
docker pull hello-world
```

Si el hello-world te ha cargado ya puedes volver a levantar desde OMV nextcloud
#### Permisos para Nextcloud (MUY IMPORTANTE)

> 💡 La imagen oficial de Nextcloud usa el usuario interno `www-data` (UID 33 y GID 33). El servidor a veces crea las carpetas como `root`, por lo que **hay que forzar los permisos** si falla el acceso.

**1. Permisos para Nextcloud (Archivos y Sistema):**

```bash
sudo chown -R 33:33 /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/nextcloud
sudo chmod -R 775 /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/nextcloud
```

**2. Permisos para la Base de Datos (MariaDB):**

```bash
sudo chown -R 999:999 /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/nextcloud-db
sudo chmod -R 775 /srv/dev-disk-by-uuid-TU_UUID_CADDY/appdata/nextcloud-db
```

**Acceder localmente:**
Abrir: `http://TU_IP_NAS:8082`

#### Si no te Entra a APPS en Nextcloud
Si no te entra a Apps hay que limpiar las caches, pon éstos 2 comandos por SSH
```
docker exec --user www-data -it nextcloud php occ config:system:set appstoreenabled --value false --type boolean

docker restart nextcloud

```


#### Configuración de Nextcloud - Estructura de Carpetas

**Objetivo:** Hacer que Nextcloud muestre **exactamente la misma estructura** de carpetas que vemos en FileBrowser y en Windows.

**Paso 1: Instalar External Storage Support**
1. En Nextcloud, haz clic en tu **avatar** (arriba a la derecha).
2. Selecciona **Apps**.
3. Ve a la pestaña **Deshabilitadas**.
4. Busca **`External storage support`**.
5. Haz clic en **Habilitar**.

**Paso 2: Configurar External Storages**
1. Haz clic en tu **avatar** → **Configuración**.
2. En el menú izquierdo selecciona **External storages**.
3. Haz clic en **+ Añadir almacenamiento externo**, selecciona **Local** y rellena:

| Nombre de carpeta | Tipo | Ruta en el contenedor | Disponible para | Solo lectura |
|---|---|---|---|---|
| **Media** | Local | `/mnt/Media` | Todos los usuarios | ✅ Sí |
| **Descargas** | Local | `/mnt/Descargas` | Todos los usuarios | ❌ No |
| **Personal** | Local | `/mnt/Personal` | tu usuario + familia | ❌ No |
| **Profesional** | Local | `/mnt/Profesional` | tu usuario | ❌ No |

> 💡 **Notas importantes sobre External Storage:**
> - **No se duplica contenido**: Nextcloud solo crea un enlace a las carpetas reales del NAS.
> - Las carpetas marcadas como "Solo lectura" evitan borrados accidentales desde la nube.
> - Si subes o borras archivos desde Nextcloud en carpetas de lectura/escritura, se reflejarán en FileBrowser y Windows (y viceversa).

**Verificación:** Ve al inicio de Nextcloud. Deberías ver las carpetas `Media`, `Personal`, `Profesional`, etc. en la raíz y poder navegar en ellas viendo el contenido real.

#### Comandos para arreglar permisos en Carpetas Externas

Dado que Nextcloud funciona con el usuario `33:33` (www-data), las carpetas externas del NAS necesitan ser accesibles para él.

**Arreglar permisos generales (ejemplo con "Media"):**
Cambia 'Media' por cada uina de las carpetas que quieras sincronizar así no tendrás problemas de permisos y podrás subir desde cualquier dispositivo lo que quieras, si no lo haces tendrás problemas de permisos

```bash
sudo chown -R 33:33 /srv/dev-disk-by-uuid-TU_UUID_CADDY/Media
sudo chmod -R 775 /srv/dev-disk-by-uuid-TU_UUID_CADDY/Media
```

**Configuración importante dentro de Nextcloud:**
Para que lo que subas desde Nextcloud se pueda modificar después desde Windows:

```bash
docker exec --user www-data -it nextcloud php occ config:system:set localstorage.umask --value 0002 --type integer
docker restart nextcloud
```

#### Reglas de Proxy para Nextcloud

En Nginx Proxy Manager → **Proxy Hosts** → **Add Proxy Host**:

| Campo | Valor |
|---|---|
| Domain Names | `cloud.TU_DOMINIO.duckdns.org` |
| Forward Hostname/IP | `TU_IP_NAS` |
| Forward Port | `8082` |
| Pestaña SSL | Mismo certificado wildcard → **Force SSL** ✅ |
| WebSocket Support | **ACTIVADO** ✅ |

En la pestaña **Advanced** pegar:

```
client_max_body_size 512M;

location / {
    proxy_pass $forward_scheme://$server:$port;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Protocol $scheme;
    proxy_set_header X-Forwarded-Host $http_host;
    proxy_buffering off;
}
```

#### Configuración de Dominios de Confianza

Si al entrar por tu dominio web Nextcloud te bloquea con el mensaje *"Acceso a través de un dominio no confiable"*, aplica estos comandos por SSH:

```bash
# Añadir tu dominio a la lista de confianza
docker exec --user www-data nextcloud php occ config:system:set trusted_domains 1 --value="cloud.TU_DOMINIO.duckdns.org"

# Añadir la IP local
docker exec --user www-data nextcloud php occ config:system:set trusted_domains 2 --value="TU_IP_NAS"

# Forzar HTTPS
docker exec --user www-data nextcloud php occ config:system:set overwriteprotocol --value="https"

# Reiniciar
docker restart nextcloud
```

> 💡 **El Bypass del Router (Archivo Hosts en Windows):**
> A veces el dominio no se ve desde dentro de casa porque el Router intercepta la comunicación (falta de NAT Loopback). Editamos el archivo de Windows:
> - **Ruta:** `C:\Windows\System32\drivers\etc\hosts`
> - **Línea añadida:** `TU_IP_NAS cloud.TU_DOMINIO.duckdns.org`
> (Esto permite que tu PC vaya directo al NAS sin pasar por el filtro del router).

---

## Pruebas, Solución de Problemas y Conexión

### Test desde fuera

1. Coge tu móvil → **desactiva el WiFi** (usa solo datos)
2. Abre el navegador:
   - `https://jellyfin.TU_DOMINIO.duckdns.org` → ¿Carga con candado HTTPS? ✅
   - `https://cloud.TU_DOMINIO.duckdns.org` → ¿Carga con candado HTTPS? ✅

### Configurar apps del móvil

**Jellyfin app:**
1. Play Store → "Jellyfin" → instalar
2. Servidor: `https://jellyfin.TU_DOMINIO.duckdns.org`
3. Login con tu usuario de Jellyfin

**Nextcloud app:**
1. Play Store → "Nextcloud" → instalar
2. Servidor: `https://cloud.TU_DOMINIO.duckdns.org`
3. Login con tu usuario de Nextcloud
4. Ajustes → Subida automática → Activar

### Resolución de Errores Comunes

| Error | Causa Probable | Solución |
|---|---|---|
| **403 Forbidden** | Error en Nginx Proxy Manager | Cambia el **Forward Port** a `80` (no el 8082). |
| **Página del Router** | Falta de NAT Loopback | Prueba con datos móviles fuera de la red Wi-Fi local. O usa el Bypass del archivo Hosts en Windows. |
| **Certificado no válido** | SSL mal configurado en NPM | Edita el Proxy Host y marca **Force SSL** y **HTTP/2 Support**. |
| **SSH no conecta** | VPN activa o usuario sin grupo `_ssh` | Cerrar VPN o activar "LAN sharing". Verificar grupo `_ssh` en Usuarios. |
| **Contraseña OMV no funciona** | Cuenta bloqueada | SSH → `su -` → `omv-firstaid` → opción 5 + opción 4 |
| **Error cpupower** | Falta paquete | `sudo apt-get install linux-cpupower && sudo omv-salt deploy run cpupower` |
| **Discos del dock no aparecen** | OMV no muestra discos USB | Crear mirror por SSH con `mdadm` |
| **FileBrowser da 403** | Permisos incorrectos | `sudo chown -R 1000:100 /srv/dev-disk-by-uuid-TU_UUID/appdata/` |
| **WARNING: REMOTE HOST** | Clave SSH cambió | `ssh-keygen -R TU_IP_NAS` |

---

## Resúmenes y Credenciales

### Resumen de URLs

**Dentro de casa:**

| Servicio | URL |
|---|---|
| Panel OMV | `http://TU_IP_NAS:8888` |
| FileBrowser | `http://TU_IP_NAS:8080` |
| Jellyfin | `http://TU_IP_NAS:8096` |
| Nextcloud | `http://TU_IP_NAS:8082` |
| Nginx Proxy Manager | `http://TU_IP_NAS:81` |
| Carpetas Windows | `\\TU_IP_NAS` |
| SSH | `ssh TU_USUARIO@TU_IP_NAS` |

**Desde fuera:**

| Servicio | URL |
|---|---|
| Jellyfin | `https://jellyfin.TU_DOMINIO.duckdns.org` |
| Nextcloud | `https://cloud.TU_DOMINIO.duckdns.org` |

> ⚠️ **SEGURIDAD:** Panel OMV, FileBrowser y Nginx Proxy Manager **NUNCA** accesibles desde fuera.


---

### Software utilizado (todo gratuito)

- Debian 13 (Trixie): https://www.debian.org
- OpenMediaVault 8: https://www.openmediavault.org
- Jellyfin: https://jellyfin.org
- Nextcloud: https://nextcloud.com
- Nginx Proxy Manager: https://nginxproxymanager.com
- DuckDNS: https://www.duckdns.org
- FileBrowser: https://filebrowser.org
- Balena Etcher: https://etcher.balena.io