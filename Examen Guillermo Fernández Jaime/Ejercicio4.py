#Vamos a crear una contraseña segura a partir de un texto. Escribe un programa que
#pida una contraseña por teclado. La contraseña debe ser una frase que solo contenga
#letras minúsculas y espacios. Por ejemplo, “mi clave segura”. Realiza las siguientes tareas:ç

#1. Convierte la cadena a formato título (la primera inicial de cada palabra enmayúscula)
#2. Sustituye los espacios por guiones bajos (caracter _) y la ‘a’ por el número 4.
#3. Añade el carácter ‘$’ al inicio y al final
#4. Busca la posición del primer carácter ‘_’, extrae la subcadena desde el siguiente
#carácter a ‘_’ hasta el final y añade esa subcadena al principio de la contraseña.
#Imprime el resultado. En el ejemplo del ejercicio, el resultado sería: Cl4ve_Segur4$$Mi_Cl4ve_Segur4$
contraseña = input("Pon una frase para crear tu contraseña: ")

mayus = contraseña.title()

guion_a = mayus.replace(' ', '_').replace('a', '4')

guion_aa = '$' + guion_a + '$'

pos = guion_aa.find('_')
res = guion_aa[pos + 1:]

pos2 = res.find('$')
carcater = res[:pos2 +1]

print(carcater + guion_aa)