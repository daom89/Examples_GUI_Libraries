from Utils import *
from typing import TypeVar

''' 
    Ejercicio 1
    
    En este problema, los datos de entrada son los dos valores enteros que ingresará
    el usuario a través del teclado (los llamaremos a y b) y la salida será su
    cociente (un número flotante). Ahora bien, existe la posibilidad de que el
    usuario ingrese como segundo valor el número 0 (cero). En este caso, no podremos
    mostrar el cociente ya que la división por cero es una indeterminación, así que
    tendremos que emitir un mensaje informando las causas por las cuales no se podrá
    efectuar la operación.
'''


class Ejercicio1:
    Ejercicio1 = TypeVar("Ejercicio1")
    def __init__(
            self,
            numero_1: int = None,
            numero_2: int = None):
        self.__numero_1 = numero_1
        self.__numero_2 = numero_2
        self.__cociente = None

    @property
    def numero_1(self) -> int:
        return self.__numero_1

    @numero_1.setter
    def numero_1(self, numero_1: int):
        self.__numero_1 = numero_1

    @property
    def numero_2(self) -> int:
        return self.__numero_2

    @numero_2.setter
    def numero_2(self, numero_2: int):
        self.__numero_2 = numero_2

    @property
    def cociente(self) -> float:
        return self.__cociente

    @cociente.setter
    def cociente(self, cociente: float):
        self.__cociente = cociente

    def calcular_cociente(self) -> Ejercicio1:
        """
        :return: Object Ejercicio1
        """
        if self.numero_2 == 0:
            self.cociente = 0
            return self
        else:
            self.cociente = round(self.numero_1 / self.numero_2, 2)
            return self

    def __str__(self):
        return f"numero_1: {self.numero_1}, numero_2: {self.numero_2}, cociente: {self.cociente}"

