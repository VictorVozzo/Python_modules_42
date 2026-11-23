# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_data_stream.py                                  :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/15 14:32:57 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/15 14:32:59 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = ["bob", "alice", "dylan", "charlie"]
    action = ["run", "eat", "sleep", "grab",
              "move", "climb", "swim", "release"]
    while True:
        event = (random.choice(names), random.choice(action))
        yield event


def consume_event(list_events: list[tuple[str, str]]) -> None:
    for i in range(10):
        index = random.randint(0, len(list_events) - 1)
        print(f"Got event from list: {list_events[index]}")
        list_events.pop(index)
        print(f"Remains in list: {list_events}")


def main() -> None:
    for i in range(1000):
        event = next(gen_event())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    list_events = []
    for i in range(10):
        event = next(gen_event())
        list_events.append(event)
    print(f"Built list of 10 events: {list_events}")
    consume_event(list_events)


if __name__ == "__main__":
    main()
