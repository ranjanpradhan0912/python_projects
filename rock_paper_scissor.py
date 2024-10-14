import random

ROCK='r'
PAPER='p'
SCISSORS='s'

emojis = {
    ROCK: '🪨',
    PAPER: '📃',
    SCISSORS: '✂️'
}


choices = (tuple(emojis.keys()))

def user_input():
    while True:
        user_ch = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user_ch in choices:
            return user_ch
        else:
            print("Invalid choice!")
            continue


def display_choice(user_choice, computer_choice):
    print(f'You choose {emojis[user_choice]}')
    print(f'Computer choose {emojis[computer_choice]}')


def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('No result')
    elif ((user_choice == SCISSORS and computer_choice == PAPER) or
          (user_choice == PAPER and computer_choice == ROCK) or
          (user_choice == ROCK and computer_choice == SCISSORS)):
        print('You win')
    else:
        print('Computer Win')


def play_game():
    while True:
        user_choice = user_input()
        computer_choice = random.choice(choices)
        display_choice(user_choice, computer_choice)
        decide_winner(user_choice, computer_choice)
        replay = input("Continue?(y/n):").lower()

        if replay == 'y' or replay == 'n':
            if replay == 'n':
                break
        else:
            print("Invalid choice!")

play_game()