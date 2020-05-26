import random

username = input("Hi.Welcome to Magic ball 8.Please enter your name:").capitalize()
print()

question = input(username + ",Please ask any questions and the magic ball will answer you:")

answers = ['It is certain.',
         'It is decidedly so.',
         'Without a doubt.',
         'Yes – definitely.',
         'You may rely on it.',
         'As I see it, yes.',
         'Most likely.',
         'Outlook good.',
         'Yes.',
         'Signs point to yes.',
         'Reply hazy, try again.',
         'Ask again later.',
         'Better not tell you now.',
         'Cannot predict now.',
         'Concentrate and ask again.',
         'Do not count on it.',
         'My reply is no.',
         'My sources say no.',
         'Outlook not so good.',
         'Very doubtful.'
    ]

magic_ball_answer = random.choice(answers)
print(magic_ball_answer)

