from shootable import Shootable

gun_list = {
            'usp': {'head': 91, 'body': 43, 'hl': 34}, 
            'glock': {'head': 78, 'body': 37, 'hl': 29},
            'deagle': {'head': 96, 'body': 77, 'hl': 62},
            'ak': {'head': 99, 'body': 38, 'hl': 35},
            'm4': {'head': 94, 'body': 41, 'hl': 30}
        }

class SpecialOPS(Shootable):

    def __init__(self, name='ColaClassic', health=100, gun='usp', defuse_kit=False, money=800):
        self.name = name
        self.health = health
        self.gun = gun
        self.defuse_kit = defuse_kit
        self.money = money
            
    def info(self):
        print(self.__dict__)