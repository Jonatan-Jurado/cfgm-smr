import os
import re
import unicodedata

def simple_slug(text):
    # Pasamos a minúsculas, quitamos acentos y ponemos guiones
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower().replace(" ", "-")
    # Quitamos cualquier cosa que no sea letra, número o guion
    text = re.sub(r'[^a-z0-9-]', '', text)
    return text

# CONFIGURACIÓN: Pon aquí la ruta a tu archivo de índice
ruta_indice = "./content/CFGM/Glosario/index.md" 

if os.path.exists(ruta_indice):
    with open(ruta_indice, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Buscamos [[Cualquier Cosa]] y lo cambiamos por [[cualquier-cosa|Cualquier Cosa]]
    def arreglar(match):
        original = match.group(1)
        if "|" in original:
            # Si ya tiene alias, arreglamos solo la parte de la izquierda (el destino)
            destino, alias = original.split("|", 1)
            return f"[[{simple_slug(destino)}|{alias}]]"
        return f"[[{simple_slug(original)}|{original}]]"

    nuevo_contenido = re.sub(r'\[\[(.*?)\]\]', arreglar, contenido)

    with open(ruta_indice, 'w', encoding='utf-8') as f:
        f.write(nuevo_contenido)
    print("✅ ¡Índice del glosario reparado!")
else:
    print("❌ No encuentro el archivo index.md en esa ruta.")