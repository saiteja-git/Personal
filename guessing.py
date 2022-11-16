import random
count = 1
rand_val = random.randint(1, 5)
while count:
    user_input = int(input("Enter any value: "))

    if rand_val > user_input:
         print(f"You entereed the greater value {user_input}")
    elif rand_val < user_input:
         print(f"You entered the lesser value {user_input}")
    elif user_input == rand_val:
         print(f"Congratulations you entered the correct value {user_input}")
         count = 0
    else:
        print("raise value error")
     
            

