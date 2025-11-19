inferior = int(input("Introduce un limite inferior: "))
superior = int(input("Introduce un limite superior: "))
num = int(input("Pide numero: "))

cont_suma = 0            
cont_limites = 0
cont_fuera = 0

while inferior > superior:
    inferior = int(input("Introduce un limite inferior: "))

while num != 0:
    if num > inferior and num < superior:
        cont_suma += num
    elif num == inferior or num == superior:
        cont_limites += 1
    else:
        num = int(input("Pide numero: "))
        cont_fuera +=1
print(f"Sumas de los intervalos: {cont_suma}, Numeros iguales a los limites: {cont_limites}, Numeros fuera del limite: {cont_fuera}")