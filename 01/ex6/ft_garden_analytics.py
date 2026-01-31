# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:50 by laveerka        #+#    #+#               #
#  Updated: 2026/01/31 13:50:05 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# include docstrings, perform height validation, check flowering vs.
# prize flowers

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


class PrizeFlower(FloweringPlant):
    total_prize = 0

    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points
        self.total_prize += 1

    def describe(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flower (blooming)"
              f", Prize points: {self.points}")


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
    def __init__(self, manager: "GardenManager"):
        self.manager = manager

    def total_plants_growth(self):
        total_growth = 0
        for garden in self.manager.gardens.values():
            for plant in garden.plants:
                total_growth += plant.growth_rate
        print(f"Plants added: {Plant.total_plants}, "
              f"Total growth: {total_growth}")

    def plant_types(self):
        regular = Plant.total_plants - FloweringPlant.total_flowering
        flowering = FloweringPlant.total_flowering - PrizeFlower.total_prize
        prize = PrizeFlower.total_prize
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers")

    def scores(self, garden: Garden) -> int:
        total = 0
        for plant in garden.plants:
            total += plant.height
        return total


class GardenManager:
    def __init__(self) -> None:
        self.gardens: dict[str, Garden] = {}
        self.stats = GardenStats(self)

    def add_garden(self, garden: Garden) -> None:
        self.gardens[garden.owner] = garden

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        manager = cls()
        alice = Garden("Alice")
        bob = Garden("Bob")
        manager.add_garden(alice)
        manager.add_garden(bob)
        return manager

    def total_gardens(self) -> int:
        total = 0
        for _ in self.gardens:
            total += 1
        return total


def print_demo() -> GardenManager:
    print("=== Garden Management System Demo ===")
    manager = GardenManager.create_garden_network()
    manager.gardens["Alice"].grow_all()
    manager.gardens["Alice"].add_plant(Plant("Oak Tree", 100))
    manager.gardens["Alice"].add_plant(FloweringPlant("Rose", 25, "red"))
    manager.gardens["Alice"].add_plant(PrizeFlower("Sunflower", 50,
                                                   "yellow", 10))
    manager.gardens["Alice"].grow_all()
    return manager


def print_report(manager: GardenManager):
    print(f"=== {manager.gardens["Alice"].owner}'s Garden Report ===")
    print("Plants in garden:")
    for plant in manager.gardens["Alice"].plants:
        plant.describe()
    print()
    manager.stats.total_plants_growth()
    manager.stats.plant_types()
    print()
    print("Height validation test: ...")
    print(f"Garden scores - Alice: "
          f"{manager.stats.scores(manager.gardens["Alice"])}, Bob: "
          f"{manager.stats.scores(manager.gardens["Bob"])}")
    print(f"Total gardens managed: {manager.total_gardens()}")


def main():
    manager = print_demo()
    print()
    print_report(manager)


if __name__ == "__main__":
    main()
