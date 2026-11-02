# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_2.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:41:21 by laveerka        #+#    #+#               #
#  Updated: 2026/11/02 16:14:40 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.elements


def main() -> None:
    """Main to call create earth function from direct import"""
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


if __name__ == "__main__":
    main()
