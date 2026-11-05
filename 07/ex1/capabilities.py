# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  capabilities.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 05:38:11 by laveerka        #+#    #+#               #
#  Updated: 2026/11/05 13:55:37 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str | None = None) -> str:
        ...


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
