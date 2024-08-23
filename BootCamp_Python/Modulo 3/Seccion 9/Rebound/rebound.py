'''REBOUND EXERCISE  M°3 S°9'''
#---------------------------------------------------------------------------------------
#Crear una función que acepte dos parámetros (base y altura) y calcule el área de un 
# rectángulo.Validar que ambos sean números positivos.
#---------------------------------------------------------------------------------------

def area (base,altura):
    if base > 0 and altura >0:
        area_rectangulo = base*altura
        return area_rectangulo
    else:
        print('Ambos valores deben ser positivos: ')
        if base < 0:
            return print(' ->  La base debe ser mayor a 0')
        else:
            return print(' ->  La altura debe ser mayor a 0')

print(area(0,74))