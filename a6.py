# Write a Python Program to Swap the First and Last Value of a List?

a = []
user_input = int(input("How many elements you want to add to a list : "))

for i in range(1,user_input):
    user = int(input("Enter the elements in a list: "))
    a.append(user)
    
print(f"Before swap {a}")
temp_var = a[0]
a[0] = a[-1]
a[-1] = temp_var
print(f"After swap {a}")



