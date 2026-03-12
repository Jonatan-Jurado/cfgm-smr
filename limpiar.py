import os
import unicodedata
import re

def limpiar_nombre(nombre):
    nombre_base, ext = os.path.splitext(nombre)
    if ext != '.md': return None
    # Quitar acentos y normalizar
    nombre_base = unicodedata.normalize('NFKD', nombre_base).encode('ascii', 'ignore').decode('ascii')
    # Minúsculas y guiones
    nombre_base = nombre_base.lower().replace(" ", "-")
    # Limpiar caracteres raros y guiones dobles
    nombre_base = re.sub(r'[^a-z0-9-]', '', nombre_base)
    nombre_base = re.sub(r'-+', '-', nombre_base).strip('-')
    return f"{nombre_base}{ext}"

ruta_glosario = "./content/CFGM/Glosario"

# Listamos todo primero para no marear al sistema de archivos
archivos = os.listdir(ruta_glosario)

for nombre_original in archivos:
    nuevo_nombre = limpiar_nombre(nombre_original)
    
    if nuevo_nombre and nuevo_nombre != nombre_original:
        path_original = os.path.join(ruta_glosario, nombre_original)
        path_nuevo = os.path.join(ruta_glosario, nuevo_nombre)
        
        # Si el archivo de destino YA existe (caso de Archivo VMX vs archivo-vmx)
        if os.path.exists(path_nuevo):
            print(f"🗑️ Duplicado detectado: Borrando {nombre_original} (ya existe {nuevo_nombre})")
            try:
                os.remove(path_original)
            except Exception as e:
                print(f"❌ Error borrando: {e}")
        else:
            # Si no existe, renombramos normal
            try:
                print(f"✅ {nombre_original} -> {nuevo_nombre}")
                os.rename(path_original, path_nuevo)
            except Exception as e:
                print(f"❌ Error renombrando: {e}")

print("\n✨ ¡Proceso finalizado! Revisa tu lista de archivos.")