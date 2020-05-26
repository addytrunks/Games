# random module
import random
import time
# rules
print("----------------------Welcome To Rock  Paper and Scissors-----------------")
print("Rules of this game are \n Rock vs scissor >== Rock wins \n Paper vs Rock >== Paper wins \n Paper vs Scissors "
      ">== Scissors win")
print("Type 'rock' ,'paper' or 'scissors' when asked::")
# user choice
while True:
        rock = 'rock'
        paper = 'paper'
        scissors = 'scissors'

        user_choice = input("Make your guess:")
        user_choice.lower()


        print("Your choice is ",user_choice)
        # computer guess
        print("Computer's choice is generating........")
        time.sleep(2)
        com_choice = random.randint(1,3)
        if com_choice == 1:
            com_choice = 'rock'
        elif com_choice == 2:
            com_choice = 'paper'
        elif com_choice == 3:
            com_choice = "scissors"
        print("Computer's guess is ", com_choice)
        print("Matchmaking...")
        time.sleep(1.25)
        #condition

        if user_choice == com_choice:
            print("Its a tie")

        if user_choice == 'rock':
                if com_choice == 'scissors':
                        print("Congrats!You win")
                elif com_choice == 'paper':
                        print("Oops..You lose")

        if user_choice == 'paper':
                if com_choice == 'rock':
                        print("Congrats!You win")
                elif com_choice == 'scissors':
                        print("Oops..You lose")

        if user_choice == 'scissors':
                if com_choice == 'paper':
                        print("Congrats!You win")
                elif com_choice == 'rock':
                        print("Oops..You lose")

        print("Want to play again ?Press 'Y' or 'N'" )
        ans = input()
        if ans == 'N' or ans == 'n':
                    break
        print()
