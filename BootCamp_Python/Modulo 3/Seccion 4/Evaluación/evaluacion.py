''' Evaluación M°3 S°4 '''
#---------------------------------------------------------------------------------------
#Requerimos crear un registro de datos personales de tres personas. Los datos que se 
# necesitan son: su nombre, apellido y teléfono. Para ello, generaremos un diccionario 
# para cada una de las personas con los datos mencionados, y luego los almacenaremos 
# dentro de una lista. Finalmente, imprimiremos en pantalla la lista
#---------------------------------------------------------------------------------------

persona_1 = {"nombre":"John", "apellido":"Snow" , "telefono":982546747}
persona_2 = {"nombre":"Ned" , "apellido":"Stark", "telefono":944151884}
persona_3 = {"nombre":"Rob" , "apellido":"Stark", "telefono":987155465}

personas = [persona_1,persona_2,persona_3]
print(personas)