import random

damage = {
            'usp': {'head': 99, 'body': 43, 'hl': 34},
            'glock': {'head': 98, 'body': 37, 'hl': 29},
            'deagle': {'head': 97, 'body': 77, 'hl': 62},
            'ak': {'head': 100, 'body': 38, 'hl': 30}
            }

class Person:    
    def __init__(self, name: str, health: int, gun: str):
        self.name = name
        self.health = health
        self.gun = gun
    

    def shoot(self, target):
            
            spisok = random.choice(['head', 'body', 'hl'])
            targetDamage = damage[self.gun][spisok]
            shoot = target.health - targetDamage

            if shoot <= 0:
                target.health = 0
                print('Убит', target.name, 'Здоровье -', target.health, target.gun)
                print('————————————————————————————————————————————————————————')
            else:
                target.health = target.health - targetDamage
                

    def info(self):
        print(self.name, "- Здоровье:", self.health, 'Оружие -', self.gun)



police = Person('Counter-Terrorist', 100, 'usp')
enemy = Person('Terrorist', 100, 'glock')


# t_ct = [police, enemy]

# while True:
#     attacker = random.choice(t_ct)
#     target = police if attacker == enemy else enemy
    
#     # Проверка завершения игры
#     attacker.shoot(target)
#     if attacker.health or target.health <= 0:
#         break
