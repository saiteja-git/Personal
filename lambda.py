user_input = str(input("Enter any word : "))

word = lambda user_input:"it is a palindrome" if user_input == user_input[::-1] else "It is not a palindrome"
print(word(user_input))