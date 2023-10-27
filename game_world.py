import random
from battle import battle
from time_functions import advance_time
from enemy import random_enemy, enemy_stats, Enemy
from character_creation import character_creation, display_character_status, save_game
from stats import check_level_up, level_up, rest, decrease_energy, view_character_stats

# Define LEVEL_UP_POINTS as a global constant
LEVEL_UP_POINTS = [100]

def buy_bounty_map(character):
    print("You approach a shady-looking Shek who sells unique bounty maps.")
    
    while True:
        print("\nOptions:")
        print("1. Buy a regular bounty map for 100 cats(Dust King Tower")
        print("2. Buy a special bounty map for 500 cats (Red Sabres Hideout)")
        print("3. Buy a legendary bounty map for 2500 cats (Bugmaster's Lair)")
        print("4. Ask about bounties")
        print("5. Leave")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            if character['cats'] >= 100:
                character['cats'] -= 100
                print("You've purchased a bounty map. It reveals the location of a dangerous outlaw in the wilderness.")
                # Incorporate the battle scenario
                explore_wilderness1(character)
            else:
                print("You don't have enough cats to buy a bounty map.")
        elif choice == '2':
            if character['cats'] >= 500:
                character['cats'] -= 500
                print("You've purchased a special bounty map. It points to the Red Sabres' hidden hideout.")
                explore_red_sabres_hideout(character)
            else:
                print("You don't have enough cats to buy the special bounty map.")
        elif choice == '3':
            if character['cats'] >= 2500:
                character['cats'] -= 2500
                print("You've acquired a legendary bounty map. It pinpoints the lair of the infamous Bugmaster.")
                explore_bugmasters_lair(character)
            else:
                print("You don't have enough cats to buy the legendary bounty map.")
        elif choice == '4':
            print("\nThe shady-looking Shek eyes you up and down.")
            print("'New to the world of bounties, eh?' he says with a smirk.")
            print("'The wilds are filled with bandits and outlaws. As their numbers grow, so does the threat they pose.'")
            print("'The authorities, unable to handle them all, place bounties on their heads.'")
            print("'Strong warriors, like yourself, can seek these bandits out and claim the bounties for a hefty reward in cats.'")
            print("'If you're good, it's a lucrative business. But be warned, some of these outlaws are not to be trifled with.'")
        elif choice == '5':
            print("You decide to leave the NPC.")
            break
        else:
            print("Invalid choice. Please select between the options provided.")

def enemy_encounter(character):
    encounter_chance = random.random()
    return encounter_chance < 0.5

def explore_city(character):
    if character['energy'] >= 20:
        character['energy'] -= 20
        print("You wander through the city streets, taking in the sights.")
        while True:
            print("Options:")
            print("1. Talk to a city guard")
            print("2. Visit the marketplace")
            print("3. Visit the Shinobi Thieves")
            print("4. Talk to B Zero 1 the saver")
            print("5. Back to the main menu")
            choice = input("Enter your choice (1/2/3/4/5): ")
            if choice == '1':
                talk_to_city_guard(character)
            elif choice == '2':
                visit_marketplace(character)
            elif choice == '3':
                visit_shinobi_thieves(character)
            elif choice == '4':
                talk_to_b_zero_1(character)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please select between the options provided.")
    else:
        print("You are too exhausted to explore. You need to rest.")

def talk_to_b_zero_1(character):
    print("You approach B Zero 1, a robot standing erect with a shiny metallic body.")
    print('"Greetings, human!" B Zero 1 says in a robotic tone. "How may I assist your binary processes today?"')
    while True:
        print("Options:")
        print("1. What's your function, B Zero 1?")
        print("2. Can you save my progress?")
        print("3. I think I'll pass, you're too digital for me.")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            print('"I am B Zero 1, programmed to assist humans and provide them with the option of saving their state in this digital world."')
        elif choice == '2':
            save_game(character)
            print('"State saved successfully. All your bytes are where they belong," B Zero 1 reports with a hint of electronic glee.')
        elif choice == '3':
            print('"Farewell, human. May your circuits always find the optimal path."')
            break
        else:
            print("Invalid choice. Please choose between the provided options.")

def visit_shinobi_thieves(character):
    print("You arrive at the hideout of the Shinobi Thieves.")
    print("Options:")
    print("1. Speak with the coach for training (500 Cats)")
    print("2. Leave the hideout")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        if character['cats'] >= 500:
            character['cats'] -= 500
            level_up(character, character['level'] + 1)
            print(f"Your current level is now: {character['level']}")
        else:
            print("You don't have enough Cats for the training.")
    elif choice == '2':
        print("You decide to leave the Shinobi Thieves hideout.")
    else:
        print("Invalid choice. Please select between the options provided.")
    
def mine_ore(character):
    if character['energy'] >= 50:
        character['energy'] -= 50
        advance_time(character, 4)
        ore_value = random.randint(20, 80)
        character['cats'] += ore_value
        print(f"You worked hard mining and sold your ore for {ore_value} cats.")
    else:
        print("You are too exhausted to go mining. You need to rest.")
        view_character_stats(character)

def visit_marketplace(character):
    while True:
        print("You are at the marketplace. There are three trading stands available:")
        print("1. Hashish Booth (Cost: 100 cats) - Gain 5 Energy")
        print("2. Junk Weapons Booth (Cost: 100 cats) - Increase Strength by 1-3 points")
        print("3. Brothel Booth (Cost: 100 cats) - Increase Health by 20 with a 1 in 10 chance of catching KenSTD")
        print("4. Back to the city")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            # Hashish Booth
            if character['cats'] >= 100:
                character['cats'] -= 100
                character['max_energy'] += 5  # Increase the maximum energy by 5.
                character['energy'] = min(character['energy'] + 5, character['max_energy'])
                print("You smoke some hashish and feel more energetic.")
            else:
                print("You don't have enough cats to buy hashish.")
        elif choice == '2':
            # Junk Weapons Booth
            if character['cats'] >= 100:
                character['cats'] -= 100
                strength_increase = random.randint(1, 3)
                character['strength'] += strength_increase
                character['max_strength'] = max(character['strength'], character['max_strength'])
                print(f"You buy some salvageable weapon parts and gain {strength_increase} strength points.")
            else:
                print("You don't have enough cats to buy weapon parts.")
        elif choice == '3':
            # Brothel Booth
            if character['cats'] >= 100:
                character['cats'] -= 100
                print("You visit the brothel for a quickie.")
                if random.random() <= 0.1:
                    print("Unfortunately, you've caught a KenSTD. The virus runs through your body and instakills you. Game over!")
                    # Game over, return to the main menu
                    game_over()
                    return {"status": "lose"}
                else:
                    character['max_health'] += 20  # Increase the maximum health.
                    character['health'] = min(character['health'] + 20, character['max_health'])
                    print("You feel rejuvenated.")
            else:
                print("You don't have enough cats to visit the brothel.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            view_character_stats(character)

def talk_to_city_guard(character):
    print("You approach a city guard.")
    print("As you approach, you notice a nervous and jittery hiver kid, around 18 years old, wearing a city guard uniform. He fidgets with his armor and stammers as he speaks.")
    print("City Guard: 'H-hello there, traveler. Do you... uh... n-need any assistance?'")
    
    while True:
        # Offer some options for the player to choose from
        print("\nOptions:")
        print("1. Ask about the city.")
        print("2. Inquire about local activities.")
        print("3. Ask the guard about himself.")
        print("4. Say hello and move on.")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            print("\nCity Guard: 'Oh, the city? It's called the Hub. It's, um, a bit of a m-melting pot, you know?'")
            print("City Guard looks around nervously before continuing.")
            print("City Guard: 'People from all over come here. Traders, travelers, even some... not-so-great folks. But it's got a, uh, certain charm to it.'")
            print("City Guard: 'The Hub's mostly ruins, but there are some buildings that folks have set up shop in. You can find all sorts of s-stuff for sale here.'")
            print("City Guard seems relieved to have shared this information.")
        elif choice == '2':
            print("\nCity Guard: 'W-well, there are a few things you can do in the Hub. It depends on what you're, um, interested in.'")
            print("City Guard: 'You could go mining in the nearby tunnels for steady profit, an honest living. It's d-dangerous but pays well.'")
            print("City Guard: 'Or you could explore the wilderness outside the city, fight bandits or monsters, earn cats, and get stronger.'")
            print("City Guard: 'If you need a break, the bar is a good place to gossip, gamble, or drink to restore your health and energy.'")
            print("City Guard: 'In the marketplace, you can purchase services that make you stronger.'")
            print("City Guard: 'If you're feeling adventurous, you can buy a bounty map and take on one of the local bounties.'")
            print("City Guard: 'Or, well, you could always give up and sleep on the streets like most of the drifters do.'")
        elif choice == '3':
            print("\nCity Guard: 'M-me? Oh, I'm just... a g-guard.'")
            print("City Guard hesitates but then sighs and continues.")
            print("City Guard: 'I used to live with some nomads, but... their caravan got attacked not too far from here. I crawled here and got h-healed up.'")
            print("City Guard: 'I wanted to, um, protect the good people here, so I became a guard. It's n-not easy, but it's... something.'")
            print("City Guard looks down at the ground, seemingly lost in thought.")
        elif choice == '4':
            print("\nCity Guard: 'O-okay, t-take care then. I'll be... right here... guarding.'")
            break  # Exit the loop when the player says hello and moves on
        else:
            print("\nCity Guard: 'I'm s-sorry, I'm not very good at this. I... um... don't understand. Try again, maybe?'")

    # The player will continue talking to the guard until they choose to say hello and move on.
def initiate_battle(character, enemy):
    result = battle(character, enemy)
    if result == "win":
        print(f"You've earned {character['cats']} Cats and {character['experience']} experience.")
    elif result == "fled":
        print("You've managed to flee from the battle.")
    else:
        print("You lost the battle.")
        # Game over, return to the main menu
        game_over()
        return {"status": "lose"}

def explore_wilderness(character):
    if character['energy'] >= 25:
        character['energy'] -= 25
        advance_time(character, 4)
        print("You journey into the wilderness.")
        
        modified_enemy, enemy_details = random_enemy(character)  # Correctly unpack the returned values

        print(f"You have encountered an enemy: {modified_enemy.name} (Strength: {modified_enemy.strength}, Health: {modified_enemy.health})")

        # Rest of your code for handling the enemy encounter
        result = battle(character, modified_enemy, enemy_details)  # Pass the character, modified_enemy, and enemy_details

        if isinstance(result, dict) and 'status' in result and result['status'] == "win":
            rewards = enemy_details['rewards']  # Extract rewards from enemy_details
            print(f"You've earned {rewards['cats']} Cats and {rewards['experience']} experience.")
        elif result == "fled":
            print("You've managed to flee from the battle.")
        elif result == "lose":
            print("You lost the battle.")
            # Game over, return to the main menu
            game_over()
            return {"status": "lose"}
    else:
        print("You are too exhausted to explore. You need to rest.")
        view_character_stats(character)
        check_level_up(character)

def sit_and_listen():
    stories = [
        '''You overhear a grizzled old trader, "You know, before the world went to hell, The Hub was the pinnacle of trade. Now, it's just a shadow of its former self. But it’s not just the hub, I once heard tales of an ancient civilization called the Second Empire. They built advanced cities and machines, but something happened, and they fell. You can still find their ruins dotted around the Outlands, with treasures waiting for those brave enough to venture."''',
        '''A bandit, nursing his drink at the corner of the bar, whispers to his mate, "I heard rumors of a place not far from here, just southeast of the Hub. They call it the Deadlands. It's a cursed place, filled with acid rain and ruins of ancient tech. But that ain't the worst part. It's guarded by these ancient robots called 'Security Spiders'. Fast, deadly, and relentless, they protect whatever secrets that land holds. I'd stay away if I were you."''',
        '''A scarred woman, who looks like she's seen many battles, says, "The Holy Nation and the United Cities are always at odds. I once was a caravan guard, traveling between Stack and The Hub. We were ambushed by Paladins just because we had a Shek with us. You know, they believe those horned folks are spawns of Narco, their dark god. It’s a mad world. If you’re traveling in these parts, better to know who your allies are."''',
        '''A bearded man with a missing eye leans into the group next to him, "You folks ever ventured to the north? There's a desert they call the Burning Sands. Daylight there can fry a man alive, and the nights, cold as the Void. But amidst those dunes, they say there's a lost city buried deep. They call it 'The Oasis'. Legends say it's a city full of treasures, but those who go looking for it rarely return. And those who do, they ain't the same anymore."''',
        '''A wandering monk, with an emblem of Okran, speaks in a hushed tone to a curious onlooker, "I once undertook a pilgrimage to the holy Rebirth. It’s a sacred place for us believers. But en route, in a hidden canyon, I stumbled upon a strange village. The inhabitants, they all wore masks, never showing their faces. They spoke in riddles, telling tales of the First Men and the Celestial Wars. I left as fast as I could, the air felt heavy with ancient mysteries best left alone."''',
        '''An agile looking thief, with nimble fingers drumming on the table, leans in to share a secret, "Between you and me, there's a stealthy route from the Swamps to the Border Zone. It’s known to a few as 'The Ghost Pass'. It's a maze of narrow cliffs and tunnels. But if you know your way, it's a gold mine. You can smuggle hashish without the Hounds or the Swampers ever catching wind. But be warned, the tunnels aren’t empty. There are... things... lurking in the dark."''',
        '''A weathered nomad, his clothes tattered from countless sandstorms, shares a tale, "Far to the East, beyond the treacherous Stenn Desert, lies an isolated land they call the Ashlands. It's a forsaken place, home only to the remnants of an ancient empire. Gigantic ruins and rusted skeletons of once-mighty war machines litter the land. They say there's treasure there, lost technology of unimaginable power. But beware, the guardians of that place do not take kindly to intruders."''',
        '''A secretive scavenger, her eyes wide with excitement, whispers, "In the hidden corners of the Outlands, there are places where reality seems to bend and twist. I found one such place, a valley shrouded in a perpetual storm. The winds howl, and the sky bleeds colors unseen. They call it the Rift. Some say it’s a gateway to another world, others believe it’s where the ancients communed with gods. But be careful, for not all that wander there find their way back."''',
        '''An old Shek warrior, his horns chipped from countless battles, grunts, "If you ever find yourself in the Borderlands, keep your eyes peeled for the Graveyard. It’s a field of stone and steel, remnants of a battle long forgotten. The locals say the spirits of fallen warriors still haunt that place, eternally locked in combat. Some foolhardy adventurers go there seeking ancient weapons and armor. Few return, and those who do are haunted by the echoes of war."''',
        '''A cunning rogue, her cloak shrouded in shadows, tells of distant lands, "You heard of the Hidden Forest? It’s a place shrouded in mist and mystery, nestled in the far South. They say it’s home to a tribe of hivers who've never seen the outside world. They guard their territory fiercely, attacking any who dare to enter. But legends speak of a hidden treasure, a relic from the Old World, guarded by the tribe's fiercest warriors."''',
        '''A jovial bartender, wiping a glass clean, laughs, "So, there's this tale about the Arm of Okran. They say it’s a giant statue, the hand of the god Okran himself, outstretched to the heavens. It's said to lie somewhere in the Northern Coast, but no one’s sure where exactly. Some believe it's a sign from the gods, others think it’s just a relic from a time long past. But the mystery of it, that's what keeps the adventurers coming, hoping to uncover the secrets of the old world."''',
        '''A seasoned hunter, her crossbow slung across her back, speaks of the wilds, "The Pits, they call it, a land twisted and corrupted, far to the South. The earth itself is poisoned, and the creatures that live there, they're like nothing you've seen before. Gigantic bugs and beasts, all twisted and malformed. The risk is high, but so are the rewards. Exotic materials, rare beasts, it's a hunter's paradise. But you'd best be prepared, for the Pits show no mercy."''',
        '''A miner, his hands stained with ore, murmurs, "I’ve been digging in the depths near Vain, and once, deep below, I came across an old cavern. It was lit up by these luminescent crystals that shone like stars. But it wasn’t their beauty that caught my eye. No, it was the murals on the walls, telling tales of a civilization that existed before the hivers. Makes you wonder how much history is buried beneath our feet."''',
        '''A veteran soldier, his armor dented from numerous battles, shares, "Have you heard of The Floodlands? It’s to the north, a sprawling expanse of submerged ruins. They say it was once a mighty city, drowned by its own ambition. Now it’s a playground for bandits and smugglers. But the real danger? The ancient machines, still patrolling the waters, waiting to strike unwary travelers."''',
        '''An explorer, her hat frayed at the edges, recounts, "In my travels, I've ventured deep into the Leviathan Coast. There's a legend there of a giant creature, bigger than any city. It roams the coast, its cries echoing for miles. They say it's an ancient guardian, a protector of hidden treasures from a bygone era. But approach with caution, for many who have sought the Leviathan have never returned."''',
        '''A wrinkled elder, his eyes filled with memories, narrates, "Long ago, there was a scholar from the United Cities who believed that Kenshi was once covered in vast forests and shimmering lakes. He spoke of ancient texts that told of a great calamity, which scorched the skies and dried the seas. Though many called him mad, some still seek those ancient texts, hoping to unlock the secrets of Kenshi's past."''',
        '''A fisherman, his net filled with the day's catch, chuckles, "You ever been to the Fishman Isle? It's a weird place, I tell ya. The island's inhabited by these... fish-like folk. Half-man, half-fish. Some say they’re remnants of a failed experiment, others believe they're protectors of a hidden underwater city. All I know is, they can be quite territorial, so steer clear if you value your limbs."''',
        '''A curious scholar, her satchel overflowing with scrolls, ponders aloud, "There are murmurings of a place called the Crater. Some ancient texts hint at it being a hub of knowledge, where scholars and thinkers from all over Kenshi gathered. Now, it’s said to be a desolate crater, its riches buried under layers of ash and time. Imagine the wisdom waiting to be unearthed!"''',
        '''A healer, her hands stained with medicinal herbs, whispers, "In the hidden reaches of the Cannibal Plains, there’s an old tale of the Spirit Tree. It's said to have healing properties, and its leaves can cure any ailment. Many have sought it out, looking for cures for loved ones. But be warned, the Cannibals consider it sacred, and trespassers pay a hefty price."''',
        '''A wanderer, his boots covered in mud, recounts, "Beyond the Bonefields, there's a valley enveloped in perpetual fog, called the Misty Ravine. Local tales speak of phantoms that lure travelers deep into the mists, never to be seen again. But a few survivors speak of a hidden village within, where time stands still and the inhabitants know secrets of the ancients."''',
        '''A trader, his caravan laden with exotic wares, shares, "During my journeys across the Northern Coast, I encountered a tribe known as the 'Wind Whisperers'. They have this uncanny ability to predict storms, and they navigate the treacherous coastlines with ease. They believe their ancestors were spirits of the wind and sea, and they protect ancient relics that grant them their powers."''',
        '''A historian, surrounded by scrolls and old books, ponders, "I've been researching the legend of the Sunken City. It's said to lie at the bottom of the Iron Sea, its spires and domes still visible during low tide. Legends speak of a crystal at its heart that powered the entire city. If it ever existed and could be retrieved, it might change Kenshi forever."''',
        '''A weary traveler, nursing a cup of warm sake, mentions, "In the depths of the Leviathan Coast, there are tales of a 'Ghost Ship'. A spectral vessel that sails with no crew, appearing during the darkest nights. Some say it’s the spirit of a ship lost in a great storm, while others believe it’s a guardian ship, protecting a hidden treasure trove on a secluded island."''',
        '''A hooded figure, his face hidden in the shadows, warns, "They say the further you travel into the Ashlands, the stranger things become. I've heard tales of 'The Inverted Mountain', a place where gravity itself is skewed. Rocks float, water flows upwards, and fires burn with cold flames. Many treasure hunters have sought it, looking for the rumored 'Gravity Stone', but its landscape is as treacherous as it is bewildering."''',
        '''An old man, his eyes distant and speech erratic, rambles, "You won't believe me, but this world... it's all a sham! A simulation! Created by a Youtuber named Cool Kid Croc! He's the puppet master, and we're just characters in his grand design!" Listening to his bizarre proclamation, you can't help but think he's lost his mind. The other patrons in the bar chuckle, dismissing his claims and suggesting he's had one too many to drink.''',
        '''A former slave, his shackles now removed, speaks in a hushed tone, "I was once held in Rebirth, the Holy Nation’s most notorious slave camp. But amidst the suffering, I heard whispers of the Phoenix's Tomb. It’s a mythical place where the ashes of past Phoenixes are said to be kept. Some believe it’s cursed, others think it holds the Holy Nation's deepest secrets. All I know is, those who go looking for it are never seen again."''',
    ]       
    
    print(random.choice(stories))


def bar_actions(character):
    while True:
        view_character_stats(character)
        print("You enter a bar.")
        print("Options:")
        print("1. Talk to the bartender")
        print("2. Sit and listen")
        print("3. Play 'Pull Chewsticks'")
        print("4. Leave the bar")
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            print("The bartender gives you a nod. 'What'll it be?'")
            print("1. Ale (5 cats)")
            print("2. Rum (10 cats)")
            print("3. Whiskey (15 cats)")
            print("4. Stop talking to the bartender")
            drink_choice = input("Enter your drink choice (1/2/3/4): ")

            if drink_choice == '1' and character['cats'] >= 5:
                character['cats'] -= 5
                character['energy'] = min(character['energy'] + 30, character['max_energy'])
                character['health'] = min(character['health'] + 30, character['max_health'])
                print("You sip the refreshing ale and feel a surge of energy and health!")
                advance_time(character, 4)

            elif drink_choice == '2' and character['cats'] >= 10:
                character['cats'] -= 10
                character['energy'] = min(character['energy'] + 60, character['max_energy'])
                character['health'] = min(character['health'] + 60, character['max_health'])
                print("You sip the refreshing rum and feel a surge of energy and health!")
                advance_time(character, 4)

            elif drink_choice == '3' and character['cats'] >= 15:
                print(f"Current Energy Before Whiskey: {character['energy']}") # Debugging line
                print(f"Current Health Before Whiskey: {character['health']}") # Debugging line
                character['cats'] -= 15
                character['energy'] = min(character['energy'] + 90, character['max_energy'])
                character['health'] = min(character['health'] + 90, character['max_health'])
                print(f"Energy After Whiskey: {character['energy']}") # Debugging line
                print(f"Health After Whiskey: {character['health']}") # Debugging line
                print("You sip the refreshing whiskey and feel a surge of energy and health!")
                advance_time(character, 4)

            elif drink_choice == '4':
                print("You walk away from the bartender")
                advance_time(character, 4)

        elif choice == '2':
            sit_and_listen()
            advance_time(character, 4)
            
        elif choice == '3':
            print("You approach a peculiar-looking individual who seems to have had one too many drinks.")
            print("'Ey there, mate! Fancy a game o' Pull Chewsticks? Double yer cats or lose 'em all!' he slurs.")
            
            # Check if player has any cats to gamble
            if character['cats'] <= 0:
                print("'Ah, seems like yer pockets are empty. Come back when you've got some cats to gamble!'")
                continue

            gamble_choice = input("Do you want to play? (yes/no): ").lower()
            if gamble_choice == 'yes':
                gamble_amount = int(input(f"How many cats do you want to gamble? (You have {character['cats']} cats): "))
                
                # Check if the player has enough cats to gamble the chosen amount
                if 0 < gamble_amount <= character['cats']:
                    print("The Vagrant places two chewsticks in his hands and shakes them.")
                    print("He then asks you to pick one. If you pick the longer stick, you win!")
                    result = random.choice(['win', 'lose'])
                    if result == 'win':
                        character['cats'] += gamble_amount
                        print(f"You picked the longer stick! You win {gamble_amount} cats! You now have {character['cats']} cats.")
                    else:
                        character['cats'] -= gamble_amount
                        print(f"Unlucky! You picked the shorter stick. You lose {gamble_amount} cats. You now have {character['cats']} cats.")
                else:
                    print("Invalid amount! Please enter a valid amount of cats to gamble.")
            elif gamble_choice == 'no':
                print("'Ah well, maybe next time!' he mumbles, taking another swig from his bottle.")

        elif choice == '4':
            print("You decide to leave the bar.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

def sleep_on_streets(character):
    if character['energy'] < character['max_energy']:
        print("You find a quiet alley and settle down for the night.")
        character['energy'] = min(character['energy'] + 20, character['max_energy'])  # Increase energy by 20
        advance_time(character, 4)
        print("You wake up feeling refreshed.")
    else:
        print("You're not tired yet.")

def purchase_home(character):
    print("\nYou approach a Hiver real estate agent.")
    print(f"\"Ah! Hello {character['race']}! Interested in buying a home? Only 1200 cats!\"")
    
    if character['cats'] < 1200:
        print("\"Looks like you don't have enough cats. Come back when you do.\"")
        print("The Hiver shoos you away.\n")
        return

    buy_choice = input("Would you like to purchase the house for 1200 cats? (yes/no): ")
    if buy_choice.lower() == 'yes':
        character['cats'] -= 1200
        character['has_home'] = True
        print("Congratulations on your new home! You can now rest there to recover health and energy.")
    else:
        print("The Hiver seems disappointed. \"Let me know if you change your mind!\"")

def rest_at_home(character):
    print("\nYou go to your home and take a 4-hour rest.")
    character['health'] = character['max_health']
    character['energy'] = character['max_energy']
    print("Your health and energy are fully restored!\n")
    advance_time(character, 4)

def city_menu(character):
    print("You find yourself in The Hub, a once bustling trade city, now a shadow of its former self, surrounded by the arid wastelands of Kenshi.")
    
    while True:
        # Random ambient thoughts/descriptions for The Hub
        events = [
            "The wind carries the distant sound of machinery. The remnants of a forgotten age.",
            "Overhead, a few birds circle the sky, their shadows flickering on the sun-scorched ground.",
            "You notice a group of children playing with a weathered ball, a small semblance of normalcy in this tough world.",
            "A sandstorm seems to be brewing in the distance, a common sight in these parts.",
            "The scent of cooked meat wafts over from a nearby stall, reminding you of hunger.",
            "You catch a snippet of conversation about some bandit activity near Stack.",
            "An elderly person sits by the street, recounting tales of The Hub's former glory to anyone who would listen.",
            "A caravan is preparing to leave The Hub, heading towards the city of Admag.",
            "You see a group of drifters sharing a meal, their laughter echoing in the near-empty streets.",
            "The ruins around you whisper stories of the old world. If only they could talk.",
            "You see a shinobi thief darting through the alleys, clearly up to some mischief.",
            "A preacher loudly proclaims the teachings of Okran, gathering a small crowd around him.",
            "The distant sound of a skirmish reminds you of the constant dangers of Kenshi's wastelands."
            "A street musician plays a haunting tune on a makeshift instrument, momentarily captivating those passing by.",
            "A dog, with its fur matted and dirty, scours the ground for scraps, reminding you of the harshness of life in The Hub.",
            "A vendor loudly haggles with a customer, both of them animated in their negotiation over some salvaged tech.",
            "You overhear a conversation about a mysterious ruin being discovered in the southeast, sparking your curiosity.",
            "Two warriors spar in a cleared-out area, their skilled movements drawing an audience.",
            "An orphan tugs at your sleeve, holding up a hand-drawn picture in exchange for a few cats.",
            "Distant shouts alert you to a street game in progress. A few local teams competing in a rough sport unique to The Hub.",
            "A battered sign reads 'Need Medic', hinting at the ever-present danger even within the city walls.",
            "You feel a tap on your shoulder, but turning around reveals no one. A reminder to always be on your guard.",
            "A local artist sketches the cityscape, capturing the juxtaposition of decay and life in The Hub.",
            "You come across a memorial, with tokens and writings paying respects to lost loved ones.",
            "From an alley, you hear the strumming of a guitar accompanied by hushed voices singing a melancholic tune.",
            "A wandering trader sets up a temporary stall, displaying exotic goods from distant lands.",
            "You spy a group gathered around a campfire, sharing stories of their travels and escapades.",
            "A tech-hunter excitedly discusses a new find with his comrades, hinting at unknown technologies lost to time.",
            "A cloud of dust in the distance suggests a caravan's approach, promising goods from distant cities.",
            "In the distance, a massive skeleton of a once-majestic building looms, hinting at The Hub's grand past.",
            "A faint glow emanates from a makeshift tavern, the hubbub of conversation promising respite from the desolation outside.",
            "A few guards lazily patrol the city's entrance, their relaxed demeanor belying their readiness to spring into action.",
            "You notice a drifter's gaze following you, eyes filled with a mix of curiosity and suspicion.",
            "The sound of metal clinking against metal draws your attention to a blacksmith, working diligently under the scorching sun.",
            "A makeshift market bustles with activity as locals barter for essentials, their determined haggling echoing survival instincts.",
            "The distant howl of a beast sends a shiver down your spine, a stark reminder of the world's lurking dangers.",
            "Clouds of dust rise from the ground as a group practices martial arts, their movements fluid and coordinated.",
            "You spot a weary traveler resting under a dilapidated awning, his tired eyes recounting countless journeys.",
            "A woman sells freshly baked bread from a cart, the aroma pulling you in despite the bread's rugged appearance.",
            "The distant hum of an engine grows louder, signaling the return of a scouting party from an expedition.",
            "You overhear an old-timer recount tales of green landscapes, a stark contrast to the barren wasteland surrounding The Hub.",
            "A man hands out leaflets, each detailing the whereabouts of the region's most dangerous bounties.",
            "A crowd gathers around a performer who balances on a tightrope strung between two ruined buildings, their gasps echoing each daring move.",
            "From a tent, the rich scent of brewed herbs wafts, hinting at a healer or herbalist practicing their trade.",
            "Children chase after a tattered kite, their laughter a brief respite from the world's hardships.",
            "A group debates animatedly over a map spread out on the ground, plotting routes and marking danger zones.",
            "A tall watchtower stands sentinel, its guards scanning the horizon for any sign of approaching threats.",
            "Nearby, a deep well offers fresh water, with locals lining up with containers, a reminder of the city's lifeblood.",
            "A storyteller captivates an audience with tales of mighty beasts and hidden treasures, offering a momentary escape from the city's grim reality.",
            "In a quiet corner, an old machine hums to life, only to sputter and die moments later, a remnant of a time long past."
        ]
        
        print(random.choice(events))
        
        view_character_stats(character)  # Display character stats
        
        print("\nOptions:")
        print("1. Explore the city")
        print("2. Go to the bar")
        print("3. Explore the wilderness")
        print("4. Sleep on the streets")
        print("5. Mine for ore")

        if character.get('has_home'):
            print("6. Rest at home")
            print("7. Buy a bounty map")
            print("8. Join the caravan to Flats Lagoon")
            print("9. Exit and save the game")
        else:
            print("6. Purchase a home")
            print("7. Buy a bounty map")
            print("8. Join the caravan to Flats Lagoon")
            print("9. Exit and save the game")

        choice = input("Enter your choice: ")

        options = {
            '1': explore_city,
            '2': bar_actions,
            '3': explore_wilderness,
            '4': sleep_on_streets,
            '5': mine_ore,
            '7': buy_bounty_map,
            '8': join_caravan  # always available
        }

        if character.get('has_home'):
            options['6'] = rest_at_home
        else:
            options['6'] = purchase_home

        if choice in options:
            options[choice](character)
        elif choice == '9':
            save_game(character)
            print("Game saved! Exiting...")
            exit() # could also be changed to intro_screen() to restart the game
        else:
            print("Invalid choice. Please select a valid option.")

def explore_wilderness1(character):
    if character['energy'] >= 25:
        character['energy'] -= 25
        advance_time(character, 8)
        print("You journey into the wilderness.")
        print("As you venture deeper into the wilderness, you come across an eerie camp. It's the rumored Dust King's camp.")
        print("In the center of the camp, you spot a tall tower. It appears to be the Dust King's stronghold.")
        print("You decide to sneak closer to the tower to gather more information. As you approach, you notice two Dust Bandits guarding the entrance of the tower.")
        print("They seem unaware of your presence.")
        print("You prepare for battle and engage the two Dust Bandits guarding the tower.")

        # Initialize Dust Bandits
        dust_bandit1 = Enemy('Dust Bandit', 7, 8, 6, 70, 35, 7)
        dust_bandit2 = Enemy('Dust Bandit', 7, 8, 6, 70, 35, 7)

        # Perform battles
        battle_results = []
        for enemy in [dust_bandit1, dust_bandit2]:
            result = battle(character, enemy)
            battle_results.append(result)

        # Check battle results
        for i, result in enumerate(battle_results):
            if isinstance(result, dict) and 'status' in result and result['status'] == "win":
                print(f"You've defeated the {dust_bandit1.name} and earned {result['cats']} Cats and {result['experience']} experience.")
            elif result == "fled":
                print("You've managed to flee from the battle.")
                # Handle consequences of fleeing here, if any
                break  # Exit the loop if the player flees successfully
            elif result == "lose":
                print("You lost the battle.")
                # Game over, return to the main menu
                game_over()
                return {"status": "lose"}

        # Proceed with the story or consequences here

        # Third battle with the Dust King
        dust_king = Enemy('Dust King', 14, 16, 12, 140, 70, 14)  # Twice as strong as Dust Bandits
        print(f"You have encountered the {dust_king.name} (Strength: {dust_king.strength}, Health: {dust_king.health})")
        result = battle(character, dust_king)
        if isinstance(result, dict) and 'status' in result and result['status'] == "win":
            print(f"You've defeated the {dust_king.name} and earned {result['cats']} Cats and {result['experience']} experience.")
            character['cats'] += 1000
            print("You've been awarded an additional 1000 cats for defeating the Dust King!")
            # Continue the game here
        elif result == "fled":
            print("You've managed to flee from the battle.")
            # Handle consequences of fleeing here, if any
        elif result == "lose":
            print("You lost the battle.")
            # Game over, return to the main menu
            game_over()
            return {"status": "lose"}

    else:
        print("You are too exhausted to explore. You need to rest.")
        view_character_stats(character)
        check_level_up(character)

def explore_red_sabres_hideout(character):
    if character['energy'] >= 25:
        character['energy'] -= 25
        advance_time(character, 8)
        print("Following the map, you journey into a hidden forest area.")
        
        # Discovering the Red Sabres Hideout
        print("Soon you discover a concealed cave entrance, guarded by three menacing Red Sabres.")
        print("Beyond them, deeper in the cave, you sense the powerful presence of the Red Sabre Boss.")
        
        red_sabers = [
            Enemy('Red Saber', 9, 7, 9, 90, 40, 7),
            Enemy('Red Saber', 9, 7, 9, 90, 40, 7),
            Enemy('Red Saber', 9, 7, 9, 90, 40, 7)
        ]
        
        for red_saber in red_sabers:
            print(f"You engage a {red_saber.name}.")
            result = battle(character, red_saber)
            if isinstance(result, dict) and 'status' in result and result['status'] == "win":
                print(f"You've defeated the {red_saber.name} and earned {result['cats']} Cats and {result['experience']} experience.")
            elif result == "fled":
                print("You've managed to flee from the battle.")
                # Handle consequences of fleeing here, if any
                break  # Exit the loop if the player flees successfully
            elif result == "lose":
                print("You lost the battle.")
                return {"status": "lose"}  # Do not call game_over() on a regular loss
        
        # Battle with the Red Sabre Boss
        red_sabre_boss = Enemy('Red Sabre Boss', 36, 28, 36, 360, 160, 28)
        print(f"\nYou come face to face with the {red_sabre_boss.name}. Prepare for a challenging battle!")
        result = battle(character, red_sabre_boss)
        if isinstance(result, dict) and 'status' in result and result['status'] == "win":
            print(f"You've successfully defeated the {red_sabre_boss.name} and earned {result['cats']} Cats and {result['experience']} experience.")
            character['cats'] += 2500
            print("You've been awarded an additional 2500 cats for defeating the Red Sabre Boss!")
        elif result == "fled":
            print("You've managed to flee from the battle.")
            # Handle consequences of fleeing here, if any
        elif result == "lose":
            print("You lost the battle.")
            game_over()
            return {"status": "lose"}  # Call game_over() only if the player loses the final battle
    else:
        print("You are too exhausted to explore the hideout. You need to rest.")
        view_character_stats(character)
        check_level_up(character)

def explore_bugmasters_lair(character):
    if character['energy'] >= 30:
        character['energy'] -= 30
        advance_time(character, 8)
        print("Following the legendary map, you venture deep into a treacherous valley.")
        
        # Discovery of Bugmaster's Lair
        print("The eerie atmosphere grows denser as you approach a cave adorned with arachnid relics. The Bugmaster's lair is close.")
        print("As you tread cautiously, three grotesque Skin Spiders appear from the shadows, their eyes fixated on you.")
        
        skin_spiders = [
            Enemy('Skin Spider', 5, 5, 12, 100, 30, 6),
            Enemy('Skin Spider', 5, 5, 12, 100, 30, 6),
            Enemy('Skin Spider', 5, 5, 12, 100, 30, 6)
        ]
        
        for skin_spider in skin_spiders:
            print(f"You prepare to face the {skin_spider.name}.")
            result = battle(character, skin_spider)
            if isinstance(result, dict) and 'status' in result and result['status'] == "win":
                print(f"You've overpowered the {skin_spider.name} and earned {result['cats']} Cats and {result['experience']} experience.")
            elif result == "fled":
                print("You've narrowly escaped from the battle.")
                # Handle consequences of fleeing here, if any
                break  # Exit the loop if the player flees successfully
            elif result == "lose":
                print("The Skin Spiders proved too much for you. You've been defeated.")
                return {"status": "lose"}  # Do not call game_over() on a regular loss
        
        # Epic Battle with the Bugmaster
        bugmaster = Enemy('Bugmaster', 48, 48, 48, 480, 240, 48)
        print(f"\nInside the lair, the infamous {bugmaster.name} emerges. Steel yourself for the fight of your life!")
        result = battle(character, bugmaster)
        if isinstance(result, dict) and 'status' in result and result['status'] == "win":
            print(f"You've triumphed over the {bugmaster.name} and earned {result['cats']} Cats and {result['experience']} experience.")
            character['cats'] += 5000
            print("You've been awarded a whopping 5000 cats for conquering the Bugmaster!")
        elif result == "fled":
            print("Somehow, you've managed to escape the clutches of the Bugmaster.")
            # Handle consequences of fleeing here, if any
        elif result == "lose":
            print("The Bugmaster has bested you in combat.")
            game_over()
            return {"status": "lose"}  # Call game_over() only if the player loses the final battle
    else:
        print("Your exhaustion is palpable. You need to rest before attempting to challenge the Bugmaster's lair.")
        view_character_stats(character)
        check_level_up(character)

def join_caravan(character):
    print("\nAs you approach the caravan, the caravan leader, a stout man with sun-beaten skin, notices you.")
    print('"Ah, looking to leave The Hub? Our caravan is preparing to travel to Flats Lagoon. This is a dangerous route, but it is also the only one. With our protection, you might arrive safely."')
    print('"However, given the dangers we might face, no less than 20,000 cats. We only take this route if it happens to be worth our while..."')

    if character.get('cats', 0) >= 20000:
        choice = input("\nDo you wish to join the caravan to Flats Lagoon for 20,000 cats? (yes/no): ").lower()
        if choice == 'yes':
            character['cats'] -= 20000
            advance_time(character, 8)
            print("\nYou hand over the 20,000 cats, and the caravan leader nods approvingly.")
            print('"Very well. Prepare yourself. We will be leaving soon."')

            # Caravan journey dialogue
            print("\nThe caravan sets off, and you find yourself on a journey through the arid wastelands of Kenshi. The scenery is both breathtaking and desolate, with vast sand dunes and rocky outcrops stretching as far as the eye can see.")
            print("As the caravan continues, you spot a group of purple-looking Hive men in the distance. But behind them stands none other than the King Crimper himself, a formidable figure even among Hive royalty.")
            print("Without hesitation, the caravan leader orders an attack on the Southern Hive group. Some of the enemies split off to attack you!")

            # Initialize enemies
            hive_warriors = [
                Enemy('Southern Hive Warrior', 32, 20, 36, 320, 120, 20),
                Enemy('Southern Hive Warrior', 32, 20, 36, 320, 120, 20),
                Enemy('Southern Hive Warrior', 32, 20, 36, 320, 120, 20),
            ]

            king_crimper = Enemy('King Crimper', 180, 100, 220, 2000, 1000, 150)

            # Combat loop
            while True:
                print("\nEnemies approach!")
                print("Your caravan comrades join the fight, and you must fend off the Southern Hive attackers to protect the caravan leader.")

                for enemy in hive_warriors:
                    battle_outcome = battle(character, enemy)
                    if battle_outcome["status"] == 'lose':
                        print("\nUnfortunately, you and your caravan comrades are defeated by the Southern Hive warriors.")
                        print("The caravan leader and your comrades are captured by the Southern Hive.")
                        print("Your journey ends here.")
                        game_over()
                        return

                if all(enemy.health <= 0 for enemy in hive_warriors):
                    print("\nYou defeated the Southern Hive warriors, but the King Crimper still stands.")
                    print("You and your caravan comrades prepare to face the mighty King Crimper!")

                    king_crimper_outcome = battle(character, king_crimper)

                    if king_crimper_outcome["status"] == 'win':
                        print("\nYou've won the battle! The King Crimper lies defeated.")
                        print("\nYou travel with the remaining caravan survivors and reach Flats Lagoon, ready to start your new life!")
                        # Display the final time and character stats
                        current_day, current_time = character['time']
                        print(f"\nYour journey ended on Day {current_day} at Hour {current_time.hour}.")
                        print("Character stats: ", character)  
                        input("Press Enter to return to the intro screen...")
                        intro_screen()
                        return

                    elif king_crimper_outcome["status"] == 'lose':
                        print("\nDespite your best efforts, the King Crimper proved too formidable, and you are defeated.")
                        # ... rest of the dialogue ...
                        game_over()
                        return

                break

def game_over():
    print("\n------------------------")
    print("        GAME OVER       ")
    print("------------------------\n")
    input("Press Enter to return to the intro screen...")
    return {"status": "lose"}
    intro_screen()  # Call the intro screen function

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

def game_world(character):
    while True:
        view_character_stats(character)
        city_menu(character)

if __name__ == "__main__":
    character = character_creation()
    game_world(character)
