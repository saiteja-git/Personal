def outerfun(fun):

    def inner(*args, **kwargs):
        var = fun(*args, **kwargs)
        get_divi_of_two = var/2
        return f"the value of function {get_divi_of_two }"
    return inner


@outerfun
def addtion(a, b):
    return a + b

print(addtion(15, 30))