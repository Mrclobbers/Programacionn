# Crea commands.txt con comandos típicos (texto). Por ejemplo ls -la, df -h, uname -a, etc. 
# Luego lee el fichero y genera commands_numbered.txt numerando cada línea (usa enumerate).
comandos = [
    "ls -la",
    "df -h",
    "uname -a",
]
lista = []

with open("commands.txt", "a") as f:
    for linea in comandos:
        f.write(f"{linea} \n")

with open("commands.txt", "r") as d:
    for lineas_no, lineas in enumerate(d, start=1):
        lista.append(f"{lineas_no} : {lineas.strip()}")
        print(lista)

with open("commands_numbered.txt", "a") as g:
    for i in lista:
        g.write(f"{i} \n")