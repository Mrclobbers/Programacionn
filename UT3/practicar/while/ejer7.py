base = float(input("Introduce una base: "))
exponente = int(input("Introduce un exponente: "))

while exponente < 0:
    exponente = int(input("Introduce un exponente: "))
if exponente >= 0:
    potencia = base ** exponente
    print(f"Resultado: {potencia}")