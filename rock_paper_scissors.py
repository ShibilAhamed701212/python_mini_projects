import random


def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer."""
    return random.choice(['r', 'p', 's'])

def get_user_choice():
    """Prompts the user for their choice and validates input."""
    options = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    while True:
        choice = input("Press r for Rock, p for Paper, s for Scissors: ").strip().lower()
        if choice in options:
            return choice
        print("Invalid choice. Please try again.")

def determine_winner(user, computer):
    """Determines the winner of the game."""
    if user == computer:
        return "It's a Draw!"
    
    wins = {('r', 's'), ('s', 'p'), ('p', 'r')}
    if (user, computer) in wins:
        return "You Win!"
    return "You Lose!"

def main():
    """Main entry point for the game."""
    print("--- Rock Paper Scissors Game ---")
    
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        
        choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
        print(f"\nYou chose: {choices[user_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nThanks for playing!")
