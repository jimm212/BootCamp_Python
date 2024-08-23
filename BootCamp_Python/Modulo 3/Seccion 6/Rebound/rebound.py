''' Rebound Exercise  M°3 S°6 '''
#---------------------------------------------------------------------------------------
# Escribir un programa que analice un número, e indique si es positivo o negativo, y 
# si es par o impar.En caso de ser cero, también indicarlo. Se debe usar la expresión 
# if-elif-else, y no usar subcondiciones; en su lugar, usar condiciones anidadas
#---------------------------------------------------------------------------------------

num = 0

if num > 0:
    if num % 2 == 0:
        print(f'El numero {num} es positivo y par')
    else:
        print(f'El numero {num} es positivo e impar')
elif num < 0:
    if num % 2 == 0:
        print(f'El numero {num} es negativo y par')
    else:
        print(f'El numero {num} es negativo e impar')
else:
    print('El numero ingresado es 0')