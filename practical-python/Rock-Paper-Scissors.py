import random

computer_choice = random.choice(['scissors', 'paper', 'rock'])
users_choice = input('Do you want - rock, paper, or scissors?\n')

if computer_choice == users_choice:
    print('TIE')
elif users_choice == 'rock' and computer_choice == 'scissors':
    print('WIN')
elif users_choice == 'paper' and computer_choice == 'rock':
    print("WIN")
elif users_choice == 'scissors' and computer_choice == "paper":
    print("WIN")
else:
    print("You lose :( and computer wins :D")