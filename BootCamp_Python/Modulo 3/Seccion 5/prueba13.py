import math

opcion = ''
while (opcion!='s'):
    print('------------------------------------------------------------------------------')
    print(f' Menú \n 1. suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Suma sucesiva \n 6. Factorial')
    opcion = input('Ingrese la operación matemática:\n Para finalizar pulse s --> ').lower()
    print('------------------------------------------------------------------------------')
    match (opcion):
        case '1':
            print('Se realizara una suma ')
            num1 = float(input('Ingrese el primer  numero '))
            num2 = float(input('Ingrese el segundo numero '))
            res = num1 + num2
            print(f' El resultado de la operación Suma es {res:.2f}')
        case '2':
            print('Se realizara una resta ')
            num1 = float(input('Ingrese el primer  numero '))
            num2 = float(input('Ingrese el segundo numero '))
            res = num1 - num2
            print(f' El resultado de la operación Resta es {res:.2f}')
        case '3':
            print('Se realizara una Multiplicación ')
            num1 = float(input('Ingrese el primer  numero '))
            num2 = float(input('Ingrese el segundo numero '))
            res = num1*num2
            print(f' El resultado de la operación Multiplicación es {res:.2f}')
        case '4':
            print('Se realizara una Division ')
            num1 = float(input('Ingrese el primer  numero '))
            num2 = float(input('Ingrese el segundo numero '))
            if num2 == 0:
                print('No se puede realizar al operación')
            else:
                res = num1/num2
                print(f' El resultado de la operación división es {res:.2f}')
        case '5':
            print('Se realizara una Suma Sucesiva ')
            num1 = int(input('Ingrese el numero entero positivo '))
            res = 0
            for i in range(1,num1+1):
                res = res+i
            print(f'El resultado de la Suma Sucesiva es: {res}')
        case '6':
            print('Se realizara un Factorial ')
            num1 = int(input('Ingrese el numero '))
            fact = math.factorial(num1)
            print(f'El resultado del factorial es: {fact}')
        case _:
            if opcion == 's':
                confirmar = input('Para finalizar el programa escriba "salir", \n para retornar presione cualquier tecla -->  ').lower()
                if confirmar == 'salir':
                    print('------------------------------------------------------------------------------')
                    print('Gracias por usar este servicio')
                    print('------------------------------------------------------------------------------')
                else:
                    opcion = ''
            else:
                print('Introdujo una opción no valida')
                