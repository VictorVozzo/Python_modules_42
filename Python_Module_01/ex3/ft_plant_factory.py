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
            self.height = self.height + 1 * total_days
        else:
            self.height = round((self.height + 0.8 * total_days), 2)

    def show_created(self) -> None:
        print("Created: ", end="")
        self.show()


def main() -> None:
    rose = Plant("rose", 25.0, 30.0)
    oak = Plant("oak", 200.0, 365.0)
    cactus = Plant("cactus", 5.0, 90.0)
    sunflower = Plant("sunflower", 80.0, 45.0)
    fern = Plant("fern", 15.0, 120.0)
    print("=== Plant Factory Output ===")
    rose.show_created()
    oak.show_created()
    cactus.show_created()
    sunflower.show_created()
    fern.show_created()


if __name__ == "__main__":
    main()
