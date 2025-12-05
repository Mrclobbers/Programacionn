# Pide una IP base tipo 192.168. (incluye el punto final).

# Pide el rango de subred (tercer octeto) inicio y fin, y el máximo host (último octeto).

# Para cada subred, muestra primero la gateway (x.x.<subred>.1)

# y luego los hosts del 2 al máximo, saltando los múltiplos de 5 (no asignables).
ip_base = input("Pon la base de una IP: ")
ini = int(input("Pon el principio del tercer octeto: "))
fin = int(input("Pon el final del tercer octeto: "))
hosts= int(input("Pon el maximo de hosts: "))

for i in range(ini, fin+1):
    print("Gateway: ",ip_base + str(i) + '.1')
    print("Subred: ",ip_base + str(i) + '.0/24')
    for host in range(2, hosts + 2):
        if host % 5 == 0:
            continue
        print("Host:", ip_base + str(i) + "." + str(host))
