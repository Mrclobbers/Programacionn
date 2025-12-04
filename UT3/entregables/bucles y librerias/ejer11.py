# Pide una IP base, por ejemplo ‘192.168.1.’ (debes incluir el punto final), y dos números: 

# inicio y fin del último octeto.

# Muestra por pantalla las IPs con último octeto par entre ese rango (incluidos)
ip = input("Pon una IP base: ")
inicio = int(input("Pon un numero: "))
fin = int(input("Pon un numero: "))

for x in range(inicio, fin + 1):
    if x % 2 == 0:
        print(ip + str(x))