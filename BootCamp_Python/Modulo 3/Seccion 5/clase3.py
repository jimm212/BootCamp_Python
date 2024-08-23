import math

saludo = 'hola'
saludo_inv = saludo[::-1]
print(f'El saludo es {saludo} y la forma invertida es {saludo_inv}')

num = 49
raiz = math.sqrt(num)
print(f'La raíz de {num} es: {raiz}')

### IF ELSE

x = int(input('Ingrese un numero: '))
if (x>0):
  print(f' {x} es positivo')
elif (x==0):
  print(f' {x} es cero')
else:
  print('Es negativo')