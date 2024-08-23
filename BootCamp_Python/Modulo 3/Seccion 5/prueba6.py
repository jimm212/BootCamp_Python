#Uso del AND y OR y estructuras compuestas
nota=float(input('Introduzca su nota'))

if nota>=4 and nota<7.1:
    resp=input('¿Juegas futbol? S/N')
    print('aprobado')
    if nota<7 and resp=='S':
        print('se otorga beca de $1000')
    elif nota==7 and resp=='S':  
        print('Sobresaliente, se otorga beca de $2000') 
elif nota>7:
        print('Introdujo una calificación erronea')
else:
    print('Reprobado! Estudia más')