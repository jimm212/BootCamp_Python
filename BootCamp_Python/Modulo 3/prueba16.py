import math

resp='S'
while (resp=='S'):
    print("Menú \n")
    print("1. Suma \n")
    print("2. Resta \n")
    print("3. Multiplicación \n")
    print("4. División \n")
    print("5. Suma sucesiva \n")
    print("6. Factorial de n \n")
    opcion=input("Introduzca una operación matemática (1,2,3,4,5 o 6)")
    match(opcion):
        case '1': 
            num1=float(input("Introduzca un primer valor"))
            num2=float(input("Introduzca un segundo valor"))
            print(f"La suma es:{(num1+num2):.2f}") 
        case '2': 
            num1=float(input("Introduzca un primer valor"))
            num2=float(input("Introduzca un segundo valor"))
            print(f"La resta es:{(num1-num2):.2f}")  
        case '3': 
            num1=float(input("Introduzca un primer valor"))
            num2=float(input("Introduzca un segundo valor"))
            print(f"El producto es:{(num1*num2):.2f}")
        case '4': 
            num1=float(input("Introduzca un primer valor"))
            num2=float(input("Introduzca un segundo valor"))
            if (num2!=0):
                print(f"La división es:{(num1/num2):.2f}")
            else:
                print("Error: División por cero indefinida")  
        case '5': 
            num1=int(input("Introduzca un valor entero"))
            resultado=0
            for contador in range (1,num1+1):
                resultado=resultado+contador        
            print(f"La suma sucesiva es:{resultado}")
        case '6': 
            num1=int(input("Introduzca un valor entero"))  
            resultado=math.factorial(num1)
            print(f"El valor del factorial de {num1} es: {resultado}")
        case _:
            print("Introdujo una opción no válida") 
            continue
    valida=True
    while valida:                 
        resp=input('¿Deseas realizar otra operación? S/N').upper()        
        if resp=='S':
            valida=False            
        elif resp=='N':
            print('Gracias por usar la aplicación. Hasta pronto!')
            break
        else:
            print('Introdujo respuesta inválida. Responda S o N')
        
    