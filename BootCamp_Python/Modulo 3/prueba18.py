import math

def obtener_numero(mensaje, tipo='float'):  
    while True:
        entrada=input(mensaje)
        try:
            if tipo=='float':
                return float(entrada)
            elif tipo== 'int':
                return int(entrada)
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido")
           
 
resp='S'
while (resp=='S'):    
    print("Menú \n")
    print("1. Suma \n")
    print("2. Resta \n")
    print("3. Multiplicación \n")
    print("4. División \n")
    print("5. Suma sucesiva \n")
    print("6. Factorial de n \n")
    opcion=input("Introduzca una operación matemática (1,2,3,4,5 o 6):")
    match(opcion):
        case '1':
            num1=obtener_numero("Introduzca un primer valor:")
            num2=obtener_numero("Introduzca un segundo valor:")
            print(f"La suma es :{(num1+num2):.1f}")
        case '2':
            num1=obtener_numero("Introduzca un primer valor:")
            num2=obtener_numero("Introduzca un segundo valor:")
            print(f"La resta es :{(num1-num2):.1f}")
        case '3':
            num1=obtener_numero("Introduzca un primer valor:")
            num2=obtener_numero("Introduzca un segundo valor:")
            print(f"La multiplicación es :{(num1*num2):.1f}")
        case '4':
            num1=obtener_numero("Introduzca un primer valor:")
            num2=obtener_numero("Introduzca un segundo valor:")
            if (num2!=0):
                print(f"La division es :{(num1/num2):.1f}")
            else:
                print("Error: División por cero indefinida")
        case '5':
            num1=obtener_numero("Introduzca un valor entero:", 'int')
            resultado=0
            for contador in range (1,num1+1):
                resultado=resultado+contador
            print(f"La suma sucesiva es: {resultado}")
        case '6':
            num1=obtener_numero("Introduzca un valor entero:", 'int')
            resultado=math.factorial(num1)
            print(f"El valor del factorial de {num1} es: {resultado}")
        case _:
            print("Introduce un valor válido")
            continue
    valida=True
    while valida:
        resp=input("Deseas realizar otra operacion? S/N").upper()
        if resp=='S':
            valida=False
        elif resp=='N':
            print("Gracias por usar la aplicación. Hasta Pronto!")
            break
        else:
            print("Introdujo respuesta inválida. Responda S o N")