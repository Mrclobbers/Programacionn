# Clasificar archivo según su tamaño

# Pistas: librería sys y librería pathlib

# Pide como argumento un nombre de archivo y averigua su tamaño.
# Si su tamaño es >= 1 MB muestra “GRANDE”,
# en caso contrario “PEQUEÑO”. (1 MB = 1_048_576 bytes)
import sys
from pathlib import Path
import os
if len(sys.argv) >= 2:
    archivo = str(sys.argv[1])
    if Path.exists(archivo):
        peso = os.path.getsize(archivo)
        if peso >= 1:
            print("GRANDE")
        else:
            print("PEQUEÑO")
    else:
        print("El archivo no existe")
   
else:
    print("No se dio un nombre de archivo")