# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:35 by laveerka        #+#    #+#               #
#  Updated: 2026/03/23 14:29:13 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


class Player:
    def __init__(self, name: str, skills: set[str]):
        self.name = name
        self.characterictics = set(skills)


def main():
    print("=== Achievement Tracker System ===")
    players = [Player("Alice", {"first kill", "level_10", "treasure_hunter",
                                "speed_demon"}), 
               Player("Bob", {"first_kill", "level_10", "boss_slayer",
                              "collector"}),
               Player("Charlie", {"level_10", "treasure_hunter",
                                  "boss_slayer", "speed_demon",
                                  "perfectionist"})]
    for player in players:
        print(f"Player {player.name} achievements: ")
        for achievement in skills:
            
    

if __name__ == "__Main__":
    main()
