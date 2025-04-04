from Perro import Perro
from Gato import Gato

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

    def menu(self):
        while True:
            print("\n--------------------- MENU ----------------------")
            print("1. Mostrar lista de animales")
            print("2. Agregar nuevo perro")
            print("3. Agregar nuevo gato")
            print("4. Salir\n")
            opcion = input("Inserta una opción: ")

            if opcion == "1":
                self.mostrar_animales()

            elif opcion == "2":
                nombre = input("Inserta el nombre del perro: ")
                edad = int(input("Inserta la edad del perro: "))
                nuevo_perro = Perro(nombre, edad)
                self.agregar_animal(nuevo_perro)
                print("Perro agregado correctamente.")

            elif opcion == "3":
                nombre = input("Inserta el nombre del gato: ")
                edad = int(input("Inserta la edad del gato: "))
                nuevo_gato = Gato(nombre, edad)
                self.agregar_animal(nuevo_gato)
                print("Gato agregado correctamente.")

            elif opcion == "4":
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Por favor, elije una opción válida.")