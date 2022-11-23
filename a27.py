
# function for calculator


def fun(operator,a,b):

    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a*b
    if operator == '//':
        return a//b
   
operator = input("Enter any sign : ")
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

print(fun(operator,a,b))


