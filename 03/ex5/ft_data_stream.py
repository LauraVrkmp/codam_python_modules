# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:44 by laveerka        #+#    #+#               #
#  Updated: 2026/09/15 11:53:08 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["climb", "eat", "grab", "move", "release", "run", "sleep", "swim"]
    player = random.choice(players)
    action = random.choice(actions)
    yield (player, action)


def main():
    print("=== Game Data Stream Processor ===")
    for iter in range(10):
        event = gen_event()
        player, action = next(event)
        print(f"Event {iter}: Player {player} did action {action}")
        iter += 1
    events = [str, str]
    for iter in range(10):
        event = gen_event()
        events.append(next(event))


if __name__ == "__main__":
    main()
