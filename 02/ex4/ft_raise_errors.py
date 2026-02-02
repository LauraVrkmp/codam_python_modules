# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_errors.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 16:33:49 by laveerka        #+#    #+#               #
#  Updated: 2026/02/02 08:29:18 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_plant_health(plant_name: str | None, water_level: int,
                       sunlight_hours: int) -> None:
    """ValueError raiser for arguments name, water level and sunlight hours"""
    if plant_name is None or plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """Plant health checker with various input values"""
    print("\nTesting good values...")
    try:
        check_plant_health("tomato", 3, 6)
    except ValueError as error:
        print(f"Error: {error}")
    print("\nTesting empty plant name...")
    try:
        check_plant_health(None, 7, 4)
    except ValueError as error:
        print(f"Error: {error}")
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as error:
        print(f"Error: {error}")
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 9, 0)
    except ValueError as error:
        print(f"Error: {error}")


def main() -> None:
    """Main to run plant health checker"""
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    main()
