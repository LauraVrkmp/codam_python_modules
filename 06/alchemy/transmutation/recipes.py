# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  recipes.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:40:35 by laveerka        #+#    #+#               #
#  Updated: 2026/11/03 13:57:49 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ..elements import create_air
from elements import create_fire  # type: ignore
from alchemy.potions import strength_potion


def lead_to_gold() -> str:
    """Returns the lead to gold transmuting string"""
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
            f"and '{strength_potion()}' mixed with '{create_fire()}'")
