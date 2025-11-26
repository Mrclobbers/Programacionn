#Recorre el directorio actual y cuenta cuántos archivos terminan en .log.
#Muestra el total encontrado.
#Librerías: from pathlib import Path
contador = 0

from pathlib import Path
directorio_actual  = Path.cwd()

for f in directorio_actual.iterdir():
    if f.is_file():
        if str(f.name).endswith(".log"):
            contador += 1

print(f"Hay {contador} ficheros .log")