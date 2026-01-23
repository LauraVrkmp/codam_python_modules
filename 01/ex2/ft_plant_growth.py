# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:35:56 by laveerka        #+#    #+#               #
#  Updated: 2026/01/23 09:27:40 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1


def get_info():
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(f"{plant.name}: {plant.height}cm, {plant.days} days old")
    for _ in range(7):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    print(f"{plant.name}: {plant.height}cm, {plant.days} days old")


if __name__ == "__main__":
    get_info()
