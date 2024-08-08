from SpecialOPS import SpecialOPS
from Terror import Terrorist

police = SpecialOPS('Police')
terror = Terrorist('Terrorist')

police.shoot(terror)
terror.shoot(police)
police.shoot(terror)
terror.shoot(police)
