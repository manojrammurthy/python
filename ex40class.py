class Employee:
    'common base class for all employees'
    empcount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount +=1
    def displaycount(self):
        print "Total employee %d " % Employee.empcount
        
    def displayEmployee(self):
        print "name :", self.name , "Salary :", self.salary
            
emp1 = Employee("manoj", 2000)
emp2 = Employee("raj", 1500)

emp1.displayEmployee()
emp1.displaycount()
print "number of employees is %d:" % Employee.empcount
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__          