# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  creature_inheritance.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 03:45:30 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 17:34:17 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .creature_class import Creature


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire", "Ember")

    def attack(self, attack_style: str | None = None) -> str:
        return super().attack(attack_style)


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying", "Flamethrower")

    def attack(self, attack_style: str | None = None) -> str:
        return super().attack(attack_style)


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water", "Water Gun")

    def attack(self, attack_style: str | None = None) -> str:
        return super().attack(attack_style)


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water", "Hydro Pump")

    def attack(self, attack_style: str | None = None) -> str:
        return super().attack(attack_style)
