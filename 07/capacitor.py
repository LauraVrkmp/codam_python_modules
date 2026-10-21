# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  capacitor.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/21 03:21:21 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 11:47:48 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex1.heal_transform_creature_factory import HealingCreatureFactory
from ex1.heal_transform_creature_factory import TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    for label, creature in (
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ):
        print(f"  {label}:")
        print(creature.describe())
        print(f"{creature.attack()}!")
        if isinstance(creature, HealCapability):
            print(creature.heal())


def transform() -> None:
    print("\nTesting Creature with transform capability")
    factory = TransformCreatureFactory()
    for label, creature in (
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ):
        print(f"  {label}:")
        print(creature.describe())
        print(f"{creature.attack()}.")
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


def main() -> None:
    healing()
    transform()


if __name__ == "__main__":
    main()
