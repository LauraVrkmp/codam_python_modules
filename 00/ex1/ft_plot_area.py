# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_plot_area.py                                    :+:    :+:             #
#                                                      +:+                     #
#    By: laveerka <laveerka@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2025/12/17 15:09:03 by laveerka      #+#    #+#                  #
#    Updated: 2026/01/19 11:41:20 by laveerka      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
	print("Enter length: ")
	length = int(input())
	print("Enter width: ")
	width = int(input())
	area = length * width
	print("Plot area: ", area)