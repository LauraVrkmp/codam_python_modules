# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laura <laura@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 17:56:57 by laura           #+#    #+#               #
#  Updated: 2026/01/19 18:01:35 by laura           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# shrink to one function?

def recursive_count(total_days, current_day):
    if (current_day > total_days):
        print("Harvest time!")
    else:
        print(f"Day {current_day}")
        recursive_count(total_days, current_day + 1)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursive_count(days, 1)
