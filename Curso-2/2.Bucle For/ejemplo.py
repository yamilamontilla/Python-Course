frutas = ['manzana', 'banana', 'cereza', 'naranja']
contador = 0

for fruta in frutas:
    contador += 1
    print(f'Fruta #{contador}: {fruta}')
    if contador == 4:
        break
   