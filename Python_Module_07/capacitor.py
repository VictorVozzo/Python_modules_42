# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   capacitor.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/26 15:07:33 by vivozzo-           #+#    #+#             #
#   Updated: 2026/06/27 14:37:28 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex1 import HealingCreatureFactory, TransformCreatureFactory


if __name__ == "__main__":

    healing_creature_factory = HealingCreatureFactory()
    transform_creature_factory = TransformCreatureFactory()

    sproutling = healing_creature_factory.create_base()
    bloomelle = healing_creature_factory.create_evolved()

    shiftling = transform_creature_factory.create_base()
    morphagon = transform_creature_factory.create_evolved()

    print("Testing Creature with healing capability")
    print(" base:")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())
    print(" evolved:")
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())

    print("\nTesting Creature with transform capability")
    print(" base:")
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())
    print(" evolved:")
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())
