# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:22 by laveerka        #+#    #+#               #
#  Updated: 2026/01/26 11:52:25 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class SecurePlant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.__name = name
        self.__height = height
        self.__days = days

    def set_height(self, new_height: int) -> None:
        if new_height > self.__height and new_height > 0:
            self.__height = new_height
            print(f"Height updated: {new_height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {new_height}cm "
                  f"[REJECTED]")
            print("Security: Negative height or decrease in height "
                  "rejected")

    def set_age(self, new_age: int) -> None:
        if new_age > self.__days and new_age > 0:
            self.__days = new_age
            print(f"Age updated: {new_age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {new_age} days "
                  f"[REJECTED]")
            print("Security: Negative days or decrease in age rejected")

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__days


def do_operations() -> SecurePlant:
    rose = SecurePlant("Rose", 10, 15)
    print(f"Plant created: {rose.get_name()}")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    return rose


def get_info(plant: SecurePlant) -> None:
    print(f"Current plant: {plant.get_name()} ({plant.get_height()}cm, "
          f"{plant.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = do_operations()
    get_info(rose)
