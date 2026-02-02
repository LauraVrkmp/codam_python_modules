# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 16:33:25 by laveerka        #+#    #+#               #
#  Updated: 2026/02/02 07:42:19 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def water_plants(plant_list: list[str | None]):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("invalid plant (None)")
            print(f"Watering {plant}")
    except ValueError as error:
        print(f"Error: Cannot water plant - {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("\nTesting normal watering...")
    normal: list[str | None] = ["tomato", "lettuce", "carrots"]
    print("Watering completed successfully!")
    water_plants(normal)
    print("\nTesting with error...")
    invalid: list[str | None] = ["tomato", None, "carrots"]
    water_plants(invalid)


def main():
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
