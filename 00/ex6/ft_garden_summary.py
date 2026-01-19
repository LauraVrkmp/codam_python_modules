# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_summary.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laura <laura@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 17:57:08 by laura           #+#    #+#               #
#  Updated: 2026/01/19 18:01:02 by laura           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_garden_summary():
    print("Enter garden name: ")
    name = input()
    print("Enter numer of plants: ")
    number = input()
    print("Garden: " + name)
    print("Plants: " + number)
    print("Status: Growing well!")
