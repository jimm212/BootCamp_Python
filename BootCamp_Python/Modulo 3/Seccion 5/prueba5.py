"""estructura condicional o de decisión anidada"""
edad=int(input('Introduzca su edad'))
if edad>17:
  print('eres un adulto', end=", ")
  if edad>=60:
    print('de la tercera edad')
  else: 
    print('joven')
else:
    print('no eres adulto \n')
    if edad>11:
        print('eres un adolescente ')    
    else:
        print('eres un niño')  

