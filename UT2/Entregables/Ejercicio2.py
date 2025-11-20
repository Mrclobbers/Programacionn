#Dada la etiqueta 'PC-AULA-23', verifica si empieza por 'PC-' (solo muestra True o False) y extrae 'AULA' y '23' usando find
#Y [:] (troceado de cadenas). No uses condicionales; solo imprime las partes obtenidas.
cad = 'PC-AULA-23'
cad1 = cad.startswith('PC-')
pos = cad.find('-')
res = cad[pos + 1:]
pos2 = res.find('-')
aula = res[: pos2]
num = res[pos2 + 1:]
print(cad1)
print(aula)
print(num)