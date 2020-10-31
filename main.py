from game import Person, Bcolors
from magic import Spell
from inventory import Item

# These are the black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# These are the white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hiPotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superPotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 5000)
megaElixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity" : 15},{"item": hiPotion, "quantity" : 5},{"item": superPotion, "quantity" : 5},{"item": elixer, "quantity" : 5},{"item": megaElixer, "quantity" : 2},{"item": grenade, "quantity" : 5},]


# Instantiate the players
player = Person(460, 65, 60, 34, player_spells, player_items)

enemy = Person(1200, 65, 45, 25, [], [])

running = True

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS! 😱" + Bcolors.ENDC)

while running:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) -1
    
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(" You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) -1

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
            enemy.take_damage(magic_dmg)
            print(Bcolors.OKBLUE + "\n " + spell.name + "deals", str(magic_dmg), "points of damage" + Bcolors.ENDC)
            
    elif index == 2:
        player.choose_item()
        Item_choice = int(input("Choose an item: ")) - 1

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
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(Bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + Bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(Bcolors.FAIL + "\n" + item.name + " deals ", str(item.prop), "points of damage" + Bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("===================================================================")
    print("Enemy HP: ", Bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolors.ENDC + "\n")
    print("Your HP: " , Bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Bcolors.ENDC)
    print("Your MP: ", Bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + Bcolors.ENDC + "\n")
    

    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "You win! 🥳" + Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.FAIL + "Your enemy has defeated you! 😢" + Bcolors.ENDC )
        running = False
