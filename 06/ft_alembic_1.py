# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_1.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:41:12 by laveerka        #+#    #+#               #
#  Updated: 2026/11/02 16:19:22 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from elements import create_water


def main() -> None:
    """Main to call create water function from elements"""
    print("=== Alembic 1 ===")
    print("Using 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
