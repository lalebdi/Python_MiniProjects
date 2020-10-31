import random
from magic import Spell


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' # this is important to end any color formatting 
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person: # hp : Health Points, mp : Magic Points, atk : Attack, atkl: Low Attack, atkh : Attack High, df : Defense
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk -10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic # going to be a dict of different spells 
        self.items = items
        self.actions = ["Attack", "Magic", "Items"] # this is whats going to be displayed everytime it prompt us to take a turn.

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh) # thats going to generate numbers for the attacks to be random 


    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(Bcolors.OKBLUE + Bcolors.BOLD + "ACTIONS:" + Bcolors.ENDC)
        for item in self.actions:
            print('    ' + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "MAGIC:" + Bcolors.ENDC)
        for spell in self.magic:
            print('    ' + str(i) + ":", spell.name, "(cost: ", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + Bcolors.OKGREEN + Bcolors.BOLD + "ITEMS:" + Bcolors.ENDC)
        for item in self.items:
            print('    ' + str(i) + ".", item.name, ":", item.description, " (x5)")
            i += 1




