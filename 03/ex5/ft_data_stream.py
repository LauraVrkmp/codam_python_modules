# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:44 by laveerka        #+#    #+#               #
#  Updated: 2026/09/15 13:45:28 by laveerka        ###   ########.fr        #
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


def main():
    print("=== Game Data Stream Processor ===")
    event = gen_event()
    for iter in range(1000):
        try:
            player, action = next(event)
        except StopIteration:
            break
        print(f"Event {iter}: Player {player} did action {action}")
    events: list[tuple[str, str]] = []
    event = gen_event()
    for _ in range(10):
        try:
            events.append(next(event))
        except StopIteration:
            break
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
