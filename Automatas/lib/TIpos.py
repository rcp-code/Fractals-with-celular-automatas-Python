import numpy as np
import math


class Automata:
    def __init__(self, num_filas, num_cols, modo_aleatorio=False):
        self.num_filas = num_filas
        self.num_cols = num_cols
        self.modo_aleatorio = modo_aleatorio
        self.automata = self.inicializa_automata()

    def inicializa_automata(self):
        '''Inicializa el autómata según el valor del atributo "modo_aleatorio". Si este es True, se
        crea un array de numpy con valores aleatorios entre 0 y 1; en caso contrario, se inicializa con
        un solo uno (situado en el centro de la primera fila) y el resto de valores 0.'''
        if self.modo_aleatorio:
            return np.random.randint(0, 1, (self.num_filas, self.num_cols))
        else:
            automata = np.zeros((self.num_filas, self.num_cols))
            mitad = math.floor(self.num_filas / 2)
            automata[mitad]
            return automata

    def obtiene_automata(self):
        return self.automata


class Pos:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def obtiene_pos(self):
        return self.fila, self.columna


class Mundo:
    '''REVISAR Y MODIFICAR SI ES NECESARIO LO DE datos_automata.'''

    def __init__(self, pantalla, regla, condiciones, datos_automata, animacion, adicional):
        self.pantalla = pantalla
        self.regla = regla
        self.condiciones = condiciones
        self.datos_automata = datos_automata
        self.animacion = animacion
        self.adicional = adicional

    def obtiene_mundo(self):
        return self.pantalla, self.regla, self.condiciones, self.datos_automata, self.animacion, self.adicional
