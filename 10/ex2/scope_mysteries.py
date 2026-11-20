# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  scope_mysteries.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/16 20:22:48 by laveerka        #+#    #+#               #
#  Updated: 2026/11/20 13:16:44 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counting() -> int:
        nonlocal count
        count += 1
        return count
    return counting


def spell_accumulator(initial_power: int) -> Callable:
    accumulated_power = initial_power

    def accumulate(amount) -> int:
        nonlocal accumulated_power
        accumulated_power += amount
        return accumulated_power
    return accumulate  


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name):
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    pass


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    counter_a = mage_counter()
    print(f"counter_a call 2: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting spell accumulator...")
    initial_power = 100
    accumulating = spell_accumulator(initial_power)
    print(f"Base {initial_power}, add 20: {accumulating(20)}")
    print(f"Base {initial_power}, add 30: {accumulating(30)}")
    print("\nTesting enchantment factory...")
    type_1 = enchantment_factory("Flaming")
    type_2 = enchantment_factory("Frozen")
    print(f"{type_1} {type_1('Sword')}")
    print(f"{type_2} {type_2('Shield')}")


if __name__ == "__main__":
    main()
