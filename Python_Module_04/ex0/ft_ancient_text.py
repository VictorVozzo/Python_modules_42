# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_ancient_text.py                                 :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/16 09:22:31 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/16 09:22:32 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import sys


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    number_args = len(sys.argv)
    if (number_args == 1):
        print("Usage: ft_ancient_text.py <file>\n")
        return
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    f = None
    try:
        f = open(file_name)
        print("---\n")
        print(f.read())
        print("---")
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}\n")
    if f is not None:
        f.close()
        print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
