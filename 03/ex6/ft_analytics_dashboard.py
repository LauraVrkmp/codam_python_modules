# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:48 by laveerka        #+#    #+#               #
#  Updated: 2026/09/15 14:28:16 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random


def main():
    print("=== Game Data Alchemist ===\n")
    players = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
               "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")
    capitalized_all = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {capitalized_all}")
    capitalized_only = [player for player in players if player[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}\n")
    dictionary = {item: random.randrange(1000) for item in capitalized_all}
    total = sum(dictionary.values())
    print(f"Score dict: {dictionary}")
    average = total / len(players)
    print(f"Score average is {average:.2f}")
    high_scores = {key: value for key, value in dictionary.items()
                   if value > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
