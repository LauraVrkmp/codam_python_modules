# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:35 by laveerka        #+#    #+#               #
#  Updated: 2026/01/27 07:52:00 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days


class Flower(Plant):
    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color = color
    
    def get_type(self) -> str:
        return "Flower"

    def bloom(self) -> None:
        print(f"{self.get_type()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, days: int, trunk_diameter: int) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
    
    def get_type(self) -> str:
        return "Tree"

    def produce_shade(self) -> None:
        print("Tree is producting shade!")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, days: int, harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_type(self) -> str:
        return "Vegetable"


def garden_types():
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    print(f"{rose.name} ({rose.get_type}): {rose.height}cm, {rose.days} days, {rose.color} color")
    rose.bloom()
    print()


if __name__ == "__main__":
    garden_types()