# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  recipes.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:40:35 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:39:50 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ..elements import create_air
from alchemy.potions import strength_potion
from elements import create_fire  # type: ignore


def lead_to_gold() -> str:
    """Returns the lead to gold transmuting string"""
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
            f"and '{strength_potion()}' mixed with '{create_fire()}'")
