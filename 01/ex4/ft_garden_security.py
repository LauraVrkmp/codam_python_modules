# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:22 by laveerka        #+#    #+#               #
#  Updated: 2026/01/25 10:14:15 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class SecurePlant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        if height > 0:
            self.height = height
        else:
            print("")
        if days > 0:
            self.days = days

    def set_height(self, update):
        if update > self.height:
            self.height = update
            print(f"Height updated: {update}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {update}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, update):
        if update > self.days:
            self.days = update
            print(f"Age updated: {update} days [OK]")
        else:
            print(f"Invalid operation attempted: age {update} days [REJECTED]")
            print("Security: Negative days rejected")

    def get_height(self):
        return self.height

    def get_age(self):
        return self.days


def get_info(plant: SecurePlant):
    print(f"Current plant: {plant.name} ({plant.get_height}cm, {plant.get_age} days)")


if __name__ == "__main__":
    rose = SecurePlant("Rose", 10, 15)
    get_info(rose)
