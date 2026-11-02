# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_4.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:41:39 by laveerka        #+#    #+#               #
#  Updated: 2026/11/02 16:16:50 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy
import traceback


def main() -> None:
    """Main to create air from general import. create earth not available"""
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end="")
    try:
        print(f"{alchemy.create_earth()}")
    except AttributeError:
        tb = traceback.format_exc()
        print("\n".join(line.strip() for line in tb.splitlines()))


if __name__ == "__main__":
    main()
