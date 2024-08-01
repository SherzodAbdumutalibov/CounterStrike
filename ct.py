class ContTerr:    

    def __init__(self, name:str='ColaClassic', health:int=100, gun:str='usp', defuse_kit:bool=False, money:int=800):
        self.name = name
        self.health = health
        self.gun = gun
        self.defuse_kit = defuse_kit
        self.money = money
            
    def info(self):
        print(self.__dict__)

