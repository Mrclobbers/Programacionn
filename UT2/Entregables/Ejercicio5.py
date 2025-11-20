#Dado el email 'admin.redes@centro.edu', extrae el usuario (antes de '@')
#El dominio (entre '@' y primer '.')
#Y el tld (después del '.'). No uses bucles.
correo = 'admin.redes@centro.edu'

pos = correo.find('a')
res = correo[pos :]

pos2 = res.find('@')  
usuario = res[: pos2]
res = res[pos2 +1:]

pos3 = res.find('.')
dominio = res[: pos3]
res = res[pos3 + 1:]

pos4 = res.find('u')
tdl = res[: pos4 + 1]



print(f"El usuario es: {usuario}")
print(f"El dominio es: {dominio}")
print(f"El tdl es: {tdl}")