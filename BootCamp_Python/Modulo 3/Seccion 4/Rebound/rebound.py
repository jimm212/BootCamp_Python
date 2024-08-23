''' Rebound Exercise  M°3 S°4 '''
# ------------------------------------------------------------------------------------------
# Requerimos  crear  una  variable  con  el  número  8,  una  con  el  número  10.5,  y  una
# con  la  palabra “ejercicio”.  Luego,  crear  un  set  que  contendrá  cada  una  de  las 
# variables  que  creamos,  y  será asignado a una variable.  
# A continuación, crearemos una lista que contendrá el set creado anteriormente, y una 
# variable con el valor lógico False. Esta lista la asignaremos a una variable que luego 
# imprimiremos en pantalla.
# ------------------------------------------------------------------------------------------
import math

var_1 = 8
var_2 = 10.5
var_3 = 'ejercicio'

set_1 = {var_1,var_2,var_3}
lista = [set_1,False]

print(f'La lista contiene lo siguiente: {lista}')