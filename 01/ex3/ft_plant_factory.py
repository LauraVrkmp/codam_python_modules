# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:09 by laveerka        #+#    #+#               #
#  Updated: 2026/01/31 12:27:28 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """Initializes Plant object with name, height and age attributes"""
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days


def create_plants() -> list[Plant]:
    """Creates a list of Plant objects"""
    plants = [Plant("Rose", 25, 30), Plant("Oak", 200, 365),
              Plant("Cactus", 5, 90), Plant("Sunflower", 80, 45),
              Plant("Fern", 15, 120)]
    return plants


def print_output(plants: list[Plant]) -> None:
    """Prints information on the created list of Plants"""
    print("=== Plant Factory Output ===")
    count = 0
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.days} days)")
        count += 1
    print(f"\nTotal plants created: {count}")


def main() -> None:
    """Main function of the plant creation factory"""
    plants = create_plants()
    print_output(plants)


if __name__ == "__main__":
    main()
