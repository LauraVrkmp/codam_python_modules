# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_0.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:40:59 by laveerka        #+#    #+#               #
#  Updated: 2026/11/02 16:12:18 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import elements


def main() -> None:
    """Main to call create fire function from import"""
    print("=== Alembic 0 ===")
    print("Using 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
