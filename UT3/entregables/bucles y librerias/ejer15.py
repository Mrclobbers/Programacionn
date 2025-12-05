# Pide el número de aulas (A) y el número de PCs por aula (P).

# Las carpetas esperadas en el sistema son (es decir, ya deben existir en el sistema, no las creamos):

# AULA-01/PC-01, AULA-01/PC-02, ..., AULA-0A/PC-0P

# Recorre la estructura de carpetas anterior y, para cada PC, si la carpeta existe, cuenta cuántos archivos .log hay dentro.

# Muestra para cada aula el total de .log encontrados y el total general al final.

# Librerías: from pathlib import Path
from pathlib import Path
total_general = 0
total_carpeta = 0
aulas = int(input("Pon el numero de aulas: "))
pc = int(input("Pon el numero de PCs: "))

base = Path.cwd()

for i in range(1,aulas + 1):
    aula_nombre = "AULA-" + str(i).zfill(2)
    aula_dir = base / aula_nombre

    for x in range(1, pc + 1):
        pc_nombre = "PC-" + str(x).zfill(2)
        pc_dir = aula_dir / pc_nombre

        if pc_dir.is_dir():
            for f in pc_dir.iterdir():
                if str(f).endswith(".log"):
                    total_general +=1
                    total_carpeta +=1
            print(f"Carpeta: {total_carpeta}")
            total_carpeta = 0
print(f"general: {total_general}")




   


