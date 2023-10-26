from character_creation import display_character_status

def check_level_up(character):
    while character['experience'] >= (100 * character['level']):
        character['experience'] -= (100 * character['level'])
        level_up(character, character['level'] + 1)
        

LEVEL_UP_POINTS = 100  # Global constant for level up

def level_up(character):
    """Check if the character has enough XP to level up and apply level up benefits."""
    while character['experience'] >= LEVEL_UP_POINTS:
        character['experience'] -= LEVEL_UP_POINTS
        new_level = character['level'] + 1
        print(f"Congratulations! You have reached level {new_level}!")
        character['strength'] += 5
        character['max_health'] += 20
        character['max_energy'] += 5
        character['health'] = min(character['health'] + 20, character['max_health'])
        character['level'] = new_level 

def rest(character):
    character['health'] = character['max_health']
    character['energy'] = character['max_energy']

def decrease_energy(character, hours):
    energy_decrease_rate = 2
    energy_decrease = energy_decrease_rate * hours
    character['energy'] = max(0, character['energy'] - energy_decrease)
    
def view_character_stats(character):
    print(display_character_status(character))
    