'''
Python is an object oriented programming language
Almost everything that is used in python is an object with properties associated to them
A class is a like an object constructor or a blueprint to create an object

The __init__() Function 

-All classes have a function called __init__(), which is always executed wen the class is being initiated
- It is used to assign values to object properties ot other operations that is required when the object is being created

The __str__() Function
- The __str__() function defines the string representation of an object , it converts an object representation into a string representation

self Parameter
- It is reference to the class object created
- It is used to access the properties and functions of the object

The pass Statement
- class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

'''
class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name},(and my age is {self.age})" # provides string representation when priting a class object
    
    def introduction(self):
        print("Hi, My name is " , self.name)
        


p1 = Person("John" , "19")

print(p1)
p1.introduction()
print(p1.name)
print(p1.age)
        