# for loops
# 형식: for x in range(1,11):
# 유용함수 range(start, end(exclusive),[step])
# continue - skip, break - loop 탈출


# 1,2,3,4,5,6,~10
# for x in range(1, 11):
#     print(x)

# 10,9,8,7,.. 1
# for x in reversed(range(1, 11)):
#     print(x)

# print("HAPPY NEW YEAR!")

# 1,3,5,... 9
# for x in range(1, 11, 2):
#     print(x)

# List
# items = [1, 2, 33, 56, 78]
# for item in items:
#     print(item)

# String
# card_number = "1234-5678-9099-3456"
# for x in card_number:
#     print(x)

# Skip - continue
# for x in range(1, 21):
#     if x == 13:
#         continue # 13일때 14로 바로 넘어간다
#     else:
#         print(x)

# Exit - break
for x in range(1, 21):
    if x == 13:
        break  # 13일때 탈출
    else:
        print(x)
