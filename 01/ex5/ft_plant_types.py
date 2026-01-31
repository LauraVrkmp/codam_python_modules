# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:35 by laveerka        #+#    #+#               #
#  Updated: 2026/01/31 13:48:38 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        """Initializes a Plant object with name, height and age attributes"""
        self.name = name
        self.height = height
        self.days = days


class Flower(Plant):
    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        """Inherits from Plant class and adds color attribute"""
        super().__init__(name, height, days)
        self.color = color

    def get_type(self) -> str:
        """Returns Flower type"""
        return "Flower"

    def bloom(self) -> None:
        """Prints the Flower blooming"""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, days: int,
                 trunk_diameter: int) -> None:
        """"Inherits from Plant class and adds trunk diameter attribute"""
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def get_type(self) -> str:
        """Returns Tree type"""
        return "Tree"

    def produce_shade(self, name: str, height: int) -> None:
        """Prints shade produced based on height"""
        pi = 3.1416
        h = height / 100
        shade = pi * h * h
        print(f"{name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, days: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Inherits from Plant class and
        adds harvest season and nutritional value
        """
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_type(self) -> str:
        """Returns Vegetable type"""
        return "Vegetable"


def main():
    print("=== Garden Plant Types ===\n")
    flowers = [Flower("Rose", 25, 30, "red"), Flower("Sunflower",
                                                     150, 45, "yellow")]
    for flower in flowers:
        print(f"{flower.name} ({flower.get_type()}): {flower.height}cm, "
              f"{flower.days} days, {flower.color} color")
        flower.bloom()
    print()
    trees = [Tree("Oak", 500, 1825, 50), Tree("Birch", 350, 1255, 32)]
    for tree in trees:
        print(f"{tree.name} ({tree.get_type()}): {tree.height}cm, {tree.days} "
              f"days, {tree.trunk_diameter}cm diameter")
        tree.produce_shade(tree.name, tree.height)
    print()
    vegetables = [Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
                  Vegetable("Sprout", 15, 60, "winter", "vitamin K")]
    for vegetable in vegetables:
        print(f"{vegetable.name} ({vegetable.get_type()}): "
              f"{vegetable.height}cm, {vegetable.days} days, "
              f"{vegetable.harvest_season} harvest")
        print(f"{vegetable.name} is rich in {vegetable.nutritional_value}")


if __name__ == "__main__":
    main()
