from Animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Gato")

    def hacer_sonido(self):
        return "Miau"