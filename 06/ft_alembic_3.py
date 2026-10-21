# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_3.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:41:31 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:43:23 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_air


def main() -> None:
    """Main to import air creating function"""
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using 'from ... import ...' "
          "structure")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
