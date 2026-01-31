# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:50 by laveerka        #+#    #+#               #
#  Updated: 2026/01/31 16:30:01 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    total_plants = 0

    def __init__(self, name: str, height: int) -> None:
        """Safely initialize Plant object and keep track of total"""
        self.name = name
        self.growth_rate = 1
        Plant.total_plants += 1
        if height > 0:
            self.height = height
        else:
            self.height = 1

    def grow(self) -> None:
        """Print growing of Plant and increase height"""
        print(f"{self.name} grew {self.growth_rate}cm")
        self.height += self.growth_rate

    def describe(self) -> None:
        """Describe Plant object"""
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    total_flowering = 0

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize FloweringPlant object, specify color and total"""
        super().__init__(name, height)
        self.color = color
        FloweringPlant.total_flowering += 1

    def describe(self) -> None:
        """Describe FloweringPlant object"""
        print(f"- {self.name}: {self.height}cm, {self.color} "
              f"flower (blooming)")


class PrizeFlower(FloweringPlant):
    total_prize = 0

    def __init__(self, name: str, height: int, color: str, points: int) -> None:
        """Initialize PrizeFlower object, specify prize points and total"""
        super().__init__(name, height, color)
        self.points = points
        PrizeFlower.total_prize += 1

    def describe(self) -> None:
        """Describe PrizeFlower object"""
        print(f"- {self.name}: {self.height}cm, {self.color} flower (blooming)"
              f", Prize points: {self.points}")


class Garden:
    def __init__(self, owner: str) -> None:
        """Initialize Garden object: owner and list of Plants"""
        self.owner = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Function to append Plant to plants list"""
        print(f"Added {plant.name} to {self.owner}'s garden")
        self.plants.append(plant)

    def grow_all(self) -> None:
        """Function to grow all plants in garden"""
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()


class GardenStats:
    def __init__(self, manager: "GardenManager") -> None:
        """Initialize GardenStats object, argument of GardenManager"""
        self.manager = manager

    def total_plants_growth(self) -> None:
        """Function to keep track of total plants and accumulative growth"""
        total_growth = 0
        for garden in self.manager.gardens.values():
            for plant in garden.plants:
                total_growth += plant.growth_rate
        print(f"Plants added: {Plant.total_plants}, "
              f"Total growth: {total_growth}")

    def plant_types(self) -> None:
        """Print all plant types in GardenManager"""
        regular = Plant.total_plants - FloweringPlant.total_flowering
        flowering = FloweringPlant.total_flowering - PrizeFlower.total_prize
        prize = PrizeFlower.total_prize
        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers")

    @staticmethod
    def scores(garden: Garden) -> int:
        """Utility function to keep track of garden scores based on height"""
        total = 0
        for plant in garden.plants:
            total += plant.height
        return total


class GardenManager:
    def __init__(self) -> None:
        """Initialize garden dictionary and helper GardenStats"""
        self.gardens: dict[str, Garden] = {}
        self.stats = GardenStats(self)

    def add_garden(self, garden: Garden) -> None:
        """Add garden to gardens dictionary"""
        self.gardens[garden.owner] = garden

    def total_gardens(self) -> int:
        """Calculate total amount of gardens added"""
        total = 0
        for _ in self.gardens:
            total += 1
        return total
    
    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """Class method to build full manager"""
        manager = cls()
        alice = Garden("Alice")
        bob = Garden("Bob")
        manager.add_garden(alice)
        manager.add_garden(bob)
        return manager


def print_demo() -> GardenManager:
    """Create garden network, add plants, grow them and print information"""
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network()
    manager.gardens["Alice"].add_plant(Plant("Oak Tree", 100))
    manager.gardens["Alice"].add_plant(FloweringPlant("Rose", 25, "red"))
    manager.gardens["Alice"].add_plant(PrizeFlower("Sunflower", 50,
                                                   "yellow", 10))
    manager.gardens["Alice"].grow_all()
    print()
    return manager


def print_report(manager: GardenManager):
    """Report on plants, totals and growth, types, height validation and scores"""
    print(f"=== {manager.gardens['Alice'].owner}'s Garden Report ===")
    print("Plants in garden:")
    for plant in manager.gardens["Alice"].plants:
        plant.describe()
    print()
    manager.stats.total_plants_growth()
    manager.stats.plant_types()
    print()
    test_plant = PrizeFlower("Tulip", -25, "purple", 15)
    print(f"Height validation test: {test_plant.height > 0}")
    print(f"Garden scores - Alice: "
          f"{manager.stats.scores(manager.gardens['Alice'])}, Bob: "
          f"{manager.stats.scores(manager.gardens['Bob'])}")
    print(f"Total gardens managed: {manager.total_gardens()}")


def main():
    manager = print_demo()
    print_report(manager)


if __name__ == "__main__":
    main()
