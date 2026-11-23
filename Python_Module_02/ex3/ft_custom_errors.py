# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_first_exception.py                              :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/08 14:05:22 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/08 14:05:25 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(name_plant: str, wilt_state: str) -> None:
    if wilt_state == "Wilt":
        raise PlantError(f"The {name_plant} plant is wilting!")
    else:
        print("It is not wilt yet")


def check_water(water_level: int) -> None:
    if water_level < 100:
        raise WaterError("Not enough water in the tank!")
    else:
        print("Water level is ok!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        check_plant("tomato", "Wilt")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        check_water(95)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        check_plant("tomato", "Wilt")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(95)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
