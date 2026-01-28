# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:35 by laveerka        #+#    #+#               #
#  Updated: 2026/01/28 08:33:45 by laveerka        ###   ########.fr        #
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
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, days: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def get_type(self) -> str:
        return "Tree"

    def produce_shade(self, name: str, height: int) -> None:
        pi = 3.1416
        h = height / 100
        shade = pi * h * h
        print(f"{name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, days: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_type(self) -> str:
        return "Vegetable"


def garden_types():
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    print(f"{rose.name} ({rose.get_type()}): {rose.height}cm, {rose.days} "
          f"days, {rose.color} color")
    rose.bloom()
    sunflower = Flower("Sunflower", 150, 45, "yellow")
    print(f"{sunflower.name} ({sunflower.get_type()}): {sunflower.height}cm, "
          f"{sunflower.days} days, {sunflower.color} color")
    sunflower.bloom()
    print()
    oak = Tree("Oak", 500, 1825, 50)
    print(f"{oak.name} ({oak.get_type()}): {oak.height}cm, {oak.days} "
          f"days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade(oak.name, oak.height)
    birch = Tree("Birch", 350, 1255, 32)
    print(f"{birch.name} ({birch.get_type()}): {birch.height}cm, {birch.days} "
          f"days, {birch.trunk_diameter}cm diameter")
    birch.produce_shade(birch.name, birch.height)
    print()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(f"{tomato.name} ({tomato.get_type()}): {tomato.height}cm, "
          f"{tomato.days} days, {tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
    sprout = Vegetable("Sprout", 15, 60, "winter", "vitamin K")
    print(f"{sprout.name} ({sprout.get_type()}): {sprout.height}cm, "
          f"{sprout.days} days, {sprout.harvest_season} havest")
    print(f"{sprout.name} is rich in {sprout.nutritional_value}")


if __name__ == "__main__":
    garden_types()
