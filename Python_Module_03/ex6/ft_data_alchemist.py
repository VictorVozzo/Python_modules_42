# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_data_alchemist.py                               :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/15 14:33:15 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/15 14:33:17 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import random


def data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")

    initial_list = ['Alice', 'bob', 'Charlie', 'dylan',
                    'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {initial_list}")

    list_all_capitalize = []
    list_only_capitalize = []

    list_all_capitalize = [x.capitalize() for x in initial_list]
    print(f"New list with all names capitalized: {list_all_capitalize}")

    list_only_capitalize = [x for x in initial_list if x == x.capitalize()]
    print(f"New list of capitalized names only: {list_only_capitalize}")

    score_dict = {i: random.randint(1, 1200) for i in list_all_capitalize}
    print(f"\nScore dict: {score_dict}")

    score_average = sum(score_dict.values())/len(score_dict)
    print(f"Score average: {score_average:.2f}")

    high_score_dict = {i: random.randint(int(score_average), 1200)
                       for i in list_all_capitalize}
    print(f"High scores: {high_score_dict}")


if __name__ == "__main__":
    data_alchemist()
