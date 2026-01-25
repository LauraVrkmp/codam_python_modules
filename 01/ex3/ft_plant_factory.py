# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:09 by laveerka        #+#    #+#               #
#  Updated: 2026/01/25 09:29:15 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days


def create_plants():
    plants = [Plant("Rose", 25, 3), Plant("Oak", 200, 365),
              Plant("Cactus", 5, 90), Plant("Sunflower", 80, 45),
              Plant("Fern", 15, 120)]
    return plants


def print_output(plants: list[Plant]):
    print("=== Plant factory Output ===")
    count = 0
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.days} days)")
        count += 1
    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    plants = create_plants()
    print_output(plants)
