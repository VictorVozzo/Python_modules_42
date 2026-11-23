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
        if (height < 0 and days < 0):
            print("Error, height and age can't be negative")
            return
        elif (height < 0):
            print("Error, height can't be negative")
            return
        elif (days < 0):
            print("Error, age can't be negative")
            return
        self._name = name.capitalize()
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
            self._height = self._height + 2.1 * total_days
        else:
            self._height = round((self._height + 0.8 * total_days), 2)

    def get_height(self) -> None:
        print(f"Height updated: {self._height}")

    def get_age(self) -> None:
        print(f"Age updated: {self._days}")

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._days:.0f} days old")

    def show_created(self) -> None:
        print("Plant created: ", end="")
        self.show()


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: float,
            color: str
    ) -> None:
        super().__init__(name, height, days)
        self._color = color

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")

    def bloom(self) -> None:
        print(
            f" {self._name} has not bloomed yet"
            f"\n[asking the {self._name} to bloom]")
        self.show()
        print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: float,
            trunk_diameter: int
    ) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(
            f"Tree Oak now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: float,
            harvest_season: str
    ) -> None:
        super().__init__(name, height, days)
        self._nutritional_value = 0.0
        self._harvest_season = harvest_season

    def age(self, total_days: float) -> None:
        super().age(total_days)
        self._nutritional_value = self._nutritional_value + total_days * 0.5

    def grow(self, total_days: float, fert_or_not: str) -> None:
        super().grow(total_days, fert_or_not)
        self._nutritional_value = self._nutritional_value + total_days * 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value:.0f}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("rose", 15.0, 10.0, "red")
    rose.show()
    rose.bloom()
    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365.0, 5)
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10.0, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.age(20.0)
    tomato.grow(20.0, "fertilized")
    tomato.show()


if __name__ == "__main__":
    main()
