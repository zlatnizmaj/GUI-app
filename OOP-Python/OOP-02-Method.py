# There are three types of methods available in python.
# They are: 1. Instance method 2. Class method 3. Static method
class DecoratorExample01:
    "Example Class"
    def __init__(self):
        "Example Setup"
        print("Hello, World!")
        self.name = "Decorator_Example"
# As an instance method uses ‘self’ as argument, it is compulsory to pass ‘cls’ as argument

    def example_function(self):
        "This method is an instance method"
        print("I\'m an instance method!")
        print(f"My name is {self.name}")

# They can’t access specific instance data, but they can call other static methods
de = DecoratorExample01()
de.example_function()

class DecoratorExample02:
    def __init__(self):
        print("Hello, World!")

    @classmethod
    def example_function(cls):
        """This method is a class method"""
        print("I\'m a class method")
        cls.some_other_function()

    @staticmethod
    def some_other_function():
        print("Hello!")
# Static method: Cannot access anything else in the class. Totally self-contained code.
de02 = DecoratorExample02()
de02.example_function()