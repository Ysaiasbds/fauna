class Animal:
    especie = "Animal"

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
        return 


class Gato(Animal):
    def hacer_sonido(self):
        return 

class ListaAnimales:
    
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        
        print("Lista de Animales:")
        
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


# Programa principal
lista_animales = ListaAnimales()
lista_animales.menu()
