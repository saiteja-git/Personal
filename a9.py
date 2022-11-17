# Write a Python Program to Check Common Letters in Two Input Strings?

input1 = str(input("Enter first input: "))
input2 = str(input("Enter second input: "))

lst1 = []
lst2 = []
for i in input1:
    lst1.append(i)

for j in input2:
    lst2.append(j)

if lst1 in lst2:
    print(lst1)
else:
    print("None of the elements are matching")



   

