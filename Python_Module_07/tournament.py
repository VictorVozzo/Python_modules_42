# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   tournament.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/26 17:31:50 by vivozzo-           #+#    #+#             #
#   Updated: 2026/06/27 15:14:42 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2 import BattleError, BattleStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    try:

        if not isinstance(opponents, list):
            raise BattleError(
                "type of the variable not correct!")

        for opponent in opponents:
            if not isinstance(opponent, tuple):
                raise BattleError(
                    "type of the variable not correct!")
            if len(opponent) != 2:
                raise BattleError(
                    "type of the variable not correct!")
            if (not isinstance(opponent[0], CreatureFactory) or
                    not isinstance(opponent[1], BattleStrategy)):
                raise BattleError(
                    "type of the variable not correct!")

        if len(opponents) < 2:
            print(
                f"Just {len(opponents)} "
                "opponent in the battle, put atleast 2!")
            return
        show_opp: list[str] = []
        for opponent in opponents:
            show_opp.append(f"({opponent[0].type}+{opponent[1].type})")
        print(show_opp)
        print("*** Tournament ***")
        print(f"{len(opponents)} opponents involved")

        index = 0
        for opponent_a in opponents:
            index += 1
            opp_a_creature_factory = opponent_a[0]
            creature_a = opp_a_creature_factory.create_base()
            opp_a_strategy = opponent_a[1]
            for opponent_b in opponents[index:]:
                opp_b_creature_factory = opponent_b[0]
                creature_b = opp_b_creature_factory.create_base()
                opp_b_strategy = opponent_b[1]
                print("\n* Battle *")
                print(creature_a.describe())
                print(" vs.")
                print(creature_b.describe())
                print(" now fight!")
                print(opp_a_strategy.act(creature_a))
                print(opp_b_strategy.act(creature_b))
    except BattleError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    opponents_0 = [(flame_factory, normal_strategy),
                   (healing_factory, defensive_strategy)]

    opponents_1 = [(flame_factory, aggressive_strategy),
                   (healing_factory, defensive_strategy)]

    opponents_2 = [(aqua_factory, normal_strategy),
                   (healing_factory, defensive_strategy),
                   (transform_factory, aggressive_strategy)]

    print("Tournament 0 (basic)")
    battle(opponents_0)
    print("\nTournament 1 (error)")
    battle(opponents_1)
    print("\nTournament 2 (multiple)")
    battle(opponents_2)
