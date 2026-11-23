# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_score_analytics.py                              :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/15 14:29:50 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/15 14:31:13 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import sys


def get_score_analytics() -> None:
    number_args = len(sys.argv)
    list_scores = []
    if (number_args == 1):
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    i = 1
    while i < number_args:
        try:
            score = int(sys.argv[i])
            list_scores.append(score)
        except Exception:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1
    if (len(list_scores) == 0):
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total_players = len(list_scores)
    total_score = sum(list_scores)
    average_score = total_score / total_players
    high_score = max(list_scores)
    low_score = min(list_scores)
    range_score = high_score - low_score
    print("=== Player Score Analytics ===")
    print(f"Scores processed: {list_scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {range_score}")


if __name__ == "__main__":
    get_score_analytics()
