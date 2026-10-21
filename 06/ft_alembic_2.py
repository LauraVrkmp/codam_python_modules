# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_2.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:41:21 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:43:01 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.elements


def main() -> None:
    """Main to import earth creating function"""
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


if __name__ == "__main__":
    main()
