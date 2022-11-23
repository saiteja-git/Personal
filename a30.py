class Calculator:

    def __init__(self,operator,a,b):
        self.operator = operator
        self.a = a
        self.b = b

    def fun(self):
        try:
            if operator == '+':
                return self.a + self.b
            if operator == '-':
                return self.a - self.b
            if operator == '*':
                return self.a * self.b
            if operator == '//':
                return self.a // self.b
        except Exception as e:
            return f'{e}'
while True:
    operator = input("Enter any symbol: ")
    if operator not in ['+','-','*','//'] :
        print("Terminating")
        break
    else:
        user1 = int(input("Enter first value: "))
        user2 = int(input("Enter second value: "))

        obj = Calculator(operator,user1,user2)
        print(obj.fun())


