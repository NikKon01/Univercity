class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

fe = Math(6, 3)
print(fe.addition())

se = Math(6, 3)
print(se.multiplication())

te = Math(6, 3)
print(te.division())

foe = Math(6, 3)
print(foe.subtraction())