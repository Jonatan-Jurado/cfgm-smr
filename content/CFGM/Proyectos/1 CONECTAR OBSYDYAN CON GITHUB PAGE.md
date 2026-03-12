#  # 📓 Publica tus notas de Obsidian gratis con Quartz y GitHub Pages

> **¿Qué vamos a hacer?** Convertir tus notas de Obsidian en una página web accesible desde cualquier navegador, alojada gratis en GitHub Pages. La URL final será algo como: `https://tunombre.github.io/my-notes`

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/IB20eEAC3Tw?si=M9H0AgW_qanvDDmn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 🧠 Entiende esto antes de empezar

Antes de tocar nada, aquí van cinco conceptos clave explicados sin tecnicismos:

| Concepto           | Analogía del mundo real                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| **Git**            | Es como el historial de versiones de Word, pero para carpetas enteras. Guarda cada cambio que haces. |
| **GitHub**         | Es como Google Drive pero para código. Guarda tu proyecto en internet.                               |
| **GitHub Pages**   | Es el servicio de GitHub que coge tu carpeta y la publica como una web. Gratis.                      |
| **Quartz**         | Es la herramienta que convierte tus notas Markdown en una web bonita.                                |
| **GitHub Actions** | Son instrucciones automáticas que le dices a GitHub: "cada vez que suba algo, haz esto".             |
| **localhost**      | Tu ordenador haciendo de servidor web. Te permite ver el resultado final ANTES de publicarlo.        |

---

## ✅ Requisitos previos

Antes de empezar, necesitas tener instalado esto en tu ordenador. Abre **PowerShell** o **cmd**  y verifica cada uno:

| Programa | Comando para verificar | Versión mínima  |
| -------- | ---------------------- | --------------- |
| Node.js  | `node -v`              | v18 o superior  |
| NPM      | `npm -v`               | v9.3 o superior |
| Git      | `git --version`        | cualquiera      |
| Obsidian | ábrelo y funciona      | cualquiera      |
| VS Code  | `code --version`       | cualquiera      |

> 💡 **¿Cómo abro PowerShell en Windows?** Pulsa `Windows + R`, escribe `powershell` y dale a Enter.

Si alguno no está instalado, descárgalo desde su web oficial antes de continuar.

---

## PASO 1 — Descargar e instalar Quartz (zona de pruebas)

### 1.1 Clonar el repositorio

> 🧠 **¿Qué significa "clonar"?** Imagina que Quartz es un proyecto que alguien tiene en Google Drive. Clonar es como hacer una copia de esa carpeta en tu propio ordenador.

Abre PowerShell y ejecuta:

```
git clone https://github.com/jackyzha0/quartz.git my-notes-borrador
```

> 💡 Fíjate que clonamos en una carpeta llamada `my-notes-borrador`. Esta será tu **zona de pruebas**, donde escribes y experimentas libremente. La carpeta definitiva que se publicará la crearemos más adelante, una vez que todo esté a tu gusto.

### 1.2 Entrar en la carpeta

```
cd my-notes-borrador
```

> 🧠 `cd` significa "change directory" (cambiar de carpeta). A partir de ahora todos los comandos se ejecutan desde dentro de `my-notes-borrador`.

### 1.3 Instalar dependencias

```
npm i
```

> 🧠 Quartz necesita otras herramientas para funcionar. Este comando las descarga todas automáticamente leyendo una lista que ya viene incluida. Puede tardar 1-2 minutos.

### 1.4 Inicializar tu proyecto

```
npx quartz create
```

Te hará dos preguntas. Responde así:

**Pregunta 1:** _"How do you want to initialize your content?"_ → Elige **`Empty Quartz`** (empezamos desde cero)

**Pregunta 2:** _"How do you want Quartz to resolve links?"_ → Elige **`Treat links as shortest path`** (es como funciona Obsidian por defecto)

---

## PASO 2 — Abrir la zona de pruebas en Obsidian y crear contenido

1. Abre Obsidian → **"Open folder as vault"**
2. Selecciona tu carpeta `my-notes-borrador`
3. Crea tus notas normalmente

> 💡 Cada nota debe empezar con este bloque para que Quartz la procese bien:
>  ```
> title: "Título de tu nota"
> draft: false
> tags:
> ```
> 
> Si pones `draft: true`, la nota existe en Obsidian pero **no se publica**.

---

## PASO 3 — Comprobar en local antes de publicar nada

> 🧠 Antes de subir nada a internet, **SIEMPRE** comprueba que todo se ve bien en tu ordenador. Es como revisar un documento antes de enviarlo. Así evitas publicar errores o contenido a medias.

Desde PowerShell, dentro de `my-notes-borrador`:

```
npx quartz build --serve
```

Abre el navegador y ve a `http://localhost:8080`. Verás tu web exactamente como quedará en internet.

- ✅ Si todo se ve bien → para el servidor con `Ctrl + C` y continúa al Paso 4
- ❌ Si algo falla → corrígelo en Obsidian y vuelve a ejecutar el comando

> 💡 Puedes repetir este paso tantas veces como quieras mientras experimentas. Nadie verá nada hasta que tú decidas publicarlo.

---

## PASO 4 — Crear la carpeta definitiva y copiar el contenido

Una vez que estés satisfecho con cómo se ve tu web en local, es el momento de preparar la carpeta que se publicará en internet.

### 4.1 Clonar Quartz en la carpeta definitiva

Abre PowerShell en la carpeta donde tienes `my-notes-borrador` y ejecuta:

```
git clone https://github.com/jackyzha0/quartz.git my-notes
cd my-notes
npm i
npx quartz create
```

Responde las mismas preguntas que antes:

- `Empty Quartz`
- `Treat links as shortest path`

Ahora tendrás esta estructura:

```
📁 my-notes-borrador   ← aquí escribes y experimentas
📁 my-notes            ← la carpeta oficial que se publicará
```

### 4.2 Copiar el contenido a la carpeta definitiva

Copia la carpeta `content` de `my-notes-borrador` a `my-notes`, reemplazando la que ya existe.

> 💡 A partir de ahora, el flujo será siempre: escribes en `my-notes-borrador`, compruebas en localhost, y cuando esté listo copias el `content` a `my-notes` para publicar.

---

## PASO 5 — Crear el repositorio en GitHub

> 🧠 **¿Por qué necesitamos GitHub?** Tu ordenador tiene el proyecto, pero para publicarlo en internet necesitas subirlo a un servidor. GitHub es ese servidor, y es gratis.

### 5.1 Crear tu cuenta y repositorio

1. Ve a [github.com](https://github.com/) y crea una cuenta gratuita si no tienes una.
2. Haz clic en el botón verde **"New"** para crear un nuevo repositorio.
3. En **"Repository name"** escribe: `my-notes`.
4. ⚠️ **MUY IMPORTANTE:** NO marques la opción _"Add a README file"_. Déjalo vacío.
5. Haz clic en **"Create repository"**.

> ⚠️ **Error frecuente:** Si marcas "Add a README", GitHub tendrá un archivo que tu ordenador no tiene. Cuando intentes sincronizar, dará error de conflicto.

### 5.2 Cambiar el "origin" (redirigir tu proyecto a TU repositorio)

> 🧠 **¿Qué es el "origin"?** Cuando clonaste Quartz, tu proyecto apunta al repositorio del creador de Quartz (jackyzha0). Es como si tu GPS tuviera guardada la dirección de otra persona. Ahora hay que cambiarla por la tuya.

Desde PowerShell, dentro de `my-notes`:

```
cd my-notes
git remote -v
```

Verás que `origin` apunta a `github.com/jackyzha0/quartz.git`. Elimínalo:

```
git remote rm origin
```

Ahora añade TU repositorio (sustituye `tunombre` por tu usuario de GitHub):

```
git remote add origin https://github.com/tunombre/my-notes.git
git remote -v
```

Ahora `origin` debe apuntar a tu repositorio. El `upstream` seguirá apuntando al original de Quartz — eso está bien, sirve para recibir actualizaciones futuras.

### 5.3 Primera subida

```
npx quartz sync --no-pull
```

> 🧠 El `--no-pull` significa "sube mis archivos sin intentar descargar nada primero". Lo usamos solo esta primera vez porque el repositorio remoto está vacío y no hay nada que descargar.

✅ **Verifica que funcionó:** Ve a `github.com/tunombre/my-notes` y recarga. Deberías ver todos los archivos de Quartz ahí.

---

## PASO 6 — Configurar el archivo de despliegue automático

> 🧠 Este archivo le dice a GitHub: "cada vez que alguien suba cambios, construye la web y publícala". Sin esto no se publica nada automáticamente.

### 6.1 Reemplazar el archivo deploy

Dentro de `my-notes`, ve a `.github/workflows/`.

> ⚠️ En Windows las carpetas que empiezan por punto están ocultas. En el Explorador de archivos ve a **Ver → marca "Elementos ocultos"**.

Verás un archivo llamado `deploy_preview.yaml`. **Renómbralo** a `deploy.yaml`, ábrelo con el Bloc de notas, **borra todo** y pega esto:

```yaml
name: Deploy Quartz to GitHub Pages

on:
  push:
    branches:
      - v4

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22

      - name: Install Dependencies
        run: npm ci

      - name: Build Quartz
        run: npx quartz build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: public

  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 6.2 Verificar la versión de Node

En la carpeta raíz de `my-notes` hay un archivo llamado `.node-version`. Ábrelo y asegúrate de que el número sea `22`. Si no, cámbialo y guarda.

### 6.3 Dar permisos de escritura a GitHub Actions

1. Ve a tu repositorio en GitHub → **Settings → Actions → General**
2. Baja al final de la página
3. Selecciona **"Read and write permissions"**
4. Haz clic en **Save**

---

## PASO 7 — Activar GitHub Pages y publicar

### 7.1 Activar GitHub Pages

> ⚠️ Este paso es imprescindible ANTES de sincronizar. Si no lo haces, el Action fallará con un error "Not Found 404".

1. Ve a tu repositorio en GitHub → **Settings → Pages**
2. En **Source** selecciona **"GitHub Actions"** (no "Deploy from a branch")
3. Guarda

### 7.2 Publicar en internet

Desde PowerShell, dentro de `my-notes`:

```
npx quartz sync
```

Ve a la pestaña **Actions** en GitHub. Verás el proceso (🟡 mientras construye, ✅ cuando termina). En 2-3 minutos tu web estará en:

```
https://tunombre.github.io/my-notes
```

---

## 🔄 Flujo de trabajo diario

Una vez configurado todo, este es el proceso que seguirás **siempre**:

```
✏️  Escribir en Obsidian (my-notes-borrador)
        ↓
👁️  Revisar en local
        cd my-notes-borrador
        npx quartz build --serve
        http://localhost:8080
        ↓
✅  ¿Se ve bien? → Ctrl+C para parar el servidor
        ↓
📋  Copiar carpeta content de my-notes-borrador → my-notes
        ↓
🚀  Publicar
        cd my-notes
        npx quartz sync
        ↓
🌐  En 2-3 minutos está en internet
```

> 💡 `npx quartz sync` solo funciona si hay cambios nuevos. Si no has tocado nada, Git no subirá nada y el Action no se disparará. Para forzarlo: GitHub → Actions → "Deploy Quartz to GitHub Pages" → **"Run workflow"**.

---

## 🛡️ Copia de seguridad

Git guarda historial, pero tener una copia extra nunca hace daño. Copia la carpeta `content` a Google Drive, OneDrive o un disco externo de vez en cuando.

> ⚠️ Más de una vez se han perdido archivos por no tener respaldo. No esperes a aprenderlo por las malas.

---

## ⏱️ Sincronización automática (opcional)

Si quieres que `my-notes` se sincronice solo cada día sin abrir la terminal:

**1. Crea el script:** Abre el Bloc de notas, pega esto y guárdalo como `sync-quartz.bat` (tipo: "Todos los archivos"):

```bat
@echo off
cd TU_RUTA
npx quartz sync
```

Sustituye `TU_RUTA` por la ruta de tu carpeta `my-notes`, por ejemplo: `C:\Users\TuNombre\Documents\my-notes`

**2. Prográmalo en Windows:**

1. `Windows + R` → `taskschd.msc` → Enter
2. **"Crear tarea básica"**
3. Nombre: `Sync Quartz` · Frecuencia: Diariamente · Hora: 23:00
4. Acción: Iniciar un programa → ruta de tu `.bat`
5. Finalizar

> ⚠️ El PC debe estar encendido a esa hora. Si está apagado, se ejecutará la próxima vez que lo enciendas.

---

## 🛠️ Errores frecuentes

### ❌ "Not Found 404" al hacer el deploy

**Causa:** GitHub Pages no está activado. **Solución:** Settings → Pages → Source → "GitHub Actions". Luego sincroniza o lanza el workflow manualmente.

### ❌ "Everything up-to-date" y el Action no se dispara

**Causa:** No hay cambios nuevos, Git no hace nada. **Solución:** GitHub → Actions → "Deploy Quartz to GitHub Pages" → "Run workflow".

### ❌ "remote rejected" o "rejected push"

**Causa:** El repositorio de GitHub tiene algo que tu ordenador no tiene (ej: marcaste "Add a README"). **Solución:**

```
git pull origin main --allow-unrelated-histories
npx quartz sync
```

### ❌ "Authentication failed"

**Causa:** GitHub ya no acepta usuario y contraseña. **Solución:** Crea un Personal Access Token en GitHub → Settings → Developer Settings → Personal Access Tokens → Generate new token (permisos: `repo`). Úsalo como contraseña.

### ❌ El deploy.yaml tiene contenido de "Cloudflare" o "Upload Preview"

**Causa:** Es el archivo original de Quartz para sus propios previews. **Solución:** Borra todo y pega el YAML del Paso 6 de esta guía.

---

## 📋 Referencia rápida de comandos

| Comando                                 | Cuándo usarlo                                           |
| --------------------------------------- | ------------------------------------------------------- |
| `npx quartz sync --no-pull`             | Solo la **primera vez** que sincronizas                 |
| `npx quartz build --serve`              | **Siempre** antes de sincronizar, para revisar en local |
| `npx quartz sync`                       | Para publicar cambios en internet                       |
| `git remote -v`                         | Ver a qué repositorio apunta tu proyecto                |
| `git remote rm origin`                  | Desconectar del repositorio actual                      |
| `git remote add origin URL`             | Conectar a tu repositorio                               |
| `git log --oneline`                     | Ver el historial de cambios                             |
| `git checkout CODIGO -- "ruta/archivo"` | Recuperar un archivo de una versión anterior            |
