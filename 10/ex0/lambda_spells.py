# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/16 20:22:05 by laveerka        #+#    #+#               #
#  Updated: 2026/11/18 15:59:43 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = [mage['power'] for mage in mages]
    return {
        "max_power": max(powers, key=lambda x: x),
        "min_power": min(powers, key=lambda x: x),
        "avg_power": round(sum(powers) / len(powers), 2)
    }


def sorter_func(artifacts: list[dict]) -> None:
    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    length_sorted = len(sorted_artifacts)
    for i in range(length_sorted - 1):
        if sorted_artifacts[i]['power'] == sorted_artifacts[i+1]['power']:
            print(f"- {sorted_artifacts[i]['name']} "
                  f"({sorted_artifacts[i]['power']} power) is of "
                  f"equal power as {sorted_artifacts[i+1]['name']} "
                  f"({sorted_artifacts[i+1]['power']} power)")
        else:
            print(f"- {sorted_artifacts[i]['name']} "
                  f"({sorted_artifacts[i]['power']} power) comes before "
                  f"{sorted_artifacts[i+1]['name']} "
                  f"({sorted_artifacts[i+1]['power']} power)")


def filter_func(mages: list[dict]) -> None:
    print("\nTesting mage filtering...")
    min_power = 78
    filtered_mages = power_filter(mages, min_power)
    length_filtered = len(filtered_mages)
    print(f"The filtered mages with a minimum power of {min_power} are:")
    for i in range(length_filtered):
        print(f"- {filtered_mages[i]['name']} of power "
              f"{filtered_mages[i]['power']}, element "
              f"{filtered_mages[i]['element']}")


def transformer_func(spells: list[str]) -> None:
    print("\nTesting spell transformation...")
    transformed_spells = spell_transformer(spells)
    length_transformed = len(transformed_spells)
    print("The transformed spells are:")
    for i in range(length_transformed):
        print(f"{transformed_spells[i]} ", end="")


def stats_func(mages: list[dict]) -> None:
    print("\n\nMage statistics...")
    statistics = mage_stats(mages)
    print(f"Maximum power level: {statistics['max_power']}")
    print(f"Minimum power level: {statistics['min_power']}")
    print(f"Average power level: {statistics['avg_power']}")


def main():
    artifacts = [{'name': 'Water Chalice', 'power': 92, 'type': 'relic'},
                 {'name': 'Wind Cloak', 'power': 97, 'type': 'armor'},
                 {'name': 'Light Prism', 'power': 92, 'type': 'relic'},
                 {'name': 'Ice Wand', 'power': 100, 'type': 'weapon'}]
    mages = [{'name': 'Phoenix', 'power': 60, 'element': 'shadow'},
             {'name': 'Luna', 'power': 73, 'element': 'wind'},
             {'name': 'Sage', 'power': 60, 'element': 'earth'},
             {'name': 'Luna', 'power': 92, 'element': 'light'},
             {'name': 'Jordan', 'power': 82, 'element': 'wind'}]
    spells = ['tornado', 'blizzard', 'shield', 'tsunami']
    sorter_func(artifacts)
    filter_func(mages)
    transformer_func(spells)
    stats_func(mages)


if __name__ == "__main__":
    main()
