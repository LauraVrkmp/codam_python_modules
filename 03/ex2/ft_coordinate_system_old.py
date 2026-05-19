# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:28 by laveerka        #+#    #+#               #
#  Updated: 2026/02/12 11:26:06 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math

# split main over try/excepts


def main() -> None:
    print("=== Game Coordinate System ===\n")
    pos_0 = (0, 0, 0)
    x_0, y_0, z_0 = pos_0
    pos_1 = (10, 20, 5)
    x_1, y_1, z_1 = pos_1
    distance_0 = math.sqrt((x_1 - x_0)**2 + (y_1 - y_0)**2 + (z_1 - z_0)**2)
    print(f"Position created: {pos_1}")
    print(f"Distance between {pos_0} and {pos_1}: {distance_0:.2f}\n")
    pos_2_str = "3,4,0"
    print(f"Parsing coordinates: \"{pos_2_str}\"")
    pos_2_list = pos_2_str.split(",")
    x_2, y_2, z_2 = 0, 0, 0
    try:
        pos_2 = tuple(int(coord) for coord in pos_2_list)
        print(f"Parsed position: {pos_2}")
        x_2, y_2, z_2 = pos_2
        distance_1 = math.sqrt((x_2 - x_0)**2 + (y_2 - y_0)**2 +
                               (z_2 - z_0)**2)
        print(f"Distance between {pos_0} and {pos_2}: {distance_1}\n")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: {type(error).__name__}, "
              f"Args: {error.args}")
    invalid_str = "abc,def,ghi"
    invalid_list = invalid_str.split(",")
    print(f"Parsing invalid coordinates: \"{invalid_str}\"")
    try:
        pos_3 = tuple(int(coord) for coord in invalid_list)
        print(f"Parsed position: {pos_3}")
        x_3, y_3, z_3 = pos_3
        distance_2 = math.sqrt((x_3 - x_0)**2 + (y_3 - y_0)**2 +
                               (z_3 - z_0)**2)
        print(f"Distance between {pos_0} and {pos_3}: {distance_2}")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: {type(error).__name__}, "
              f"Args: {error.args}")
    print("\nUnpacking demonstration:")
    print(f"Player at x={x_2}, y={y_2}, z={z_2}")
    print(f"Coordinates: X={x_2}, Y={y_2}, Z={z_2}")


if __name__ == "__main__":
    main()
