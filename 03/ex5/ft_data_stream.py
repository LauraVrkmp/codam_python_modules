# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/03 10:33:44 by laveerka        #+#    #+#               #
#  Updated: 2026/09/11 12:44:17 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random
from typing import Generator

def gen_event() -> Generator[tuple[str, str], None, None]:
	players = ["alice", "bob", "charlie", "dylan"]
	actions = ["climb", "eat", "grab", "move", "release", "run", "sleep", "swim"]
	for _ in range(10):
		player = random.choice(players)
		action = random.choice(actions)
		yield (player, action)


def main():
	print("=== Game Data Stream Processor ===")
	events = gen_event()
	iter = 0
	while True:
		try:
			player, action = next(events)
		except StopIteration:
			break
		print(f"Event {iter}: Player {player} did action {action}")
		iter += 1


if __name__ == "__main__":
	main()