
class Calculadora:
    def __init__(self, val1, val2):
        self.a = val1
        self.b = val2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def divi(self):
        return self.a / self.b

    def resto(self):
        return self.a % self.b


calculadora = Calculadora(10, 2)

print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.divi())
print(calculadora.resto())
print(calculadora.mult())
