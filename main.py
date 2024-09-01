# collection = multiple values를 가지는 하나의 변수
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# *************************************************
# List
# *************************************************
# fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits)) # object의 속성과, 메서드를 알수 있다.
# print(help(fruits)) # List object의 속성과 메서드의 설명을 확인할 수 있다.
# print(len(fruits)) # List object의 크기를 알수 있다.
# print("apple" in fruits) # True 리턴

# List: changeable
# fruits[0] = "pineapple"
# print(fruits) # ['pineapple', 'orange', 'banana', 'coconut']

# List: append 메소드, 제일 마지막에 요소 추가
# fruits.append("pineapple")
# print(fruits)

# List: remove 메소드, 항목을 찾아서 없앤다.
# fruits.remove("apple")
# print(fruits) # ['orange', 'banana', 'coconut']

# List: insert 메소드, 해당 위치에 항목을 삽입한다..
# fruits.insert(0, "pineapple") # 위치:0, 항목:"pineapple"
# print(fruits)  # ['pineapple', 'apple', 'orange', 'banana', 'coconut']

# List: sort 메소드, 알파벳 순서로.
# fruits.sort()
# print(fruits)  # ['apple', 'banana', 'coconut', 'orange']

# List: revers 메소드, list item 역순, 알파벳 순서와 관계 X.
# fruits.reverse()
# print(fruits)  # ['coconut', 'banana', 'orange', 'apple']

# List: clear 메소드, list item 삭제.
# fruits.clear()
# print(fruits)  # []

# List: index 메소드, 해당항목의 index 값 리턴.
# print(fruits.index("apple")) # 0, 항목이 없으면 error


# print(fruits[::-1]) # ['coconut', 'banana', 'orange', 'apple']
# for fruit in fruits:
#     print(fruit)


# *************************************************
# Set: 순서가 없다, 변경 불가, 추가/삭제는 OK, 중복 불가
# *************************************************
# fruits = {"apple", "orange", "banana", "coconut"}
# print(fruits)  # {'apple', 'banana', 'orange', 'coconut'} 순서가 없다
# print(len(fruits))
# print("apple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()

# for fruit in fruits:
#     print(fruit)

# print(fruits)

# *************************************************
# Tuple: 순서가 있다, 변경 불가, 중복가능, List보다 빨라
# *************************************************

fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(dir(fruits)) # object의 속성과, 메서드를 알수 있다.
# print(help(fruits)) # Tuple object의 속성과 메서드의 설명을 확인할 수 있다.
# print(len(fruits)) # Tuple object의 크기를 알수 있다.
# print("apple" in fruits)  # True 리턴

# print(fruits.index("orange"))
# print(fruits.count("coconut"))
# print(fruits[3])
