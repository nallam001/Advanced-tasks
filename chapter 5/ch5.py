#Problem 1: Rectangle Class
class Rectangle:
def __init__(self, width, height):
self.width = width
self.height = height

def area(self):
return self.width * self.height

def perimeter(self):
return 2 * (self.width + self.height)

# Test
rect = Rectangle(10, 5)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")


#Problem 2: Employee Class

class Employee:
def __init__(self, name, employee_id, salary):
self.name = name
self.employee_id = employee_id
self.salary = salary

@classmethod
def from_string(cls, employee_str):
name, emp_id, salary = employee_str.split(',')
return cls(name, emp_id, float(salary))
    
def display_employee_info(self):
print(f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}")

# Test
emp1 = Employee("John Doe", "E123", 50000)
emp2 = Employee.from_string("Jane Smith,E124,60000")
emp1.display_employee_info()
emp2.display_employee_info()



#Problem 3: Vehicle Hierarchy
class Vehicle:
 def move(self):
       print("Vehicle is moving")

class Car(Vehicle):
  def move(self):
       print("Car is driving")

 class Bike(Vehicle):
  def move(self):
    print("Bike is cycling")

# Test polymorphism
vehicles = [Vehicle(), Car(), Bike()]
for vehicle in vehicles:
vehicle.move()




#Problem 4: Vector Class with Operator Overloading


class Vector:
def __init__(self, x, y):
self.x = x
self.y = y

def __add__(self, other):
return Vector(self.x + other.x, self.y + other.y)

def __sub__(self, other):
return Vector(self.x - other.x, self.y - other.y)

def __mul__(self, other):
return self.x * other.x + self.y * other.y

def __repr__(self):

# Test
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 - v2)
print(v1 * v2)




#Problem 5: Shape Polymorphism Function

class Shape:
def area(self):
raise NotImplementedError
 
class Circle(Shape):
def __init__(self, radius):
self.radius = radius
  
def area(self):
import math
return math.pi * self.radius ** 2

class Rectangle(Shape):
def __init__(self, width, height):
self.width = width
self.height = height   
def area(self):
return self.width * self.height
 
def print_shape_area(shape):
print(f"Area: {shape.area()}")
 
# Test polymorphism
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
print_shape_area(shape)
