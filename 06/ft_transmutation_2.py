# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_2.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:43:05 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 02:57:37 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy


def main() -> None:
    """Main to call lead_to_gold function through import ... only"""
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print(f"Testing lead to gold: {alchemy.transmutation.lead_to_gold()}")


if __name__ == "__main__":
    main()
