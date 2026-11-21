# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  functools_artifacts.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/16 20:23:09 by laveerka        #+#    #+#               #
#  Updated: 2026/11/21 00:48:39 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, Callable
from functools import reduce
from functools import partial
from functools import lru_cache
from functools import singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation not in ("add", "multiply", "max", "min"):
        raise ValueError(f"The provided operation '{operation}' is unknown")
    elif spells and len(spells) > 0:
        if operation == "add":
            result = reduce(operator.add, spells)
        elif operation == "multiply":
            result = reduce(operator.mul, spells)
        elif operation == "max":
            result = reduce(lambda x, y: x if operator.gt(x, y) else y,
                            spells)
        else:
            result = reduce(lambda x, y: x if operator.lt(x, y) else y,
                            spells)
    elif not spells or len(spells) == 0:
        return 0
    return result


def enchant(power: int, element: str, target: str) -> str:
    return f"The element {element} hits {target} by {power} HP!"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "earth": partial(base_enchantment, 50, "earth"),
        "water": partial(base_enchantment, 50, "water"),
        "fire": partial(base_enchantment, 50, "fire")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(value: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def spell_int(value: int) -> str:
        return f"The spell did {value} HP damage!"

    @spell.register(str)
    def spell_str(value: str) -> str:
        return f"The spell {value} was cast!"

    @spell.register(list)
    def spell_list(value: list) -> str:
        return "Combo! " + "\n       ".join(spell(item) for item in value)
    return spell


def print_reducer() -> None:
    numbers = [10, 20, 30, 40]
    empty: list = []
    try:
        print(f"Sum: {spell_reducer(numbers, "add")}")
    except ValueError as e:
        print(e)
    try:
        print(f"Product: {spell_reducer(numbers, "multiply")}")
    except ValueError as e:
        print(e)
    try:
        print(f"Max: {spell_reducer(numbers, "max")}")
    except ValueError as e:
        print(e)
    try:
        print(f"Min: {spell_reducer(numbers, "min")}")
    except ValueError as e:
        print(e)
    try:
        print(f"Invalid: {spell_reducer(numbers, "try")}")
    except ValueError as e:
        print(e)
    try:
        print(f"Empty list: {spell_reducer(empty, "add")}")
    except ValueError as e:
        print(e)


def print_enchanter() -> None:
    enchantments = partial_enchanter(enchant)
    print(enchantments["earth"]("the dwarf"))
    print(enchantments["water"]("the wizard"))
    print(enchantments["fire"]("the gnome"))


def print_fibonacci() -> None:
    numbers = [0, 1, 10, 15]
    for number in numbers:
        print(f"Fib({number}): {memoized_fibonacci(number)}")


def print_dispatcher() -> None:
    dispatcher = spell_dispatcher()
    print(dispatcher(25))
    print(dispatcher("charm"))
    print(dispatcher(["wind", 15, "fire", {"key": 2}]))


def main() -> None:
    print("\nTesting spell reducer...\n")
    print_reducer()
    print("\nTesting partial enchanter...\n")
    print_enchanter()
    print("\nTesting memoized fibonacci...\n")
    print_fibonacci()
    print("\nTesting spell dispatcher...\n")
    print_dispatcher()


if __name__ == "__main__":
    main()
