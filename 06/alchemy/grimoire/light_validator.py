# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  light_validator.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:39:52 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:39:26 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Returns wether any ingredient is on the allow list"""
    allowed = light_spell_allowed_ingredients()
    if any(item in ingredients.lower() for item in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
