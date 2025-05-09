''' defining mathods within a class the first parameter is always self 
and it is convention not a keyword and its play key role in python''' 

'''In Python, self is a reference to the current object (the instance).

It must be the first parameter in instance methods inside a class.

It lets you access the variables and methods of the object.'''
class Student:
    def __init__(self, name, age):
        self.name = name     
        self.age = age

    def show(self):  #emplicit self        
        print(f"Name: {self.name}, Age: {self.age}")

# Create object
s1 = Student("Alice", 21)

# Call method
s1.show()     # Python internally(implicit object) does: Student.show(s1)
