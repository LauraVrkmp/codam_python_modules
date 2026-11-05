# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  creature_class.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 03:37:24 by laveerka        #+#    #+#               #
#  Updated: 2026/11/05 14:26:24 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract creature class with characteristics"""
    def __init__(self, name: str, type: str, attack_style: str) -> None:
        self.name = name
        self.type = type
        self.attack_style = attack_style

    """Attack method required to instantiate Creature"""
    @abstractmethod
    def attack(self, attack_style: str | None = None) -> str:
        return f"{self.name} uses {self.attack_style}!"

    """Describe method required to instantiate Creature"""
    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"
