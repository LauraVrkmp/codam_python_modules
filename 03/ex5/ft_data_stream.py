# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:44 by laveerka        #+#    #+#               #
#  Updated: 2026/09/16 13:30:42 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["climb", "eat", "grab", "move", "release", "run", "sleep",
               "swim"]
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(events: list[tuple[str, str]]) -> Generator[tuple[str, str],
                                                              None, None]:
    while events:
        index = random.randrange(len(events))
        item = events[index]
        del events[index]
        yield item


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event = gen_event()
    for iter in range(1000):
        player, action = next(event)
        print(f"Event {iter}: Player {player} did action {action}")
    events: list[tuple[str, str]] = []
    event = gen_event()
    for _ in range(10):
        events.append(next(event))
    print(f"Built list of 10 events: {events}")
    for ev in consume_event(events):
        print(f"Got event from list: {ev}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
