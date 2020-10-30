import random

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person: # hp : Health Points, mp : Magic Points, atk : Attack, atkl: Low Attack, atkh : Attack High, df : Defense
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk -10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic # going to be a dict of different spells 
        self.actions = ["Attack", "Magic"] # this is whats going to be displayed everytime it prompt us to take a turn.

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh) # thats going to generate numbers for the attacks to be random 



