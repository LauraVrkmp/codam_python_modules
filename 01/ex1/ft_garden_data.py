# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:35:43 by laveerka        #+#    #+#               #
#  Updated: 2026/01/31 12:21:38 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """Initializes a plant object, with attributes name, height and age"""
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days


def display_info() -> None:
    """Creates three plant objects and displays their information"""
    plants = [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45),
              Plant("Cactus", 15, 120)]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.days} days old")


if __name__ == "__main__":
    display_info()
