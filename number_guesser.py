import random # importing random module

print("Welcome to Number Guesser Hope u will have fun")

random_range = int(input("Enter the upper range for Number Guesser:"))
random_number = random.randint(0, random_range)
guesses=0
if random_range < 2:
    print("Please enter the upper range for Number Guesser greater than 1 next time")
    quit()

while True:
    guesses+=1
    guess = int(input(f"Please guess the number b/w 0 to {random_range}:"))
    if guess < random_number:
        print('Guess is too low')
        continue
    elif guess > random_number:
        print('Guess is too high')
        continue
    else:
        print(f"Yay!! you guessed the right number in {guesses} guesses")
        break
