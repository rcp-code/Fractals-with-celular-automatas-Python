import math
import numpy as np

'''Funciones de matrices en útiles.'''


def rangos(m):
    return m.shape()


def vacia():
    return np.zeros((1, 1))


'''Funciones normales en útiles.'''


def cabeza(funcion, lista):
    try:
        return lista[0]
    except ValueError:
        print("La lista pasada en la funcion ", funcion, "está vacía.")


def binario(n):
    if n % 2 == 0:
        return 0
    else:
        return 1


def es_int(s):
    return s.isNumeric()


def es_real(s):
    try:
        fraccionaria = ""
        numero = s.split('.')
        ind = s.find('.')
        entero = numero[0]
        f = s[ind:]
        if f is not None:
            fraccionaria = f[1:]
        if es_int(entero) and es_int(fraccionaria):
            return True
        else:
            return False
    except ValueError:
        print("La cadena proporcionada en la función esReal no es un número en coma flotante.")


# def string_to_int(s):
#    if s == "":
#        return 0
#    else:
#        for c in s:
#            if c == '-':
#                (-1) * string_to_int(s)
#            else:
#                int(s) * 10 ^ (len(s[1:]) - 1) + string_to_int(s)

def string_to_int(s):
    if s == "":
        return 0
    else:
        return int(s)


# stringToFloat :: String -> Float
# stringToFloat [] = 0.0
# stringToFloat s = entera + fraccionaria
#   where
#       e = stringToInt $ takeWhile (/= '.') s
#       entera = fromInteger $ toInteger e
#       f = tail $ dropWhile (/= '.') s
#       fracEnt = fromInteger $ toInteger $ stringToInt f
#       fraccionaria = fracEnt / (10 ^ length f)*/

def string_to_float(s):
    if s == "":
        return 0
    else:
        return float(s)


# listasDePares :: [a] -> [[a]]
# listasDePares [] = []
# listasDePares lista = par : listasDePares resto
#   where
#       par = take 2 lista
#       resto = drop 2 lista
def listas_de_pares(lista):
    pass


def distancia_euclidea(a, b):
    base = a - b
    potencia = pow(base, 2)
    return math.sqrt(potencia)


def intercambia(lista, a, p):
    pass


def introduce(lista, a, p):
    pass


def elimina(lista, p):
    pass


def elimina_elemento(lista, a):
    pass


def aleatorio(al, lista):
    pass


def escoge_aleatorios(al, lista):
    aleatorios = list()
    p = normaliza(al)
    return aleatorios


def normaliza(numero):
    return numero - float(math.floor(numero))


def genera_aleatorios(semilla):
    np.random.seed(semilla)
    lista = np.random.rand(1000000000000)
    aleatorios = [x % 1000000000000 for x in lista]
    return aleatorios
