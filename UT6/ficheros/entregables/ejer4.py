# Crea paths.txt con varias rutas (una por línea). 
# Luego lee el fichero y crea paths_status.txt 
# indicando para cada ruta si existe y si es archivo o directorio (usa pathlib). 
# En concreto, los estados pueden ser: Directorio, Archivo, Otro, No Existe. 
# El formato de cada línea debería ser: ruta -> estado
from pathlib import Path

lista = []

rutas = ["/", "/home", "/var", "/python"]

with open("paths.txt", "w", encoding="utf-8") as f:
    for ruta in rutas:
        f.write(ruta + "\n")

with open("paths.txt", "r", encoding="utf-8") as f:
    for linea in f:
        r = linea.strip()
        path = Path(r)

        if path.exists():
            if path.is_dir():
                estado = "Directorio"
            elif path.is_file():
                estado = "Archivo"
            else:
                estado = "Otro"
        else:
            estado = "No existe"

        lista.append(f"{r} -> {estado}")

with open("paths_status.txt", "w", encoding="utf-8") as f:
    for linea in lista:
        f.write(linea + "\n")

