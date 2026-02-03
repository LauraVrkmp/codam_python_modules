# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 16:34:06 by laveerka        #+#    #+#               #
#  Updated: 2026/02/03 09:20:46 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    """Custum error class based on Exception"""
    pass


class PlantError(GardenError):
    """Custom error class based on GardenError"""
    pass


class WaterError(GardenError):
    """Custom error class based on GardenError"""
    pass


class Plant:
    def __init__(self, name: str | None, water_level: int,
                 sunlight_hours: int) -> None:
        """
        Initizalize Plant class with name, water level and
        sunlight hours attributes
        """
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self, tank_water: int) -> None:
        """Initialize GardenManager with Plant list and tank water level"""
        self.plants: list[Plant] = []
        self.tank_water = tank_water

    def add_plant(self, plant: Plant) -> None:
        """Try except clause to add a Plant to list"""
        try:
            check_name_value(plant)
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as error:
            print(f"Error adding plant: {error}")

    def water_plants(self) -> None:
        """Try except finally clause to water Plants"""
        try:
            for plant in self.plants:
                if self.tank_water <= 0:
                    raise PlantError("Not enough water in tank")
                plant.water_level += 1
                self.tank_water -= 1
                print(f"Watering {plant.name} - success")
        except PlantError as error:
            print(f"Caught GardenError: {error}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        """Try except clause to test Plant health attributes"""
        print("\nChecking plant health...")
        for plant in self.plants:
            try:
                check_attribute_values(plant)
                print(f"{plant.name}: healthy (water: {plant.water_level}, "
                      f"sun: {plant.sunlight_hours})")
            except PlantError as error:
                print(f"Error checking {plant.name}: {error}")


def check_name_value(plant: Plant) -> None:
    """Raises PlantError is Plant name is invalid"""
    if plant.name is None or plant.name == "":
        raise PlantError("Plant name cannot be empty!")


def check_attribute_values(plant: Plant) -> None:
    """Raised PalntError if water level or sunlight hours is unsuitable"""
    if plant.water_level < 1:
        raise PlantError(f"Water level {plant.water_level} is too ow (min 1)")
    elif plant.water_level > 10:
        raise PlantError(f"Water level {plant.water_level} "
                         f"is too high (max 10)")
    elif plant.sunlight_hours < 2:
        raise PlantError(f"Sunlight hours {plant.sunlight_hours} "
                         f"is too low (min 2)")
    elif plant.sunlight_hours > 12:
        raise PlantError(f"Sunlight hours {plant.sunlight_hours} "
                         f"is too high (max 12)")


def test_garden_management() -> None:
    """Garden management function to test error handling of GardenManager"""
    garden = GardenManager(4)
    print("\nAdding plants to garden...")
    plants = [Plant("tomato", 5, 8), Plant("lettuce", 15, 6),
              Plant(None, 7, 9)]
    for plant in plants:
        garden.add_plant(plant)
    print("\nWatering plants...")
    print("Opening watering system")
    garden.water_plants()
    garden.check_health()
    print("\nTesting error recovery...")
    try:
        garden.tank_water = 0
        garden.water_plants()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    print("System recovered and continuing...")


def main() -> None:
    """Main to test Garden Management including error handling"""
    print("=== Garden Management System ===")
    test_garden_management()
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
