from game import Person, Bcolors
from magic import Spell
from inventory import Item
import random

# print("\n\n")
# print("Name                 HP                                   MP")
# print("                     _________________________            __________ ")
# print(Bcolors.BOLD + "Valos:  "+ "460/460      |" + Bcolors.OKGREEN + "████████                " + Bcolors.ENDC + Bcolors.BOLD + "|   " + "65/65   |" + Bcolors.OKBLUE + "█████████" + Bcolors.ENDC + "|")

# print("                     _________________________            __________ ")
# print("Valos:  460/460      |                        |   65/65   |         |")

# print("                     _________________________            __________ ")
# print("Valos:  460/460      |                        |   65/65   |         |")

# print("\n\n")

# These are the black magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 50, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# These are the white magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hiPotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superPotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 5000)
megaElixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity" : 15},{"item": hiPotion, "quantity" : 5},{"item": superPotion, "quantity" : 5},{"item": elixer, "quantity" : 5},{"item": megaElixer, "quantity" : 2},{"item": grenade, "quantity" : 5},]


# Instantiate the players
player1 = Person("Natasha:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Bella:  ", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Maryusa:", 3089, 174, 288, 34, player_spells, player_items)

enemy1 = Person("Minion",1250, 130, 560, 325, [], [])
enemy2 = Person("Vegas ",18200, 700, 525, 25, [], [])
enemy3 = Person("Minion",1250, 130, 560, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS! 😱" + Bcolors.ENDC)

while running:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print('\n\n')
    print("NAME        HP                                       MP")
    for player in  players:
        player.get_stats()

    print('\n')
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("     Choose action: ")
        index = int(choice) -1
        
        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print(" You attacked" + enemies[enemy].name + "for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died")
                del enemies[enemy]
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) -1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(Bcolors.FAIL + "\n Not enough MP \n" + Bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + "heals for", str(magic_dmg), "HP." + Bcolors.ENDC)
            elif spell.type == "black":

                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                
                print(Bcolors.OKBLUE + "\n " + spell.name + "deals", str(magic_dmg), "points of damage to" + enemies[enemy].name + Bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died")
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            Item_choice = int(input("    Choose an item: ")) - 1

            if Item_choice == -1:
                continue

            item = player.items[Item_choice]["item"]

            if player.items[Item_choice]["quantity"] == 0:
                print(Bcolors.FAIL + "\n" + " None left... 😥" + Bcolors.ENDC)
                continue
            player.items[Item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(Bcolors.OKGREEN + "\n" + item.name + " heals for ", str(item.prop), "HP" + Bcolors.ENDC)

            elif item.type == "elixer":
                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(Bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + Bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                
                print(Bcolors.FAIL + "\n" + item.name + " deals ", str(item.prop), "points of damage to "+ enemies[enemy].name + Bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died")
                    del enemies[enemy]

    enemy_choice = 1
    
    target = random.randrange(0, 3)
    enemy_dmg = enemies[0].generate_damage()

    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies +=1

    for player in players:
        if player.get_hp() == 0:
            defeated_players +=1
    
    if defeated_enemies == 2:
        print(Bcolors.OKGREEN + "You win! 🥳" + Bcolors.ENDC)
        running = False
    elif defeated_players == 2:
        print(Bcolors.FAIL + "Your enemy have defeated you! 😢" + Bcolors.ENDC )
        running = False
