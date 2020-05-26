import random
import time


#choosing the faces(heads or tails)
user_toss_choice = input("Heads or Tails?:").lower()#this will convert the string into lower case

if user_toss_choice == 'heads':
    comp_toss_choice = 'tails'
    print('Deciding the toss winner...')
    time.sleep(2)
elif user_toss_choice == 'tails':
    comp_toss_choice = 'heads'
    print('Deciding the toss winner...')
    time.sleep(2)

choice = ['heads','tails']

flip_the_coin = random.choice(choice)#will choose the toss winner

if user_toss_choice == flip_the_coin:
    user_choice = input("You won the toss!Do you want to bat or bowl?").lower()
    print()

    if user_choice == 'bat':
        print("You chose to bat and you will be playing against the computer.")
        print("--------------------------- First Innings ----------------------------------")
        user_score = 0
        while True:
            user_runs = int(input("Play your turn:"))

            while user_runs > 6 or user_runs < 1:
                user_runs = int(input("Wrong input.Enter numbers from 1 to 6:"))

            comp = random.randint(1,6)
            if user_runs != comp:
                user_score = user_score + user_runs
                print("Your current score is ",user_score)#user batting

            elif user_runs == comp:
                print("You lost.")
                print("Your score is {}".format(user_score))
                time.sleep(3)
                break

        print("------------------------------- Second Innings ----------------------------------------")
        print("Now its computer's turn to bat.")


        comp_score = 0
        while True:
            user_bowl = int(input("Play your turn:"))
            comp_runs = random.randint(1,6)

            if user_bowl != comp_runs:
                comp_score = comp_score + comp_runs
                print("Computer's score is  ", comp_score)
            elif user_bowl == comp_runs:
                print("Congrats!You scored a wicket!")
                if user_score > comp_score:
                    print("You win the match!")
                    break
                elif user_score < comp_score:
                    print("User score = {} , Computer score = {} ".format(user_score,comp_score))
                    print("You lose the match")
                    break
                elif user_score == comp_score:
                    print("User score = {} , computer score = {}".format(user_score, comp_score))
                    print("Its a tie.")
                    break

    if user_choice == 'bowl':
        print("You chose to bowl and you will be playing against the computer.")
        print("--------------------------- First Innings ----------------------------------")
        comp_score = 0
        while True:
            user_bowl = int(input("Play your turn:"))

            while user_bowl > 6 or user_bowl < 1:
                user_runs = int(input("Wrong input.Enter numbers from 1 to 6:"))

            comp_runs = random.randint(1,6)
            if comp_runs != user_bowl:
                comp_score = comp_score + comp_runs
                print("Computer's current score is ",comp_score)
            elif comp_runs == user_bowl:
                print("You scored a wicket.")
                time.sleep(3)
                break

        print("------------------------------- Second Innings ----------------------------------------")
        print("Now its your turn to bat.")


        user_score = 0
        while True:
            user_runs = int(input("Play your turn:"))

            while user_runs > 6 or user_runs < 1:
                user_runs = int(input("Wrong input.Enter numbers from 1 to 6:"))

            comp = random.randint(1, 6)

            if user_runs != comp:
                user_score = user_score + user_runs
                print("Your current score is ", user_score)
            elif user_runs == comp:
                print("You lost a wicket.")

                if user_score > comp_score:
                    print("Congrats!You win the match!")
                    break
                elif user_score < comp_score:
                    print("Computer score = {},User score = {}".format(comp_score,user_score))
                    print("Oops ): You lost the match.Better luck next time")
                    break
                elif user_score == comp_score:
                    print("User score = {} , computer score = {}".format(user_score, comp_score))
                    print("Its a tie.")
                    break


elif user_toss_choice != flip_the_coin:#this means you lost the toss
    comp_toss = random.randint(1,2)

    if comp_toss == 1:#making the computer to choose bat or bowl
        print("Computer won the toss chose to bat")
        print("--------------------------- First Innings ----------------------------------")
        comp_score = 0
        while True:
            user_bowl = int(input("Play your turn:"))

            while user_bowl > 6 or user_bowl < 1:
                user_runs = int(input("Wrong input.Enter numbers from 1 to 6:"))

            comp_runs = random.randint(1, 6)
            if comp_runs != user_bowl:
                comp_score = comp_score + comp_runs
                print("Computer's current score is ", comp_score)
            elif comp_runs == user_bowl:
                print("You scored a wicket.")
                print()
                time.sleep(3)
                break

        print("---------------------------- Second Innings --------------------------")
        print("Now its your turn to bat.")

        user_score = 0
        while True:
            user_runs = int(input("Play your turn:"))

            while user_runs > 6 or user_runs < 1:
                user_runs = int(input("Wrong input.Enter numbers from 1 to 6:"))

            comp = random.randint(1, 6)

            if user_runs != comp:
                user_score = user_score + user_runs
                print("Your current score is ", user_score)
            elif user_runs == comp:
                print("You lost a wicket.")

                if user_score > comp_score:
                    print("Congrats!You win the match!")
                    break
                elif user_score < comp_score:
                    print("User score = {} , computer score = {}".format(user_score, comp_score))
                    print("Oops ): You lost the match.Better luck next time")
                    break
                elif user_score == comp_score:
                    print("User score = {} , computer score = {}".format(user_score, comp_score))
                    print("Its a tie.")
                    break


    elif comp_toss == 2:
        print("Computer won the toss chose to bowl")
        print("------------------------------ First Innings ----------------------------")

        user_score = 0
        while True:
            user_runs = int(input("Play your turn:"))

            while user_runs > 6 or user_runs < 1:
                user_runs = int(input("Wrong input.Enter numbers from 1 to 6:"))

            comp = random.randint(1, 6)
            if user_runs != comp:
                user_score = user_score + user_runs
                print("Your current score is ", user_score)
            elif user_runs == comp:
                print("You lost.")
                print("Your score is {}".format(user_score))
                time.sleep(3)
                break

        print("----------------------- Second Innings --------------------------")
        print("Now its your turn to play bowling.")

        comp_score = 0
        while True:
            user_bowl = int(input("Play your turn:"))
            comp_runs = random.randint(1, 6)

            if user_bowl != comp_runs:
                comp_score = comp_score + comp_runs
                print("Computer's score is  ", comp_score)
            elif user_bowl == comp_runs:
                print("Congrats!You scored a wicket!")
                if user_score > comp_score:
                    print("You win the match!")
                    break
                elif user_score < comp_score:
                    print("User score = {} , computer score = {}".format(user_score, comp_score))
                    print("You lose the match")
                    break
                elif user_score == comp_score:
                    print("User score = {} , computer score = {}".format(user_score, comp_score))
                    print("Its a tie.")
                    break








