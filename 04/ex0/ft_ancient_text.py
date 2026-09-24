# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/16 17:40:59 by laveerka        #+#    #+#               #
#  Updated: 2026/09/24 12:04:23 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def read_file(file_name: str) -> None:
    """Reading and printing from file"""
    try:
        f = open(file_name, "r")
        print("---\n")
        content = f.read()
        print(content)
        print("\n---")
        f.close()
        print(f"File '{file_name}', closed.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_name}': {e}")


def main() -> None:
    """Main to read file from command line"""
    args = sys.argv
    if len(args) == 2:
        print("==== Cyber Archives Recovery ===")
        file_name = args[1]
        print(f"Accessing file '{file_name}'")
        read_file(file_name)
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
