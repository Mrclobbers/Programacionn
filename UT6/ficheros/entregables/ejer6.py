# Pide al usuario un nombre de usuario (por ejemplo rafa) 
# y guarda en users.txt el nombre y su ruta HOME estimada (en Linux /home/<usuario>) usando pathlib.
# El formato de cada línea debería ser: nombre,ruta. Si el usuario ya estaba, no lo repitas.
from pathlib import Path

usuario = Path(input("Pon un usuario: "))
home = Path(f"/home/{usuario}")
ruta = Path("users.txt")
usuarios_creados = {}

if ruta.exists():
    with open("users.txt", "r") as f:
        for linea in f:
            partes = linea.split(",", 1)
            if len(partes) >= 1:
                usuarios_creados[partes[0].strip()] = partes[1].strip()

if usuario not in usuarios_creados:
    print("Usuario creado")
    with open("users.txt", "a") as f:
        f.write(f"{usuario},{home}\n")
else:
    print("Ya creado")