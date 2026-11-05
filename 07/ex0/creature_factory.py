# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  creature_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 04:01:16 by laveerka        #+#    #+#               #
#  Updated: 2026/11/05 11:18:39 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from .creature_class import Creature
from .creature_inheritance import Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """Abstract method to create a base Creature"""
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    """Abstract method to create an evolved Creature"""
    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    """"Concrete method to create base Flame Creature"""
    def create_base(self) -> Creature:
        return Flameling()

    """Concrete method to create evolved Flame Creature"""
    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Concrete method to create base Aqua Creature"""
    def create_base(self) -> Creature:
        return Aquabub()

    """Concrete method to create evolved Aqua Creature"""
    def create_evolved(self) -> Creature:
        return Torragon()
