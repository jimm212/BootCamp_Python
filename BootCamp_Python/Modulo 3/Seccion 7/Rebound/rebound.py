''' Rebound Exercises  M°3 S°7 '''
#---------------------------------------------------------------------------------------
# Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for, 
# e imprimir en pantalla el valor de cada elemento indicando si es par, impar o cero.
#---------------------------------------------------------------------------------------

for element in range(0,10):
    if element == 0:
        print(f'El numero {element} es cero')
    elif element % 2 == 0:
        print(f'El numero {element} es par')
    else:
        print(f'El numero {element} es impar')