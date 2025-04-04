class Animal:
    def __init__(self, nombre, edad, especie):
        self._nombre = nombre
        self._edad = edad
        self._especie = especie

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

    @property
    def especie(self):
        return self._especie

    def hacer_sonido(self):
        pass