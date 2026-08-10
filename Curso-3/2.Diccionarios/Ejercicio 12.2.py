persona1  = {
    "nombre": None,
    "edad": None,
    "direccion": None,
    "telefono": None,
}

persona1['nombre']= input("Introduce un nombre:")
persona1['edad']= input("Introduce tu edad:")
persona1['direccion']= input("Introduce tu direccion:")
persona1['telefono']= input("Introduce tu telefono:")

print(persona1['nombre'], "tiene", persona1['edad'], "años, vive en", persona1['direccion'], "y su numero de telefono es", persona1['telefono'])