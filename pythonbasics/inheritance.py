from app import Parent

class Child(Parent):
    pass

c1 = Child()
print(c1.name)

class Person:

    def __init__(self,fname,lname) -> None:
        self.firstname = fname
        self.lastname = lname 
    
    def printname(self):

        print("Hi my name is", self.firstname , self.lastname)
    

'''
INHERITANCE 
- concept in which the child class inherits the properties and methods of its parent class
- When creating a child class and if we use an __init__ funtion it overrides the __init__ function of the parent class and we need to makea call to the init function of the parent by usinga super() function 
'''

# class Student(Person): #Here the child class has no additional properties or methods of its own
#     pass

class Student(Person):
    
    def __init__(self, fname, lname , year) -> None:
        super().__init__(fname, lname) # inheriting the properties of Person
        self.graduationyear = year

    def getDetails(self):

        print("Hi i am", self.firstname , self.lastname, "and i will be graduating in" , self.graduationyear)

x = Person("Sahil" , "Tuladhar")
y = Student("Salina" , 'Gurung' , '2024')
x.printname()
y.printname()
y.getDetails()
