#Bytecode Inspection:

def square(x):
return x * x

def multiply(a, b):
return a * b 

# Bytecode analysis
print("Square function bytecode:")
dis.dis(square)

print("\nMultiply function bytecode:")
dis.dis(multiply)

#Dynamic Typing in Action:
data = 5
print(type(data))  

data = [1, 2, 3]
print(type(data)) 

def my_func():
pass
data = my_func
print(type(data)) 

#AST Exploration:
import ast
code = "y = (4 * 5) - 3"
tree = ast.parse(code)
print(ast.dump(tree, indent=4))

#Mutability and Object Identity:
my_list = [10, 20, 30]
print(id(my_list))   
my_list.append(40)
print(id(my_list)) 
