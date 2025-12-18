# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_plant_age.py                                    :+:    :+:             #
#                                                      +:+                     #
#    By: laveerka <laveerka@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2025/12/18 10:56:06 by laveerka      #+#    #+#                  #
#    Updated: 2025/12/18 10:57:12 by laveerka      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	print("Enter plant age in days: ")
	age = int(input())
	if age > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")