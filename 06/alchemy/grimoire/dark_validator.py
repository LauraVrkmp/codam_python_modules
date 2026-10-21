# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dark_validator.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:39:34 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:38:39 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    """Returns wether any ingredient is on the allow list"""
    allowed = dark_spell_allowed_ingredients()
    if any(item in ingredients.lower() for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
