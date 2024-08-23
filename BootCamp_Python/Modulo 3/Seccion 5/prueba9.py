#Estructura de repetición multiple match ...case
print('Menú \n')
print('1. Pan $1 \n')
print('2. Carne $7 \n')
print('3. Queso $8 \n')
print('4. Huevos $0.5 \n')
producto=input('Seleccione un producto')

match(producto):
    case '1':
        cantidad=int(input('¿Cantidad a llevar?'))
        PT=cantidad*1
        print(f'El costo de las {cantidad} unidades de pan es: ${PT}')
    case '2':
        cantidad=int(input('¿Cantidad a llevar?'))
        PT=cantidad*7
        print(f'El costo de los {cantidad} kilos de carne es: ${PT}')
    case '3':
        cantidad=int(input('¿Cantidad a llevar?'))
        PT=cantidad*8
        print(f'El costo de los {cantidad} kilos de queso es: ${PT}')
    case '4':
        cantidad=int(input('¿Cantidad a llevar?'))
        PT=cantidad*0.5
        print(f'El costo de las {cantidad} unidades de huevos es: ${PT}')
    case _:
        print('Introdujo una opción inválida')
        
#print(f'El costo del producto es:{PT}')
        




