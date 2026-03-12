import os
import re
import unicodedata

def slugify(text):
    # Esta función debe hacer EXACTAMENTE lo mismo que el script anterior
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower().replace(" ", "-")
    text = re.sub(r'[^a-z0-9-]', '', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text

def corregir_contenido(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Buscar enlaces tipo [[Texto]] o [[Texto|Alias]]
    def reemplazar_enlace(match):
        enlace_completo = match.group(1)
        if '|' in enlace_completo:
            nombre_archivo, alias = enlace_completo.split('|', 1)
            return f"[[{slugify(nombre_archivo)}|{alias}]]"
        else:
            # Mantenemos el nombre original como Alias para que visualmente no cambie la wiki
            return f"[[{slugify(enlace_completo)}|{enlace_completo}]]"

    nuevo_contenido = re.sub(r'\[\[(.*?)\]\]', reemplazar_enlace, contenido)
    
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        f.write(nuevo_contenido)

# Ruta a TODA tu carpeta content (para que arregle el glosario y las notas que apuntan al glosario)
ruta_content = "./content/media"

for raiz, dirs, archivos in os.walk(ruta_content):
    for nombre in archivos:
        if nombre.endswith('.md'):
            ruta_completa = os.path.join(raiz, nombre)
            corregir_contenido(ruta_completa)
            print(f"Enlaces corregidos en: {nombre}")