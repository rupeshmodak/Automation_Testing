from python_OOP import Advay


class Inherit(Advay):

    e = 500

    def __init__(self, j, k):
        self.j = j
        self.k = k
        Advay.__init__(self, 200, 200)
        print("My name is Rupesh")

    def methodone(self):
        print("I am Rupesh")

    def methodtwo(self):
        return self.e + self.firstNumber + self.secondNumber + self.j + self.k


newobj = Inherit(300, 300)
newobj.function()
newobj.methodone()
print(newobj.methodtwo())



