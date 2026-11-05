# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  capabilities_inheritance.py                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 05:39:53 by laveerka        #+#    #+#               #
#  Updated: 2026/11/05 14:26:54 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.creature_class import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass", "Vine Whip")

    def attack(self, attack_style: str | None = None) -> str:
        return super().attack(attack_style)

    def heal(self, target: str | None = None) -> str:
        if target:
            return f"{self.name} heals {target} for a small amount"
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloumelle", "Grass/Fairy", "Petal Dance")

    def attack(self, attack_style: str | None = None) -> str:
        return super().attack(attack_style)

    def heal(self, target: str | None = None) -> str:
        if target:
            return f"{self.name} heals {target} and others for a large amount"
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal", "attacks normally")

    def attack(self, attack_style: str | None = None) -> str:
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        else:
            return f"{self.name} {attack_style}."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon", "attacks normally")

    def attack(self, attack_style: str | None = None) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        else:
            return f"{self.name} {attack_style}."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."
