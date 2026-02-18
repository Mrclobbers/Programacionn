# Lee admin_log.txt y muestra cuántas líneas contiene y cuál es la última línea (si existe).
from pathlib import Path

ruta = Path("admin_log.txt")

if ruta.exists():
    with open(ruta, "r") as f:
        lineas = f.readlines()
        print(len(lineas))

        ultima_linea = lineas[-1]
        print(ultima_linea)
else:
    print("Error, no existe")


