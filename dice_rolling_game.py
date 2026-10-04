import random


def roll_dice(num_dice):
    """Simulates rolling a specified number of dice."""
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def main():
    """Main function to handle user interaction for the dice rolling game."""
    print("--- Professional Dice Roller ---")
    roll_count = 0
    
    while True:
        choice = input("\nRoll the dice? (y/n): ").strip().lower()
        
        if choice == 'y':
            try:
                num_dice = int(input("How many dice would you like to roll?: "))
                if num_dice <= 0:
                    print("Please enter a positive number.")
                    continue
                    
                rolls = roll_dice(num_dice)
                print("Results:", " ".join([f"({r})" for r in rolls]))
                
                roll_count += len(rolls)
                print(f"Total dice rolled in this session: {roll_count}")
                
            except ValueError:
                print("Error: Please enter a valid integer for the number of dice.")
        elif choice == 'n':
            print("Thanks for using the Dice Roller. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
