class Person():
    def __init__(self, name='Person', health=100, gun='usp', money=800):
        self.name = name
        self.health = health
        self.gun = gun
        self.money = money
        self.__bomb = False
        self.__defuse_kit = False

    def info(self):
        print(self.__dict__)
