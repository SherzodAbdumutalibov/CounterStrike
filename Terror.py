from shootable import Shootable

class Terror(Shootable):    

    def __init__(self, name:str='ZeroSugar', health:int=100, gun:str='glock', bomb:bool=False, money:int=800):
        self.name = name
        self.health = health
        self.gun = gun
        self.bomb = bomb
        self.money = money

    def info(self):
        print(self.__dict__)