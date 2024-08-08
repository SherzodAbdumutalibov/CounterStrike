from shootable import Shootable
from Person import Person

class SpecialOPS(Person, Shootable):

    def buy_defuse_kit(self): # Купить набор сапера
        self.__defuse_kit = True
        if self.__defuse_kit == False:
            print('Набор сапера приобретено')

        ## AttributeError: 'Terrorist' object has no attribute '_Terrorist__bomb'

        # if self.__defuse_kit == False:
        #     self.__defuse_kit = True
        #     print('Купил набор сапера')
        # else:
        #     print('Киты имеются')     

    def throw_dufuse_kit(self):
        self.__defuse_kit = False
        if self.__defuse_kit == True:
            print('Выбрасил киты')
