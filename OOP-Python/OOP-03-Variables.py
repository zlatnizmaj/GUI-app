# In python programming, we have three types of variables,
# They are: 1. Class variable 2. Instance variable 3. Global variable

# Class variable
class Test():
    class_var = "Class Variable"
    class_var2 = "Class Variable2"

# print(class_var) --> error, not defined
x = Test()
print(x.class_var)
print(x.class_var2)