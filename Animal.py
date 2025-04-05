from Gato import Gato
from Perro import Perro

class Animal:
    especie = "Animal"  # Atributo de clase

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return f"Especie: {self.especie}"


class Gato(Animal):
    def hacer_sonido(self):
        return f"Especie: {self.especie}"