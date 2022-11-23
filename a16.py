# Function to check whether the given word is Palindrome or not

def fun_pali(name):
    if name == name[::-1]:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"
print(fun_pali(str(input("Enter any word: "))))

