# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_0.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:42:43 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 03:13:39 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.transmutation.recipes as recipes


def main() -> None:
    """Main to call lead_to_gold function in import ... directly"""
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(f"Testing lead to gold: {recipes.lead_to_gold()}")


if __name__ == "__main__":
    main()
