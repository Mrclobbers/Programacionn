#Dada la IP ' 192.168.001.010 ': limpia bordes, cuenta puntos
#Extrae el primer octeto (hasta primer '.') y último octeto (desde último '.'). Imprime estos 2 octetos.
IP = ' 192.168.001.010 '
IP = IP.strip()

IP2 = IP.count('.')

pos = IP.find('1')
res = IP[pos:]

pos2 = res.find('.')  
oct1 = res[:pos2]
res = res[pos2+1:]

pos3 = res.find('.')  
res = res[pos3+1:]

pos4 = res.find('.')  
oct4 = res[pos4+1:]

print(IP)
print(IP2)
print(oct1)
print(oct4)
