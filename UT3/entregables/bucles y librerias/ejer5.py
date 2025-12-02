# Pide por teclado un umbral de uso de disco (entre 0 y 100).

# Si no es válido, vuelve a pedirlo (máximo 3 intentos).

# A continuación, muestra el porcentaje real de uso de la raíz / y dí si supera o no el umbral.

# Librerías: import shutil

import shutil

contador = 0

num = int(input("Pon un umbral de disco de 0 a 100: "))

for umbral in range(0,100):
    if num < 0 and num > 100:
        print("Fuera de rango, pide otro numero")
else:
    total, usado, libre = shutil.disk_usage("/")
    porcentaje = (usado * 100 / total)
    if num > porcentaje:
        print("Supera el umbral")
    else:
        print("No supera el umbral")