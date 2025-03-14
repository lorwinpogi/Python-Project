import random

def get_user_choice():
    """Gets the user's choice."""
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice! Try again.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    """Gets the computer's random choice."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    """Determines the winner of the game."""
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Main function to play the game."""
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
play_game()
