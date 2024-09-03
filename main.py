# List comprehension: A concise way to create lists in Python
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

# traditional way
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

# concise way
# doubles = [expression for value in iterable if condition]
doubles = [x * 2 for x in range(1, 11)]
print(doubles)

fruits = ["apple", "orange", "banana", "coconut"]
# ['APPLE', 'ORANGE', 'BANANA', 'COCONUT']
upper_fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]  # ['a', 'o', 'b', 'c']

print(upper_fruits)
print(fruit_chars)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)  # [1, 3, 5]
print(negative_nums)  # [-2, -4, -6, -7]
print(even_nums)  # [-2, -4, -6, 8]
print(odd_nums)  # [1, 3, 5, -7]

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)  # [85, 79, 90, 61]
