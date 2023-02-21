import random

choices = ["rock", "paper", "scissors"]
play_again = "yes"
while play_again == 'yes':

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    print("computer: ", computer)
    print("You: ", player)

    if player == "rock":
        if computer == "rock":
            print('You are equal !!')
        elif computer == "paper":
            print('You are LOST !!!')
        elif computer == "scissors":
            print('YOU WON :)')

    elif player == "scissors":
        if computer == "rock":
            print('You LOST !!')
        elif computer == "paper":
            print('You WON :)')
        elif computer == "scissors":
            print('You are  equal')

    elif player == "paper":
        if computer == "rock":
            print('You WON :)')
        elif computer == "paper":
            print('You are equal !!!')
        elif computer == "scissors":
            print('Yu LOST :)')

    play_again = input('Do You Want To Play Again yes / no?').lower()

    if play_again != "yes":
        break

print('Bye !!!')
