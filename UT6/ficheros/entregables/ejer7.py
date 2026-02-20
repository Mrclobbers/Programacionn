# Lee users.txt y crea homes_check.txt que indique si la carpeta HOME de cada usuario existe (usa pathlib). 
# El formato de cada línea debería ser: usuario -> home_path -> estado. El estado puede ser OK o No existe.
from pathlib import Path

lista = []
ruta = Path("users.txt")

if not ruta.exists():
    print("No existe")

else:
    with open('users.txt' , 'r') as f: 
        for linea in f:
            usuario, home = linea.strip().split(',',1)
            home_path = Path(home.strip())
            
            if home_path.exists() and home_path.is_dir():
                estado = "OK"
            else:
                estado = "NO existe"
                
                lista.append(f"{usuario.strip()} -> {home_path} -> {estado}")

    with open('homes_check.txt' , 'w') as f:
        for linea in lista:
            f.write(f'{linea}\n')