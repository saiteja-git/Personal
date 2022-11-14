lst = []
i=1
count = 5
while i:
    lst.append(input("Enter values: "))
    i+=1
    if len(lst) == count:
        user_guide = input("Please enter'Y' to continue or press 'N' to stop : ")
        if user_guide == 'Y':
            pass
            count+=5
            print(lst)
        else:
            break
print(lst)








        



        
