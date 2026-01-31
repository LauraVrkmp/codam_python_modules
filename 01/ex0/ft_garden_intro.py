# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:35:30 by laveerka        #+#    #+#               #
#  Updated: 2026/01/31 12:21:46 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_garden_intro() -> None:
    """Saves name, height and age and displays information"""
    name = "Rose"
    height = 25
    days = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}cm\nAge: {days} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
