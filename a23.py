class Calculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b
   
    def calsi(self):
        user = input("Enter any operator which you want: ")

        if user == '+':
                return self.a + self.b
        elif user == '-':
                return self.a - self.b
        elif user == '*':
                return self.a * self.b
        elif user == '//':
                return self.a // self.b
        elif user == "q":
                return f"Terminating the calculator"

    def faulty(self):
        return f"it is a faluty calculator"

obj1 = Calculator(int(input("Enter first value: ")),int(input("Enter second value: ")))

print(obj1.faulty())




            