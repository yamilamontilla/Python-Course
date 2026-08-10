suma = 0

numero = int(input('Ingresa un numero positivo (o un numero negativo para salir):'))

while numero >= 0:
    suma += numero
    numero = int(input('Ingresa un numero positivo (o un numero negativo para salir):'))

print('La suma de los numeros ingresados es:', suma)