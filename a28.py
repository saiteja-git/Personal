
class Calculator:
    def __init__(self,operator,a,b):
        self.operator = operator
        self.a = a
        self.b = b

    def fun(self):

        if operator == '+':
            return self.a + self.b
        elif operator == '-':
            return self.a - self.b
        elif operator == '*':
            return self.a*self.b
        elif operator == '//':
            return self.a//self.b

    def fun_1(self):
        return f"This the the output for Normal calculator: {self.fun()}"
    
    def faulty_calsi(self):
        falsy_value = self.fun() * self.b
        return f"This is the output for Falsi Calculator: {falsy_value}"


while True:
    operator = input("What operation you want ? Please select in symbols - add(+), sub(-), mul(*), div(/), exit(q) :- ")
    dict = {'+':'Add','-':'Subtract','*':'Multiply','//':'Divide'}
    values = dict.get(operator)

    if operator == 'q':
        print("Terminating")
        break
    else: 
        a = int(input(f"Enter first value to {values}: "))
        b = int(input(f"Enter second value to {values}: "))

        obj = Calculator(operator,a,b)
        print(obj.fun())
        print(obj.fun_1())
        print(obj.faulty_calsi())
