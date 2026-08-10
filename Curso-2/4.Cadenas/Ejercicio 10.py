nombre = 'Yamila'
apellido = 'MoNtiLLa'
frace = 'Hola Esta Es una Frase'

longitud = len(frace)
print(longitud)

print(apellido[6])

palabras = frace.split()
print(palabras)
mayusculas = frace.upper()
print(mayusculas)
texto = apellido.lower()
print(texto)

mensaje = 'Hola, Mundo'
print(mensaje)
cambio = mensaje.replace('Hola', 'Yamila')
print(cambio)

for x in apellido:
    print(x)
