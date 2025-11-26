#Recorre el directorio actual y suma el tamaño (en bytes) de todos los ficheros .log.

#Muestra la suma y, si es mayor o igual que 1 MB, imprime ALTO VOLUMEN, si no, imprime OK.

#Librerías: from pathlib import Path
from pathlib import Path

contador = 0
suma = 0

directorio_actual  = Path.cwd()

for f in directorio_actual.iterdir():
    if f.is_file():
        if str(f.name).endswith(".log"):
            contador += 1
            suma += f.stat().st_size

print(suma)
if suma >= 1_048_576:
    print("ALTO VOLUMEN")
else:
    print("OK")
print(f"Hay {contador} ficheros .log")
