# Context Manager: Timer : 

import time
   
  class Timer:
      def __enter__(self):
         self.start = time.time()
        return self
     
   def __exit__(self, exc_type, exc_val, exc_tb):
         self.end = time.time()
        print(f"Execution took {self.end - self.start:.2f} seconds")
 
with Timer():
    for i in range(1000000):
        pass
  

# Generator: even_numbers : 

 def even_numbers(n):
     for i in range(2, n + 1, 2):
         yield i
  
 # Usage
 for num in even_numbers(10):
     print(num)
 

# Coroutine: filter_positive : 

def filter_positive():
      while True:
          num = yield
          if num > 0:
              print(f"Positive number: {num}")
   
  co = filter_positive()
  next(co)
 co.send(-3)
 co.send(5)
 co.send(0)
  

# Factory Pattern : 

class Circle:
      def draw(self):
          print("Drawing a Circle")
   
  class Square:
      def draw(self):
          print("Drawing a Square")
   
 def shape_factory(shape_type):
     if shape_type == "circle":
        return Circle()
     elif shape_type == "square":
         return Square()
     else:
         raise ValueError("Unknown shape type")
  
 shape = shape_factory("circle")
 shape.draw()
  

# Observer Pattern : 

class Subject:
     def __init__(self):
         self._observers = []
     
     def attach(self, observer):
         self._observers.append(observer)
     
     def detach(self, observer):
         self._observers.remove(observer)
     
     def notify(self, message):
         for observer in self._observers:
             observer.update(message)
  
 class Observer:
     def update(self, message):
         print(f"Received update: {message}")
  
 subject = Subject()
 obs1 = Observer()
 obs2 = Observer()
  
 subject.attach(obs1)
 subject.attach(obs2)
 subject.notify("Update available!")