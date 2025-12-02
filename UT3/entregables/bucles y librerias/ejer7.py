# Pide al usuario un nombre de archivo hasta que exista en el directorio actual.

# Cuando exista, muestra su tamaño en bytes y termina el programa.

# Librerías: from pathlib import Path
from pathlib import Path

archivo = Path(input("Pon el nombre de un archivo: "))

while not archivo.exists():
    archivo = Path(input("El archivo no existe, pon otro archivo: "))

print("Archivo encontrado:")
print(f"Ruta: {archivo}")
print(f"Información: {archivo.stat()}")