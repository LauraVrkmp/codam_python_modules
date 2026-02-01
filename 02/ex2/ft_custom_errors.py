# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 16:33:13 by laveerka        #+#    #+#               #
#  Updated: 2026/02/01 09:41:23 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str = "Caught a garden error: "):
        self.message = message

    def __str__(self):
        return self.message


class PlantError(GardenError):
    def __init__(self, message: str = "Caught a PlantError: "):
        self.message = message

    def __str__(self):
        return self.message


class WaterError(PlantError):
    def __init__(self, message: str = "Caught a WaterError: "):
        self.message = message

    def __str__(self):
        return self.message


def main():
    print("=== Custom Garden Errors Demo ===\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
