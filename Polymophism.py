## Polymophism with functions and methods

class Shape:
    def area(self):
        return "The area of the figure"
    
#Derived Class 1

class Rectangle (Shape):
    def __init__(self, length, height):
        self.length=length
        self.height=height

    def area(self):
        return self.length * self.height
    
## Derived Class

class Circle (Shape):
    def __init__(self,radius):
        self.radius=radius

    def area (self):
        return (self.radius **2) * 3.142

# Function that demonstrate Polymorphism
def print_area(calculate):
    print(f"The area  = {calculate.area()}")

rectangle = Rectangle(4,5)
circle = Circle (7)

print_area(rectangle)
print_area(circle)

## Abstract Class

from abc import ABC, abstractmethod

## Define an abstract class

class Vehicle (ABC):
    @abstractmethod
    def start_engine (self):
        pass

class Car (Vehicle):
    def start_engine(self):
        return "Car Engine Started"
    
#Derived class 2

class Motorcycle (Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

def start_vehicle (vehicle):
    print(vehicle.start_engine())

# create objects of Car and Motorcycle

car = Car()
motorcycle = Motorcycle()

start_vehicle(car)
start_vehicle (motorcycle)