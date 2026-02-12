# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:21 by laveerka        #+#    #+#               #
#  Updated: 2026/02/12 11:11:29 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def main() -> None:
    """Main to analyze player scores based on program arguments"""
    print("=== Player Score Analytics ===")
    args = len(sys.argv)
    if args > 1:
        arg_list: list[int] = []
        for argument in sys.argv[1:]:
            try:
                arg_list.append(int(argument))
            except ValueError:
                print("User provided non-numeric value")
        print(f"Scores processed: {arg_list}")
        print(f"Total players: {len(arg_list)}")
        print(f"Total score: {sum(arg_list)}")
        print(f"Average score: {sum(arg_list) / len(arg_list)}")
        print(f"High score: {max(arg_list)}")
        print(f"Low score: {min(arg_list)}")
        print(f"Score range: {max(arg_list) - min(arg_list)}")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")


if __name__ == "__main__":
    main()
