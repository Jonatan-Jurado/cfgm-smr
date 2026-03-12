import os
import re

def corregir_imagenes_guiones(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # 1. Buscar ![[Pasted image XXXXX.png]] y convertirlo en ![[Pasted-image-XXXXX.png]]
    # Captura "Pasted image" con espacios y lo cambia por guiones
    def poner_guiones(match):
        enlace = match.group(0) # Esto es ![[Pasted image ... .png]]
        return enlace.replace(" ", "-")

    # Esta regex busca específicamente el formato de imagen de Obsidian
    nuevo_contenido = re.sub(r'\!\[\[Pasted image.*?\.png\]\]', poner_guiones, contenido)

    # 2. Limpieza extra: por si se quedó algún rastro de "media/" o rutas raras
    # Esto asegura que quede limpio: ![[Pasted-image-XXXX.png]]
    nuevo_contenido = re.sub(r'\!\[\[(?:.*?/)?(Pasted-image-.*?\.png)\]\]', r'![[\1]]', nuevo_contenido)

    if contenido != nuevo_contenido:
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            f.write(nuevo_contenido)
        return True
    return False

# IMPORTANTE: La ruta debe ser donde están tus NOTAS (.md), no donde están las fotos
# Porque queremos cambiar el TEXTO de las notas que llaman a las fotos.
ruta_notas = "./content" 

for raiz, dirs, archivos in os.walk(ruta_notas):
    for nombre in archivos:
        if nombre.endswith('.md'):
            ruta_completa = os.path.join(raiz, nombre)
            if corregir_imagenes_guiones(ruta_completa):
                print(f"✅ Imagen corregida en: {nombre}")