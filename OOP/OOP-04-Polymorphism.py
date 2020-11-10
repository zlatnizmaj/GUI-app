# Polymorphism
# Basically, we can use features of the class in other classes,
# avoiding the same feature of other classes.
class shark():
    def swim(self):
        print("Shark can swim")

class whale():
    def swim(self):
        print("Whale can swim")

x = shark()
y = whale()
x.swim()
y.swim()
#  when an instance of shark class is created it will return
#  a feature of shark class and not of whale class and vice-versa

def in_practice(name):
    name.swim()

in_practice(x)
in_practice(y)
# we have made another function which will take any argument and returns the function.
# Thus, due to polymorphism it will return different methods.