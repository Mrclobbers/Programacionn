#Dada una ruta como 'C:\\Users\\alumno\\Desktop\\proyecto'
#Extrae: unidad 'C', usuario 'alumno' y carpeta 'Desktop' usando find/index y [:]. Imprime cada uno de los valores.
ruta = 'C:\\Users\\alumno\\Desktop\\proyecto'
unidad = ruta[0]

pos = ruta.find('\\')
res = ruta[pos + 1:]

pos2 = res.find('\\')
res = res[pos2 + 1:]

pos3 = res.find('\\')
user = res[: pos3]
res = res[pos3 + 1:]

pos4 = res.find('\\')
carpeta = res[: pos4]
print(f"User: {user}")
print(f"Carpeta: {carpeta}")
print(f"Unidad: {unidad}")
