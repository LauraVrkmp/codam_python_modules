# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dark_spellbook.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:39:23 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:37:34 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Returns the allowed ingredients"""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Returns wether a spell is recorded or rejected"""
    result = dark_validate_ingredients(ingredients)
    if "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
    return f"Spell recorded: {spell_name} ({result})"
