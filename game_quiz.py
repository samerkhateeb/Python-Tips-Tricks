

# Dictionary Key / Valu Pairs
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "D"
}


# two dimentional array
options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A.True", "B. False", "C. sometimes", "D. What's Earth?"]]

play = ''


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key, value in questions.items():
        print('---------------------------')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input('Enter (A, B, C, D): ').upper()
        guesses.append(guess)
        correct_guesses += check_answer(value, guess)

        question_num += 1

    display_score(correct_guesses, guesses)
    play_again()
# -----------------------------


def check_answer(correct_answer, guest_answer):
    if correct_answer == guest_answer:
        print('CORRECT !!')
        return 1
    else:
        print('Wrong')
        return 0
# -----------------------------


def display_score(correct_guesses, guesses):

    for key, value in questions.items():
        print(' {} '.format(value), end="")
    print('')
    for i in guesses:
        print(' {} '.format(i), end="")
    print('')
    print('Your Score Is: {} %'.format(int((correct_guesses/len(guesses))*100)))
# -----------------------------


def play_again():
    if play is None:
        play = 'firstplay'
        return 'YES'
    else:
        return input('Would You Like To Play Again? Yes / No: ').upper()

# -----------------------------


while play_again() == 'YES':
    new_game()

print('Byeeeee !!!! ')
