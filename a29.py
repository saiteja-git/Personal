

def calsi(operator,a,b):

    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a*b
    elif operator == '//':
        return a//b
    elif operator == 'q':
        return f'Terminating'

def user_inputs(operator,a,b):
    return calsi(operator,a,b)

operator = input("Enter any sign : ")
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
result = calsi(operator,a,b)
   
print(user_inputs(operator,a,b))

   


