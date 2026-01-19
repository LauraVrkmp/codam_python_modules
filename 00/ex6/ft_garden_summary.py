# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_garden_summary.py                               :+:    :+:             #
#                                                      +:+                     #
#    By: laveerka <laveerka@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2026/01/19 11:44:47 by laveerka      #+#    #+#                  #
#    Updated: 2026/01/19 11:47:02 by laveerka      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
	print("Enter garden name: ")
	name = input()
	print("Enter numer of plants: ")
	number = input()
	print("Garden: " + name)
	print("Plants: " + number)
	print("Status: Growing well!")