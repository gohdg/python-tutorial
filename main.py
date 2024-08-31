# conditional expression = ternary operator, 한줄 if-else 문
# X if condition else Y

from sys import maxunicode


num = 6
a = 6
b = 7
age = 13
temperature = 20
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# result = "Even" if (num % 2 == 0) else "Odd"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >=13 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)
