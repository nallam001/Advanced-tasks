# 1. Transform and Clean Data
products = [" LAPTOP ", "phone ", " Tablet", "CAMERA "]
cleaned_products = list(map(lambda p: p.strip().title(), products))
print(cleaned_products)
# Output: ['Laptop', 'Phone', 'Tablet', 'Camera']


# 2. Convert Temperatures (Celsius → Fahrenheit)
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (9/5) * c + 32, celsius))
print(fahrenheit)
# Output: [32.0, 50.0, 68.0, 86.0, 104.0]


# 3. Apply Multiple Transformations
nums = [1, 2, 3, 4, 5]
transformed_nums = list(map(lambda x: x**2 + 10, nums))
print(transformed_nums)
# Output: [11, 14, 19, 26, 35]


# 4. Extract First and Last Characters
words = ["python", "lambda", "programming", "map", "function"]
first_last = list(map(lambda w: (w[0], w[-1]), words))
print(first_last)
# Output: [('p', 'n'), ('l', 'a'), ('p', 'g'), ('m', 'p'), ('f', 'n')]


# 5. Nested Map Transformation (Challenge)
marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]
increased_marks = list(map(lambda row: list(map(lambda x: round(x * 1.05), row)),
marks))
print(increased_marks)
# Output: [[47, 84, 74], [95, 63, 105], [92, 80, 97]]


# 6. Normalize a List of Numbers Between 0 and 1
numbers = [10, 20, 30, 40, 50]
min_val, max_val = min(numbers), max(numbers)
normalized = list(map(lambda x: (x - min_val) / (max_val - min_val), numbers))
print(normalized)
# Example Output: [0.0, 0.25, 0.5, 0.75, 1.0]


# 7. Extract the Length of Each Word in Every Sentence
sentences = ["Python is fun", "Map and lambda are useful"]
word_lengths = list(map(lambda s: list(map(lambda w: len(w), s.split())), sentences))
print(word_lengths)
# Output: [[6, 2, 3], [3, 3, 6, 3, 6]]