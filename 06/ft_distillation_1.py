# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_distillation_1.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:42:15 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:54:29 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy


def main() -> None:
    """Main to import strength and healing potion brew functions"""
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strenght_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")


if __name__ == "__main__":
    main()
