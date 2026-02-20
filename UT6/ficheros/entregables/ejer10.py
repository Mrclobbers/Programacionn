# Programa que recibe por sys.argv el nombre de un fichero de texto.
# Debe imprimir el número de líneas, palabras y caracteres del fichero (si no existe, mostrar un error amigable).
import sys
from pathlib import Path

ruta = Path(sys.argv[1])

if not ruta.exists():
    print(f"La ruta {ruta} no existe")

else:
    texto = ruta.read_text()
    num_lineas = len(texto.splitlines())
    num_palabras = len(texto.split())
    num_caracteres = len(texto)

    print(num_caracteres)
    print(num_palabras)
    print(num_lineas)