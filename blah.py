import random

user_call = input('Call heads or tails')
comput_call = random.randint(1, 2)#spelling mistake wrote 'randit' instead of 'randint'
if (comput_call == 1):#called 'call' instead of 'comput_call'
    out_toss = 'heads'
else:
    out_toss = 'tails'
if (user_call == out_toss):
    print('you win :) choose bat/bowl')
    user_choice = input('bat/bowl??')
    if (user_choice == 'bat'):
        print('1st innings')
        score = 0
        while True:
            u = int(input('play your turn'))  # missed to close the bracket
            y = random.randint(1, 6)
            print('computer plays', y)
            if (u != y):
                score = score + u
                print(score)
            else:
                print('oops! wicket lost')
                print(score)
                break
        print('2nd innings')
        cscore = 0
        while True:
            u = int(input('play your turn'))  # didnt close the bracket
            y = random.randint(1, 6)
            print('computer plays ', y)
            if (y != u):
                cscore = cscore + y
                print(cscore)
            elif (y == u):
                print('yay :) wicket taken')
                print(cscore)
                if (cscore == score):
                    print('woah! a tie')
                    break
                elif (score > cscore):
                    print('bravo, u win the match')
                    break
                elif (cscore > score):  # did not indent
                    print(cscore)
                    print('oops you loose')
                    break

    elif (user_choice == 'bowl'):#did not indent
        print('1st innings')
        cscore = 0
        while True:
            u = int(input('play your turn'))  # missed a bracket
            y = random.randint(1, 6)
            print('computer plays', y)
            if (y != u):
                cscore = cscore + y
                print(cscore)
            elif (y == u):
                print('yay :) wicket taken')
                print(cscore)
                break
        print('2nd innings')
        score = 0
        while True:
            u = int(input('play your turn'))  # missed a bracket
            y = random.randint(1, 6)
            print('computer plays', y)
            if (u != y):
                score = score + u
                print(score)
            elif (u == y):
                print('oops! wicket lost')
                print(score)

                if (cscore == score):
                    print('woah! a tie')
                    break
                elif (cscore > score):
                    print('oops you loose')
                    break
                elif (score > cscore):
                    print(score)
                    print('bravo, u win')
                    break
    else:
        x = random.randint(1, 2)
        if x == 1:
            print('computer chooses to bat first')
            print('1st innings')
        cscore = 0

        while True:
            u = int(input('play your turn'))#missed a bracket
            y = random.randint(1, 6)
            print('computer plays ', y)
            if (y != u):
                cscore = cscore + y
                print(cscore)
            elif (y == u):
                print('yay :) wicket taken')
                print(cscore)
                break

        print('2nd innings')
        score = 0
        while True:
            u = int(input('play your turn'))#missed a bracket
            y = random.randint(1, 6)
            print('computer plays', y)
            if (u != y):
                score = score + u
                print(score)
            elif (u == y):
                print('oops! wicket lost')
                print(score)
                if (cscore == score):
                    print('woah! a tie')
                    break
                elif (cscore > score):
                    print('oops you loose')
                    break
                elif (score > cscore):
                    print(score)
                    print('bravo, u win')#missed a indent
                    break
            elif x == 2:
                print('computer chooses to bowl')
                print('1st innings')
                score = 0

            while True:
                u = int(input('play your turn'))#missed a bracket
                y = random.randint(1, 6)
                print('computer plays', y)
                if (u != y):
                    score = score + u
                    print(score)
                else:
                    print('oops! wicket lost')
                    print(score)
                    break

                print('2nd innings')
                cscore = 0
            while True:
                u = int(input('play your turn'))#missed a bracket
                y = random.randint(1, 6)
                print('computer plays', y)
                if (y != u):
                    cscore = cscore + y
                    print(cscore)
                elif (y == u):
                    print('yay :) wicket taken')
                    print(cscore)
                    if (cscore == score):
                        print('woah! a tie')
                        break
                    elif (score > cscore):
                        print('bravo, u win the match')
                        break
                    elif (cscore > score):
                        print(cscore)
                        print('oops you loose')
                        break

