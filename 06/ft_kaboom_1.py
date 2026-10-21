# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_1.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:42:33 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:48:26 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import traceback


def main() -> None:
    """Main to test circular dependencies - nonfunctional"""
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        print(dark_spell_record("Doom", "bats and frogs"))
    except ImportError:
        traceback.print_exc()


if __name__ == "__main__":
    main()
