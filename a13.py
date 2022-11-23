# Faulty calculator

while True:

    def dummy_calculator(a,b,operation):

        return a,b,operation

    user = input("What operation you want ? Please select in symbols - add(+), sub(-), mul(*), div(/), exit(q) :- ")

    if user == '+':
        a_add = int(input("Enter first number to add: "))
        b_add = int(input("Enter second number to add: "))
        add_total = a_add + b_add
        addition_result = add_total*b_add
        print(f"Adition result: {addition_result}")
    if user == "-":
        a_sub = int(input("Enter first number to sub: "))
        b_sub = int(input("Enter second number to sub: "))
        sub_total = a_sub-b_sub
        subtraction_result = sub_total * b_sub
        print(f"Subtraction result: {subtraction_result}")
    if user == "*":
        a_mul = int(input("Enter first number to multiply: "))
        b_mul = int(input("Enter second number to multiply: "))
        mul_total = a_mul * b_mul
        multiplication_result = mul_total * b_mul
        print(f"Multiplication result: {multiplication_result}")
    if user == "/":
        a_div = int(input("Enter first number to divide: "))
        b_div = int(input("Enter second number to divide: "))
        div_total = a_div / b_div
        division_result = div_total * b_div
        print(f"Division result: {division_result}")
    if user == 'q':
        print(f'Terminating!')
        break