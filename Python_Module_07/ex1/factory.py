# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   factory.py                                          :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/26 14:47:24 by vivozzo-           #+#    #+#             #
#   Updated: 2026/06/27 14:37:58 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0 import CreatureFactory
from ex1.creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):

    type = "Healing"

    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    type = "Transform"

    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
