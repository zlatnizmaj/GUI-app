# https://towardsdatascience.com/understand-inheritance-in-python-74f8e3025f3c
"""
Inheritance is when a class is created based on an existing class,
and the new class inherits the attributes and methods from the existing class.
The new class is usually called “child class”, and the existing class is called “parent class”.

Liskov substitution principle:
if S is a subtype of T, then objects of type T may be replaced with objects of type S

It means that the child class will inherit attributes, methods, and implementations from the parent class.
It’s allowed to modify and add new features, but not delete features from the parent.

"""
class Student:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

class HighSchoolStudent(Student):
    def __init__(self, name, age, school):
        super().__init__(name, age, school)
        self.grade_range = [11, 13]

class PrimarySchoolStudent(Student):
    def __init__(self, name, age, school):
        super().__init__(name, age, school)
        self.grade_range = [1, 6]

high_school_student_A = HighSchoolStudent("Linda", 16, "high-school-1")
primary_school_student_B = PrimarySchoolStudent("Johan", 8, "primary-school-1")

print(high_school_student_A.grade_range)
print(primary_school_student_B.grade_range)

"""
The ancestor of every class: Object
Class object is the ancestor of every class in Python. 
If you do object.__bases__, you will get an empty value.
"""
"""
Single inheritance is when the class inherits from only one class
"""
"""
Exp01: I have a parent class Job with an attribute person_name and a method task. 
I want to create a child class Teacher inherited from Job and override task with “teach student”.
The UML diagram looks like this. This is a very simple example, 
and the only thing we need to do is to override method task()
"""
# inheritance-override-method
class Job:
    def __init__(self, person_name):
        self.name = person_name

    def task(self):
        print("Working")

class Teacher(Job):
    def task(self):
        print("teach students")

teacher = Teacher("NamNg")
teacher.task() # teach students

"""
Example 2: We still use Job as the parent class, but this time, in addition to overriding task(), 
I also want to create the child class Teacher with an extra attribute school_name.
In the UML diagram, we would find a new attribute in the class Teacher

school is a new attribute, so it means that we need to override __init__ method to add the attribute. 
In this example, we will use a built-in function super().
In a nutshell, super() returns an object that delegates method calls to a parent class. 
It allows you to reuse the attributes and behaviors from the parent class. 
In the code below, super().__init__ will execute everything inside Job.__init__ to avoid duplicated code.
"""
class Teacher02(Job):
    def __init__(self, person_name, school):
        super().__init__(person_name)
        self.school = school

    def task(self):
        print("Working")

teacher02 = Teacher02("DiepNg", "HCMUE")
print(teacher02.school)
# HCMUE
# super() can be used in other methods, so you can also invoke super().task() in the child class.
"""
Exp3: In addition to the example 2, 
I want to prevent class Job from being instantiated because there is no job named Job.
To make this happen, we will talk about the concept of abstract class in Python. 
Abstract class is a class that is intended to be inherited but never instantiated. 
Python provides abc module to define abstract base classes 
and @abstractmethod decorator to define abstract methods.
"""
from abc import ABC, abstractmethod

class Job2(ABC):
    def __init__(self, person_name):
        self.name = person_name

    @abstractmethod
    def task(self):
        pass

# job = Job2("Gao") # TypeError: Can't instantiate abstract class Job2 with abstract methods task

"""
Multi inheritance
Multi inheritance is when the class inherits from more than one parent class.
"""
class Dad:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "black"
        self.city = "Amsterdam"
    def swim(self):
        print("I can swim")

class Mum:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "brown"
        self.city = "Amsterdam"
    def dance(self):
        print("I can dance")

class Kid(Dad, Mum):
    pass
"""
Ok, so the question comes. What is the default eye_color of akid object? 
When it comes to multi inheritance, the child class will first search the attribute in its own class, 
if not, then search in its parent classes in depth-first, left-right order. 
This is called Method Resolution Order (MRO) in Python. 
MRO defines how Python searches for inherited methods.
"""
print(Kid.__mro__)
kid = Kid()
print(kid.eye_color) # blue
print(kid.city) # Amsterdam

kid.swim()
kid.dance()

class Kid2(Dad, Mum):
    def __init__(self):
        Mum.__init__(self) # inherit attributes only from class Mum

kid2 = Kid2()
print(kid2.eye_color) # brown

# test "git commit -a"
