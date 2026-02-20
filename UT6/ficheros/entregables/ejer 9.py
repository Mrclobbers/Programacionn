# Crea cleanup_plan.txt con una lista de carpetas temporales (una por línea). 
# Por ejemplo, /tmp, /var/tmp, /noexiste, etc. 
# Genera cleanup_report.txt indicando cuáles existen y cuántos elementos contienen (usa pathlib.iterdir() y recuento). 
# Cada línea debería tener el siguiente formato: ruta -> existe -> elementos: 3 o ruta -> NO existe.
from pathlib import Path

comandos = [
    "/tmp",
    "/var/tmp",
    "/noexiste",
]
lista = []

with open("cleanup_plan.txt", "a") as f:
    for linea in comandos:
        f.write(f"{linea} \n")

with open("cleanup_plan.txt", "r") as d:
    for linea in d:
        ruta = Path(linea.strip())

        if ruta.exists() and ruta.is_dir():
            cantidad = 0
            for elem in ruta.iterdir():
                cantidad+=1
            lista.append(f"{ruta} -> existe -> elementos: {cantidad}")     
                
        else:
            lista.append(f"{ruta} -> NO existe")

with open("cleanup_report.txt", "a") as g:
    for a in lista:
        g.write(f"{a} \n")