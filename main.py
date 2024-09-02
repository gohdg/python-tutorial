# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"
            }

# print(dir(capitals))
# print(capitals.get("Japan")) # Key가 없으면 None 리턴, 있으면 value 리턴

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})  # key가 없으면 insert, 있으면 value 업데이트
# capitals.update({"USA": "Detroit"})

# capitals.pop("China")
# print(capitals)

# (capitals.popitem())  # 마지막 아이템을 추출한다.
# print(capitals)
# print(len(capitals))

# capitals.clear()
# print(capitals)

# print("Moscow" in capitals)

# keys = capitals.keys()
# print(keys) # dict_keys(['USA', 'India', 'China', 'Russia'])
# for key in keys:
#     print(key)

# values = capitals.values()
# print(values) # dict_values(['Washington D.C', 'New Delhi', 'Beijing', 'Moscow'])
# for value in values:
#     print(value)

# items = capitals.items()
# print(items) # dict_items([('USA', 'Washington D.C'), ('India', 'New Delhi'), ('China', 'Beijing'), ('Russia', 'Moscow')])
# for key, value in items:
#     print(f"{key}: {value}")
