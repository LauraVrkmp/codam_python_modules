# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_seed_inventory.py                               :+:    :+:             #
#                                                      +:+                     #
#    By: laveerka <laveerka@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2026/01/19 11:48:44 by laveerka      #+#    #+#                  #
#    Updated: 2026/01/19 12:06:13 by laveerka      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
	seed_type = seed_type.capitalize()
	if (unit == "packets"):
		print(seed_type + " seeds: " + quantity + " " + unit + " available")
	elif (unit == "grams"):
		print(seed_type + " seeds: " + quantity + " " + unit + " total")
	elif (unit == "area"):
		print(seed_type + " seeds: " + quantity + " covers " + unit + " square meters")
	else:
		print("Unknown unit type")