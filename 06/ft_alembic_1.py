# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_1.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:41:12 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:50:57 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from elements import create_water


def main() -> None:
    """Main to import water creating function"""
    print("=== Alembic 1 ===")
    print("Using 'form ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
