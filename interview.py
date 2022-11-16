class Method:
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2
    def multiply(self):
        return f"This is a {self.name1} and we call it as {self.name2}"

    def adding(self):
        return self.name1 + self.name2

    def fun(self):
        if self.name1 % 2 == 0 and self.name2 % 2 ==0:
            return f"it is even number"
        else:
            return f"it is odd number"


obj1 = Method("Lion","animal")
print(obj1.multiply())

obj2 = Method(4,5)
print(obj2.adding())

obj3 = Method(2,4)
print(obj3.fun())




