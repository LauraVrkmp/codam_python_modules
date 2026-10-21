# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_transmutation_1.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/10/20 23:42:54 by laveerka        #+#    #+#               #
#  Updated: 2026/10/21 03:13:26 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.transmutation as transmutation


def main() -> None:
    """Main to call lead_to_gold function through import ... as ..."""
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {transmutation.lead_to_gold()}")


if __name__ == "__main__":
    main()
