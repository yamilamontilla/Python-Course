class calculadora1:
    def __init__(self, numero):
        self.resultado = numero

    def sumar(self, numero):
        self.resultado += numero

    def restar(self, numero):
        self.resultado -= numero
    
    def multiplicar(self, numero):
        self.resultado *= numero

    def dividir(self, numero):
        if numero != 0:
            self.resultado /= numero
        else:
            print("Error: Nose puede dividir por cero.")
    
    def rusultado(self):
        return self.resultado
    
calculo = calculadora1(0)

calculo.sumar(5)
calculo.multiplicar(4)
calculo.restar(5)
calculo.dividir(2)

resultado = calculo.resultado
print("Resultado:", resultado)
