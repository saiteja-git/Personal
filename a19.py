# Function to Swap the First and Last Value of a List?


def fun_reverse(number):
    temp = number[0]
    number[0] = number[-1]
    number[-1] = temp
    return number

number = list(input("Enter any number: "))
print(fun_reverse(number))




