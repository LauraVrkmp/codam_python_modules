# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laura <laura@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 17:56:26 by laura           #+#    #+#               #
#  Updated: 2026/01/19 17:59:29 by laura           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plant_age():
    print("Enter plant age in days: ")
    age = int(input())
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
