# Write a Python Program to Count the Number of Vowels in a String?

name = "sAiteja"
vowels = "aeiou"
vowels_1 = vowels.upper()

lst =[]
for i in name:
    if i in vowels or i in vowels_1:
        lst.append(i)
print(f"The count of Vowels in a given string is {len(lst)} and those are {lst}")






