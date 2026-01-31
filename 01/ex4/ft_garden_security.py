# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:36:22 by laveerka        #+#    #+#               #
#  Updated: 2026/01/31 13:33:00 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class SecurePlant:
    def __init__(self, name: str, height: int, days: int) -> None:
        """Initializes SecurePlant object, ensuring positive height and age"""
        if height > 0 and days > 0:
            self.__name = name
            self.__height = height
            self.__days = days
            print("Plant created successfully [OK]")
        else:
            self.__name = name
            self.__height = 0
            self.__days = 0
            print("Invalid Plant data. Switching to safe defaults")

    def set_height(self, new_height: int) -> None:
        """Sets height attribute of SecurePlant, ensuring proper values"""
        if new_height > self.__height and new_height > 0:
            self.__height = new_height
            print(f"Height updated: {new_height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {new_height}cm "
                  f"[REJECTED]")
            print("Security: Negative height or decrease in height "
                  "rejected")

    def set_age(self, new_days: int) -> None:
        """Sets age attribute of SecurePlant, ensuring proper values"""
        if new_days > self.__days and new_days > 0:
            self.__days = new_days
            print(f"Age updated: {new_days} days [OK]")
        else:
            print(f"Invalid operation attempted: age {new_days} days "
                  f"[REJECTED]")
            print("Security: Negative days or decrease in age rejected")

    def get_name(self) -> str:
        """Returns the SecurePlant's name"""
        return self.__name

    def get_height(self) -> int:
        """Returns the SecurePlant's height"""
        return self.__height

    def get_age(self) -> int:
        """Returns the SecurePlant's age"""
        return self.__days


def main() -> None:
    """Main function of the Garden Security System"""
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 10, 15)
    print(f"Plant created: {rose.get_name()}")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    print(f"Current plant: {rose.get_name()} ({rose.get_height()}cm, "
          f"{rose.get_age()} days)")


if __name__ == "__main__":
    main()
