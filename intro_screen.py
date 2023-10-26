from character_creation import character_creation  # Import the character_creation function

def intro_screen():
    print("Welcome to the World of Kenshi Text RPG")
    print("1. New Game")
    print("2. Load Game")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        # Start a new game (move to character creation)
        character_creation()  # Call the character_creation function
    elif choice == '2':
        # Load a saved game (implement this)
        print("Loading a saved game...")
        # Add code to load a saved game
    elif choice == '3':
        print("Goodbye!")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# You can call the intro_screen function here if you want to start the game from this script.
