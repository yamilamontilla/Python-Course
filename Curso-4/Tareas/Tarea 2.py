from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

# Crear instancias de las subclases
perro = Perro("Buddy")
gato = Gato("Whiskers")

# Mostrar el nombre y el sonido de cada animal
print(f"{perro.nombre} dice: {perro.hablar()}")
print(f"{gato.nombre} dice: {gato.hablar()}")


