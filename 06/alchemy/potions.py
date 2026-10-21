# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:40:03 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:41:10 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_air, create_earth
from elements import create_fire, create_water  # type: ignore


def healing_potion() -> str:
    """Returns the brewing process of a healing potion"""
    return (f"Healing potion brewed with '{create_earth()}' and "
            f"'{create_air()}'")


def strength_potion() -> str:
    """Returns the brewing process of a strength potion"""
    return (f"Strength potion brewed with '{create_fire()}' and "
            f"'{create_water()}'")
