# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 16:32:10 by laveerka        #+#    #+#               #
#  Updated: 2026/02/01 08:04:47 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_temperature(temp_str: str) -> int:
    """Checks string for int value and returns int if within bounds"""
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return -1
    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        return -1
    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        return -1
    else:
        print(f"Temperature {temp}°C is perfect for plants!\n")
        return temp


def test_temperature_input() -> None:
    """Calls temperature check with strings as input"""
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")


def main() -> None:
    """Main to run temperature checker"""
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
