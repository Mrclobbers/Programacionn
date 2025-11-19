#Escribe un programa que cada vez que se ejecute pida por teclado dos números, uno
#de ellos que represente el peso de una persona (entre 50 y 100 kilos) y el otro la altura
#(entre 1.50 y 2.00 metros) y que escriba el IMC (Índice de Masa Corporal)
#correspondiente, redondeado con un decimal. Se recuerda que el IMC se calcula con
#la fórmula IMC = peso / altura2.

peso = float(input("Pon tu peso: "))
altura = float(input("Pon tu altura: "))

IMC = (peso / altura ** 2)
IMC2 = round(IMC, 2)

print(f"Tu IMC es: {IMC2}")