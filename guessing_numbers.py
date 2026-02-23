import random

def get_valid_int(prompt):
    """Helper function to get a valid integer from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def play_game():
    """Logic for exactly one round of the number guessing game."""
    print("\n--- Number Guessing Game ---")
    start = get_valid_int("Enter the starting range: ")
    end = get_valid_int("Enter the ending range: ")
    
    if start >= end:
        print("Range error: Starting number must be less than ending number.")
        return

    secret_number = random.randint(start, end)
    attempts = 0
    
    print(f"I've picked a number between {start} and {end}. Good luck!")

    while True:
        guess = get_valid_int("Enter your guess: ")
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You found the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            if guess < secret_number / 2:
                print("Too low! Not even close.")
            else:
                print("Low, but getting closer.")
        else:
            if guess > secret_number * 2:
                print("Too high! Way off.")
            else:
                print("High, but you're in the neighborhood.")

def main():
    """Main entry point for the guessing game."""
    while True:
        play_game()
        if input("\nPlay another round? (y/n): ").strip().lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()


