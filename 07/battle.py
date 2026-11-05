# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  battle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 03:21:00 by laveerka        #+#    #+#               #
#  Updated: 2026/11/05 11:32:55 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.creature_factory import CreatureFactory, FlameFactory, AquaFactory


def test_factory(players: list[CreatureFactory]) -> None:
    for player in players:
        creatures = [player.create_base(), player.create_evolved()]
        text = ["Testing factory"]
        for creature in creatures:
            text.append(creature.describe())
            text.append(creature.attack())
        print("\n".join(text))
        print()


def test_battle(players: list[CreatureFactory]) -> None:
    print("Testing battle")
    creatures = [
        player.create_base()
        for player in players
    ]
    print("\n  vs.\n".join(creature.describe() for creature in
                           creatures) + "\n  fight!")
    for creature in creatures:
        print(f"{creature.attack()}")


def main():
    test_factory([FlameFactory(), AquaFactory()])
    test_battle([FlameFactory(), AquaFactory()])


if __name__ == "__main__":
    main()
