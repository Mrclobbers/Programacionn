# Un administrador de sistemas quiere automatizar la instalación de paquetes con un comando tipo:
# apt install paquete1 paquete2 paquete3.
# Crea una lista con varios nombres de paquetes,
# por ejemplo, ["vim", "curl", "htop"],
# simula que el usuario añade uno más por teclado,
# y construye la cadena completa del comando apt install ... a partir de la lista.
paquetes = ["vim", "curl", "htop"]
nuevo_paquete = input('Pon un paquete mas: ')
nuevo_paquete.lower()

if nuevo_paquete not in paquetes:
    paquetes.append(nuevo_paquete)

paquetes = ' '.join(paquetes)

print(f'apt install {paquetes}')