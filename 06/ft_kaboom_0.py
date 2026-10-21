# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_kaboom_0.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:42:25 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:48:38 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.grimoire


def main() -> None:
    """Main to test circular dependencies - functional"""
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: "
          f"{alchemy.grimoire.light_spell_record(
              f"Fantasy", "Earth, wind and fire")}")


if __name__ == "__main__":
    main()
