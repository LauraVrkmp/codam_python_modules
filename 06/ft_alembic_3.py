# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_3.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:41:31 by laveerka        #+#    #+#               #
#  Updated: 2026/11/02 16:15:26 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_air


def main() -> None:
    """Main to call create air function specifically imported"""
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using 'from ... import ...' "
          "structure")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
