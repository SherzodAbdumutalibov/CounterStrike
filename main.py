from ct import ContTerr
from t import Terror 
from shoot import shoot
from gun import choose_gun

person_1 = ContTerr()
person_2 = Terror()

person_1.info()
person_2.info()

person_1.shoot(person_2)
