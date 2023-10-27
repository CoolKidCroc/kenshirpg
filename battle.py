import random
from enemy import random_enemy
from stats import check_level_up

def enemy_encounter():
    return random.choice([True, False])

def rest(character):
    character['energy'] = min(character['energy'] + 20, 100)
    print("You take a moment to rest and restore some energy.")

def calculate_damage(strength, toughness, critical_hit=False):
    base_damage = random.randint(1, 10)
    adjusted_damage = base_damage + (strength - toughness)
    if critical_hit:
        adjusted_damage *= 2  # Double the damage for critical hits
    return max(adjusted_damage, 1)  # Ensure damage is at least 1

def calculate_critical_hit_chance(attacker_dexterity, defender_dexterity):
    if attacker_dexterity > 2 * defender_dexterity:  # 200% more dexterity
        return 1.0  # 100% critical hit chance
    else:
        return attacker_dexterity / (2 * defender_dexterity)  # Proportional chance

def handle_attack(attacker, defender):
    # Determine attacker's stats
    if isinstance(attacker, dict):
        attacker_strength = attacker.get('strength')
        attacker_dexterity = attacker.get('dexterity')
        attacker_name = attacker.get('name')
    else:  # Assume attacker is an instance of the Enemy class
        attacker_strength = attacker.strength
        attacker_dexterity = attacker.dexterity
        attacker_name = attacker.name

    # Determine defender's stats
    if isinstance(defender, dict):
        defender_toughness = defender.get('toughness')
        defender_dexterity = defender.get('dexterity')
        defender_name = defender.get('name')
    else:  # Assume defender is an instance of the Enemy class
        defender_toughness = defender.toughness
        defender_dexterity = defender.dexterity
        defender_name = defender.name

    # Check for critical hit
    critical_hit_chance = calculate_critical_hit_chance(attacker_dexterity, defender_dexterity)
    is_critical = random.random() < critical_hit_chance

    damage_dealt = calculate_damage(attacker_strength, defender_toughness, critical_hit=is_critical)
    if isinstance(defender, dict):
        defender['health'] -= damage_dealt
    else:  # Assume defender is an instance of the Enemy class
        defender.health -= damage_dealt

    # Print a message about the attack
    if is_critical:
        print(f"Critical Hit! {attacker_name} attacks {defender_name} for {damage_dealt} damage!")
    else:
        print(f"{attacker_name} attacks {defender_name} for {damage_dealt} damage!")

def print_stats(character, enemy):
    print(f"Your Health: {character['health']} | Your Energy: {character['energy']} | "
          f"Your EXP: {character['experience']} | Your Level: {character['level']} | Your Cats: {character['cats']}")
    print(f"{enemy.name}'s Health: {enemy.health}")

def battle_menu_choice():
    print("Battle Menu:")
    print("1. Attack (Cost: 5 Energy)")
    print("2. Flee (Cost: 25 Energy)")
    print("3. Rest (Restore: 10 Energy and pass your turn)")
    return input("Enter your choice (1/2/3): ")

def battle(character, enemy, enemy_details=None):
    cats_reward = 0
    experience_reward = 0  # Initialize rewards with default values

    while character['health'] > 0 and enemy.health > 0:
        print_stats(character, enemy)
        choice = battle_menu_choice()

        if choice == '1' and character['energy'] >= 5:
            handle_attack(character, enemy)
            character['energy'] -= 5
        elif choice == '2' and character['energy'] >= 25:
            if random.random() > 0.5:
                print("You successfully fled from the battle!")
                return "fled"
            else:
                print("Flee attempt failed! You must continue the battle.")
        elif choice == '3':
            character['energy'] = min(character['energy'] + 10, character['max_energy'])
            handle_attack(enemy, character)
        else:
            print("Invalid choice or not enough energy. Please make another selection.")

        # Enemy's turn
        if enemy.health > 0:
            handle_attack(enemy, character)

        character['energy'] = max(character['energy'], 0)

    # Post-battle results
    if enemy.health <= 0:
        print(f"You defeated the {enemy.name}!")
        if enemy_details:
            experience_reward = enemy_details['rewards']['experience'] + random.randint(1, 20)
            character['experience'] += experience_reward

            cats_reward = enemy_details['rewards']['cats'] + random.randint(1, 10)
            character['cats'] += cats_reward

            print(f"You earned {experience_reward} experience points.")
            print(f"Total experience: {character['experience']}")

            check_level_up(character)  # Check for leveling up after gaining experience
        return {"status": "win", "cats": cats_reward, "experience": experience_reward}

    elif character['health'] <= 0:
        print(f"You were defeated by the {enemy.name}!")
        # Handle character reset here
        print("\nStarting a new game...")
        return {"status": "lose"}
