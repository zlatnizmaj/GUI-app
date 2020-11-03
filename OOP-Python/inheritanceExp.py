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