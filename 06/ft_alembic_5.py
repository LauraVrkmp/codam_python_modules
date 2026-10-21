# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_5.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:41:47 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:53:04 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy import create_air


def main() -> None:
    """Main to import air creating function"""
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
