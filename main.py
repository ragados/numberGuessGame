# Number Guessing Game
# Coded by Dev Sodagar, Nov 29th 2021
import random

# Machine determines a random number between 0 and 99
target_num = random.randrange(99)

# Primary Game Function
def guess_game(target):
    i = 0
    while i < 1:
        # User Inputs number
        guess = input("Enter your guess integer number between 0 and 99: ")
        # Machine returns Guess number and higher, lower or Correct!
        if int(guess) == target:
            print("Guess " + guess + " is Correct!")
            i = i + 1
            return
        if int(guess) > target:
            print("Guess " + guess + " is High")
        else:
            print("Guess " + guess + " is Low")

print(target_num)
guess_game(target_num)
