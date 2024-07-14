import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins\n"
      + "Rock vs Scissors -> Rock wins\n"
      + "Paper vs Scissors -> Scissor wins\n")

while True:
    print("Enter your choice\n1 - Rock\n2 - Paper\n3 - Scissors\n")

    choice = int(input("Enter your choice: "))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please ☺'))

    if choice == 1:
        user_choice = 'Rock'
    elif choice == 2:
        user_choice = 'Paper'
    else:
        user_choice = 'Scissors'

    print('User choice is:\n', user_choice)
    print('Now it\'s Computer\'s Turn....')

    bot_choice = random.randint(1, 3)

    while bot_choice == choice:
        bot_choice = random.randint(1, 3)

    if bot_choice == 1:
        bot_choice_name = 'RocK'
    elif bot_choice == 2:
        bot_choice_name = 'Paper'
    else:
        bot_choice_name = 'Scissors'

    print("Computer choice is:\n", bot_choice_name)
    print(user_choice, 'Vs', bot_choice_name)

    if choice == bot_choice:
        print('It\'s a Draw', end="")
        result = "DRAW"

    if (choice == 1 and bot_choice == 2):
        print('Paper wins =>', end="")
        result = 'Paper'
    elif (choice == 2 and bot_choice == 1):
        print('Paper wins =>', end="")
        result = 'Paper'

    if (choice == 1 and bot_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (choice == 3 and bot_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'RocK'

    if (choice == 2 and bot_choice == 3):
        print('Scissors wins =>', end="")
        result = 'Scissors'
    elif (choice == 3 and bot_choice == 2):
        print('Scissors wins =>', end="")
        result = 'Rock'

    if result == 'DRAW':
        print("<== It's a tie ==>")
    if result == user_choice:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing")
