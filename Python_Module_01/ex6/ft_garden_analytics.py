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
        if height < 0 and days < 0:
            print("Error, height and age can't be negative")
            return
        elif height < 0:
            print("Error, height can't be negative")
            return
        elif days < 0:
            print("Error, age can't be negative")
            return
        self._name = name.capitalize()
        self._height = height
        self._days = days
        self._age_calls = 0
        self._grow_calls = 0
        self._show_calls = 0

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    def set_height(self, height: float) -> None:
        if height < 0:
            print("Height update rejected")
            return
        self._height = height

    def set_age(self, days: float) -> None:
        if days < 0:
            print("Age update rejected")
            return
        self._days = days

    def age(self, total_days: float) -> None:
        self._days = self._days + total_days
        self._age_calls = self._age_calls + 1

    def grow(self, total_days: float, fert_or_not: str) -> None:
        if fert_or_not == "fertilized":
            self._height = self._height + 1.0 * total_days
        else:
            self._height = round((self._height + 0.8 * total_days), 2)
        self._grow_calls = self._grow_calls + 1

    def get_height(self) -> None:
        print(f"Height updated: {self._height}")

    def get_age(self) -> None:
        print(f"Age updated: {self._days}")

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._days:.0f} days old")
        self._show_calls = self._show_calls + 1

    def show_created(self) -> None:
        print("Plant created: ", end="")
        self.show()

    @staticmethod
    def check_age(check_days: int) -> None:
        if check_days > 365:
            boolean = "True"
        else:
            boolean = "False"
        print(f"Is {check_days} days more than a year? -> {boolean}")


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: float,
            color: str,
    ) -> None:
        super().__init__(name, height, days)
        self._color = color
        self._bloom_status = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._bloom_status:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} has already bloomed")

    def bloom(self) -> None:
        if not self._bloom_status:
            super().show()
            print(f" Color: {self._color}")
            print(f" {self._name} is blooming beautifully!")
            self._bloom_status = True
        else:
            print(f" {self._name} has already bloomed")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: float,
            trunk_diameter: int,
    ) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter
        self._produce_shade_calls = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree Oak now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )
        self._produce_shade_calls = self._produce_shade_calls + 1

    def show_stats(self) -> None:
        show_stats(self)
        print(f" {self._produce_shade_calls} shade")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: float,
            harvest_season: str,
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
        print(f" Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(
            self,
            name: str,
            height: float,
            days: float,
            color: str
    ) -> None:
        super().__init__(name, height, days, color)
        self._seeds_number = 0

    def bloom(self) -> None:
        print(f" Seeds: {self._seeds_number}")
        super().bloom()
        self._seeds_number = self._seeds_number + 42
        print(f" Seeds: {self._seeds_number}")

    def show(self) -> None:
        super().show()


def show_stats(plant: Plant) -> None:
    print(f" [statistics for {plant._name}]")
    print(
        f" Stats: {plant._grow_calls} grow, "
        f"{plant._age_calls} age, "
        f"{plant._show_calls} show")


def main() -> None:
    print("=== Garden statistics ===\n=== Check year-old")
    rose = Flower("rose", 15, 10, "red")
    rose.check_age(30)
    rose.check_age(400)
    print("\n=== Flower")
    rose.show()
    show_stats(rose)
    print(f"[asking the {rose._name} to grow and bloom]")
    rose.grow(8.0, "fertilized")
    rose.bloom()
    show_stats(rose)
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365.0, 5)
    oak.show()
    oak.show_stats()
    print(f" [asking the {oak._name} to produce shade]")
    oak.produce_shade()
    oak.show_stats()
    print("\n=== Seed")
    sunflower = Seed("sunflower", 80.0, 45.0, "yellow")
    sunflower.show()
    print(f"[make {sunflower._name} grow, age and bloom]")
    sunflower.age(20.0)
    sunflower.grow(20.0, "fertilized")
    sunflower.bloom()
    show_stats(sunflower)
    print("\n=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    show_stats(anonymous)


if __name__ == "__main__":
    main()
