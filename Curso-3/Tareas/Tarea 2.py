datos_personales = {
    'nombre': None,
    'edad': None,
    'direccion': None,
    'telefono': None
}

datos_personales['nombre'] = input('Ingresa tu nombre: ')
datos_personales['edad'] = input('Ingresa tu edad: ')
datos_personales['direccion'] = input('Ingresa tu dirección: ')
datos_personales['telefono'] = input('Ingresa tu número de teléfono: ')

# Mostrar los datos personales ingresados
print("\nTus datos personales:")
print("Tu nombre es", datos_personales['nombre'] + ".")
print("Tienes", datos_personales['edad'] + " años.")
print("Vives en", datos_personales['direccion'] + ".")
print("Tu número de teléfono es", datos_personales['telefono'] + ".")


