num1 = int(input("Introduce el número 1: "))
num2 = int(input("Introduce el número 2: "))

if num1 % 2 != 0:
    num1 += 1

while num1 <= num2:
    print(f"{num1}")
    num1+=2