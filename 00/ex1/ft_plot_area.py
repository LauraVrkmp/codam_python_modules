# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plot_area.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laura <laura@student.42.fr>               +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 17:56:05 by laura           #+#    #+#               #
#  Updated: 2026/01/19 17:58:49 by laura           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plot_area():
    print("Enter length: ")
    length = int(input())
    print("Enter width: ")
    width = int(input())
    area = length * width
    print("Plot area: ", area)
