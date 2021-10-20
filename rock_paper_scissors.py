import random

computer_wins = 0
user_wins = 0

while True:
    user_input = input("Please Enter Rock/Paper/Scissors or press Q/q to quit: ").lower()
    if user_input == 'q':
        if user_wins > computer_wins:
            print(f'User score = {user_wins}')
            print(f'Computer score = {computer_wins}')
            print('User won the game')
        elif user_wins < computer_wins:
            print(f'User score = {user_wins}')
            print(f'Computer score = {computer_wins}')
            print('Computer won the game')
        else:
            print(f'User score = {user_wins}')
            print(f'Computer score = {computer_wins}')
        quit()
    choices = ['rock', 'paper', 'scissors']
    if user_input not in choices:
        print("Please enter the right choice")
        continue
    random_choice = random.choice(choices)
    print(f"computer picked {random_choice}")
    if user_input == 'rock' and random_choice == 'paper':
        print('You lost')
        computer_wins += 1
        continue
    elif user_input == 'paper' and random_choice == 'scissors':
        print('You lost')
        computer_wins += 1
        continue
    elif user_input == 'scissors' and random_choice == 'rock':
        print('You lost')
        computer_wins += 1
        continue
    else:
        print('You win')
        user_wins += 1
        continue

