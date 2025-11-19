texto = str(input('Dime un caracter: '))

while len(texto) < 1:
    while texto == '1' or texto == '2' or texto == '3' or texto == '4' or texto == '5' or texto == '6' or texto == '7' or texto == '8' or texto == '9' or texto == '0':
        print('No has escrito un caracter, vuelve a escribirlo.')
        texto = str(input('Dime un caracter: '))
    else:
        while texto != ' ':
            if texto == 'a' or texto == 'e' or texto == 'i' or texto == 'o' or texto == 'u':
                print('VOCAL')
                texto = str(input('Dime otro caracter: '))
            else:
                print('NO VOCAL')
                texto = str(input('Dime un caracter: '))