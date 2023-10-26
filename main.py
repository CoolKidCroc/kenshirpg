import os  # Import the os module
from character_creation import character_creation
from game_world import game_world

def intro_screen():
    print("========================================")
    print("           Kenshi Text RPG              ")
    print("========================================")
    print("\nIn a post-apocalyptic wasteland, you find yourself amidst the ruins of the Hub.")
    print("Starting with nothing but the clothes on your back, your journey begins at level 1.")
    print("Facing adversity, bandits, and countless challenges, you strive to grow stronger, amass wealth,")
    print("and gather resources. The ultimate goal? To become influential and affluent enough to")
    print("join a caravan, leaving the Hub's desolation behind and venturing to prosperous new cities.")
    print("\nBut remember, every choice you make, every battle you face, shapes your destiny.")
    print("\nThis game was coded in Python by Cool Kid Croc with the help of his best friend, CHATGPT4.")
    print("\nThis game is a fan made project as proof of concept and does not intend to infringe Lofi Games or their game Kenshi.")
    print("\nFor more adventures, visit: www.youtube.com/coolkidcroc\n")
    input("Press Enter to embark on your journey...")
        
def game_over(character):
    print("\n------------------------")
    print("        GAME OVER       ")
    print("------------------------\n")
    input("Press Enter to return to the intro screen...")
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    return None  # Return None to indicate a new game

def start_game():
    character = None  # Initialize character as None
    
    while True:
        intro_screen()

        print("\nWelcome to Your Game!")
        input("Press Enter to begin...")

        if character is None:
            # Character creation only if character is None (new game or after game over)
            character = character_creation()

        if character:  # Ensure character creation was successful
            while True:
                # Enter the game world
                game_result = game_world(character)

                if game_result == "game_over":
                    character = game_over(character)  # Restart the game with a new character
                    break  # Exit the current game loop to restart
                elif game_result == "win":
                    # Handle win condition (if needed)
                    pass
                else:
                    # Handle other game outcomes (if needed)
                    pass

if __name__ == "__main__":
    start_game()