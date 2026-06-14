# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:28 by laveerka        #+#    #+#               #
#  Updated: 2026/06/14 04:07:43 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            initial = input(
                "Enter new coordinates as floats in format "
                "'x,y,z': "
            )
            parts = initial.split(",")
            if (len(parts) != 3):
                print("Invalid syntax")
                continue
            final: list[float] = []
            for x in parts:
                try:
                    final.append(float(x))
                except ValueError as error:
                    raise ValueError(f"'{x}': {error}") from error
            break
        except ValueError as error:
            print(f"Error on parameter: {error}")
    return final[0], final[1], final[2]


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_0, first_1, first_2 = get_player_pos()
    print(f"Got a first tuple: ({first_0}, {first_1}, {first_2})")
    print(f"It includes: X={first_0}, Y={first_1}, Z={first_2}")
    base = (0, 0, 0)
    base_0, base_1, base_2 = base
    distance_center = math.sqrt((first_0 - base_0)**2 +
                                (first_1 - base_1)**2 + (first_2 + base_2)**2)
    print(f"Distance to center: {distance_center}\n")
    print("Get a second set of coordiantes")
    second_0, second_1, second_2 = get_player_pos()
    distance_points = math.sqrt((second_0 - base_0)**2 +
                                (second_1 - base_1)**2 +
                                (second_2 - base_2)**2)
    print(f"Distance between the 2 sets of coordinates: {distance_points}")


if __name__ == "__main__":
    main()
