# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_0.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:42:25 by laveerka        #+#    #+#               #
#  Updated: 2026/11/03 14:05:19 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.grimoire


def main() -> None:
    """Main to test circular dependencies - functional"""
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    spell_name: str = "Fantasy"
    ingredients: str = "Earth, wind and fire"
    result: str = alchemy.grimoire.light_spell_record(spell_name, ingredients)
    print(f"Testing record light spell: {result}")


if __name__ == "__main__":
    main()
