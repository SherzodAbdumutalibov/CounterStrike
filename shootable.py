import random

gun_list = {
            'usp': {'head': 91, 'body': 43, 'hl': 34}, 
            'glock': {'head': 78, 'body': 37, 'hl': 29},
            'deagle': {'head': 96, 'body': 77, 'hl': 62},
            'ak': {'head': 99, 'body': 38, 'hl': 35},
            'm4': {'head': 94, 'body': 41, 'hl': 30}
        }

class Shootable:
    def shoot(self, target):
        if self.health >= 1:
            hit = random.choice(['head', 'body', 'hl'])
            global gun_list
            damage = gun_list[self.gun][hit]
            target.health = target.health - damage

            if target.health <= 0:
                print('\033[31m' + target.name, '\033[37m''убит!')
                print('Осталось здоровья', '\033[34m', self.health, '\033[37m')
