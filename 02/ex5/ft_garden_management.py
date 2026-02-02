# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 16:34:06 by laveerka        #+#    #+#               #
#  Updated: 2026/02/02 09:54:21 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

class GardenManager:
    def __init__(self):
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant):
        try:
            self.plants.append(plant)
        except ValueError:
            print("Error adding plant: Plant name cannot be empty!")

    def water_plants(self):
        print("Watering plants...")
        print("Opening watering system")
        for plant in self.plants:
            print(f"Watering {plant.name} - success")
        print("Closing watering system (cleanup)")

    def check_health(self):
        print("Checking plant health...")
        for plant in self.plants:
            if plant.water_level < 1:
                print(f"Error: Water level {plant.water_level} is too low (min 1)")
            elif plant.water_level > 10:
                print(f"Error: Water level {plant.water_level} is too high (max 10)")
            if plant.sunlight_hours < 2:
                print(f"Error: Sunlight hours {plant.sunlight_hours} is too low (min 2)")
            elif plant.sunlight_hours > 12:
                print(f"Error: Sunlight hours {plant.sunlight_hours} is too high (max 12)")
            print(f"{plant.name}")


def test_garden_management():


def main():
    print("=== Garden Management System ===")
    test_garden_management()
    print("Garden management system test complete!")


if __name__ == "__main__":
    main()