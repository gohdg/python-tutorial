# Concession stand program 극장 매점

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25
        }

cart = []
total = 0

print("---------- MENU -----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------------")

# 구매 아이템 등록
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

# 금액 계산
print("-------- YOUR ORDER ---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total is: ${total:.2f}")
