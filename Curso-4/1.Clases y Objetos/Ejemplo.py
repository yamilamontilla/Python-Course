class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Llamar al método saludar
persona1.saludar()

# Crear otra instancia de la clase Persona
persona2 = Persona("María", 25)

# Llamar al método saludar para la segunda persona
persona2.saludar()