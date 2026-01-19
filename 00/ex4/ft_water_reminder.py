# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laura <laura@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 17:56:36 by laura           #+#    #+#               #
#  Updated: 2026/01/19 17:59:49 by laura           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_water_reminder():
    print("Days since last watering: ")
    days = int(input())
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
