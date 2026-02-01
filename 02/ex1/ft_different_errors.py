# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 16:32:29 by laveerka        #+#    #+#               #
#  Updated: 2026/02/01 09:26:32 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations(choice: int) -> None:
    """Tries operations based on argument choice, including except clauses"""
    if choice == 1:
        try:
            int("abc")
        except ValueError:
            print("Caught ValueError: invalid literal for int()\n")
    elif choice == 2:
        try:
            x = 5 / 0
            print(x)
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")
    elif choice == 3:
        file = "missing_file.txt"
        try:
            fd = open(file)
            fd.close()
        except FileNotFoundError:
            print(f"Caught FileNotFoundError: No such file '{file}'\n")
    elif choice == 4:
        key = "Flower"
        try:
            data = {"Plant": "Sunflower"}
            print(data[key])
        except KeyError:
            print(f"Caught KeyError: '{key}'\n")
    else:
        try:
            value = int("abc")
            print(value)
        except (ValueError, ZeroDivisionError, FileExistsError, KeyError):
            print("Caught an error, but program continues!\n")


def test_error_types():
    """Singular or multiple error testing"""
    print("Testing ValueError...")
    garden_operations(1)
    print("Testing ZeroDivisionError...")
    garden_operations(2)
    print("Testing FileNotFoundError...")
    garden_operations(3)
    print("Testing KeyError...")
    garden_operations(4)
    print("Testing multiple errors together...")
    garden_operations(5)


def main():
    """Main to runt he error types demo"""
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
