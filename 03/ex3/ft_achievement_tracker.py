# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/08 15:38:56 by laveerka        #+#    #+#               #
#  Updated: 2026/09/08 15:45:54 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random


class Player:
    def __init__(self, name: str, achievements: set[str]):
        self.name = name
        self.achievements = achievements


def gen_player_achievements() -> set[str]:
    achievements = ["Boss Slayer", "Collector Supreme", "Crafting Genius",
                    "First Steps", "Master Explorer", "Sharp Mind",
                    "Speed Runner", "Strategist", "Survivor",
                    "Treasure Hunter", "Unstoppable", "Untouchable",
                    "World Savior"
                    ]
    amount = random.randint(1, len(achievements))
    return set(random.sample(achievements, amount))


def distinct_achievements(players: list[Player]) -> set[str]:
    all_achievements: set[str] = set()
    for player in players:
        all_achievements = all_achievements.union(player.achievements)
    return set(all_achievements)


def common_achievements(players: list[Player]) -> set[str]:
    all_achievements = [player.achievements for player in players]
    return all_achievements[0].intersection(*all_achievements[1:0])


def unique_achievements(player: Player, players: list[Player]) -> set[str]:
    others = [p.achievements for p in players if p is not player]
    if not others:
        return player.achievements
    others_union = others[0].union(*others[1:])
    return player.achievements - others_union


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    players = [
        Player(name, gen_player_achievements())
        for name in names
    ]
    for player in players:
        print(f"Player {player.name}: {player.achievements}")
    print(f"\nAll distinct achievements: {distinct_achievements(players)}")
    print()
    print(f"Common achievements: {common_achievements(players)}")
    print()
    for player in players:
        print(f"Only {player.name} has: "
              f"{unique_achievements(player, players)}")
    print()
    for player in players:
        print(f"{player.name} is missing: "
              f"{distinct_achievements(players) - player.achievements}")


if __name__ == "__main__":
    main()
