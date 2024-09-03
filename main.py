# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop
# 반복 가능한 객체를 말한다.List, Tuple, Set, string, Dictionary

# ** List
# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number, end=" ")

# print()
# # 역순
# for number in reversed(numbers):
#     print(number, end="-")

# ** Set
# fruits = {"apple", "orange", "banana", "coconut"}

# for fruit in fruits:
#     print(fruit)

# ** Set은 순서가 없다. 따라서 reversed 사용 X
# for fruit in reversed(fruits):
#     print(fruit)

# ** String
# name = "Bro Code"

# for character in name:
#     print(character, end=" ")

# ** Dictionary
my_dictionary = {"A": 1, "B": 2, "C": 3}

# default로 key를 리턴한다
for key in my_dictionary:
    print(key)

for value in my_dictionary.values():
    print(value)

for key, value in my_dictionary.items():
    print(f"{key} = {value}")
