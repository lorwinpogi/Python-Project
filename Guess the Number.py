import random

def get_user_input(prompt, error_message="Invalid input! Please enter a number."):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)

def setup_game():
    print("Welcome to the Number Guessing Game!")
    upper_range = get_user_input("Enter the maximum range (starting from 1): ")
    chances = get_user_input("Enter the number of chances: ")
    return upper_range, chances

def play_game(upper_range, chances):
    number_to_guess = random.randint(1, upper_range)
    print(f"Great! I have chosen a number between 1 and {upper_range}. You have {chances} chances to guess it!")
    
    for attempt in range(1, chances + 1):
        guess = get_user_input(f'Attempt {attempt}/{chances} - Enter your guess: ')
        
        if guess == number_to_guess:
            print(f'Congratulations! You guessed the number {number_to_guess} correctly in {attempt} attempts!')
            return
        elif guess > number_to_guess:
            print('Your guess is too high.')
        else:
            print('Your guess is too low.')
    
    print(f'Sorry, you used all your chances. The number was {number_to_guess}. Better luck next time!')

def main():
    upper_range, chances = setup_game()
    play_game(upper_range, chances)

if __name__ == "__main__":
    main()
