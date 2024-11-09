import random

# Use random.choice to pick a random option from the list
computer_choice = random.choice(['Scissors', 'rock', 'paper'])
user_choice = input('Do you want rock, paper, or scissors?\n')

if computer_choice == user_choice:
    print('Tie')
elif user_choice == 'rock' and computer_choice == 'Scissors':
    print('You win')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win')
elif user_choice == 'Scissors' and computer_choice == 'paper':
    print('You win')
else:
    print(f'You lose to the computer. Computer chose {computer_choice}')

