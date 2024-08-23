cadena   = input('Introduzca una cadena de caracteres:  ')
caracter = input('Introduzca el carácter a buscar:      ')

for element in cadena.lower():
    if  element == caracter.lower():
        print(element)