# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   battle.py                                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/25 16:30:39 by vivozzo-           #+#    #+#             #
#   Updated: 2026/06/27 14:39:31 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import ex0


def fight(fact1: ex0.CreatureFactory, fact2: ex0.CreatureFactory) -> None:

    if not isinstance(fact1, ex0.CreatureFactory):
        raise Exception("Invalid First Factory!")

    if not isinstance(fact2, ex0.CreatureFactory):
        raise Exception("Invalid Second Factory!")

    base_creature_1 = fact1.create_base()
    base_creature_2 = fact2.create_base()

    print("\nTesting battle")
    print(base_creature_1.describe())
    print(" vs.")
    print(base_creature_2.describe())
    print(" fight!")
    print(base_creature_1.attack())
    print(base_creature_2.attack())


def factory_verification(factory: ex0.CreatureFactory) -> None:

    if not isinstance(factory, ex0.CreatureFactory):
        raise Exception("Invalid Factory!")

    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


if __name__ == "__main__":
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()

    print("Testing factory")
    factory_verification(flame_factory)

    print("\nTesting factory")
    factory_verification(aqua_factory)

    fight(flame_factory, aqua_factory)
