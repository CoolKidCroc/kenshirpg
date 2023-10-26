import random
import datetime

# Define the character dictionary
character = {
    'name': '',
    'race': '',
    'strength': 0,
    'dexterity': 0,
    'toughness': 0,
    'athletics': 0,
    'level': 1,
    'experience': 0,
    'health': 0,
    'energy': 0,
    'time': (1, datetime.time(12, 0)),
    'cats': 0,
    'max_strength': 0,
    'max_dexterity': 0,
    'max_toughness': 0,
    'max_health': 0,
    'max_energy': 0,
}

def get_character_name():
    while True:
        name = input("What is your name? ")
        if name:
            return name
        print("Name cannot be empty. Please enter a name.")

def choose_race():
    while True:
        print("Who would you like to be?")
        print("1. Human")
        print("2. Hiver")
        print("3. Shek")
        print("4. Skeleton")

        race_choice = input("Enter the number corresponding to your race choice: ")

        if race_choice in ['1', '2', '3', '4']:
            return race_choice
        print("Invalid choice. Please select 1, 2, 3, or 4.")

def reroll_stats(character, min_stat_value, max_stat_value):
    # Reset character stats
    character['strength'] = random.randint(min_stat_value, max_stat_value)
    character['dexterity'] = random.randint(min_stat_value, max_stat_value)
    character['toughness'] = random.randint(min_stat_value, max_stat_value)
    character['athletics'] = random.randint(min_stat_value, max_stat_value)
    
    # Update energy based on the rerolled toughness, and also update max_energy.
    character['energy'] = min(character['energy'] + (character['toughness'] * 2), character['max_energy'])
    
    # Update health based on the rerolled toughness, but don't exceed the max_health.
    character['health'] = min(character['health'] + (character['toughness'] * 10), character['max_health'])
    
    print("Stats rerolled successfully.")

def display_character_status(character):
    formatted_text = "<><><><><><><><><><><><><><><>\n"
    formatted_text += "Character stats:\n"
    formatted_text += f"Name: {character['name']}\n"
    formatted_text += f"Race: {character['race']}\n"
    formatted_text += f"Strength: {character['strength']} / {character['max_strength']}\n"
    formatted_text += f"Dexterity: {character['dexterity']} / {character['max_dexterity']}\n"
    formatted_text += f"Toughness: {character['toughness']} / {character['max_toughness']}\n"
    formatted_text += f"Health: {character['health']} / {character['max_health']}\n"
    formatted_text += f"Energy: {character['energy']} / {character['max_energy']}\n"
    formatted_text += f"Athletics: {character['athletics']}\n"
    formatted_text += f"Level: {character['level']}\n"
    formatted_text += f"Experience: {character['experience']}\n"
    formatted_text += f"Time: Day {character['time'][0]}, {character['time'][1].strftime('%H:%M')}\n"
    formatted_text += f"Cats: {character['cats']}\n"
    formatted_text += "<><><><><><><><><><><><><><><>\n"
    return formatted_text

def character_creation():
    print("Character Creation")
    name = get_character_name()
    race_choice = choose_race()

    # Convert race_choice into race string
    race_dict = {
        '1': 'Human',
        '2': 'Hiver',
        '3': 'Shek',
        '4': 'Skeleton',
    }
    chosen_race = race_dict.get(race_choice, "Unknown")

    character['name'] = name
    character['race'] = chosen_race
    character['level'] = 1
    character['experience'] = 0
    character['health'] = 0
    character['energy'] = 0
    character['time'] = (1, datetime.time(12, 0))
        
    # Set stats and max values based on the chosen race
    if race_choice == '1':  # Human
        character['strength'] = character['max_strength'] = 10
        character['dexterity'] = character['max_dexterity'] = 10
        character['toughness'] = character['max_toughness'] = 10
        character['health'] = character['max_health'] = 100
        character['athletics'] = 5
        character['cats'] = 0
    elif race_choice == '2':  # Hiver
        character['strength'] = character['max_strength'] = 8
        character['dexterity'] = character['max_dexterity'] = 12
        character['toughness'] = character['max_toughness'] = 8
        character['health'] = character['max_health'] = 80
        character['athletics'] = 8
        character['cats'] = 0
    elif race_choice == '3':  # Shek
        character['strength'] = character['max_strength'] = 12
        character['dexterity'] = character['max_dexterity'] = 8
        character['toughness'] = character['max_toughness'] = 12
        character['health'] = character['max_health'] = 120
        character['athletics'] = 3
        character['cats'] = 0
    elif race_choice == '4':  # Skeleton
        character['strength'] = character['max_strength'] = 11
        character['dexterity'] = character['max_dexterity'] = 9
        character['toughness'] = character['max_toughness'] = 10
        character['health'] = character['max_health'] = 90
        character['athletics'] = 6
        character['cats'] = 0

    # Display the character's stats
    print(display_character_status(character))

    while True:
        # Reroll stats
        print("Do you want to reroll your character's stats? (yes/no): ")
        reroll_choice = input()
        if reroll_choice.lower() == 'yes':
            reroll_stats(character, 5, 15)
            print(display_character_status(character))
        else:
            break

    # Set max energy based on toughness
    character['max_energy'] = character['toughness'] * 10
    character['energy'] = character['max_energy']

    return character

if __name__ == "__main__":
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
    print("For more adventures, visit: www.youtube.com/coolkidcroc")
    input("\nPress Enter to embark on your journey...")
    
    while True:
       character = character_creation()  # Move the character creation inside the loop
       print("New game started!")