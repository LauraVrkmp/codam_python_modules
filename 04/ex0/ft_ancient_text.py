# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/16 17:40:59 by laveerka        #+#    #+#               #
#  Updated: 2026/09/17 14:53:03 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def main():
    args = sys.argv
    if len(args) == 2:
        print("==== Cyber Archives Recovery ===")
        file_name = args[1]
        print(f"Accessing file '{file_name}'")
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
            
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
