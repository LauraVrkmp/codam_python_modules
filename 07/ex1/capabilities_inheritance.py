# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  capabilities_inheritance.py                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 05:39:53 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 15:52:17 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0 import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass", "Vine Whip")

    def attack(self, attack_style: str | None = None) -> str:
        return super().attack(attack_style)

    def heal(self, target: Creature | None = None) -> str:
        if self.name == "Sproutling":
            return f"{self.name} heals itself for a small amount"
        else:
            return f"{self.name} heals itself and others for a large amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloumelle", "Grass/Fairy", "Petal Dance")

    def attack(self, attack_style: str | None = None) -> str:
        return super().attack(attack_style)

    def heal(self, target: Creature | None = None) -> str:
        if self.name == "Sproutling":
            return f"{self.name} heals itself for a small amount"
        else:
            return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal", "attacks normally")
        self.turn = False

    def attack(self, attack_style: str | None = None) -> str:
        if self.turn:
            return f"{self.name} performs a boosted strike!"
        elif self.attack_style == "attacks normally":
            return f"{self.name} attacks normally."
        else:
            return super().attack(attack_style)

    def transform(self) -> str:
        self.turn = True
        if self.name == "Shiftling":
            return f"{self.name} shifts into a sharper form!"
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon", "attacks normally")
        self.turn = False

    def attack(self, attack_style: str | None = None) -> str:
        if self.turn:
            return f"{self.name} unleashes a devastating morph strike!"
        elif self.attack_style == "attacks normally":
            return f"{self.name} attacks normally."
        else:
            return super().attack(attack_style)

    def transform(self) -> str:
        if self.name == "Shiftling":
            return f"{self.name} shifts into a sharper form!"
        else:
            return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        return f"{self.name} stabilizes its form."
