# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:16 by laveerka        #+#    #+#               #
#  Updated: 2026/02/12 11:11:34 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def main() -> None:
    """Main to display arguments to program execution"""
    print("=== Command Quest ===")
    arg_count = len(sys.argv)
    if arg_count == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if arg_count > 1:
        print(f"Arguments received: {arg_count - 1}")
        iter = 1
        for argument in sys.argv[1:]:
            print(f"Argument {iter}: {argument}")
            iter += 1
    print(f"Total arguments: {arg_count}")


if __name__ == "__main__":
    main()
