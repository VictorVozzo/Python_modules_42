# ************************************************************************** #
#                                                                            #
#                                                        :::      ::::::::   #
#   potions.py                                         :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>    +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2026/06/22 14:11:06 by vivozzo-          #+#    #+#             #
#   Updated: 2026/06/22 14:11:07 by vivozzo-         ###   ########.fr       #
#                                                                            #
# ************************************************************************** #

from .elements import create_air, create_earth
from elements import create_water, create_fire


def healing_potion() -> str:
    return ("Healing potion brewed with "
            f"'{create_earth()}' and '{create_air()}'")


def strength_potion() -> str:
    return ("Strength potion brewed with "
            f"'{create_fire()}' and '{create_water()}'")
