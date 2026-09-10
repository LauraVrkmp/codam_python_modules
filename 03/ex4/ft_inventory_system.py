# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:41 by laveerka        #+#    #+#               #
#  Updated: 2026/09/10 14:27:26 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def create_inventory(arguments: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for argument in arguments:
        try:
            key, value = argument.split(":")
        except ValueError:
            print(f"Error - invalid parameter: '{argument}'")
            continue
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            inventory[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
    return inventory


def print_inventory(inventory: dict[str, int], stage: str) -> None:
    result = "{"
    keys = list(inventory.keys())
    values = list(inventory.values())
    count = 0
    total = len(inventory)
    while count < total:
        result += f"'{keys[count]}': {values[count]}"
        count += 1
        if count < total:
            result += ", "
    result += "}"
    if stage == "init":
        print(f"Got inventory: {result}")
    elif stage == "update":
        print(f"Updated inventory: {result}")


def print_list(inventory: dict[str, int]) -> None:
    result = "["
    keys = list(inventory.keys())
    count = 0
    total = len(inventory)
    while count < total:
        result += f"'{keys[count]}'"
        count += 1
        if count < total:
            result += ", "
    result += "]"
    print(f"Item list: {result}")


def print_quantities(inventory: dict[str, int]) -> None:
    keys = list(inventory.keys())
    values = list(inventory.values())
    key_min = ""
    key_max = ""
    value_min = 100000000
    value_max = -1
    categories = len(keys)
    totals = sum(values)
    print(f"Total quantity of the {categories} items: {totals}")
    count = 0
    while count < len(keys):
        key = keys[count]
        value = values[count]
        print(f"Item {key} represents {round(value / totals * 100, 1)}%")
        if value == -1 or value > value_max:
            value_max = value
            key_max = key
        if value == -1 or value < value_min:
            value_min = value
            key_min = key
        count += 1
    print(f"Item most abundant: {key_max} with quantity {value_max}")
    print(f"Item least abundant: {key_min} with quantity {value_min}")


def update_inventory(inventory: dict[str, int]) -> dict[str, int]:
    new_key = "magic item"
    new_value = 1
    inventory[new_key] = new_value
    return inventory


def main():
    print("=== Inventory System Analysis ===")
    args = len(sys.argv)
    if args > 1:
        inventory = create_inventory(sys.argv[1:])
        print_inventory(inventory, "init")
        print_list(inventory)
        print_quantities(inventory)
        inventory = update_inventory(inventory)
        print_inventory(inventory, "update")


if __name__ == "__main__":
    main()
