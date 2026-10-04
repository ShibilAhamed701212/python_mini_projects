def display_menu():
    """Prints the action menu for the user."""
    print("\n--- Name List Manager ---")
    print("1. View Names")
    print("2. Add Name")
    print("3. Remove Name")
    print("4. Clear All Names")
    print("5. Exit")

def main():
    """Main loop for the Name List Manager."""
    names = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            if not names:
                print("The list is currently empty.")
            else:
                print("\nCurrent Names:")
                for idx, name in enumerate(names, 1):
                    print(f"{idx}. {name}")
                    
        elif choice == '2':
            new_name = input("Enter the name to add: ").strip()
            if new_name:
                names.append(new_name)
                print(f"'{new_name}' added to the list.")
            else:
                print("Name cannot be empty.")
                
        elif choice == '3':
            if not names:
                print("Nothing to remove.")
                continue
            name_to_remove = input("Enter the name to remove: ").strip()
            if name_to_remove in names:
                names.remove(name_to_remove)
                print(f"'{name_to_remove}' removed.")
            else:
                print(f"'{name_to_remove}' not found in the list.")
                
        elif choice == '4':
            confirm = input("Are you sure you want to clear the entire list? (y/n): ").strip().lower()
            if confirm == 'y':
                names.clear()
                print("List cleared.")
                
        elif choice == '5':
            print("Exiting Name List Manager. Bye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")
