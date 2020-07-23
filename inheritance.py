class Parent:
    def __init__(self,lastname,eyeColor):
        print("Parent Constructor called")
        self.lastname,self.eyeColor = lastname,eyeColor

class Child(Parent):
    def __init__(self,lastname,eyeColor,noOfToys):
        print("Child Contructor called")
        Parent.__init__(self,lastname,eyeColor)
        self.noOfToys = noOfToys


c1 = Child("c1","red",102020)
print(c1.lastname)
print(c1.noOfToys)
