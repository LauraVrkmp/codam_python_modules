# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_5.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:41:47 by laveerka        #+#    #+#               #
#  Updated: 2026/11/02 16:21:33 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy import create_air


def main() -> None:
    """Main to call create air function specifically imported"""
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
