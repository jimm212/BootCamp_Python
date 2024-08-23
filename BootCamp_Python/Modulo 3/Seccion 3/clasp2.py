''' Parte 2 de la Clase '''
import secrets as sct
import random as rnd

valor1 = sct.token_bytes(16)
valor2 = sct.choice('3445678912544')
print(f'El token generado es: {valor1} y el aleatorio generado es: {valor2}')

valor3 = rnd.randrange(1,100,1)
print(valor3)