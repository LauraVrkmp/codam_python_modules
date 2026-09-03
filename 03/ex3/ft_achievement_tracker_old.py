# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:35 by laveerka        #+#    #+#               #
#  Updated: 2026/03/30 14:56:43 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


class Player:
    def __init__(self, name: str, skills: set[str]):
        self.name = name
        self.characterictics = set(skills)


def main():
    print("=== Achievement Tracker System ===\n")
    players = [Player("alice", {"first kill", "level_10", "treasure_hunter",
                                "speed_demon"}), 
               Player("bob", {"first_kill", "level_10", "boss_slayer",
                              "collector"}),
               Player("charlie", {"level_10", "treasure_hunter",
                                  "boss_slayer", "speed_demon",
                                  "perfectionist"})]
    for player in players:
        print(f"Player {player.name} achievements: {{", end="")
        for characteristic in player.characterictics:
            print(f"'{characteristic}'", end=" ")
        print("}")
    print("\n=== Achievement Analytics ===")


if __name__ == "__main__":
    main()
