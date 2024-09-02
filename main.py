import random

low = 1
high = 100

# number = random.randint(low, high)  # 1에서 20사이에서 랜덤 숫자 출력
# number = random.random()  # float 숫자 between 0 and 1

# choice method
options = ("rock", "scissors", "paper")
option = random.choice(options)  # choice 메소드, 범위 내에서 랜덤 선택
print(option)

# shuffle method
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
# ['10', '4', '8', 'J', '3', '5', '9', 'A', '7', '2', 'Q', '6', 'K']
print(cards)
