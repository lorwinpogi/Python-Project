import random

print("Welcome to the Number Guessing Game!")

# Taking user input for range and chances
upper_range = int(input("Enter the maximum range (starting from 1): "))
chances = int(input("Enter the number of chances: "))

number_to_guess = random.randint(1, upper_range)
guess_counter = 0

print(f"Great! I have chosen a number between 1 and {upper_range}. You have {chances} chances to guess it!")

while guess_counter < chances:
    guess_counter += 1
    try:
        my_guess = int(input(f'Attempt {guess_counter}/{chances} - Enter your guess: '))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if my_guess == number_to_guess:
        print(f'Congratulations! You guessed the number {number_to_guess} correctly in {guess_counter} attempts!')
        break
    elif my_guess > number_to_guess:
        print('Your guess is too high.')
    else:
        print('Your guess is too low.')

    if guess_counter == chances:
        print(f'Sorry, you used all your chances. The number was {number_to_guess}. Better luck next time!')
