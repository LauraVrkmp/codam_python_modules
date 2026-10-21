# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  creature_class.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 03:37:24 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 15:51:42 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str, attack_style: str) -> None:
        self.name = name
        self.type = type
        self.attack_style = attack_style

    @abstractmethod
    def attack(self, attack_style: str | None = None) -> str:
        return f"{self.name} uses {self.attack_style}"

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"
