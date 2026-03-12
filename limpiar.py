import os
import unicodedata
import re

def limpiar_nombre(nombre):
    # Separar extensión
    nombre_base, ext = os.path.splitext(nombre)
    if ext != '.md': return nombre
    
    # Normalizar (quitar acentos)
    nombre_base = unicodedata.normalize('NFKD', nombre_base).encode('ascii', 'ignore').decode('ascii')
    # Minúsculas y cambiar espacios por guiones
    nombre_base = nombre_base.lower().replace(" ", "-")
    # Quitar cualquier cosa que no sea letras, números o guiones
    nombre_base = re.sub(r'[^a-z0-9-]', '', nombre_base)
    # Evitar guiones dobles
    nombre_base = re.sub(r'-+', '-', nombre_base).strip('-')
    
    return f"{nombre_base}{ext}"

ruta_glosario = "./content/CFGM/Glosario" # Ajusta esta ruta a tu carpeta real

for archivo in os.listdir(ruta_glosario):
    nuevo_nombre = limpiar_nombre(archivo)
    if nuevo_nombre != archivo:
        print(f"Renombrando: {archivo} -> {nuevo_nombre}")
        os.rename(os.path.join(ruta_glosario, archivo), os.path.join(ruta_glosario, nuevo_nombre))