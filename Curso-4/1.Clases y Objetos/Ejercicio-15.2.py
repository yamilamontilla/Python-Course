class calculadora2:
    def suma(self, num1, num2):
        return num1 + num2
    
    def resta(self, num1, num2):
        return num1 - num2
    
    def multiplicar(self, num1, num2):
        return num1 * num2
    
    def divicion(self, num1, num2):
        if num2 == 0:
            return "Error: No se puede dividir por cero."
        
num1 = float(input("Ingresa el primer numero:"))
num2 = float(input("Ingresa el segundo numero:"))

calc = calculadora2()

resulsuma = calc.suma(num1, num2)
resulresta = calc.resta(num1, num2)
resulmultiplicacion = calc.multiplicar(num1, num2)
resuldivicion = calc.divicion(num1, num2)

print("Suma:", resulsuma)
print("Resta:", resulresta)
print("Multiplicacion:", resulmultiplicacion)
print("Divicion:", resuldivicion)