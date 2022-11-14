lst = [1,2,3,4,"f","g","r","s"]
str_1 = []
int_1 = []

for i in lst:
    if type(i) == str:
        str_1.append(i)
    elif type(i) == int:
        int_1.append(i)
print(str_1 ,f"the length of the string is {len(str_1)}")
print(int_1 , f" the length is the integers is {len(int_1)}")


