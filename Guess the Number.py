import random

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>Guess the number<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("In this game, the computer will randomly choose a number and you have to guess it right.\nHelp will be provided")

try:
    user_input = int(input("Enter a two digit number:"))
except ValueError:
    print("Invalid input.Try again")
    user_input = int(input("Enter a two digit number:"))
finally:
    pass
print()


computer = random.randint(1,100)

while user_input >= 100 or user_input <=0 :
    print("Do not enter a number more than two digits or less than two digits")
    user_input = int(input("Enter a two digit number:"))
    print()

while user_input != computer:
    if user_input < computer:
        print("You need to guess higher")
        user_input = int(input("Enter a two digit number:"))
        print()

    elif user_input > computer:
        print("You need to guess lower ")
        user_input = int(input("Enter a two digit number:"))
        print()



print("The number was {} .You guessed it right".format(computer))
