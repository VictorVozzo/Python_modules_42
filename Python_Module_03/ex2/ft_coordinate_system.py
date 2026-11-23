# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_coordinate_system.py                            :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/15 14:31:58 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/15 14:32:01 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        tuple_coordinates: tuple[float, ...] = ()
        list_coordinates = []
        text_input = "Enter new coordinates as floats in format 'x,y,z': "
        list_coordinates = input(text_input).split(",")
        count = 0
        for i in list_coordinates:
            count += 1
        if (count != 3):
            print("Invalid syntax")
            continue
        try:
            for coordinates in list_coordinates:
                float_coordinates = float(coordinates)
                tuple_coordinates = tuple_coordinates + (float_coordinates, )
            return tuple_coordinates
        except Exception as e:
            print(f"Error on parameter '{coordinates}': {e}")


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    t_coord_1 = get_player_pos()
    print(f"Got a first tuple: {t_coord_1}")
    print(f"It includes: X={t_coord_1[0]}, Y={t_coord_1[1]}, Z={t_coord_1[2]}")
    dist = math.sqrt(t_coord_1[0]**2 + t_coord_1[1]**2 + t_coord_1[2]**2)
    print(f"Distance to center: {dist:.4f}")

    print("\nGet a second set of coordinates")
    t_coord_2 = get_player_pos()
    dist = math.sqrt((t_coord_2[0] - t_coord_1[0])**2 +
                     (t_coord_2[1] - t_coord_1[1])**2 +
                     (t_coord_2[2] - t_coord_1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {dist:.4f}")


if __name__ == "__main__":
    main()
