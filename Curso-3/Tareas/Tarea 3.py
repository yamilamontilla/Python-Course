# Define la función calculadora
def calculadora(num1, num2, operacion):
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        return num1 / num2
    else:
        return "Operación no válida"

num1 = float(input('Ingresa el primer número: '))
num2 = float(input('Ingresa el segundo número: '))
operacion = input('Selecciona la operación (+, -, *, /): ')

resultado = calculadora(num1, num2, operacion)
print(f"Resultado: {num1} {operacion} {num2} = {resultado}")

