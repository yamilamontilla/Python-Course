def espar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = int(input('Introduce un numero:'))
if espar(numero) == True:
    print(f'{numero} es un numero par')
else:
    print(f'{numero} es un numero inpar')

