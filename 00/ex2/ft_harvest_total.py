# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laura <laura@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 17:56:16 by laura           #+#    #+#               #
#  Updated: 2026/01/19 17:59:03 by laura           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_harvest_total():
    day_1 = int(input("Day 1 harvest: "))
    day_2 = int(input("Day 2 harvest: "))
    day_3 = int(input("Day 3 harvest: "))
    total = day_1 + day_2 + day_3
    print(f"Total harvest: {total}")
