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
        self._name = name.capitalize()
        if (height < 0 and days < 0):
            print(f"{self._name}: Error, height and age can't be negative")
            return
        elif (height < 0):
            self._days = days
            print(f"{self._name}: Error, height can't be negative")
            return
        elif (days < 0):
            self._height = height
            print(f"{self._name}: Error, age can't be negative")
            return
        self._height = height
        self._days = days

    def set_height(self, height: float) -> None:
        if (height < 0):
            print("Height update rejected")
            return
        self._height = height

    def set_age(self, days: float) -> None:
        if (days < 0):
            print("Age update rejected")
            return
        self._days = days

    def age(self, total_days: float) -> None:
        self._days = self._days + total_days

    def grow(self, total_days: float, fert_or_not: str) -> None:
        if (fert_or_not == "fertilized"):
            self._height = self._height + 1 * total_days
        else:
            self._height = round((self._height + 0.8 * total_days), 2)

    def get_height(self) -> None:
        print(f"Height updated: {self._height:.0f} cm")

    def get_age(self) -> None:
        print(f"Age updated: {self._days:.0f} days")

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._days:.0f} days old")

    def show_created(self) -> None:
        print("Plant created: ", end="")
        self.show()


def main() -> None:
    rose = Plant("Rose", 15.0, 10.0)
    print("=== Garden Security System ===")
    rose.show_created()
    print()
    rose.set_height(25.0)
    rose.get_height()
    rose.set_age(30.0)
    rose.get_age()
    print()
    rose.set_height(-25)
    rose.set_age(-30)
    print("\nCurrent state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
