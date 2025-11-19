# #Pistas: sys.argv

# Dado un hostname (que se pide como argumento), muestra:

# “VÁLIDO” si empieza por “PC-“ y su longitud es al menos 7
# “NO VÁLIDO” en caso contrari

import sys
if len(sys.argv) >= 2:
    hostname = sys.argv[1]
    hostname = str(hostname)

    if hostname.startswith('PC-') == True and len(hostname) >=7:
        print("Tu hostname es VALIDO")
    else:
        print("Tu hostname es NO VALIDO")
else:
    print("No pusiste ningun valor")