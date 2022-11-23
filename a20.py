# function to find vowels in a string

lst =[]
def fun_vowels(word):
    vowels = "aeiou"
    vowels_1 = vowels.upper()
    for i in word:
        if i in vowels or i in vowels_1:
            lst.append(i)
    return lst

print(fun_vowels("sAiteja"))




