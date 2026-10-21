# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  light_spellbook.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:39:45 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:39:14 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def light_spell_allowed_ingredients() -> list[str]:
    """Returns the allowed ingredients"""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Returns wether a spell is recorded or rejected"""
    from .light_validator import validate_ingredients
    result = validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    return f"Spell recorded: {spell_name} ({result})"
