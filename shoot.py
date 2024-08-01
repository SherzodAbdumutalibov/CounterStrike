import random
import ct
import t
import gun

damage = {
            'usp': {'head': 91, 'body': 43, 'hl': 34}, 
            'glock': {'head': 78, 'body': 37, 'hl': 29},
            'deagle': {'head': 96, 'body': 77, 'hl': 62},
            'ak': {'head': 99, 'body': 38, 'hl': 35},
            'm4': {'head': 94, 'body': 41, 'hl': 30}
        }

class Attack:

    def shoot(self, target):
        self.shoot = shoot
        hit = random.choice(['head', 'body', 'hl'])
        damage = damage[self.gun][hit]
        target.health = target.health - damage


person_1 = ct.ContTerr()
person_2 = t.Terror()

person_1.shoot(person_2s)















#     spisok = random.choice(['head', 'body', 'hl'])
#     targetDamage = damage[self.gun][spisok]
#     shoot = target.health - targetDamage

#     if shoot <= 0:
#         target.health = 0
#         print('Убит', target.name, 'Здоровье -', target.health, target.gun)
#         print('————————————————————————————————————————————————————————')
#     else:
#         target.health = target.health - targetDamage


