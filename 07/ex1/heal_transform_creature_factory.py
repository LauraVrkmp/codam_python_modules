# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  heal_transform_creature_factory.py                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 07:04:41 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 13:00:13 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0 import Creature, CreatureFactory
from ex1.capabilities_inheritance import Sproutling, Bloomelle
from ex1.capabilities_inheritance import Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
