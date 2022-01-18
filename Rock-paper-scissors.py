# Rock paper and scissors game, with random module

import random

options = ['Rock', 'Paper', 'Scissors']

comp_option = random.choice(options)

user = False

computer_score = 0

user_score = 0

# Using a while loop to iterate the game

while True:
    user = input('Rock, Paper or Scissors?').capitalize()
    # Conditions for the game
    if user == comp_option:
        print("It's a tie!!")
    elif user == 'Rock':
        if comp_option == 'Paper':
            print('You lose!', comp_option, 'covers', user)
            computer_score += 1
        else:
            print('You win!', user, 'win', comp_option)
            user_score += 1
    elif user == 'Paper':
        if comp_option == 'Scissors':
            print('You lost again!', comp_option, 'cuts', user)
            computer_score += 1
        else:
            print('You win!', user, 'wrapped', comp_option)
            user_score += 1
    elif user == 'Scissors':
        if comp_option == 'Rock':
            print('You lost!', comp_option, 'crashes', user)
            computer_score += 1
        else:
            print('You win!', user, 'cuts', comp_option)
            user_score += 1
    elif user == 'End':
        print('Final scores:')
        print(f'Computer score: {computer_score}')
        print(f'User score: {user_score}')
        break