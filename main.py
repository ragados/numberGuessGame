# Number Guessing Game
# Coded by Dev Sodagar, Nov 29th 2021
import random

# Machine determines a random number between 0 and 99
target_num = random.randrange(100)


# Primary Game Function
def guess_game(target):
    while True:
        # User Inputs number
        invalid = False
        numerals = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
        guess = input("Enter your guess integer number between 0 and 99: ")
        # Data entry validation - Had trouble with the escaping here.
        for char in range(len(guess)):
            if guess[char] not in numerals:
                invalid = True
        if invalid is True:
            print("Entry is not a valid number. Please try again.")
        # Machine returns Guess number and higher, lower or Correct!
        else:
            guess_num = int(guess)
            if guess_num > 99:
                print("Guess outside of stated range. Please try again.")
            elif guess_num == target:
                print("Guess " + guess + " is Correct!")
                break
            elif guess_num > target:
                print("Guess " + guess + " is High")
            else:
                print("Guess " + guess + " is Low")


def guess_game_good(target):
    while True:
        # User Inputs number
        guess = input("Enter your guess integer number between 0 and 99: ")
        # Data entry validation - Had trouble with the escaping here.
        # This is a longwinded way of doing .isnumeric() & is.decimal() checks
        numerals = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
        for char in range(len(guess)):
            if guess[char] not in numerals:
                print("Entry is not a valid number. Please try again.")
                continue
        # Machine returns Guess number and higher, lower or Correct!
        guess_num = int(guess)
        if guess_num > 99:
            print("Guess outside of stated range. Please try again.")
        elif guess_num == target:
            print("Guess " + guess + " is Correct!")
            break
        elif guess_num > target:
            print("Guess " + guess + " is High")
        else:
            print("Guess " + guess + " is Low")


print(target_num)
# guess_game(target_num)
guess_game_good(target_num)
