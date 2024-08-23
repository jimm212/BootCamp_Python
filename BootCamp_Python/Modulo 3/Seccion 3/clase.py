'''Program Test - BootCamp Python'''
import decimal as dec # redondea decimales

edad   = int(input('Introduzca su edad: '))
nombre = input('Introduzca su nombre: ')

print(f'Su nombre es: {nombre} y su edad es {edad} años')


resultado = 8+5*(3+4)-2/1+5*10+((4+6/2))
print(resultado)

#  ver determinado numero float '{:.2f}'.format
valor = dec.Decimal(float('6.735823'))
res = 4.5523
res2 = valor.quantize(dec.Decimal('1.00000000000000')) # los ceros la cantidad de decimales
print(f'El resultado es {'{:.2f}'.format(res)}')
print(f'El resultado es {res:.2f}')
print(f'El resultado es {res2}')