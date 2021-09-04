class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addtion(self):
        print("Addition",self.a+self.b)
    def Subtraction(self):
        print("Subtraction",self.a-self.b)
    def multiplication(self):
        print("Multiplication",self.a*self.b)
    def division(self):
        print("Division",self.a%self.b)

Cal1 = Calculator(5,5)
print("A=",Cal1.a)
print("B",Cal1.b)
Cal1.addtion()
Cal1.Subtraction()
Cal1.multiplication()
Cal1.division()
