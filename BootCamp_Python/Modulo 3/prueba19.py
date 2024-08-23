"""Crea un programa en el que el usuario debe adivinar un número secreto entre 1 y 10. 
El programa debe seguir pidiendo al usuario que adivine el número mientras no acierte y 
mientras no ingrese un valor que no esté en el rango especificado, esto debe hacerse un 
máximo de 5 veces. Cuando el usuario adivine el número correctamente o ingrese una opcion
para salir, el programa debe terminar"""
 
import random
repetir = True
while repetir:
    generado=random.randint(1, 10)
    intento=0
    x=False
    while(intento<5) and (x==False):
        entrada=input('Adivine un número entre el 1 y 10 (o escribe "salir" para terminar): ')
    
        if entrada.lower()=='salir':
            print(f'Has decidido salir: El número secreto es {generado}')
            break
    
        if not entrada.isdigit():
            print('Entrada invalida. Por favor ingrese un numero de 1 a 10 o "salir"')
            continue
    
        valor=int(entrada)
    
        if valor<1 or valor>10:
            print('fuera de rango')
        elif valor<generado:
            print('El numero secreto es mayor al indicado')
        elif valor>generado:
            print('El numero secreto es menor al indicado')
        else:
            print('felicidades, acertaste al numero')
            x=True
        intento+=1
    val = True
    while val:
        entrada = input('Desea repetir el juego S/N').lower()
        if entrada == 's':
            repetir = True
            val = False
            print('JUGARA OTRA VEZ!!')
        elif entrada == 'n':
            repetir = False
            print('Has decidido no continuar')
            val = False
        else:
            print('Valor no permitido')