# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_4.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:41:39 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:52:18 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy
import traceback


def main() -> None:
    """Main to import air vs. earth creating functions"""
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
