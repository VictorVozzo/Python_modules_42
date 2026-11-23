# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_garden_intro.py                                 :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/08 09:38:00 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/08 09:38:02 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

def print_garden(name: str, height: str, age: int) -> None:
    print("=== Welcome to My Garden ===")
    name = name.capitalize()
    print(f"Plant: {name}")
    print(f"Height: {height}")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


def main() -> None:
    print_garden("rose", "25cm", 30)


if __name__ == "__main__":
    main()
