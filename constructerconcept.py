class Student:
    def __init__(self, name,age,roll,marks,):  
        self.name = name
        self.age = age
        self.roll = roll
        self.marks = marks
    def printdetail(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"roll is{self.roll}")
        print(f"marks is {self.marks}")
        print("_" * 30)

s1 = Student("prinka", 23, 1034, 3000)
s2 = Student("adil", 24, 1000, 3000)
s1.printdetail()
s2.printdetail()
