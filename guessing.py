user_input = str(input("Enter any word : "))

def pali(user_input):

    if user_input == user_input[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

pali(user_input)