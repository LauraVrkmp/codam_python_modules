# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/16 20:22:05 by laveerka        #+#    #+#               #
#  Updated: 2026/11/18 13:43:10 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def main():
    artifacts = [{'name': 'Wind Cloak', 'power': 89, 'type': 'armor'},
                 {'name': 'Fire Staff', 'power': 118, 'type': 'focus'},
                 {'name': 'Lightning Rod', 'power': 97, 'type': 'focus'},
                 {'name': 'Storm Crown', 'power': 97, 'type': 'armor'}]
    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    length_sorted = len(sorted_artifacts)
    for i in range(length_sorted - 1):
        if sorted_artifacts[i]['power'] == sorted_artifacts[i+1]['power']:
            print(f"{sorted_artifacts[i]['name']} ({sorted_artifacts[i]['power']} power) is of equal power as {sorted_artifacts[i+1]['name']} ({sorted_artifacts[i+1]['power']} power)")
        else:
            print(f"{sorted_artifacts[i]['name']} ({sorted_artifacts[i]['power']} power) comes before {sorted_artifacts[i+1]['name']} ({sorted_artifacts[i+1]['power']} power)")
    mages = [{'name': 'Storm', 'power': 88, 'element': 'light'},
             {'name': 'Morgan', 'power': 60, 'element': 'wind'},
             {'name': 'Casey', 'power': 59, 'element': 'wind'},
             {'name': 'River', 'power': 80, 'element': 'lightning'},
             {'name': 'Nova', 'power': 78, 'element': 'shadow'}]
    print("\nTesting mage filtering...")
    min_power = 78
    filtered_mages = power_filter(mages, min_power)
    length_filtered = len(filtered_mages)
    print(f"The filtered mages of a minimum power of {min_power} are:")
    for i in range(length_filtered):
        print(f"- {filtered_mages[i]['name']} of power {filtered_mages[i]['power']}, element {filtered_mages[i]['element']}")


if __name__ == "__main__":
    main()
