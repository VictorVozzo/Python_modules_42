# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   functools_artifacts.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/08 11:08:46 by vivozzo-           #+#    #+#             #
#   Updated: 2026/07/10 12:14:14 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from collections.abc import Callable
from typing import Any
from operator import add, mul
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0

    operations: dict[str, Callable] = {
        "add": add,
        "mul": mul,
        "max": max,
        "min": min,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: '{operation}'!")
    resultado = reduce(operations[operation], spells)
    return resultado


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchant {target} with {element} and power = {power}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    power = 50
    fire = partial(base_enchantment, power, "fire")
    shadow = partial(base_enchantment, power, "shadow")
    lightning = partial(base_enchantment, power, "lightning")
    return {"fire": fire, "shadow": shadow, "lightning": lightning}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(any_variable: Any) -> str:
        return "Unknown spell type"

    @spell.register
    def damage_spell(damage: int) -> str:
        return f"Damage spell: {damage} damage"

    @spell.register
    def enchantment(enchant: str) -> str:
        return f"Enchantment: {enchant}"

    @spell.register
    def multi_cast(spells: list) -> str:
        return f"Multi-cast: {len(spells)} spells"

    return spell


if __name__ == "__main__":
    try:
        spell_power = [13, 12, 49, 24, 21, 37]
        fibonacci_tests = [0, 1, 10, 15]
        spells = ["fireball", "lightning", "freeze"]

        print("Testing spell reducer: ")
        print(f"Spell power: {spell_power}")
        print(f"Sum: {spell_reducer(spell_power, 'add')}")
        print(f"Product: {spell_reducer(spell_power, 'mul')}")
        print(f"Max: {spell_reducer(spell_power, 'max')}")

        print("\nTesting spell reducer with invalid operator: ")

        try:
            print(f"division: {spell_reducer(spell_power, 'division')}")
        except Exception as e:
            print(e)

        print("\nTesting partial enchanter: ")
        enchanter = partial_enchanter(base_enchantment)
        print(enchanter["fire"]("sword"))
        print(enchanter["shadow"]("boots"))
        print(enchanter["lightning"]("shield"))

        print("\nTesting memoized fibonacci: ")
        for fibonacci in fibonacci_tests:
            print(f"Fib({fibonacci}): {memoized_fibonacci(fibonacci)}")

        print("\nTesting spell dispatcher: ")
        print(spell_dispatcher()(spell_power[2]))
        print(spell_dispatcher()(spells[0]))
        print(spell_dispatcher()(spells))
        print(spell_dispatcher()(("teste1", "teste2")))
    except Exception as e:
        print(e)
