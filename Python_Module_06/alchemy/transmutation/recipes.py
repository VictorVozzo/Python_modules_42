# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   recipes.py                                         :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/22 15:51:23 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/22 15:51:24 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from elements import create_fire
from ..potions import strength_potion
from ..elements import create_air


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew ’{create_air()}’ "
            f"and ’{strength_potion()}’ mixed with ’{create_fire()}’")
