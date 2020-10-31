# Instance
# snippet how to instance is created
class Employee:
    "Common base class for all employees"
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print(f"Total Employee {Employee.empCount}")

    def displayEmployee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

"This would create first object of Employee class"
emp1 = Employee("Nam", 9000)
"This would create second object of Employee class"
emp2 = Employee("Pooh", 7000)

emp1.displayEmployee()
emp2.displayEmployee()

print(f"Total Employee {Employee.empCount}")