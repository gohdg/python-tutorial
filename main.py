# Python number guessing game
import random

# lowest_num = 1
# highest_num = 100
# is_running = True
# guesses = 0

# answer = random.randint(lowest_num, highest_num)

# # print(answer)

# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num} ")

# while is_running:
#     guess = input("Enter your guess: ")

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1

#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {
#                   lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low! Try again!")
#         elif guess > answer:
#             print("Too high! Try again!")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False

#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")

# while True:
#     guess_num = int(input("Enther the number you guess: ").replace(" ", ""))
#     if guess_num == answer:
#         break
#     elif answer > guess_num:
#         print(f"Greater than {guess_num}")
#     else:
#         print(f"Less than {guess_num}")

# print(f"Correct! you hit the answer {answer}")


# Python rock, scissors, paper game

options = ("rock", "scissors", "paper")

playing = True

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, scissors, paper): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n) ").lower() == "y":
        playing = False

print("Thanks for playing!")
