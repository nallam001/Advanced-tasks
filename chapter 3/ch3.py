#Question 1: remove_vowels function
def remove_vowels(text):
vowels = 'aeiouAEIOU'
return ''.join(char for char in text if char not in vowels)

#Question 2: map() and filter() with odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 1, numbers)))

#Question 3: Fibonacci with lru_cache
from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fib(n):
if n < 2:
return n
return fib(n-1) + fib(n-2)

start = time.time()
result1 = fib(35)
end1 = time.time() - start 
def fib_no_cache(n):
if n < 2:
return n
return fib_no_cache(n-1) + fib_no_cache(n-2) 
start = time.time()
result2 = fib_no_cache(30)
end2 = time.time() – start

#Question 4: make_adder closure
def make_adder(n):
def adder(x):
return n + x
return adder 
add5 = make_adder(5)

print(add5(3)) 


#Question 5: apply_twice function
def apply_twice(func, value):
return func(func(value))

print(apply_twice(lambda x: x + 1, 5))  # 7

#Question 6: ETL pipeline
from collections import Counter 
def etl_pipeline(texts, stopwords=None):
if stopwords is None:
stopwords = {"the", "a", "an", "is", "in", "on", "at", "and", "or"}    
words = []
for text in texts:
words.extend(text.lower().split())    
filtered = [word for word in words if word not in stopwords]     
return dict(Counter(filtered))


#Question 7: Custom reduce()

def my_reduce(func, iterable, initial=None):
it = iter(iterable)   
if initial is None:
value = next(it)
else:
value = initial
    
for element in it:
value = func(value, element)
     
return value





#Question 8: log_call decorator
def log_call(func):
def wrapper(*args, **kwargs):
print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
result = func(*args, **kwargs)
print(f"{func.__name__} returned: {result}") return result
return wrapper
 
@log_call
def add(a, b):
    return a + b
