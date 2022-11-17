class Main:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b

    
    def fun(self):
        
        if self.a > self.b:
            return f"{self.a} is greater than {self.b}"
        elif self.a == self.b:
            return f"{self.a} is equal to {self.b}"
        else:
            return f"{self.b} is greater than {self.a}"

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
obj1 = Main(a,b)
print(obj1.fun())








    