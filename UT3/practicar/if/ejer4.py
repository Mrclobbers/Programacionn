#Crea un programa que pida al usuario dos números y muestre su división
#si el segundo no es cero o un mensaje de aviso en caso contrario
num1 = float(input("Pon el primer numero: "))
num2 = float(input("Pon el segundo numero: "))

if num2 == 0:
    print("No se puede dividir")

else:
    print(f"Resultado de la division: {num1 / num2}")

