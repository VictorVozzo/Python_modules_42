# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   ft_alembic_1.py                                    :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/22 11:44:56 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/22 11:44:57 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from elements import create_water


if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print("Testing create_water: ", end="")
    print(create_water())
