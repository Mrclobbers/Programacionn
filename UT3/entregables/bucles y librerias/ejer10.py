# Pide por teclado nombres de archivos de backup hasta que el usuario introduzca FIN.

# Cuenta cuántos terminan en .zip y cuántos en .tar.gz o .tgz y muéstralo al final.

# Cuenta también los archivos introducidos con cualquier otra extensión.

# Librerías: from pathlib import Path
from pathlib import Path

zip_count = 0
tar_count = 0
otros_count = 0

while True:
    nombre = input("Archivo (FIN para terminar): ")
    if nombre == "FIN":
        break
    p = Path(nombre)

    if str(p.name).endswith(".tar.gz") or str(p.name).endswith(".tgz"):
        tar_count = tar_count + 1
    elif str(p.name).endswith(".zip"):
        zip_count = zip_count + 1
    else:
        otros_count += 1

print("ZIP:", zip_count)
print("TAR.GZ:", tar_count)
print("OTROS:", otros_count)


