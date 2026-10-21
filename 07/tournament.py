# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  tournament.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 03:21:35 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 18:09:18 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from itertools import combinations
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
     BattleStrategy,
     NormalStrategy,
     AggressiveStrategy,
     DefensiveStrategy,
     InvalidStrategyError,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    opponent = [(f.create_base(), s) for f, s in opponents]
    try:
        print("\n* Battle *")
        for (c1, s1), (c2, s2) in combinations(opponent, 2):
            print(f"{c1.describe()}\n  vs.\n{c2.describe()}\n  now fight!)")
            for line in s1.act(c1):
                print(line)
            for line in s2.act(c2):
                print(line)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (healing, defensive)])
    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggresive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (healing, defensive)])
    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggresive) ]")
    battle([(aqua, normal), (healing, defensive), (transform, aggressive)])


if __name__ == "__main__":
    main()
