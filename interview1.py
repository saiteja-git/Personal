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
    @classmethod
    def fun_1(cls,a,b):
        return cls(a,b)

    def display(cls):
        return cls.a + cls.b
    
try:
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))

   # obj1 = Main(a,b)
   # print(obj1.fun())

    obj2 = Main.fun_1(1,2)
    print(obj2.display())

except Exception as k:
    print(f"value error")

