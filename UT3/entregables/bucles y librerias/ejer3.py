#Pide mediante un bucle while hostnames al usuario hasta que escriba FIN.

#Cuenta cuántos has introducido y muestra el total al final.

#No uses listas; solo un contador y cadenas

contador = 0
hostname = str(input("Pon uns hostname: "))

while hostname != "FIN":
    hostname = str(input("Pon otro hostname: "))
    contador += 1

print(f"Introduciste {contador} hostnames antes de poner FIN")