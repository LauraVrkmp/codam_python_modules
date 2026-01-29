# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:50 by laveerka        #+#    #+#               #
#  Updated: 2026/01/29 10:39:47 by laveerka        ###   ########.fr        #
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
        print(f"{name} grew {self.growth_rate}cm")
        self.height += self.growth_rate

    def describe(self):
        print(f"- {self.name}: {self.height}cm")

    @classmethod
    def get_total(cls):
        return cls.total_plants


class FloweringPlant(Plant):
    total_flowering = 0

    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        FloweringPlant.total_flowering += 1

    def describe(self):
        print(f"- {self.name}: {self.height}cm, {self.color} "
              f"flower (blooming)")

    @classmethod
    def get_total(cls):
        return cls.total_flowering


class PrizeFlower(FloweringPlant):
    total_prize = 0

    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points
        self.total_prize += 1

    def describe(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flower (blooming)"
              f", Prize points: {self.points}")

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
    def total_plants(self):
        total = (Plant.get_total() + FloweringPlant.get_total()
                 + PrizeFlower.get_total())
        print(f"Plants added: {total}")

    @staticmethod
    def total_growth(garden: Garden):
        total = 0
        for plant in garden.plants:
            total += plant.growth_rate
        print(f"Total growth: {total}")

    def plant_types(self):
        print(f"Plant types: {Plant.get_total()} regular, "
              f"{FloweringPlant.get_total()} flowering, "
              f"{PrizeFlower.get_total()} prize flowers")

    def scores(self, garden: Garden):
        total = 0
        for plant in garden.plants:
            total += plant.height
        print(f"Total growth: {total}cm")


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
    alice_garden = manager.gardens[0]
    bob_garden = manager.gardens[1]
    print("\n=== Alice's Garden Report ===")
    print("Plants in garden:")
    for plant in manager.gardens[0].plants:
        plant.describe()
    manager.stats.total_plants()
    manager.stats.total_growth(alice_garden)
    manager.stats.plant_types()
    print()
    print("Height validation test: ...")
    print(f"Garden scores - {manager.gardens[0].name}: "
          f"{manager.stats.scores(alice_garden)}, Bob: "
          f"{manager.stats.scores(bob_garden)}")
    print(f"Total gardens managed: {manager.total_gardens()}")


if __name__ == "__main__":
    manager = print_demo()
    print_report(manager)
