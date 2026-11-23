# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   strategies.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/26 16:14:41 by vivozzo-           #+#    #+#             #
#   Updated: 2026/06/27 15:16:01 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod
from typing import Any
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleError(Exception):
    pass


class BattleStrategy(ABC):
    type: str

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Any) -> str:
        pass


class NormalStrategy(BattleStrategy):
    type = "Normal"

    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            return (creature.attack())
        raise BattleError("Invalid Creature for this normal strategy")


class AggressiveCreature(Creature, TransformCapability):
    pass


class AggressiveStrategy(BattleStrategy):
    type = "Aggressive"

    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, Creature) and isinstance(
            creature, TransformCapability)

    def act(self, creature: AggressiveCreature) -> str:
        if self.is_valid(creature):
            actions = (
                f"{creature.transform()}\n"
                f"{creature.attack()}\n"
                f"{creature.revert()}"
            )
            return (actions)
        name = f"'{creature.name}' " if isinstance(creature, Creature) else ""
        raise BattleError(
            f"Invalid Creature {name}for this aggressive strategy")


class DefensiveCreature(Creature, HealCapability):
    pass


class DefensiveStrategy(BattleStrategy):
    type = "Defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature) and isinstance(
            creature, HealCapability)

    def act(self, creature: DefensiveCreature) -> str:
        if self.is_valid(creature):
            actions = f"{creature.attack()}\n{creature.heal()}"
            return (actions)
        name = f"'{creature.name}' " if isinstance(creature, Creature) else ""
        raise BattleError(
            f"Invalid Creature {name}for this defensive strategy")
