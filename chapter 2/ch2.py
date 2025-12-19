class Vector3D:
def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

#Overload using (+)
def __add__(self, other):
return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
#Overload using (-)
def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
#Overload using (*)
def __mul__(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z
    
#Implementation :
def __repr__(self):
    return f"Vector3D({self.x}, {self.y}, {self.z})"

#Question 2: Positive Number Descriptor

#Create descriptor class named positive
class Positive:
def __set_name__(self, owner, name):
    self.name = f"_{name}"
    
def __get__(self, obj, objtype):
    return getattr(obj, self.name, 0)
def __set__(self, obj, value)

#Ensure attribute can only be non-negative
def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        setattr(obj, self.name, value)


#Apply descriptor to bank account class
class BankAccount:
    balance = Positive()   
def __init__(self, initial_balance=0):
    self.balance = initial_balance



#Question 3 : Point Class with slots

#Define a class
class Point:
    __slots__ = ['x', 'y']     
def __init__(self, x, y):
    self.x = x
    self.y = y

#Create instance
p = Point(10, 20)
print(p.x, p.y)

#Try add third attribute
p.z = 5

#Disassembling a Simple Function

import dis
def calculate_sum(a, b):
return a + b
dis.dis(calculate_sum)
