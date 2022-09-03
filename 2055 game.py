import random
# Works fantastically and is completely idiotproof!
# Tiitus PB 63 days


class bcolors:  # funky thing to make text colored
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# works like this "print(f"{bcolors.BLUE} Hello, World!{bcolors.END}")"


inventory = ["Water bottle", "MRE", "Pistol"]  # What you have at a given time
# Possible_items = ["Water bottle", "MRE", "Beans", "Soda", "Medical kit", "Pistol", "Shotgun"]  # All items in game
# possible items is an old test, serves no purpose now.
# it's still handy in order to show all items in the game.


def difficulty_selector():
    user_input = input("SELECT DIFFICULTY | (1) Easy (20 days) | (2) Medium (30 days) | (3) Hard (45 days) ")
    if user_input == 1:
        total_trip = 20
    elif user_input == 2:
        total_trip = 30
    else:
        total_trip = 45
    return total_trip


# best function in the game, makes names for town.
def area_namer():
    random_value1 = random.randint(0, 24)
    random_value2 = random.randint(0, 17)
    list1 = ["John", "Josh", "Mark", "Freak", "Dumb", "Idiot", "Cursed", "Evil", "Deadly", "Adorable",
             "Adventurous", "Aggressive", "Agreeable", "Alert", "Alive", "Amused", "Angry", "Annoyed", "Annoying",
             "Anxious", "Arrogant", "Ashamed", "Attractive", "Average", "Shithole"]
    list2 = [" Peninsula", " Stream", " River", " of no return", "-topia", " Land", " Kingdom", " Republic",
             " Delta", " Volcano", " Hill", " Town", " Forest", " Lake", " Mountain", " Plain", " Taiga", " Swamp"]
    word1 = list1[random_value1]
    word2 = list2[random_value2]
    land_name = word1 + word2
    return land_name


# for inventory management and stuff use
def inv_sys(bullets, shells, food, hydration, health, pistol_equipped, shotgun_equipped, survived_days):
    if pistol_equipped != 0:  # most likely useless, but this was to fix wierd shit, so it's staying in
        pistol_equipped = 1  # it's not harming anything, right?
        shotgun_equipped = 0
    if shotgun_equipped != 0:
        pistol_equipped = 0
        shotgun_equipped = 1
    while True:
        if len(inventory) > 15:
            input(f"{bcolors.YELLOW}You are carrying too much! Throw something away.")
        print("")
        if hydration > 100:
            hydration = 100
        if hydration < 0:
            hydration = 0
        if hydration <= 25 and hydration != 0:
            input(f"{bcolors.RED}You are very thirsty!{bcolors.END}")
        if food > 100:
            food = 100
        if food < 0:
            food = 0
        if food <= 20 and food != 0:
            input(f"{bcolors.RED}You are very hungry{bcolors.END}")
        if health > 100:
            health = 100
        if health <= 0:
            print(f"{bcolors.RED}You died!{bcolors.END}")
            print(f"Days survived: {survived_days}")
            exit()
        print(inventory)
        print(f"{bcolors.END}{bcolors.BOLD}{bullets} 9mm ammo | {shells} shotgun shells")
        print(f"{food} food | {hydration} hydration | {health} HP{bcolors.END}")
        print(str(len(inventory)) + " kg | Max weight 15 kg")
        user_input = input(f"{bcolors.GREEN}USE, DROP or leave ")
        if user_input.lower() == "drop":
            while 1:
                user_input = input("Select which item! (Type 1 for the first item...) ")
                try:
                    anti_crash_measure = len(inventory)
                    anti_crash_measure = anti_crash_measure - int(user_input)
                    if anti_crash_measure >= 0:
                        selected_item = inventory[int(user_input)-1]
                        inventory.remove(selected_item)
                    else:
                        break
                except ValueError:
                    print("You didn't drop anything.")
                    break
        if user_input.lower() == "use":
            while True:
                print(inventory)
                user_input = input("Select which item! 1 for the first... Type CLOSE to close your bag ")
                try:
                    anti_crash_measure = len(inventory)
                    anti_crash_measure = anti_crash_measure - int(user_input)
                    if anti_crash_measure >= 0:
                        try:
                            selected_item = inventory[int(user_input) - 1]
                            if selected_item == "Water bottle":
                                input("You drank the water bottle. +85 hydration")
                                hydration = hydration + 85
                                inventory.remove(selected_item)
                            elif selected_item == "MRE":
                                input("You ate the MRE. +85 food")
                                food = food + 85
                                inventory.remove(selected_item)
                            elif selected_item == "Beans":
                                input("You ate the beans. +40 food")
                                food = food + 40
                                inventory.remove(selected_item)
                            elif selected_item == "Soda":
                                input("You drank the soda. +40 hydration")
                                hydration = hydration + 40
                                inventory.remove(selected_item)
                            elif selected_item == "Medical kit":
                                input("You used the medical kit. +40 health")
                                health = health + 40
                                inventory.remove(selected_item)
                            elif selected_item == "Pistol":
                                user_input = input(f"It's your trusty pistol. "
                                                   f"You have {bullets} bullets for it. Equip it? (Y/N) ")
                                if user_input.lower() == "y":
                                    input("You equip the pistol.")
                                    shotgun_equipped = 0
                                    pistol_equipped = 1
                                    return food, hydration, health, pistol_equipped, shotgun_equipped
                                else:
                                    print("You keep it in your bag.")
                            elif selected_item == "Shotgun":
                                user_input = input(
                                    f"It's a 12 gauge beast! You have {shells} shells for it. Equip it? (Y/N) ")
                                if user_input.lower() == "y":
                                    input("You equipped the shotgun!")
                                    shotgun_equipped = 1
                                    pistol_equipped = 0
                                    return food, hydration, health, pistol_equipped, shotgun_equipped
                                else:
                                    print(f"You keep the shotgun in your bag.{bcolors.END}")
                            else:
                                break
                        except ValueError:
                            break
                except ValueError:
                    break
                if user_input.lower() == "close":
                    break
                if user_input == "":
                    break
        elif len(inventory) < 15:
            print(f"{bcolors.END}")
            return food, hydration, health, pistol_equipped, shotgun_equipped
        else:
            input(f"{bcolors.YELLOW}You are carrying too much! Throw something away.{bcolors.END}")


# gives you loot after you defeat the location enemies
def loot_system(loot, bullets, shells):
    luck = random.randint(0, 3)
    number_item = 1
    if luck == 3:
        number_item = 2
    for i in range(number_item):
        luck = random.randint(0, 4)
        final_loot_value = luck + loot
        if final_loot_value == 0:
            input(f"{bcolors.CYAN}You found nothing.")
        elif final_loot_value == 1:
            gamble = random.randint(5, 10)
            b_a = gamble + luck
            input(f"You found {b_a} 9mm bullets!")
            bullets = bullets + b_a
        elif final_loot_value == 2:
            input("You found an old can of soda!")
            inventory.append("Soda")
        elif final_loot_value == 3:
            input("You find an medical kit")
            inventory.append("Medical kit")
        elif final_loot_value == 4:
            input("You found an can of beans!")
            inventory.append("Beans")
        elif final_loot_value == 5:
            input("You find an water bottle!")
            inventory.append("Water bottle")
        elif final_loot_value == 6:
            input("You find an Meal Ready to Eat!")
            inventory.append("MRE")
        elif final_loot_value == 7:
            gamble = random.randint(10, 20)
            b_a = gamble + luck
            input(f"You find {b_a} 9mm ammo!")
            bullets = bullets + b_a
        elif final_loot_value == 8:
            gamble = random.randint(3, 8)
            s_a = gamble + luck
            input(f"You find {s_a} shotgun shells!")
            shells = shells + s_a
        elif final_loot_value == 9:
            gamble = random.randint(15, 35)
            b_a = gamble + luck
            input(f"You found {b_a} 9mm bullets!")
            bullets = bullets + b_a
        else:
            if final_loot_value > 0:
                input(f"You found an shotgun!{bcolors.END}")
                inventory.append("Shotgun")
        return bullets, shells


# If you visit a settlement this shit comes on
def settlement_visit(bullets, shells, health, hydration, food, town,
                     shotgun_equipped, pistol_equipped, survived_days, loot):
    work = random.randint(0, 2)
    area_name = area_namer()
    while True:
        user_input = input(f"""You are the town of {area_name}! Where do you want to go?
{bcolors.UNDERLINE}(1) Shop | (2) Bar | (3) Motel | (4) Pawn shop | (5) Inventory | (6) Leave{bcolors.END} """)
        if user_input == "1":  # ammunition used as currency!
            while True:
                user_input = input(f"""Welcome to {area_name}'s shop! What can I get you?{bcolors.GREEN}
    Bullets: {bullets} | Shells: {shells}{bcolors.END}{bcolors.BOLD}
    (1) 10 bullets -> 2 shells
    (2) 2 shell -> 10 bullets
    (3) 20 bullets -> Medical kit
    (4) 100 bullets -> Shotgun
    (5) 20 bullets -> MRE
    (6) 20 bullets -> Water bottle
    (7) 10 bullets -> Can of Beans
    (8) 10 bullets -> Can of Soda{bcolors.END}
    Type anything to leave """)
                if user_input == "1" and bullets >= 10:
                    print("You bought 2 shells for 10 bullets.")
                    bullets = bullets - 10
                    shells = shells + 2
                if user_input == "2" and shells >= 2:
                    print("You bought 10 bullets for 2 shells.")
                    shells = shells - 2
                    bullets = bullets + 10
                if user_input == "3" and bullets >= 20:
                    print("You bought an medical kit for 20 bullets!")
                    inventory.append("Medical kit")
                    bullets = bullets - 20
                if user_input == "4" and bullets >= 100:
                    print("You bought the shotgun for 100 bullets!")
                    inventory.append("Shotgun")
                    bullets = bullets - 100
                if user_input == "5" and bullets >= 20:
                    print(" You bought the MRE for 20 bullets!")
                    inventory.append("MRE")
                    bullets = bullets - 20
                if user_input == "6" and bullets >= 20:
                    print("You bought the Water bottle for 20 bullets!")
                    inventory.append("Water bottle")
                    bullets = bullets - 20
                if user_input == "7" and bullets >= 10:
                    print("You bought the can of beans for 10 bullets!")
                    inventory.append("Beans")
                    bullets = bullets - 10
                if user_input == "8" and bullets >= 10:
                    print("You bought the can of soda for 10 bullets!")
                    inventory.append("Soda")
                    bullets = bullets - 10
                else:
                    user_input = input(f"{bcolors.GREEN}Are you done shopping? (Y/N) {bcolors.END}")
                    if user_input.lower() == "y":
                        break
        if user_input == "2":
            while True:
                user_input = input(f"""Welcome to {area_name}'s bar!{bcolors.BOLD}
    (1) 5 bullets -> beer
    (2) 1 shell -> beer
    (3) 10 bullets -> Steak dinner
    (4) 2 shells -> Steak dinner
    (5) Gossip
    Type: Leave {bcolors.END}""")
                if user_input == "1" and bullets >= 5:
                    print("Bottoms up!")
                    bullets = bullets - 5
                    hydration = hydration + 50
                if user_input == "2" and shells >= 1:
                    print("Bottoms up!")
                    shells = shells - 1
                    hydration = hydration + 50
                if user_input == "3" and bullets >= 10:
                    print("Enjoy!")
                    bullets = bullets - 10
                    food = food + 50
                if user_input == "4" and shells >= 2:
                    print("Enjoy!")
                    shells = shells - 2
                    food = food + 50
                if user_input == "5":
                    user_input = input(f"""{bcolors.BOLD}
    (1) Work
    (2) This place {bcolors.END}""")
                    if user_input == "1" and work == 1:
                        user_input = input("""Well... I need someone to do some manual labour... 
Moving 10000 bricks, I'll give you 30 9mm if you do it! Deal? (Y/N) """)
                        if user_input.lower() == "y":
                            bricks = 0
                            while True:
                                bricks = bricks + 1
                                input(f"Press enter to move bricks | Bricks moved {bricks}")
                                if bricks >= 10000:
                                    user_input = input("Well, i'll be damned! You did it! (type pay for payment) ")
                                    if user_input.lower() == "pay":
                                        bullets = bullets + 30
                                        work = work - 1
                                        break
                        else:
                            print("Shame, i knew you was a slacker...")
                    if user_input == "1" and work == 2:
                        user_input = input("""Well, there is this raider gang of 7 that I need clearing...
I'll give you 35 9mm if you do it! Deal? (Y/N) """)
                        if user_input.lower() == "y":
                            work = work - 1
                            threat = 7
                            coward_check = health
                            threat, bullets, shells, health = threat_battle(threat, bullets, shells, health,
                                                                            shotgun_equipped, pistol_equipped,
                                                                            survived_days, loot)
                            if coward_check == health:
                                input("Hmm, you're not even slightly scratched? I dont think you took care of them...")
                            if coward_check != health:
                                input("You took care of them? That's great!")
                                bullets = bullets + 35
                        else:
                            print("Shame... I knew you was a slacker...")

                    if user_input == "2":
                        input(f"{area_name} is a small town, I have {work} job offers.")
                if user_input.lower() == "leave":
                    break
        if user_input == "3":
            user_input = input(f"""Welcome to {area_name}'s motel! 
{bcolors.BOLD}A night costs 10 bullets! Interested? (Y/N) {bcolors.END}""")
            if user_input.lower() == "y":
                print("You slept the night in the motel and regained all HP.")
                health = 100
            else:
                print("You left the motel.")
        if user_input == "4":
            while True:
                # Possible_items = ["Water bottle", "MRE", "Beans", "Soda", "Medical kit", "Pistol (ns)", "Shotgun"]
                # ns = not sellable
                print(f"Welcome to {area_name}'s pawn shop!")
                print(inventory)
                user_input = input(f"{bcolors.GREEN}What do you want to sell? 1 for first, 2 for second... ")
                try:
                    anti_crash_measure = len(inventory)
                    anti_crash_measure = anti_crash_measure - int(user_input)
                    if anti_crash_measure >= 0:
                        selected_item = inventory[int(user_input)-1]
                        if selected_item == "Water bottle":
                            user_input = input("Are you sure you want to sell water bottle for 18 bullets? ")
                            if user_input.lower() == "y":
                                inventory.remove(selected_item)
                                print("Sold!")
                                bullets = bullets + 18
                        elif selected_item == "MRE":
                            user_input = input("Are you sure you want to sell MRE for 18 bullets? ")
                            if user_input.lower() == "y":
                                inventory.remove(selected_item)
                                print("Sold!")
                                bullets = bullets + 18
                        elif selected_item == "Beans":
                            user_input = input("Are you sure you want to sell Beans for 8 bullets? ")
                            if user_input.lower() == "y":
                                inventory.remove(selected_item)
                                print("Sold!")
                                bullets = bullets + 8
                        elif selected_item == "Soda":
                            user_input = input("Are you sure you want to sell Soda for 8 bullets? ")
                            if user_input.lower() == "y":
                                inventory.remove(selected_item)
                                print("Sold!")
                                bullets = bullets + 8
                        elif selected_item == "Medical kit":
                            user_input = input("Are you sure you want to sell Medical kit for 18 bullets? ")
                            if user_input.lower() == "y":
                                inventory.remove(selected_item)
                                print("Sold!")
                                bullets = bullets + 18
                        elif selected_item == "Pistol":
                            print("How old is that thing? Im not buying that!")
                        elif selected_item == "Shotgun":
                            user_input = input("Are you sure you want to sell an Shotgun for 90 bullets? ")
                            if user_input.lower() == "y":
                                inventory.remove(selected_item)
                                print("Sold")
                                bullets = bullets + 90
                        else:
                            user_input = input(f"Are you done shopping? (Y/N) {bcolors.END}")
                            if user_input.lower() == "y":
                                break
                        user_input = input(f"Are you done shopping? (Y/N) {bcolors.END}")
                        if user_input.lower() == "y":
                            break
                except ValueError:
                    break
        if user_input == "5":
            print(inventory)
            print(f"{bcolors.BOLD}{bullets} 9mm ammo | {shells} shells")
            print(f"{health}HP | {food} food | {hydration} thirst{bcolors.END}")
        if user_input == "6":
            user_input = input(f"{bcolors.YELLOW}Are you sure you want to leave the town? (Y/N) {bcolors.END}")
            if user_input.lower() == "y":
                town = town - 1
                print(f"You left {area_name}")
                return bullets, shells, health, hydration, food, town


# made by Tiitus 27.8.2022


# aka combat system
def threat_battle(threat, bullets, shells, health, shotgun_equipped, pistol_equipped, survived_days, loot):
    if survived_days > 15:
        enemy_hp = 30
        threat = threat + 1
    else:
        enemy_hp = 20
    enemy_hp = enemy_hp * threat
    if pistol_equipped == 1:
        while True:
            if health <= 0:
                print(f"{bcolors.RED}You died!{bcolors.END}")
                print(f"Days survived: {survived_days}")
                exit()
            if health <= 10:
                input(f"{bcolors.YELLOW}You are severely hurt, now would be a good time to run!{bcolors.END}")
            if bullets == 0:
                input(f"{bcolors.RED}You are out of ammo!{bcolors.END}")
            user_input = input(f"""{bcolors.RED}{threat} enemies! | {enemy_hp} Enemy HP!
{bullets} ammo {health}HP {bcolors.END}
{bcolors.YELLOW}(1) Shoot  | (2) Melee | (3) Flee """)
            if user_input == "1" and bullets >= 4:
                pistol_damage = random.randint(5, 15)
                shots = random.randint(1, 4)
                bullets = bullets - shots
                pistol_damage = pistol_damage * shots
                input(f"You shot at them {shots} times and did {pistol_damage} damage!")
                enemy_hp = enemy_hp - pistol_damage
                if enemy_hp <= 0:
                    input(f"{bcolors.END}You won!")
                    threat = 0
                    bullets, shells = loot_system(loot, bullets, shells)
                    return threat, bullets, shells, health
                health = health - 10
                input(f"{bcolors.RED}They attacked you for 10 HP!")
            elif user_input == "1" and bullets > 0:
                pistol_damage = random.randint(5, 15)
                bullets = bullets - 1
                input(f"You shot once in order to preserve ammunition and did {pistol_damage} damage!")
                enemy_hp = enemy_hp - pistol_damage
                if enemy_hp <= 0:
                    input(f"{bcolors.END}You won!")
                    threat = 0
                    bullets, shells = loot_system(loot, bullets, shells)
                    return threat, bullets, shells, health
                health = health - 10
                input(f"{bcolors.RED}They attacked you for 10 HP!")
            elif user_input == "2":
                melee_damage = random.randint(5, 15)
                input(f"You pistol whipped the enemy and did {melee_damage} damage!")
                enemy_hp = enemy_hp - melee_damage
                if enemy_hp <= 0:
                    input(f"{bcolors.END}You won!")
                    threat = 0
                    bullets, shells = loot_system(loot, bullets, shells)
                    return threat, bullets, shells, health
                health = health - 20
                input(f"{bcolors.RED}They attacked you for 20 HP!")
            elif user_input == "3":
                print("You ran away, how cowardly.")
                threat = 0
                return threat, bullets, shells, health
            else:
                input(f"{bcolors.GREEN}You just stood there idly!")
    if shotgun_equipped == 1:
        while True:
            if health <= 0:
                print(f"{bcolors.RED}You died!{bcolors.END}")
                print(f"Days survived: {survived_days}")
                exit()
            if health <= 10:
                input(f"{bcolors.YELLOW}You are severely hurt, now would be a good time to run!{bcolors.END}")
            if shells == 0:
                input(f"{bcolors.RED}You are out of shells!{bcolors.END}")
            user_input = input(f"""{bcolors.RED}{threat} enemies! | {enemy_hp} Enemy HP!{bcolors.YELLOW}
{shells} shells {health}HP 
(1) Shoot | (2) Melee | (3) Flee """)
            if user_input == "1" and shells >= 3:
                shotgun_damage = random.randint(15, 35)
                shots = random.randint(1, 3)
                shells = shells - shots
                shotgun_damage = shotgun_damage * shots
                input(f"You shot at them {shots} times and did {shotgun_damage} damage!")
                enemy_hp = enemy_hp - shotgun_damage
                if enemy_hp <= 0:
                    input(f"{bcolors.END}You won!")
                    threat = 0
                    return threat, bullets, shells, health
                health = health - 10
                input(f"{bcolors.RED}They attacked you for 10 HP!")
            if user_input == "1" and shells > 0:
                shotgun_damage = random.randint(15, 35)
                input(f"You shot once in order to preserve ammunition and did {shotgun_damage} damage!")
                enemy_hp = enemy_hp - shotgun_damage
                if enemy_hp <= 0:
                    input(f"{bcolors.END}You won!")
                    threat = 0
                    bullets, shells = loot_system(loot, bullets, shells)
                    return threat, bullets, shells, health
                health = health - 10
                input(f"{bcolors.RED}They attacked you for 10 HP!")
            elif user_input == "2":
                melee_damage = random.randint(10, 15)
                input(f"You melee attacked the enemy with the shotgun and did {melee_damage} damage!")
                enemy_hp = enemy_hp - melee_damage
                if enemy_hp <= 0:
                    input(f"{bcolors.END}You won!")
                    threat = 0
                    bullets, shells = loot_system(loot, bullets, shells)
                    return threat, bullets, shells, health
                health = health - 20
                input(f"{bcolors.RED}They attacked you for 20 HP!")
            elif user_input == "3":
                print("You ran away, how cowardly.")
                threat = 0
                return threat, bullets, shells, health
            else:
                input(f"{bcolors.GREEN}You just stood there idly!{bcolors.END}")


# main() function, how does it work? I don't know
def main():
    town = 0  # if it's not 0, you will enter a town
    health = 100  # If it hits 0 you die
    hydration = 100  # If it hits 0 you start to lose health
    food = 100  # -||-
    threat = 0  # How many enemies you will face
    shells = 0  # shotgun ammo amount
    bullets = 25  # pistol ammo
    pistol_equipped = 1  # if you have pistol equipped
    shotgun_equipped = 0  # blah blah blah
    survived_days = 0  # how many days you have survived, it gets hellish after 15, and you win after 30
    total_trip = difficulty_selector()
    days_spent_dehydrated = 0
    days_spent_starving = 0
    while 1:
        loot = -10
        if hydration <= 0:
            input(f"{bcolors.RED}You are dying from dehydration!{bcolors.END}")
            health = health - 15
            days_spent_dehydrated = days_spent_dehydrated + 1
        if food <= 0:
            input(f"{bcolors.RED}You are starving to death!{bcolors.END}")
            health = health - 10
            days_spent_starving = days_spent_starving + 1
        hydration = hydration - 25
        food = food - 20
        health = health + 5
        food, hydration, health, pistol_equipped, shotgun_equipped = \
            inv_sys(bullets, shells, food, hydration, health, pistol_equipped, shotgun_equipped, survived_days)
        random_event = random.randint(0, 10)
        survived_days = survived_days + 1
        trip_left = (survived_days / total_trip) * 100
        print(f"You have survived {survived_days} days! You have travelled {round(trip_left)}% to the safe zone!")
        if survived_days == round(total_trip / 2):
            user_input = input(f"""You arrive at the large slum town, which is the halfway point to the safe zone. 
{bcolors.UNDERLINE}The local governor ask you to join him in his personal quarters. Do you accept? (Y/N) 
{bcolors.END}""")
            if user_input.lower() == "y" and len(inventory) > 6:
                user_input = input(f"""{bcolors.RED}It was a trap! The governor and his men are after your loot!
Do you: (1) Fight (8 enemies) | (2) Flee""")
                if user_input == "1":
                    threat = 8
                    loot = 8
                    threat, bullets, shells, health = threat_battle(threat, bullets, shells, health, shotgun_equipped,
                                                                    pistol_equipped, survived_days, loot)
                    print("You murdered the governor and his men. There was quite a bit of loot!")
                    print(f"""{bcolors.GREEN}+ 50 9mm | + 20 12g | + 3 MRE | + 3 Water bottle |
            + 2 Medical kit | + 1 Shotgun{bcolors.END}""")
                    bullets = bullets + 50
                    shells = shells + 20
                    inventory.append("MRE")
                    inventory.append("MRE")
                    inventory.append("MRE")
                    inventory.append("Water bottle")
                    inventory.append("Water bottle")
                    inventory.append("Water bottle")
                    inventory.append("Medical kit")
                    inventory.append("Medical kit")
                    inventory.append("Shotgun")
                    survived_days = survived_days + 1
                else:
                    survived_days = survived_days + 1
                    print("You got out of there faster than you ever have before!")
            if user_input.lower() == "y" and len(inventory) < 7:
                print(f"""I have heard a lot about your travels. You have made impressively far. I want to help you. 
If you decide to continue, do know that {bcolors.BOLD}out there is a lot more hostiles than what you're used to...
{bcolors.GREEN}You got 2x Water bottles, 1x MRE, 20x 9mm, Shotgun, 10x 12g!{bcolors.END}""")
                inventory.append("Water bottle")
                inventory.append("Water bottle")
                inventory.append("MRE")
                inventory.append("Shotgun")
                bullets = bullets + 20
                shells = shells + 10
            survived_days = survived_days + 1
            bullets, shells, health, hydration, food, town = \
                settlement_visit(bullets, shells, health, hydration, food, town, shotgun_equipped, pistol_equipped,
                                 survived_days, loot)

        car = 0
        if random_event == 0:
            location = "an house"
            loot = 2
            threat = 2
        elif random_event == 1:
            location = "an car"
            loot = 1
            threat = 0
            car = 1
        elif random_event == 2:
            location = "an church"
            loot = 1
            threat = 2
        elif random_event == 3:
            location = "an cabin"
            loot = 2
            threat = 1
        elif random_event == 4:
            location = "an old military convoy"
            loot = 5
            threat = 8
        elif random_event == 5:
            location = "an TV station"
            loot = 3
            threat = 2
        elif random_event == 6:
            location = "an settlement"
            loot = -10
            town = 1
        elif random_event == 7:
            location = "an old fire station"
            loot = 4
            threat = 3
        elif random_event == 8:
            location = "an police station"
            loot = 6
            threat = 5
        elif random_event == 9:
            location = "an school"
            loot = 3
            threat = 4
        else:
            location = "an hospital"
            loot = 3
            threat = 5
        if survived_days == total_trip:
            print("""I really did it. I made it here. It's quite the overpopulated city, 
but the best damn city this side of the earth.""")
            print("Final stats:")
            print(inventory)
            print(f"""{bullets} 9mm | {shells} 12g
{health} HP | {food} Food | {hydration} Hydration
Total days spent dehydrated: {days_spent_dehydrated}
Total days spent starving: {days_spent_starving}""")
            user_input = input("Do you want to continue in endless mode? (Somethings will break!) (Y/N) ")
            if user_input.lower() == "n":
                print("Congratulations on your win and goodbye!")
                exit()
        user_input = input(f"{bcolors.CYAN}You find {location}. Do you want to go in? (Y/N) ")
        if user_input.lower() == "y":
            if car == 1:
                bullets, shells = loot_system(loot, bullets, shells)
            if threat > 0:
                input(f"{bcolors.YELLOW}{threat} enemies blocked your path!{bcolors.END}")
                threat, bullets, shells, health = threat_battle(threat, bullets, shells, health,
                                                                shotgun_equipped, pistol_equipped,
                                                                survived_days, loot)
            if town >= 1:
                bullets, shells, health, hydration, food, town \
                    = settlement_visit(bullets, shells, health, hydration, food, town, shotgun_equipped,
                                       pistol_equipped, survived_days, loot)

        else:
            threat = 0
            town = 0


input("""
  ___   ___  _____ _____ 
 |__ \\ / _ \\| ____| ____|
    ) | | | | |__ | |__  
   / /| | | |___ \\|___ \\ 
  / /_| |_| |___) |___) |
 |____|\\___/|____/|____/ 
                         
                    
The year is 2055 and the world has collapsed into anarchy. Mutated creatures roam the earth and raider gangs control
significant parts of the territory. A couple pockets of organised government activity still exist. These areas are so 
called safe zones. You hope to start a new life at the nearest safe zone, but it is an 30 day trip through the 
challenging no mans land.
""")

if __name__ == '__main__':
    main()


# made by Tiitus 27.8.2022
