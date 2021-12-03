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
            # Check input number within stated bounds
            if guess_num > 99:
                print("Guess outside of stated range. Please try again.")
            # Compare input number to target number
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
        # Replacing the original solution with .isnumeric() check
        if guess.isnumeric():
            guess_num = int(guess)
            # Check input number within stated bounds
            if guess_num > 99:
                print("Guess outside of stated range. Please try again.")
            # Compare input number to target number
            elif guess_num == target:
                print("Guess " + guess + " is Correct!")
                break
            elif guess_num > target:
                print("Guess " + guess + " is High")
            else:
                print("Guess " + guess + " is Low")
        else:
            print("Entry is not a valid number. Please try again.")


def guess_game_better(target):
    while True:
        # User Inputs number
        guess = input("Enter your guess integer number between 0 and 99: ")
        # Data entry validation - Had trouble with the escaping here.
        # Probably the most 'correct' method of acting.
        # This is explicitly catching the error and moving past it.
        try:
            guess_num = int(guess)
        except ValueError as err:
            print('Input error:', err)
            continue
        # Check input number within stated bounds
        if guess_num > 99:
            print("Guess outside of stated range. Please try again.")
        # Compare input number to target number
        elif guess_num == target:
            print("Guess " + guess + " is Correct!")
            break
        elif guess_num > target:
            print("Guess " + guess + " is High")
        else:
            print("Guess " + guess + " is Low")


print(target_num)
# guess_game(target_num)
guess_game_better(target_num)
