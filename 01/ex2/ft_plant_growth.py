# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:35:56 by laveerka        #+#    #+#               #
#  Updated: 2026/01/31 12:21:25 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """
    Generates a plant object with name, height and age attributes
    """
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    """Allows the plant object to grow height by 1"""
    def grow(self) -> None:
        self.height += 1

    """Allows the plant object to grow age by 1"""
    def age(self) -> None:
        self.days += 1


def get_info(plant: Plant, current_day: int) -> None:
    """Prints information on the current day and attibutes of Plant"""
    print(f"=== Day {current_day} ===")
    print(f"{plant.name}: {plant.height}cm, {plant.days} days old")


def main() -> None:
    """Main function simulating plant growth"""
    plant = Plant("Rose", 25, 30)
    current_day = 1
    growth = 0
    get_info(plant, current_day)
    for _ in range(6):
        plant.grow()
        plant.age()
        current_day += 1
        growth += 1
    get_info(plant, current_day)
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
