#Dado el texto ' pc -- aula - 07 \n' debes convertirlo a 'PC-AULA-07' sin usar condicionales ni bucles. Imprime el resultado.
cad_vieja =' pc -- aula - 07 \n'
cad = cad_vieja.replace('--', '-')
cad2 = cad.replace(' ', '')
cad2 = cad2.upper()
cad2 = cad2.strip()
print(cad2)