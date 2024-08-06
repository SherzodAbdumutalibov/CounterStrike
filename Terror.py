from shootable import Shootable
from Person import Person

class Terrorist(Person, Shootable):    

    def pickup_bomb(self): # Подобрать бомбу
        self.__bomb = True
        print('Я подобрал бомбу')
        
        ## AttributeError: 'Terrorist' object has no attribute '_Terrorist__bomb'
        
        # if self.__bomb == True:
        #     print('Бомба у меня. Я готов закладывать')
        # else:
        #     self.__bomb = True
        #     print('Я подобрал  бомбу')
        
    def throw_bomb(self): # Бросить бомбу
        self.__bomb = False
        print('Я бросил бомбу')
