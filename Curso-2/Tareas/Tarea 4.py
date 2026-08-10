palabras = ['manzana', 'platano', 'cereza']

palabra_buscar = input('Ingrese una palabra para buscar: ')
if palabra_buscar in palabras:
    print('La palabra', palabra_buscar, 'está en la tupla.')
else:
    print('La palabra', palabra_buscar, 'no está en la tupla.')
