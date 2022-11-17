# Write a Python Program to Check Common Letters in Two Input Strings?

input1 = str(input("Enter first input: "))
input2 = str(input("Enter second input: "))

lst1 = []
lst2 = []
final_1 = []

for i in input1:
    lst1.append(i)

for j in input2:
    lst2.append(j)

for i in lst1:
    if i in lst2:
        final_1.append(i)
        print(final_1)
if len(final_1)<1:
    print("These is no common letters")







