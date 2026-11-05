# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  heal_transform_creature_factory.py                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 07:04:41 by laveerka        #+#    #+#               #
#  Updated: 2026/11/05 11:51:16 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.creature_class import Creature
from ex0.creature_factory import CreatureFactory
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
