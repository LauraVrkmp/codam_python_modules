# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 16:33:13 by laveerka        #+#    #+#               #
#  Updated: 2026/02/02 07:23:47 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    """Base class for garden errors, based on Exception"""
    pass


class PlantError(GardenError):
    """"Child class for plant errors, based on GardenError"""
    pass


class WaterError(GardenError):
    """Child class for water errors, based on GardenError"""
    pass


def check_plant() -> None:
    """Raises PlantError with custom message"""
    raise PlantError("The tomato plant is wilting!")


def check_tank() -> None:
    """Raises WaterError with custom message"""
    raise WaterError("Not enough water in the tank!")


def specific_errors() -> None:
    """Tests plant and water errors"""
    print("\nTesting PlantError...")
    try:
        check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print("\nTesting WaterError...")
    try:
        check_tank()
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def garden_errors() -> None:
    """Tests general garden errros"""
    print("\nTesting catching all garden errors...")
    for function in (check_plant, check_tank):
        try:
            function()
        except GardenError as error:
            print(f"Caught a garden error: {error}")


def main() -> None:
    """Main to demonstrate garden errors"""
    print("=== Custom Garden Errors Demo ===")
    specific_errors()
    garden_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
