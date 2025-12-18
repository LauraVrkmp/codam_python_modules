# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_water_reminder.py                               :+:    :+:             #
#                                                      +:+                     #
#    By: laveerka <laveerka@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2025/12/18 10:57:47 by laveerka      #+#    #+#                  #
#    Updated: 2025/12/18 10:58:47 by laveerka      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	print("Days since last watering: ")
	days = int(input())
	if days > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")