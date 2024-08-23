#Uso del AND y OR y estructuras compuestas y anidadas
nota=float(input('Introduzca su nota'))

if nota>=4 and nota<7.1:
    print('aprobado') 
    resp=input('¿Juegas futbol? S/N')
    if resp not in ['S','s','N','n']:
        print('Introdujo una respuesta inválida')
    elif nota<7 and (resp=='S' or resp=='s'):
        print('se otorga beca de $1000')
    elif nota==7 and (resp=='S' or resp=='s'):  
        print('Sobresaliente, se otorga beca de $2000') 
elif nota>7:
        print('Introdujo una calificación erronea')
else:
    print('Reprobado! Estudia más')