
# Write a Python Program to Check if a Number is a Palindrome or Not?

lst =[]
no_input = int(input("How many elements you want in a list: "))

for i in range(1,no_input):
    user = int(input("Enter the elements you want to add to the list: "))
    lst.append(user)

if lst == lst[::-1]:
    print(f"This number is a Palindrome {lst}")
else:
    print(f"This number is not a Palindrome {lst}")





