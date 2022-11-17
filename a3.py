# Write a Python Program to Check if a string is a Palindrome or not?

user_input = str(input("Enter any word to check whether it is Palindrome or not! : "))

if user_input == user_input[::-1]:
    print("It is Palindrome")
else:
    print("It is not Palindrome")