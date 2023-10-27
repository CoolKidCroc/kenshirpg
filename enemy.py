import random

class Enemy:
    def __init__(self, name, strength, dexterity, toughness, health, energy, athletics):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.toughness = toughness
        self.athletics = athletics
        self.health = health
        self.energy = energy
        
enemy_stats = {
    'bonedog': Enemy('Bonedog', 8, 5, 10, 75, 30, 5),
    'beakthing': Enemy('Beakthing', 15, 10, 10, 150, 35, 6),
    'fogmen': Enemy('Fogmen', 6, 6, 6, 50, 40, 6),
    'dust_bandit': Enemy('Dust Bandit', 7, 8, 6, 70, 35, 7),
    'starving_vagrant': Enemy('Starving Vagrant', 5, 6, 4, 40, 25, 4),
    'swamp_ninja': Enemy('Swamp Ninja', 6, 7, 8, 60, 40, 6),
    'hive_bandit': Enemy('Hive Bandit', 8, 5, 9, 80, 30, 5),
    'beak_thing_alpha': Enemy('Beakthing Alpha', 20, 12, 12, 200, 40, 8),
    'red_saber': Enemy('Red Saber', 9, 7, 9, 90, 40, 7),
    'sand_ninja': Enemy('Sand Ninja', 7, 10, 7, 70, 45, 7),
    'skin_spider': Enemy('Skin Spider', 5, 5, 12, 100, 30, 6),
    'garru': Enemy('Garru', 7, 5, 7, 60, 25, 7),
    'river_raptor': Enemy('River Raptor', 5, 7, 5, 45, 30, 8),
    'scrawny_cannibal': Enemy('Scrawny Cannibal', 5, 5, 4, 40, 30, 6),
    'skimmer': Enemy('Skimmer', 9, 6, 9, 80, 35, 7),
    'manslaver': Enemy('Manslaver', 7, 5, 6, 70, 30, 6),
    'escaped_servant': Enemy('Escaped Servant', 5, 6, 4, 50, 35, 5),
    'wandering_assassin': Enemy('Wandering Assassin', 8, 8, 7, 80, 40, 7),
    'gorillo': Enemy('Gorillo', 12, 4, 10, 120, 40, 10),
    'landbat': Enemy('Landbat', 6, 7, 5, 60, 35, 7),
    'grass_pirate': Enemy('Grass Pirate', 7, 7, 7, 75, 35, 6),
    'blood_raider': Enemy('Blood Raider', 8, 8, 7, 110, 38, 7),
    'black_dragon': Enemy('Black Dragon', 9, 9, 8, 90, 40, 7),
    'krall': Enemy('Krall', 8, 6, 10, 110, 32, 7),
    'lost_drone': Enemy('Lost Drone', 7, 4, 11, 70, 31, 6),
    'desert_dervish': Enemy('Desert Dervish', 9, 10, 6, 85, 37, 7),
    'iron_spider': Enemy('Iron Spider', 25, 25, 25, 250, 30, 8),
    'mud_ronin': Enemy('Mud Ronin', 6, 8, 8, 65, 38, 6),
    'thrall': Enemy('Thrall', 8, 5, 9, 90, 32, 7),
    'stone_raptor': Enemy('Stone Raptor', 7, 9, 6, 70, 35, 7),
    'leviathan_pup': Enemy('Leviathan Pup', 10, 5, 12, 500, 40, 9),
    'leviathan': Enemy('Leviathan', 50, 12, 18, 5800, 40, 9),
    'sun_guard': Enemy('Sun Guard', 9, 7, 8, 100, 38, 8),
    'sentinel': Enemy('Sentinel', 8, 8, 8, 85, 37, 7),
    'prowler': Enemy('Prowler', 8, 9, 7, 90, 36, 7),
    'doomed_monk': Enemy('Doomed Monk', 7, 7, 7, 70, 35, 6),
    'ruined_guardian': Enemy('Ruined Guardian', 9, 6, 9, 95, 33, 8),
    'desert_bandit': Enemy('Desert Bandit', 7, 9, 6, 75, 36, 7),
}

def random_enemy(character):
    # Ensure that the 'level' attribute is present in the character dictionary
    if 'level' not in character:
        character['level'] = 1

    # Create a list of potential enemies based on player's level
    potential_enemies = [enemy for enemy, base_stats in enemy_stats.items()
                         if (character['level'] <= 5 and base_stats.health <= 100) or
                         (character['level'] > 5 and base_stats.health > 100)]

    # Randomly select an enemy type from the potential list
    selected_enemy = random.choice(potential_enemies)

    # Get the base stats for the selected enemy type
    base_stats = enemy_stats[selected_enemy]

    # Modify stats based on character level (slightly reducing the scaling)
    modified_strength = base_stats.strength + character['level']
    modified_toughness = base_stats.toughness + character['level']
    modified_health = base_stats.health + character['level'] * 5

    modified_enemy = Enemy(
    base_stats.name,
    modified_strength,
    base_stats.dexterity,
    modified_toughness,
    modified_health,          # Corrected the order here
    base_stats.energy,
    base_stats.athletics      # And here
)

    # Calculate rewards based on the enemy's health
    cats_reward = max(1, modified_health // 20)
    experience_reward = max(1, modified_health // 10)

    # Construct the final enemy dictionary
    enemy_dict = {
        'name': selected_enemy,
        'strength': modified_strength,
        'dexterity': base_stats.dexterity,
        'toughness': modified_toughness,
        'athletics': base_stats.athletics,
        'health': modified_health,
        'energy': base_stats.energy,
        'rewards': {
            'cats': cats_reward,
            'experience': experience_reward,
        }
    }

    return modified_enemy, enemy_dict