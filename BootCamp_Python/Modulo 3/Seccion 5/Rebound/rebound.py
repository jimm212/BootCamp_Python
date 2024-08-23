''' Rebound Exercise  M°3 S°5 '''
# Requerimos  calcular  el  factorial  de  un  número,  asignarlo  a  una  variable,  
# y  luego  imprimirla. 
# Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros 
# positivos que hay entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.

import math

num = 10
num2 =  num

for i in range(1, num):
    num2 = num2*i
print(f'El factorial de {num} es {num2}')