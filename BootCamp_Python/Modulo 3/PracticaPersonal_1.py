from math import pi
from typing import TypeVar

#from hypothesis import given
#from hypothesis import strategies as st

A = TypeVar('A')
# ---------------------------------------------------------------------
# Ejercicio 1. Definir la función
# media3 : (float, float, float) -> float
# tal que (media3 x y z) es la media aritmética de los números x, y y
# z. Por ejemplo,
# media3(1, 3, 8) == 4.0
# media3(-1, 0, 7) == 2.0
# media3(-3, 0, 3) == 0.0
# ---------------------------------------------------------------------

def media3(x: float, y: float, z:float):
    media =  (x + y + z )/3
    return media

media = media3(20,455,9)
print(f'La medina de los números es: {media}')

# ---------------------------------------------------------------------
# Ejercicio 2. Definir la función
# sumaMonedas : (int, int, int, int, int) -> int
# tal que sumaMonedas(a, b, c, d, e) es la suma de los euros
# correspondientes a a monedas de 1 euro, b de 2 euros, c de 5 euros, d
# 10 euros y e de 20 euros. Por ejemplo,
# sumaMonedas(0, 0, 0, 0, 1) == 20
# sumaMonedas(0, 0, 8, 0, 3) == 100
# sumaMonedas(1, 1, 1, 1, 1) == 38
# ---------------------------------------------------------------------

def sumaMonedas(a: int, b: int, c: int, d: int, e: int) -> int:
    total = a*1 + b*2 + c*5 + d*10 + e*20
    return total

monedas = sumaMonedas(1, 1, 1, 1, 5)
print(f'La Cantidad total de monedas hace un total de {monedas} euros')

# ---------------------------------------------------------------------
# Ejercicio 3. Definir la función
# volumenEsfera : (float) -> float
# tal que volumenEsfera(r) es el volumen de la esfera de radio r. Por
# ejemplo,
# volumenEsfera(10) == 4188.790204786391
# ---------------------------------------------------------------------

def volumenEsfera(r: float) -> float:
    vol = (4*pi/3)*r**3
    return vol

r = 10
volumen = volumenEsfera(r)
print(f'El volumen de una esfera de radio {r} es volumen {volumen}')

# ---------------------------------------------------------------------
# Ejercicio 4. Definir la función
# areaDeCoronaCircular : (float, float) -> float
# tal que areaDeCoronaCircular(r1, r2) es el área de una corona
# circular de radio interior r1 y radio exterior r2. Por ejemplo,
# areaDeCoronaCircular(1, 2) == 9.42477796076938
# areaDeCoronaCircular(2, 5) == 65.97344572538566
# areaDeCoronaCircular(3, 5) == 50.26548245743669
# ---------------------------------------------------------------------

def areaDeCoronaCircular (r1: float, r2: float) -> float:
    area_in = pi*r1**2
    area_ex = pi*r2**2
    area_corona = area_ex - area_in
    return area_corona

corona = areaDeCoronaCircular(2, 5)
print(f'El area de la corona circular es {corona}')

# ---------------------------------------------------------------------
# Ejercicio 5. Definir la función
# ultimoDigito : (int) -> int
# tal que ultimoDigito(x) es el último dígito del número x. Por
# ejemplo,
# ultimoDigito(325) == 5
# ---------------------------------------------------------------------

def ultimoDigito (x :int) -> int:
    ultimo = x % 10
    return ultimo

numero = ultimoDigito(325)
print(f'El ultimo dígito es {numero}')

# ---------------------------------------------------------------------
# Ejercicio 6. Definir la función
# maxTres : (int, int, int) -> int
# tal que maxTres(x, y, z) es el máximo de x, y y z. Por ejemplo,
# maxTres(6, 2, 4) == 6
# maxTres(6, 7, 4) == 7
# maxTres(6, 7, 9) == 9
# ---------------------------------------------------------------------

def maxTres( x : int, y : int, z : int) -> int:
    maximo = max (x,y,z)
    return maximo

maximo = maxTres(6,200,4500)
print(f'El maximo de los numeros es {maximo}')

# ---------------------------------------------------------------------
# Ejercicio 7. Definir la función
# rota1 : (List[A]) -> List[A]
# tal que rota1(xs) es la lista obtenida poniendo el primer elemento de
# xs al final de la lista. Por ejemplo,
# rota1([3, 2, 5, 7]) == [2, 5, 7, 3]
# rota1(['a', 'b', 'c']) == ['b', 'c', 'a']
# ---------------------------------------------------------------------

def rota1(xs: list[A]) -> list[A]:
    if xs == []:
        return []
    # ys = xs[1:]
    # ys = ys.append(xs[0])
    rot = xs[1:] + [xs[0]]
    return rot

rotación = rota1(['a', 'b', 'c'])
print(f'La rotación de la lista es {rotación}')

# ---------------------------------------------------------------------
# Ejercicio 8. Definir la función
# rota : (int, List[A]) -> List[A]
# tal que rota(n, xs) es la lista obtenida poniendo los n primeros
# elementos de xs al final de la lista. Por ejemplo,
# rota(1, [3, 2, 5, 7]) == [2, 5, 7, 3]
# rota(2, [3, 2, 5, 7]) == [5, 7, 3, 2]
# rota(3, [3, 2, 5, 7]) == [7, 3, 2, 5]
# ---------------------------------------------------------------------

def rota(n : int, xs : list[A]) -> list[A]:
    if xs == []:
        return []
    rot = xs[n:] + xs[:n]
    return rot

rotación2 = rota(2, [3, 2, 5, 7])
print(f'La rotación de la lista es {rotación2}')

# ---------------------------------------------------------------------
# Ejercicio 9. Definir la función
# rango : (List[int]) -> List[int]
# tal que rango(xs) es la lista formada por el menor y mayor elemento
# de xs.
# rango([3, 2, 7, 5]) == [2, 7]
# ---------------------------------------------------------------------

def rango( xs: list[int]) -> list[int]:
    menor = min(xs)
    mayor = max(xs)
    ran = [menor,mayor]
    return ran

ran = rango([3, 2, 7, 5])
print(f'El rango es {ran}')

# ---------------------------------------------------------------------
# Ejercicio 10. Definir la función
# palindromo : (List[A]) -> bool
# tal que palindromo(xs) se verifica si xs es un palíndromo; es decir,
# es lo mismo leer xs de izquierda a derecha que de derecha a
# izquierda. Por ejemplo,
# palindromo([3, 2, 5, 2, 3]) == True
# palindromo([3, 2, 5, 6, 2, 3]) == False
# ---------------------------------------------------------------------

def palindromo( xs : list[A]) -> bool:
    # xs == list(reversed(xs))
    if xs == xs[::-1]:
        return True
    else:
        return False

print(f'La operación palindromo([3, 2, 5, 2, 3]) es  {palindromo([3, 2, 5, 2, 3])}')

# ---------------------------------------------------------------------
# Ejercicio 11. Definir la función
# interior : (list[A]) -> list[A]
# tal que interior(xs) es la lista obtenida eliminando los extremos de
# la lista xs. Por ejemplo,
# interior([2, 5, 3, 7, 3]) == [5, 3, 7]
# ---------------------------------------------------------------------

def interior( xs: list[A])->list[A]:
    inter = xs[1:][:-1]
    # xs[1:-1]
    return inter

ver =  interior([2, 5, 3, 7, 3])
print(f'El interior de la lista [2, 5, 3, 7, 3] es {ver}')

# ---------------------------------------------------------------------
# Definir la función
# finales : (int, list[A]) -> list[A]
# tal que finales(n, xs) es la lista formada por los n finales
# elementos de xs. Por ejemplo,
# finales(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]
# ---------------------------------------------------------------------

def finales(n: int, xs: list[A])-> list[A]:
    if n == 0:
        return []
    fin = xs[(len(xs)-n):]
    # fin xs[-n:]
    return fin

fin  = finales(3, [2, 5, 4, 7, 9, 6])
print(f'Los numeros finales son {fin}')

# ---------------------------------------------------------------------
# Ejercicio 13. Definir la función
# segmento : (int, int, list[A]) -> list[A]
# tal que segmento(m, n, xs) es la lista de los elementos de xs
# comprendidos entre las posiciones m y n. Por ejemplo,
# segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
# segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
# segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []
# ---------------------------------------------------------------------

def segmento(m:int, n:int, xs: list[A]) -> list[A]:
    if m == 0 or n == 0:
        return []
    fin = xs[m-1:n]
    return fin

fin  = segmento(3, 5, [3, 4, 1, 2, 7, 9, 0])
print(f'Los numeros finales son {fin}')

# ---------------------------------------------------------------------
# Ejercicio 14. Definir la función
# extremos : (int, list[A]) -> list[A]
# tal que extremos(n, xs) es la lista formada por los n primeros
# elementos de xs y los n finales elementos de xs. Por ejemplo,
# extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]) == [2, 6, 7, 9, 2, 3]
# ---------------------------------------------------------------------

def extremos (n : int, xs : list[A] ) -> list[A]:
    if n == 0:
        return []
    # xs[:n] + xs[-n:]
    newlist = xs[:n]+xs[(len(xs)-n):]
    return newlist

listnew  = extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3])
print(f'Los extremos son {listnew}')

# ---------------------------------------------------------------------
# Ejercicio 15. Definir la función
# mediano : (int, int, int) -> int
# tal que mediano(x, y, z) es el número mediano de los tres números x, y
# y z. Por ejemplo,
# mediano(3, 2, 5) == 3
# mediano(2, 4, 5) == 4
# mediano(2, 6, 5) == 5
# mediano(2, 6, 6) == 6
# ---------------------------------------------------------------------

def mediano(x: int, y: int, z: int) -> int:
    sol = x + y + z - min([x,y,z]) - max([x,y,z])
    return sol

med  = mediano(2, 6, 5)
print(f'Los extremos son {med}')

# ---------------------------------------------------------------------
# Ejercicio 16. Definir la función
# tresIguales : (int, int, int) -> bool
# tal que tresIguales(x, y, z) se verifica si los elementos x, y y z son
# iguales. Por ejemplo,
# tresIguales(4, 4, 4) == True
# tresIguales(4, 3, 4) == False
# ---------------------------------------------------------------------

def tresIguales(x:int, y:int, z:int) -> bool:
    if x == y == z:
        igual = True
        return igual
    else:
        igual = False
        return igual
        
igd  = tresIguales(9, 9, 9)
print(f'La igualdad es {igd}')

# ---------------------------------------------------------------------
# Ejercicio 17. Definir la función
# tresDiferentes : (int, int, int) -> bool
# tal que tresDiferentes(x, y, z) se verifica si los elementos x, y y z
# son distintos. Por ejemplo
# tresDiferentes(3, 5, 2) == True
# tresDiferentes(3, 5, 3) == False
# ---------------------------------------------------------------------

def tresDiferentes(x:int, y:int, z:int) -> bool:
    if x != y != z and x!= z:
        igual = True
        return igual
    else:
        igual = False
        return igual
        
igd2  = tresDiferentes(2, 8, 5)
print(f'La des-igualdad es {igd2}')

# ---------------------------------------------------------------------
# Ejercicio 18. Definir la función
# cuatroIguales : (int, int, int, int) -> bool
# tal que cuatroIguales(x,y,z,u) se verifica si los elementos x, y, z y
# u son iguales. Por ejemplo,
# cuatroIguales(5, 5, 5, 5) == True
# cuatroIguales(5, 5, 4, 5) == False
# ---------------------------------------------------------------------

def cuatroIguales(x:int, y:int, z:int, u:int) -> bool:
    # x == y == z == u
    if x == y and tresIguales(y,z,u):
        igual = True
        return igual
    else:
        igual = False
        return igual
        
igd3 = cuatroIguales(8, 8, 8, 8)
print(f'La igualdad es {igd3}')

# ---------------------------------------------------------------------