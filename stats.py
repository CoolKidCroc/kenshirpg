from character_creation import display_character_status

LEVEL_UP_POINTS = 100  # Global constant for level up

def check_level_up(character):
    while character['experience'] >= LEVEL_UP_POINTS:
        character['experience'] -= LEVEL_UP_POINTS
        level_up(character)

def level_up(character):
    """Apply level up benefits to the character."""
    character['level'] += 1
    print(f"Congratulations! You have reached level {character['level']}!")
    character['strength'] += 5
    character['max_health'] += 20
    character['max_energy'] += 5
    character['health'] = min(character['health'] + 20, character['max_health'])

def rest(character):
    character['health'] = character['max_health']
    character['energy'] = character['max_energy']

def decrease_energy(character, hours):
    energy_decrease_rate = 2
    energy_decrease = energy_decrease_rate * hours
    character['energy'] = max(0, character['energy'] - energy_decrease)

def view_character_stats(character):
    print(display_character_status(character))