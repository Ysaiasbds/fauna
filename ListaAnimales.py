class ListaAnimales:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        if not self.animales:
            print("No hay animales en la lista.")
        else:
            print("\nLista de Animales:")
            for i, animal in enumerate(self.animales, 1):
                print(f"{i}. Nombre: {animal.nombre}, Edad: {animal.edad}, Especie: {animal.especie}")