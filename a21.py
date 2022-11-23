# function to Check Common Letters in Two Input Strings?


lst1 = []
lst2 = []
output = []
user1 = str(input("Enter first string: "))
user2 = str(input("Enter second string: "))

def fun_common():

    for i in user1:
        lst1.append(i)
    for j in user2:
        lst2.append(j)

    for i in lst2:
        if i in lst1:
            output.append(i)
    return output

print(fun_common())








