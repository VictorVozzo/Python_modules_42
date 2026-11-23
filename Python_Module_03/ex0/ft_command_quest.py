# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_command_quest.py                                :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/09 10:04:03 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/09 10:04:04 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import sys


def print_args() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
    i = 1
    while (i < len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print_args()
