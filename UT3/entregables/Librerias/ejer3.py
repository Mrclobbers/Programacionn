import platform

print("Sistema operativo: ", platform.system())
print("Versión: ", platform.release())
print("Procesador: ", platform.processor())

if platform.system() == "Windows":
    print("Gestor de paquetes recoemdado: winget")

elif platform.system() == "Linux":
    print("Gestor de paquetes recoemdado: apt")

elif platform.system() == "macOS":
    print("Gestor de paquetes recoemdado: brew")

else:
    print("Gestor no definido")