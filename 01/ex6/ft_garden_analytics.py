# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:50 by laveerka        #+#    #+#               #
#  Updated: 2026/01/30 10:35:43 by laveerka        ###   ########.fr        #
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

    # @classmethod
    # def get_total(cls):
    #     return cls.total_flowering


class PrizeFlower(FloweringPlant):
    total_prize = 0

    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points
        self.total_prize += 1

    def describe(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flower (blooming)"
              f", Prize points: {self.points}")

    # @classmethod
    # def get_total(cls):
    #     return cls.total_prize


class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant):
        print(f"Added {plant.name} to {self.owner}'s garden")
        self.plants.append(plant)

    def grow_all(self):
        print(f"\n{self.owner} is helping all plants grow...")
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
        self.gardens: dict[str, Garden] = {}
        self.stats = GardenStats()

    def add_garden(self, garden: Garden) -> None:
        self.gardens[garden.owner] = garden

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        manager = cls()
        alice = Garden("Alice")
        bob = Garden("Bob")
        manager.add_garden(alice)
        manager.add_garden(bob)
        alice.add_plant(Plant("Oak Tree", 100))
        alice.add_plant(FloweringPlant("Rose", 25, "red"))
        alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
        return manager

    def total_gardens(self) -> int:
        total = 0
        for _ in self.gardens:
            total += 1
        return total


def print_demo() -> GardenManager:
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network()
    manager.gardens["Alice"].grow_all()
    return manager


def print_report(manager: GardenManager):
    alice_garden = manager.gardens["Alice"]
    bob_garden = manager.gardens["Bob"]
    print("\n=== Alice's Garden Report ===")
    print("Plants in garden:")
    for plant in manager.gardens["Alice"].plants:
        plant.describe()
    manager.stats.total_plants()
    manager.stats.total_growth(alice_garden)
    manager.stats.plant_types()
    print()
    print("Height validation test: ...")
    print(f"Garden scores - Alice: "
          f"{manager.stats.scores(alice_garden)}, Bob: "
          f"{manager.stats.scores(bob_garden)}")
    print(f"Total gardens managed: {manager.total_gardens()}")


if __name__ == "__main__":
    print("== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network()
    print_report(manager)
