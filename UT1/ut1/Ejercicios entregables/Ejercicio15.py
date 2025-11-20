#Dadas dos variables numéricas A y B, que el usuario debe teclear
#Se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables
A= float(input("El númer A es: "))
B= float(input("El númer B es: "))

aux= A
A= B
B= aux

print(f"El número A invertido es: {A}")
print(f"El número B invertido es: {B}")