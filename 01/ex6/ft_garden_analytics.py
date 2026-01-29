# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:50 by laveerka        #+#    #+#               #
#  Updated: 2026/01/29 09:01:53 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    total_plants = 0

    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.growth_rate = 1
        Plant.total_plants += 1

    def grow(self, name: str):
        print(f"{name} grew 1cm")
        self.height += self.growth_rate

    @classmethod
    def get_total(cls):
        return cls.total_plants


class FloweringPlant(Plant):
    total_flowering = 0

    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        FloweringPlant.total_flowering += 1

    @classmethod
    def get_total(cls):
        return cls.total_flowering


class PrizeFlower(FloweringPlant):
    total_prize = 0

    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points
        self.total_prize += 1

    @classmethod
    def get_total(cls):
        return cls.total_prize


class Garden:
    def __init__(self, name: str):
        self.name = name
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant):
        print(f"Added {plant.name} to {self.name}'s garden")
        self.plants.append(plant)

    def grow_all(self):
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(plant.name)


class GardenStats:
    def total_plants(self, garden: Garden):
        total = (Plant.get_total() + FloweringPlant.get_total()
                 + PrizeFlower.get_total())
        print(f"Plants added: {total}")

    def total_growth(self, garden: Garden):
        return sum(plant.growth_rate for plant in garden.plants)

    def plant_types(self, garden: Garden):
        print(f"Plant types: {Plant.get_total()} regular, "
              f"{FloweringPlant.get_total()} flowering, "
              f"{PrizeFlower.get_total()} prize flowers")

    def scores(self, garden: Garden):
        return sum(plant.height for plant in garden.plants)


class GardenManager:
    def __init__(self) -> None:
        self.gardens: list[Garden] = []
        self.stats = GardenStats()

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)

    def total_gardens(self) -> int:
        return len(self.gardens)


def print_demo() -> GardenManager:
    print("=== Garden Management System Demo ===\n")
    alice = Garden("Alice")
    oak = Plant("Oak Tree", 101)
    rose = FloweringPlant("Rose", 26, "red")
    sunflower = PrizeFlower("Sunflower", 51, "yellow", 10)
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    alice.grow_all()
    bob = Garden("Bob")
    manager = GardenManager()
    manager.add_garden(alice)
    manager.add_garden(bob)
    return manager


def print_report(manager: GardenManager):
    print("=== Alice's Garden Report ===")
    print(f"Total gardens managed: {manager.total_gardens()}")


if __name__ == "__main__":
    manager = print_demo()
    print_report(manager)
