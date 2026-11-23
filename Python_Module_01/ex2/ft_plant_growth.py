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

class Plant:
    def __init__(self, name: str, height: float, days: float) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days:.0f} days old")

    def age(self, total_days: float) -> None:
        self.days = self.days + total_days

    def grow(self, total_days: float, fert_or_not: str) -> None:
        if (fert_or_not == "fertilized"):
            self.height = self.height + 1.0 * total_days
        else:
            self.height = round((self.height + 0.8 * total_days), 1)


def main() -> None:
    rose = Plant("rose", 25.0, 30.0)
    print("=== Garden Plant Growth ===")
    rose_height_before = rose.height
    rose.show()
    for i in range(1, 8, 1):
        rose.age(1.0)
        rose.grow(1.0, "not fertilized")
        print(f"=== Day {i} ===")
        rose.show()
        if (i == 7):
            rose_height_after = rose.height
            rose_growth = rose_height_after - rose_height_before
            print(f"Growth this week: {rose_growth:.1f}cm")


if __name__ == "__main__":
    main()
