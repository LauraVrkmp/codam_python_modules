# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_distillation_0.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:42:00 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:54:01 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    """Main to import strength and healing potion brew functions"""
    print("== Distilation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")


if __name__ == "__main__":
    main()
