# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:28 by laveerka        #+#    #+#               #
#  Updated: 2026/02/12 09:02:19 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys, math


def main():
    print("=== Game Coordinate System ===\n")
    pos_0 = (0, 0, 0)
    x_0, y0_z0 = pos_0
    pos_1 = (10, 20, 5)
    x_1, y1, z1 = pos_1
    distance_0 = math.sqrt((x_1 - x_0)**2 + (y_1 - y_0)**2 + (z_1 - z_0)**2)
    print(f"Position created: {pos_1}")
    print(f"Distance between {pos_0} and {pos_1}: ")


if __name__ == "__main__":
    main()