# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_count_harvest_iterative.py                      :+:    :+:             #
#                                                      +:+                     #
#    By: laveerka <laveerka@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2025/12/18 10:59:25 by laveerka      #+#    #+#                  #
#    Updated: 2025/12/18 11:09:53 by laveerka      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	print("Days until harvest: ")
	days = int(input())
	for i in range(1, days + 1):
		print("Day ", i)
	print("Harvest time!")