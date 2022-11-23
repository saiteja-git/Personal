class Faulty_calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
user = input("Please select in symbols - add(+), sub(-), mul(*), div(/), exit(q) :- ")
user1 = int(input("Enter first value: "))
user2 = int(input("Enter second value: "))

while True:
    def calsi(self):
            #user = input("Please select in symbols - add(+), sub(-), mul(*), div(/), exit(q) :- ")
            #user1 = int(input("Enter first value: "))
            #user2 = int(input("Enter second value: "))

        if user == '+':
            return self.a + self.b
        if user == '-':
            return self.a - self.b
        if user == 'q':
            return "Terminating"
    break

obj = Faulty_calculator(user1,user2)
print(obj.calsi())


