# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_alembic_0.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:40:59 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:41:55 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import elements


def main() -> None:
    """Main to import fire creating function"""
    print("===Alembic 0 ===")
    print("Using 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
