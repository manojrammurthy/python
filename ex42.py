class Animal(object):
    pass

# dog is a class
class Dog(animal):
    
    def __init__(self, name):
        #has a object name
        self.name = name
        
# cat is a class animal
class Cat(Animal):
        
        def __init__(self, name):
            # has a object name
            self.name = name

# person is a class
class person(object):
    
    def __init__(self, name):
        # has a object name
        self.name = name
        #person has a pet of some kind
        self.pet = None
        
# Employee is a class of type person
class Employee(person):
    
    def __init__(self, name, salary):
        #
        super(Employee, self).__init__(name)
        #
        self.salary = salary

#
class Fish(object):
    pass
    
#
class salmon(Fish):
    pass
    
class halibut(Fish):
    pass
    
#rover is a dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = salmon()

## ??
harry = halibut()
    