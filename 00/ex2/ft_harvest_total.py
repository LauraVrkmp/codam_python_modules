# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_harvest_total.py                                :+:    :+:             #
#                                                      +:+                     #
#    By: laveerka <laveerka@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2025/12/17 15:12:06 by laveerka      #+#    #+#                  #
#    Updated: 2025/12/17 15:14:43 by laveerka      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	print("Day 1 harvest: ")
	day_1 = int(input())
	print("Day 2 harvest: ")
	day_2 = int(input())
	print("Day 3 harvest: ")
	day_3 = int(input())
	total = day_1 + day_2 + day_3
	print("Total harvest : ", total)