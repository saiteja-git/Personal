# Guess the number

import random
var = random.randint(0,100)

while True:
    user = int(input("Enter any value in the range of 0-100 : "))
    if var < user:
        print(f"You have entered greater number {user}")
    elif var > user:
        print(f"You have entered smaller number {user}")
    elif var == user:
        print(f"Congratulations you guessed the correct number")
        break




