class Info:
    age = 30  # class variable

    # default constructor
    def __init__(self, a, b):
        self.firstNumber = a  # class instance variable
        self.secondNumber = b
        print("This is call automatically when object is crated")

    def printInfo(self):
        print("I am Haris")

    def sum(self):
        print(self.firstNumber + self.secondNumber)


obj = Info(2, 3)
obj.printInfo()
print(obj.age)

obj2 = Info(5, 6)
obj2.sum()

