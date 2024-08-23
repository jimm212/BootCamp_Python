'''Evaluación M°3 S°9'''
#---------------------------------------------------------------------------------------
#rear una función que sume dos números, otra que reste dos números, otra que multiplique 
# dos números, y otra que divida dos números. Adicionalmente, crear una función que 
# acepte dos números como parámetros y regrese el resultado en forma de tupla de su 
# suma, resta, multiplicación y división. 
# Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta,
# Multiplicación y División, y los valores de cada clave serán los resultados obtenidos
# con la función creada anteriormente.
#---------------------------------------------------------------------------------------

def suma(a,b):
    sumar = a + b
    return sumar

def resta(a,b):
    restar = a - b
    return restar

def multiplicacion(a,b):
    multiplicar = a * b
    return multiplicar

def dividir(a,b):
    if b == 0:
        print('Operación no valida')
        return None
    else:  
        divide = a / b
        return divide

def devolver(a,b):
    tupla = (suma(a,b),resta(a,b),multiplicacion(a,b),dividir(a,b))
    return tupla

a = 4587
b = 958
diccionario = {
    'SUMA': suma(a,b),
    'RESTA': resta(a,b),
    'MULTIPLICACIÓN': multiplicacion(a,b),
    'DIVISION': dividir(a,b),
    'TUPLA': devolver(a,b) 
}
print(diccionario)
