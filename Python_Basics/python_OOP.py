class Advay():

    d = 100

    def __init__(self, b, c):
        self.firstNumber = b
        self.secondNumber = c
        print("I am called automatically when object is created")

    def function(self):
        print("Hello World")

    def summation(self):
        return self.firstNumber + self.secondNumber + Advay.d

    a = "Rupesh Modak"


obj = Advay(200, 400)
obj.function()
print(obj.a)
print(obj.summation())

