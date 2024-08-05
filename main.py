from SpecialOPS import SpecialOPS
from Terror import Terror

police = SpecialOPS('Police')
terror = Terror('Terrorist')

terror.shoot(police)
police.shoot(terror)
terror.shoot(police)
police.shoot(terror)
