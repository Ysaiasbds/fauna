from Animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Perro")

    def hacer_sonido(self):
        return "Guau"